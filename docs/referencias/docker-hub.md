# Referência rápida: Docker Hub

Docker Hub é um registro de imagens. Ele armazena versões construídas localmente
para que outras máquinas, pipelines e ambientes de deploy possam baixá-las.

## Modelo de nome

Uma imagem publicada no Docker Hub segue este formato:

```text
USUARIO_OU_ORGANIZACAO/REPOSITORIO:TAG
```

Exemplo:

```text
meu-usuario/minha-app:1.0.0
```

| Parte | Função |
|---|---|
| `meu-usuario` | Namespace da conta ou organização |
| `minha-app` | Repositório que agrupa as imagens da aplicação |
| `1.0.0` | Tag que identifica uma versão ou variante |

Quando a tag é omitida, o Docker usa `latest`. Esse nome não significa “versão
mais nova” automaticamente. Ele é apenas uma tag convencional que pode apontar
para qualquer imagem.

## Autenticação

O comando padrão abre o fluxo de autenticação pelo navegador:

```bash
docker login
```

Para autenticar pelo terminal com um token pessoal:

```bash
docker login --username USUARIO
```

Quando o comando solicitar a senha, forneça um Personal Access Token (PAT). O
token pode ter permissões de leitura, escrita ou exclusão e é obrigatório para a
CLI quando a conta usa autenticação em dois fatores.

Para encerrar a sessão local:

```bash
docker logout
```

!!! danger "Não exponha o token"
    Não escreva o token no comando, no Dockerfile, em arquivos do projeto ou em
    variáveis versionadas. Em CI/CD, armazene-o no mecanismo de segredos da
    plataforma e conceda somente as permissões necessárias.

## Primeiro push

Construa a imagem já com o namespace e uma versão explícita:

```bash
docker build -t USUARIO/minha-app:1.0.0 .
docker push USUARIO/minha-app:1.0.0
```

O ponto final é o contexto do build. O nome antes dos dois-pontos identifica o
repositório; o valor depois deles é a tag enviada.

Se a imagem já foi construída com outro nome, crie uma nova tag sem refazer o
build:

```bash
docker tag minha-app:local USUARIO/minha-app:1.0.0
docker push USUARIO/minha-app:1.0.0
```

`docker tag` cria outra referência para a mesma imagem local. Ele não duplica as
camadas.

## Estratégia simples de tags

Use uma versão imutável para cada entrega e mova `latest` apenas quando quiser
indicar a versão padrão:

```bash
docker build -t USUARIO/minha-app:1.2.0 .
docker push USUARIO/minha-app:1.2.0

docker tag USUARIO/minha-app:1.2.0 USUARIO/minha-app:latest
docker push USUARIO/minha-app:latest
```

No deploy, prefira a tag fixa:

```bash
docker pull USUARIO/minha-app:1.2.0
docker run --name app -p 8080:8080 USUARIO/minha-app:1.2.0
```

Assim, o ambiente executa uma versão conhecida. Usar apenas `latest` dificulta
saber qual conteúdo estava em produção e repetir um deploy anterior.

## Atualizar uma aplicação

```bash
docker pull USUARIO/minha-app:1.3.0
docker stop app
docker rm app
docker run --name app -p 8080:8080 USUARIO/minha-app:1.3.0
docker logs -f app
```

Baixe a nova versão antes de parar a atual. Isso reduz o tempo entre a remoção do
container antigo e o início do novo.

## Comandos de consulta

| Objetivo | Comando |
|---|---|
| Listar imagens locais | `docker images` |
| Baixar uma versão | `docker pull USUARIO/minha-app:1.0.0` |
| Publicar uma versão | `docker push USUARIO/minha-app:1.0.0` |
| Publicar todas as tags locais | `docker push --all-tags USUARIO/minha-app` |
| Criar outra tag | `docker tag ORIGEM DESTINO` |
| Remover uma imagem local | `docker rmi USUARIO/minha-app:1.0.0` |
| Encerrar autenticação | `docker logout` |

## Erros comuns

| Mensagem ou sintoma | Verificação |
|---|---|
| `requested access to the resource is denied` | Confirme o login, o namespace e a permissão de escrita |
| `tag does not exist` | Execute `docker images` e confira nome e tag locais |
| Push foi para `latest` sem intenção | Informe `:TAG` no build e no push |
| Deploy continua na versão anterior | Use uma tag nova, execute `docker pull` e recrie o container |
| Pull de repositório privado falha | Autentique a máquina com uma credencial de leitura |

## Checklist antes de publicar

- [ ] A imagem usa o namespace correto.
- [ ] A entrega possui uma tag de versão explícita.
- [ ] O build não contém chaves, senhas ou arquivos locais sensíveis.
- [ ] A conta ou token possui somente as permissões necessárias.
- [ ] O repositório está público ou privado conforme a necessidade.
- [ ] O deploy referencia uma versão reproduzível.
- [ ] O container foi iniciado e seus logs foram conferidos.

## Documentação oficial

- [Início rápido do Docker Hub](https://docs.docker.com/docker-hub/quickstart/)
- [Tags no Docker Hub](https://docs.docker.com/docker-hub/repos/manage/hub-images/tags/)
- [Personal Access Tokens](https://docs.docker.com/security/access-tokens/)
- [Referência de `docker login`](https://docs.docker.com/reference/cli/docker/login/)
- [Referência de `docker push`](https://docs.docker.com/reference/cli/docker/image/push/)
