# Aulas

## Materiais disponíveis

| Aula | Assunto | PDF |
|---|---|---:|
| [01](aula-01-introducao.md) | Arquitetura, requisitos e decisões | 37 páginas |
| [02](aula-02-manutenibilidade.md) | Manutenibilidade e SOLID | 18 páginas |
| [03.1](aula-03-docker.md) | Docker, imagens e containers | 2 páginas |
| [03.2](aula-03-tutorial-aws.md) | Implantação manual na AWS | 2 páginas |
| [04](aula-04-confiabilidade.md) | Disponibilidade e confiabilidade | 15 páginas |
| [05](aula-05-redes-docker.md) | Redes Docker e PostgreSQL | 3 páginas |

### Subaulas da Aula 01

1. [Requisitos de qualidade](aula-01-requisitos-qualidade.md): cenários
   mensuráveis para confiabilidade, escalabilidade, segurança e manutenibilidade.
2. [Decisões arquiteturais e trade-offs](aula-01-decisoes-arquiteturais.md):
   comparação de alternativas, restrições, consequências e evidências.

### Subaulas da Aula 02

As subaulas ampliam o tema de padrões sem adicionar novos PDFs ao inventário:

1. [Padrões fundamentais](aula-02-padroes-fundamentais.md): Strategy, Factory,
   Repository e Injeção de Dependência.
2. [Padrões complementares](aula-02-padroes-complementares.md): Adapter,
   Decorator, Observer, Builder e Composite.

### Percurso da Aula 03

1. [Docker, imagens e containers](aula-03-docker.md): construir, executar,
   inspecionar e publicar o artefato.
2. [Implantação manual na AWS](aula-03-tutorial-aws.md): instalar, implantar,
   verificar e reverter uma versão.

### Subaulas da Aula 04

1. [Testes, erros e idempotência](aula-04-testes-erros.md): proteger regras,
   contratos HTTP e operações repetidas.
2. [Entrega e observabilidade](aula-04-entrega-observabilidade.md): promover o
   artefato com segurança e observar o resultado em execução.

## Mapa conceitual

As duas primeiras aulas definem **o que avaliar** e **como organizar o design**.
Docker e AWS introduzem uma forma concreta de empacotar e implantar a aplicação.
A aula de confiabilidade fecha o ciclo com prevenção, automação, observabilidade
e aprendizado após falhas. A Aula 05 retoma a implantação para conectar aplicação
e banco por uma rede Docker com descoberta de serviço por nome.

!!! tip "Revisão cumulativa"
    Ao estudar uma técnica, pergunte qual requisito ela melhora e qual custo ou
    risco ela adiciona. Essa pergunta transforma uma lista de ferramentas em
    raciocínio arquitetural.
