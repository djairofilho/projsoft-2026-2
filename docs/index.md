# Projeto de Software — 2026.2

Material de estudo sobre arquitetura de software, requisitos de qualidade e
práticas de engenharia. Cada aula combina notas estruturadas com o PDF original
aberto diretamente na página.

[Começar pela Aula 01](aulas/aula-01-introducao.md){ .md-button .md-button--primary }
[Ver todas as aulas](aulas/index.md){ .md-button }

!!! info "Material independente"
    Este site não é uma publicação oficial do Insper. As notas foram organizadas
    para estudo e devem ser usadas junto com as aulas e os materiais originais.

## Aulas disponíveis

O tamanho das notas acompanha o conteúdo de cada material. Aulas conceituais têm
explicações e exemplos mais extensos. Os guias operacionais mantêm o formato curto
e direto dos PDFs.

<div class="grid cards" markdown>

-   :material-sitemap:{ .lg .middle } **Aula 01: Introdução**

    Arquitetura, requisitos mensuráveis, decisões, restrições e *trade-offs*.

    **PDF com 37 páginas**

    [Estudar Introdução](aulas/aula-01-introducao.md)

    [Requisitos de qualidade](aulas/aula-01-requisitos-qualidade.md) ·
    [Decisões arquiteturais](aulas/aula-01-decisoes-arquiteturais.md)

-   :material-tools:{ .lg .middle } **Aula 02: Manutenibilidade**

    Acoplamento, coesão, métricas, SOLID e duas subaulas de padrões de projeto.

    **PDF com 18 páginas**

    [Estudar Manutenibilidade](aulas/aula-02-manutenibilidade.md)

    [Padrões fundamentais](aulas/aula-02-padroes-fundamentais.md) ·
    [Padrões complementares](aulas/aula-02-padroes-complementares.md)

-   :material-docker:{ .lg .middle } **Aula 03: Containers e implantação**

    Imagens, containers, Docker Hub, implantação manual e reversão na AWS.

    **Dois materiais originais com 2 páginas cada**

    [Docker, imagens e containers](aulas/aula-03-docker.md) ·
    [Implantação manual na AWS](aulas/aula-03-tutorial-aws.md)

-   :material-shield-check-outline:{ .lg .middle } **Aula 04: Confiabilidade**

    Disponibilidade, testes, idempotência, CI/CD e observabilidade.

    **PDF com 15 páginas**

    [Estudar Confiabilidade](aulas/aula-04-confiabilidade.md)

    [Testes, erros e idempotência](aulas/aula-04-testes-erros.md) ·
    [Entrega e observabilidade](aulas/aula-04-entrega-observabilidade.md)

-   :material-access-point-network:{ .lg .middle } **Aula 05: Redes Docker**

    Comunicação entre a aplicação Java e o PostgreSQL usando rede bridge, DNS
    interno e variáveis de ambiente.

    **PDF com 3 páginas**

    [Estudar Redes Docker](aulas/aula-05-redes-docker.md)

</div>

## Como usar o material

1. **Leia a visão geral.** Comece pelos objetivos e identifique o problema que a
   aula pretende resolver.
2. **Acompanhe o PDF.** Use o visualizador para consultar os slides sem sair da
   página. Ele oferece navegação, zoom, download e impressão.
3. **Estude as notas.** Relacione os conceitos, exemplos e tabelas ao conteúdo dos
   slides.
4. **Leve para o projeto.** Aplique a técnica em um caso concreto e registre qual
   requisito melhora, quais restrições existem e qual custo foi introduzido.

```text
problema real
    ↓
requisito de qualidade
    ↓
alternativas e restrições
    ↓
decisão arquitetural
    ↓
implementação e medição
```

## Ideia central da disciplina

Arquitetura de software é o conjunto de decisões estruturais usado para atender
requisitos de qualidade dentro de restrições reais. Não existe solução perfeita.
Custo, prazo, conhecimento da equipe e risco produzem *trade-offs*.

Uma tecnologia só faz sentido quando está ligada a um problema. Cache, filas,
containers, pipelines e padrões de projeto são mecanismos. A decisão começa pelo
resultado esperado e termina com evidência de que esse resultado foi alcançado.

## Referências rápidas

Use estas páginas durante exercícios e implementação:

- [Docker](referencias/docker.md): comandos para imagens, containers e redes;
- [Docker Hub](referencias/docker-hub.md): login, tags, publicação e download de
  imagens;
- [Máquinas AWS](referencias/aws.md): acesso remoto e fluxo seguro de deploy;
- [Glossário](referencias/glossario.md): conceitos de arquitetura e requisitos de
  qualidade;
- [Bibliografia e O’Reilly](referencias/bibliografia.md): acesso institucional e
  leituras recomendadas para aprofundar as aulas.
- [Fontes e atribuição](fontes.md): origem dos materiais e aviso de direitos.
