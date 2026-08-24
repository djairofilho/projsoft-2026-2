# Aula 03 — Tutorial AWS

[Baixar o PDF original](../assets/pdfs/2026-2/aula-03-tutorial-aws.pdf){ .md-button }

## Objetivos

- Acessar uma máquina remota por SSH.
- Preparar uma instância Ubuntu para executar Docker.
- Publicar uma imagem local e executá-la remotamente.
- Repetir o deploy sem expor chaves, IPs ou senhas.

## Acesso por SSH

No Linux, macOS, WSL ou Git Bash, proteja a chave e conecte-se usando valores
locais:

```bash
chmod 400 CAMINHO_DA_CHAVE.pem
ssh -i CAMINHO_DA_CHAVE.pem ubuntu@IP_DA_MAQUINA
```

!!! danger "Nunca publique a chave"
    Uma chave `.pem` concede acesso à infraestrutura. Ela não deve ser copiada
    para este repositório, enviada em mensagens ou incluída em capturas de tela.

## Instalação do Docker

Use as instruções oficiais de instalação do
[Docker Engine no Ubuntu](https://docs.docker.com/engine/install/ubuntu/). Depois,
adicione o usuário ao grupo Docker e atualize a sessão:

```bash
sudo usermod -aG docker ubuntu
newgrp docker
docker version
```

## Fluxo de deploy

Na máquina local:

```bash
./mvnw clean package
docker build -t USUARIO/minha-app .
docker push USUARIO/minha-app
```

Na máquina remota:

```bash
docker pull USUARIO/minha-app
docker run --name app -p 8080:8080 USUARIO/minha-app
docker logs app
```

Para substituir a versão em execução:

```bash
docker stop app
docker rm app
docker pull USUARIO/minha-app
docker run --name app -p 8080:8080 USUARIO/minha-app
```

O processo manual ajuda a entender as etapas. Em produção, um pipeline deve
automatizar build, testes, publicação e deploy, parando quando uma validação falha.

## Perguntas de revisão

1. Por que a permissão da chave SSH deve ser restrita?
2. Quais etapas acontecem localmente e quais acontecem na instância?
3. Por que `docker pull` deve ocorrer antes de reiniciar a aplicação?
4. O que ainda falta nesse fluxo para caracterizá-lo como entrega contínua?
