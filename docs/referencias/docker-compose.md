# Referência rápida: Docker Compose

Docker Compose descreve e executa uma aplicação com vários containers a partir
de um arquivo `compose.yaml`. Em vez de repetir uma sequência de `docker run`, a
equipe registra serviços, redes, volumes, portas e configurações em um modelo
reproduzível.

## Quando usar

Compose é útil quando a aplicação depende de outros serviços, como PostgreSQL,
Redis ou uma fila, e todos precisam ser iniciados com a mesma configuração.

| Com comandos separados | Com Docker Compose |
|---|---|
| Cada `docker run` precisa ser repetido | A topologia fica no `compose.yaml` |
| Rede e volume são criados manualmente | Compose gerencia recursos do projeto |
| Nomes e opções podem divergir | Serviços recebem configuração consistente |
| Encerramento exige vários comandos | `docker compose down` encerra o conjunto |

!!! note "Compose não substitui o Dockerfile"
    O `Dockerfile` define como construir uma imagem. O `compose.yaml` define como
    executar e conectar uma ou mais imagens.

## YAML essencial

YAML representa mapas, listas e valores por indentação.

```yaml
services:                 # mapa
  app:                    # chave dentro de services
    ports:                # lista
      - "8080:8080"       # item da lista
    environment:          # outro mapa
      APP_PROFILE: dev
```

- use espaços, nunca tabulações;
- mantenha elementos do mesmo nível com a mesma indentação;
- use `-` para itens de uma lista;
- coloque mapeamentos de porta entre aspas;
- valide o resultado com `docker compose config`.

## Exemplo: aplicação e PostgreSQL

O arquivo abaixo representa a topologia usada na Aula 05:

```yaml
services:
  postgres:
    image: postgres:VERSAO
    environment:
      POSTGRES_DB: ${DB_NAME:-ecommerce}
      POSTGRES_USER: ${DB_USER:-app}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - dados-postgres:/var/lib/postgresql/data
    healthcheck:
      test:
        - CMD-SHELL
        - pg_isready -U ${DB_USER:-app} -d ${DB_NAME:-ecommerce}
      interval: 5s
      timeout: 3s
      retries: 10

  app:
    image: ${APP_IMAGE}
    ports:
      - "8080:8080"
    environment:
      DB_HOST: postgres
      DB_PORT: 5432
      DB_NAME: ${DB_NAME:-ecommerce}
      DB_USER: ${DB_USER:-app}
      DB_PASSWORD: ${DB_PASSWORD}
    depends_on:
      postgres:
        condition: service_healthy

volumes:
  dados-postgres:
```

| Elemento | Função |
|---|---|
| `services` | Define os componentes executáveis da aplicação |
| `image` | Indica a imagem e a versão do serviço |
| `ports` | Publica uma porta do container na máquina |
| `environment` | Define variáveis dentro do container |
| `volumes` | Preserva dados fora do ciclo de vida do container |
| `healthcheck` | Verifica se o serviço está pronto para uso |
| `depends_on` | Expressa dependência e ordem de inicialização |

## Rede padrão e descoberta por nome

Ao executar `docker compose up`, o Compose cria uma rede padrão para o projeto e
conecta os serviços. Cada serviço pode ser localizado pelo próprio nome.

No exemplo, a aplicação usa `DB_HOST=postgres`. Não é necessário descobrir o IP
do container nem declarar uma rede manualmente.

```text
navegador → localhost:8080 → serviço app
                                  ↓ rede padrão do projeto
                            serviço postgres:5432
```

Somente a porta `8080` foi publicada. O PostgreSQL permanece acessível para a
aplicação na rede interna, mas não diretamente pela porta da máquina.

### Rede explícita

Declare uma rede quando precisar controlar isolamento, driver ou conexão com
outros projetos:

```yaml
services:
  postgres:
    image: postgres:VERSAO
    networks:
      - rede-ecommerce

  app:
    image: ${APP_IMAGE}
    networks:
      - rede-ecommerce

networks:
  rede-ecommerce:
    driver: bridge
```

Para a maioria dos ambientes locais com uma única aplicação, a rede padrão é
suficiente.

## `.env`, interpolação e ambiente do container

Um arquivo `.env` ao lado do `compose.yaml` fornece valores usados para
interpolar expressões `${VAR}`. Ele não injeta automaticamente todas as
variáveis nos containers; o `environment` ou `env_file` de cada serviço define
o que entra no ambiente do processo.

Registre somente um `.env.example` com marcadores:

```dotenv
APP_IMAGE=USUARIO/ecommerce:VERSAO
DB_NAME=ecommerce
DB_USER=app
DB_PASSWORD=FORNECER_EM_AMBIENTE_SEGURO
```

Crie o `.env` real fora do controle de versão e valide a interpolação:

```bash
docker compose config
docker compose config --environment
```

Também é possível escolher outro arquivo:

```bash
docker compose --env-file CAMINHO.env up -d
```

### `env_file` de um serviço

`env_file` injeta variáveis no container de um serviço:

```yaml
services:
  app:
    image: ${APP_IMAGE}
    env_file:
      - CAMINHO_DO_ARQUIVO.env
```

| Recurso | Uso |
|---|---|
| `.env` do projeto | Interpolar valores no modelo do Compose |
| `--env-file` na CLI | Escolher a fonte de interpolação |
| `environment` | Declarar variáveis do container no YAML |
| `env_file` do serviço | Carregar variáveis para um container |

!!! danger "Não publique segredos"
    `.env` e `env_file` facilitam configuração, mas não são cofres. Não versione
    credenciais reais e não compartilhe a saída de `docker compose config` sem
    revisar valores resolvidos. Em produção, use o mecanismo de segredos da
    plataforma.

## Ordem de inicialização

A forma curta de `depends_on` inicia a dependência primeiro, mas não garante que
ela já aceite conexões. Para esperar pelo PostgreSQL, o exemplo combina um
`healthcheck` com `condition: service_healthy`.

```yaml
depends_on:
  postgres:
    condition: service_healthy
```

A aplicação ainda deve tratar indisponibilidade transitória. Um *healthcheck*
melhora a coordenação local, mas não substitui timeout, repetição controlada e
tratamento de erros.

## Volumes e persistência

Um volume nomeado preserva os dados quando o container é recriado:

```yaml
services:
  postgres:
    volumes:
      - dados-postgres:/var/lib/postgresql/data

volumes:
  dados-postgres:
```

`docker compose down` remove containers e redes do projeto, mas preserva volumes
nomeados. `docker compose down --volumes` também remove esses volumes e seus
dados; use essa opção somente quando a exclusão for intencional.

## Comandos principais

Execute os comandos na pasta que contém o `compose.yaml`:

| Objetivo | Comando |
|---|---|
| Validar e exibir o modelo resolvido | `docker compose config` |
| Criar ou atualizar os serviços | `docker compose up -d` |
| Construir imagens antes de iniciar | `docker compose up -d --build` |
| Listar serviços e estado | `docker compose ps` |
| Acompanhar todos os logs | `docker compose logs -f` |
| Acompanhar um serviço | `docker compose logs -f app` |
| Executar comando em serviço ativo | `docker compose exec app COMANDO` |
| Baixar imagens | `docker compose pull` |
| Parar sem remover | `docker compose stop` |
| Remover containers e redes | `docker compose down` |

## Diagnóstico

```bash
docker compose config
docker compose ps
docker compose logs postgres
docker compose logs app
docker network ls
```

| Sintoma | Verificação |
|---|---|
| Variável ficou vazia | Conferir `.env`, ambiente do terminal e `config --environment` |
| Aplicação não encontra o banco | Usar `postgres`, não `localhost`, como hostname |
| Banco inicia, mas recusa conexão | Conferir `healthcheck`, usuário, banco e senha |
| Alteração do código não aparece | Reconstruir a imagem com `up -d --build` |
| Serviço encerra ao iniciar | Ler `docker compose logs NOME_DO_SERVICO` |

## Referências relacionadas

- [Docker](docker.md): containers, imagens, redes e variáveis de ambiente.
- [Docker Hub](docker-hub.md): tags, publicação e download de imagens.
- [Aula 05](../aulas/aula-05-redes-docker.md): construção manual da topologia.

## Documentação oficial

- [Início rápido do Docker Compose](https://docs.docker.com/compose/gettingstarted/)
- [Redes no Docker Compose](https://docs.docker.com/compose/how-tos/networking/)
- [Variáveis de ambiente no Compose](https://docs.docker.com/compose/how-tos/environment-variables/)
- [Ordem de inicialização](https://docs.docker.com/compose/how-tos/startup-order/)
- [Referência do arquivo Compose](https://docs.docker.com/reference/compose-file/)
