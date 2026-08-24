# Aula 01 — Introdução

[Baixar o PDF original](../assets/pdfs/2026-2/aula-01-introducao.pdf){ .md-button }

## Objetivos

- Diferenciar requisitos funcionais de requisitos de qualidade.
- Entender arquitetura como um processo de decisão sob restrições.
- Reconhecer os principais requisitos de qualidade e seus *trade-offs*.
- Explicar o papel do arquiteto em sistemas que precisam evoluir e operar.

## Do CRUD ao problema arquitetural

Criar, listar, atualizar e excluir dados resolve grande parte dos requisitos
funcionais de uma aplicação. O desafio cresce quando o mesmo comportamento
precisa funcionar com muitos usuários, alto volume de dados, picos de demanda,
dependências externas, múltiplas equipes e consequências financeiras para falhas.

| Tipo | Pergunta | Exemplo |
|---|---|---|
| Funcional | O que o sistema faz? | Realizar uma compra |
| Qualidade | Como e em quais condições ele faz? | Manter a compra consistente durante uma falha |

## Principais requisitos de qualidade

=== "Confiabilidade"
    O sistema executa corretamente e produz resultados consistentes. Envolve
    disponibilidade, resiliência, tolerância a falhas, recuperação e observação.

=== "Escalabilidade"
    O desempenho continua aceitável quando carga e volume mudam. Cache, filas,
    balanceamento e particionamento são técnicas possíveis, não respostas
    automáticas.

=== "Segurança"
    Autenticação, autorização, confidencialidade, integridade e auditoria devem
    estar presentes do desenvolvimento à operação.

=== "Manutenibilidade"
    Mudanças permanecem localizadas, testáveis e compreensíveis. Boas práticas,
    padrões e testes reduzem o custo de evolução.

## Trade-offs

Uma decisão arquitetural melhora algumas propriedades e cobra um preço em outras.
Adicionar cache pode reduzir latência, por exemplo, mas introduz invalidação e o
risco de dados desatualizados. Uma solução tecnicamente superior também pode ser
inadequada se a equipe não souber operá-la ou se seu custo for proibitivo.

Use este roteiro para registrar uma decisão:

1. Qual requisito de qualidade precisa melhorar?
2. Qual evidência ou métrica define sucesso?
3. Quais restrições limitam a solução?
4. Quais alternativas foram consideradas?
5. Que benefícios e custos cada alternativa cria?
6. Como a decisão será revisada no futuro?

## O que é arquitetura de software?

Uma definição operacional para a disciplina:

> Arquitetura de software é tomar decisões estruturais para que um sistema atenda
> seus requisitos de qualidade dentro das restrições existentes.

O arquiteto não escolhe apenas tecnologias. Ele torna as decisões explícitas,
compara alternativas, comunica consequências e acompanha se as hipóteses continuam
verdadeiras.

## Perguntas de revisão

1. Por que duas aplicações com os mesmos CRUDs podem exigir arquiteturas muito
   diferentes?
2. Qual é a diferença entre disponibilidade e confiabilidade?
3. Como uma técnica pode melhorar um requisito e piorar outro?
4. Que restrições não técnicas influenciam uma decisão arquitetural?
5. Em que situações a decisão tecnicamente mais avançada não é a melhor escolha?
