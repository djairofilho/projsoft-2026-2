# Aula 03 — Docker

Este guia reúne os comandos apresentados no material. Como o PDF tem duas
páginas e funciona como referência operacional, a anotação mantém o mesmo foco:
executar, inspecionar, construir e publicar containers sem acrescentar uma camada
conceitual desnecessária.

## Material original

<iframe
  class="pdf-preview"
  src="../../assets/pdfs/2026-2/aula-03-docker.pdf"
  title="Visualização do PDF da Aula 03: Docker">
</iframe>

<div class="pdf-preview-actions" markdown>
[Abrir ou baixar o PDF](../assets/pdfs/2026-2/aula-03-docker.pdf){ .md-button .md-button--primary }

<p class="pdf-preview-note">2 páginas. O visualizador usa o leitor de PDF do navegador.</p>
</div>

## Objetivos

- Executar e nomear um container.
- Publicar uma porta e fornecer variáveis de ambiente.
- Inspecionar logs e o estado dos containers.
- Construir, listar, publicar e remover imagens.
- Conectar containers por uma rede Docker.

## Imagem, container, porta e rede

Uma **imagem** empacota a aplicação e suas dependências. Um **container** é uma
execução isolada dessa imagem. O parâmetro `-p` publica uma porta do container na
máquina, enquanto `--network` conecta o container a uma rede Docker.

```text
requisição → porta 8080 da máquina → porta 8080 do container → aplicação
```

## Executar um container

```bash
docker run --name app -p 8080:8080 USUARIO/minha-app
```

| Opção | Função |
|---|---|
| `--name app` | Define um nome estável para os próximos comandos |
| `-p 8080:8080` | Mapeia `porta_da_máquina:porta_da_aplicação` |
| `-e CHAVE=valor` | Fornece uma variável de ambiente |
| `--network rede-app` | Conecta o container a uma rede existente |

Nomear o container é opcional, mas evita depender de um identificador aleatório.
Sem a publicação de porta, a aplicação pode executar normalmente e ainda assim
não ficar acessível pela porta da máquina.

Um exemplo com rede e configuração:

```bash
docker network create -d bridge rede-app
docker run --name app \
  --network rede-app \
  -e APP_PROFILE=dev \
  -p 8080:8080 \
  USUARIO/minha-app
```

## Inspecionar e controlar containers

```bash
docker ps
docker ps --all
docker logs app
docker stop app
docker rm app
```

`docker ps` mostra apenas containers em execução. A opção `--all` inclui os que
já pararam. `docker stop` encerra o processo, mas preserva o container; `docker rm`
remove esse container parado. A imagem continua disponível para novas execuções.

Quando um comando falhar, comece por `docker ps --all` e `docker logs app`. Eles
mostram se o processo terminou e qual mensagem foi produzida pela aplicação.

## Construir e publicar imagens

Na pasta que contém o `Dockerfile`:

```bash
docker build -t USUARIO/minha-app .
docker images
docker push USUARIO/minha-app
```

O ponto final define o diretório enviado como contexto de build. Para publicar no
Docker Hub, o nome da imagem precisa começar pelo usuário ou pela organização do
repositório.

Para remover uma imagem local que não está em uso:

```bash
docker rmi USUARIO/minha-app
```

Se houver um container baseado nela, remova primeiro o container. Parar e remover
containers não é o mesmo que remover imagens.

!!! caution "Não compartilhe segredos em comandos"
    Valores de `-e` podem aparecer no histórico do terminal e na configuração do
    container. Use apenas marcadores em documentação e o mecanismo de segredos da
    plataforma em ambientes reais.

Veja também as referências rápidas de [Docker](../referencias/docker.md) e
[Docker Hub](../referencias/docker-hub.md), que reúnem o fluxo completo em formato
de consulta.
