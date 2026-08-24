# Referência rápida — Docker

## Containers

| Objetivo | Comando |
|---|---|
| Iniciar | `docker run --name app -p 8080:8080 imagem` |
| Listar ativos | `docker ps` |
| Listar todos | `docker ps --all` |
| Ver logs | `docker logs app` |
| Acompanhar logs | `docker logs -f app` |
| Parar | `docker stop app` |
| Remover | `docker rm app` |

## Imagens

| Objetivo | Comando |
|---|---|
| Construir | `docker build -t usuario/imagem .` |
| Listar | `docker images` |
| Publicar | `docker push usuario/imagem` |
| Baixar | `docker pull usuario/imagem` |
| Remover | `docker rmi usuario/imagem` |

## Redes Docker

Uma rede Docker permite que containers se comuniquem sem publicar todas as
portas na máquina. O driver `bridge` cria uma rede privada no próprio host e é o
mais comum durante desenvolvimento local.

### Bridge padrão e bridge criada pelo usuário

Quando nenhum `--network` é informado, o container entra na rede `bridge` padrão.
Ela oferece conectividade básica, mas uma rede criada pelo usuário é preferível
para aplicações com vários containers porque fornece isolamento explícito e
resolução de nomes entre os participantes.

| Rede | Característica | Uso indicado |
|---|---|---|
| `bridge` padrão | Usada automaticamente e compartilhada por containers sem rede explícita | Testes simples com um único container |
| `bridge` criada pelo usuário | Possui nome próprio e descoberta por nome de container | Aplicação, banco e outros serviços relacionados |

Crie uma rede e conecte dois containers:

```bash
docker network create --driver bridge rede-ecommerce

docker run -d \
  --name banco \
  --network rede-ecommerce \
  postgres:VERSAO

docker run -d \
  --name app \
  --network rede-ecommerce \
  -p 8080:8080 \
  USUARIO/ecommerce:VERSAO
```

Dentro da `rede-ecommerce`, a aplicação pode usar `banco` como nome do host. O
endereço IP interno pode mudar quando o container é recriado, por isso não deve
ser fixado na configuração.

### Rede interna não é publicação de porta

`--network rede-ecommerce` permite comunicação entre containers. Já
`-p 8080:8080` publica uma porta do container na máquina para acesso externo.
O banco não precisa publicar sua porta quando somente a aplicação o utiliza.

```text
navegador → porta 8080 da máquina → app:8080
                                      ↓ rede-ecommerce
                                   banco:5432
```

### Comandos de rede

| Objetivo | Comando |
|---|---|
| Listar redes | `docker network ls` |
| Criar uma bridge | `docker network create --driver bridge rede-ecommerce` |
| Inspecionar participantes e configuração | `docker network inspect rede-ecommerce` |
| Conectar um container existente | `docker network connect rede-ecommerce app` |
| Desconectar um container | `docker network disconnect rede-ecommerce app` |
| Remover uma rede sem containers | `docker network rm rede-ecommerce` |

Uma rede não pode ser removida enquanto possui containers conectados. Use
`docker network inspect` para localizar os participantes antes de desconectá-los.

## Variáveis de ambiente

Variáveis de ambiente separam a configuração que muda entre execuções da imagem
imutável. Elas podem definir perfil, endereço de dependência, porta e outras
opções que não devem ser gravadas no `Dockerfile`.

### Informar valores no comando

```bash
docker run --name app \
  --network rede-ecommerce \
  -e APP_PROFILE=dev \
  -e DB_HOST=banco \
  -p 8080:8080 \
  USUARIO/ecommerce:VERSAO
```

Também é possível repassar uma variável já definida no terminal sem repetir seu
valor:

```bash
docker run -e APP_PROFILE USUARIO/ecommerce:VERSAO
```

Nesse formato, o Docker procura `APP_PROFILE` no ambiente que executa o comando.

### Usar um arquivo de ambiente

Para muitas variáveis, use um arquivo fora do controle de versão:

```dotenv
APP_PROFILE=dev
DB_HOST=banco
DB_PORT=5432
```

```bash
docker run --env-file CAMINHO_DO_ARQUIVO.env USUARIO/ecommerce:VERSAO
```

Um arquivo `.env.example` pode registrar apenas nomes e valores fictícios. O
arquivo usado de verdade não deve ser commitado quando contém credenciais ou
outros dados sensíveis.

| Forma | Exemplo | Observação |
|---|---|---|
| Valor direto | `-e APP_PROFILE=dev` | Claro para configurações não sensíveis e pontuais |
| Ambiente atual | `-e APP_PROFILE` | Reutiliza o valor definido no terminal |
| Arquivo | `--env-file CAMINHO.env` | Evita uma linha de comando extensa |

!!! danger "Variável de ambiente não é cofre de segredos"
    Valores podem aparecer no histórico do terminal, em ferramentas do sistema e
    na inspeção do container. Em ambientes reais, use o mecanismo de segredos da
    plataforma, limite permissões e nunca publique credenciais no repositório.

!!! tip "Diagnóstico"
    Quando a aplicação não responde, verifique se o container está ativo, leia os
    logs, inspecione a rede e confirme o mapeamento entre a porta da máquina e a
    porta da aplicação.

```bash
docker ps --all
docker logs app
docker network inspect rede-ecommerce
docker inspect app
```

Para autenticação, tags e publicação de imagens, consulte a
[referência rápida de Docker Hub](docker-hub.md).

Para registrar aplicação, banco, rede, variáveis e volumes em um único arquivo,
consulte a [referência rápida de Docker Compose](docker-compose.md).
