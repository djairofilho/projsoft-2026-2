# Referência rápida — AWS

## Conexão segura

```bash
chmod 400 CAMINHO_DA_CHAVE.pem
ssh -i CAMINHO_DA_CHAVE.pem ubuntu@IP_DA_MAQUINA
```

## Verificações iniciais

```bash
whoami
docker version
docker ps
```

## Atualizar a aplicação

```bash
docker pull USUARIO/minha-app
docker stop app
docker rm app
docker run --name app -p 8080:8080 USUARIO/minha-app
docker logs -f app
```

## Checklist de segurança

- [ ] Chave SSH armazenada somente em local privado.
- [ ] Chave, IP e credenciais ausentes do Git.
- [ ] Apenas portas necessárias liberadas.
- [ ] Senhas fornecidas por mecanismo de segredos.
- [ ] Imagens identificadas por versão, não apenas por `latest`.
- [ ] Logs inspecionados após o deploy.
