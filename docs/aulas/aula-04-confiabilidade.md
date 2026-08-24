# Aula 04 — Confiabilidade

[Baixar o PDF original](../assets/pdfs/2026-2/aula-04-confiabilidade.pdf){ .md-button }

## Objetivos

- Definir confiabilidade e disponibilidade sem tratá-las como sinônimos.
- Interpretar metas de disponibilidade e seu orçamento de indisponibilidade.
- Relacionar testes, tratamento de erros, CI/CD e monitoramento à confiabilidade.
- Usar códigos HTTP para comunicar falhas entre sistemas.

## Confiabilidade e disponibilidade

Confiabilidade é a capacidade de funcionar corretamente e de forma consistente.
Disponibilidade mede a proporção de tempo em que o serviço permanece utilizável.
Um sistema pode estar no ar e produzir uma resposta incorreta; nesse caso, está
disponível, mas não é confiável.

| Meta | Indisponibilidade aproximada por ano | Por mês |
|---:|---:|---:|
| 99% | 3 dias, 15 h e 39 min | 7 h e 18 min |
| 99,9% | 8 h e 45 min | 43 min |
| 99,99% | 52 min | 4 min e 23 s |
| 99,999% | 5 min e 15 s | 26 s |

Quanto maior a meta, mais caros e rigorosos se tornam arquitetura, operação,
testes e resposta a incidentes.

## Práticas que aumentam a confiabilidade

### Testes

Testes automatizados verificam regras de forma repetível. Testes de unidade
isolam comportamentos; integração verifica componentes colaborando; ponta a ponta
exercita fluxos completos. O conjunto deve refletir riscos reais do sistema.

### Tratamento de erros

Exceções precisam ser tratadas no nível apropriado. Em APIs, o código HTTP deve
permitir que outra máquina diferencie uma entrada inválida, uma ausência de
recurso, um conflito e uma falha interna.

| Situação | Código comum |
|---|---:|
| Requisição inválida | `400` |
| Não autenticado | `401` |
| Sem permissão | `403` |
| Recurso não encontrado | `404` |
| Conflito de estado | `409` |
| Falha inesperada | `500` |

### Integração e entrega contínuas

CI integra alterações com validações automáticas. CD torna a entrega reproduzível
e interrompe o processo quando testes, cobertura ou outras políticas falham.

```text
pull request → testes → análise → build da imagem → publicação → deploy
```

### Monitoramento

Aplicação, servidor, banco e integrações externas precisam produzir sinais. Logs,
métricas e rastreamento devem ajudar a detectar, explicar e corrigir problemas.
Ferramentas possíveis incluem Grafana, Logstash e serviços gerenciados.

## Perguntas de revisão

1. Como um sistema pode estar disponível e ainda assim não ser confiável?
2. Quanto tempo de falha uma meta de 99,9% permite aproximadamente por mês?
3. Por que códigos HTTP corretos aumentam a confiabilidade de integrações?
4. Qual é a diferença entre integração contínua e entrega contínua?
5. Que sinais você monitoraria em uma API de pagamentos?
