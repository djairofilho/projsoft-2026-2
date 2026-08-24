# Aula 03 — Docker

[Baixar o PDF original](../assets/pdfs/2026-2/aula-03-docker.pdf){ .md-button }

## Objetivos

- Diferenciar imagem, container, porta e rede.
- Construir uma imagem e iniciar um container nomeado.
- Inspecionar logs e remover recursos que não são mais necessários.
- Publicar uma imagem no Docker Hub.

## Modelo mental

Uma **imagem** é um pacote imutável com aplicação e dependências. Um **container**
é uma execução isolada dessa imagem. O mapeamento de portas conecta uma porta da
máquina a uma porta exposta pela aplicação.

```text
requisição → porta 8080 da máquina → porta 8080 do container → aplicação
```

## Fluxo essencial

```bash
docker build -t USUARIO/minha-app .
docker run --name app -p 8080:8080 USUARIO/minha-app
docker logs app
docker stop app
docker rm app
```

Variáveis de ambiente e redes podem ser acrescentadas durante a execução:

```bash
docker network create -d bridge rede-app
docker run --name app \
  --network rede-app \
  -e NOME_DA_VARIAVEL=valor \
  -p 8080:8080 \
  USUARIO/minha-app
```

## Imagens e Docker Hub

```bash
docker images
docker push USUARIO/minha-app
docker rmi USUARIO/minha-app
```

O nome da imagem deve começar pelo usuário ou pela organização quando o destino é
o Docker Hub.

!!! caution "Dados sensíveis"
    Não grave senhas reais no Dockerfile, no comando compartilhado ou no histórico
    do shell. Em ambientes reais, use o mecanismo de segredos da plataforma.

Veja a [referência rápida de Docker](../referencias/docker.md) para a lista
consolidada de comandos.

## Perguntas de revisão

1. Qual é a diferença entre parar e remover um container?
2. O que significa `-p 8080:8080`?
3. Por que nomear containers facilita a operação?
4. Quando uma rede Docker é necessária?
5. Por que uma imagem parada ainda ocupa espaço local?
