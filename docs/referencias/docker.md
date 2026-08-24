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

## Redes e configuração

```bash
docker network create -d bridge rede-app
docker run --name app --network rede-app -e CHAVE=valor imagem
```

!!! tip "Diagnóstico"
    Quando a aplicação não responde, verifique se o container está ativo, leia os
    logs e confirme o mapeamento entre a porta da máquina e a porta da aplicação.
