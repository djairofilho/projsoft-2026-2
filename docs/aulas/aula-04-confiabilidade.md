# Aula 04: Confiabilidade

Confiabilidade é a capacidade de o software produzir resultados corretos e
consistentes. Ela depende de decisões tomadas durante desenvolvimento, entrega e
operação, não apenas da infraestrutura onde o sistema executa.

## Material original

<iframe
  class="pdf-preview"
  src="../../assets/pdfs/2026-2/aula-04-confiabilidade.pdf"
  title="Visualização do PDF da Aula 04: Confiabilidade">
</iframe>

<div class="pdf-preview-actions" markdown>
[Abrir ou baixar o PDF](../assets/pdfs/2026-2/aula-04-confiabilidade.pdf){ .md-button .md-button--primary }

<p class="pdf-preview-note">15 páginas. O visualizador usa o leitor de PDF do navegador.</p>
</div>

## Objetivos

- Diferenciar confiabilidade de disponibilidade.
- Interpretar metas e orçamentos de indisponibilidade.
- Relacionar prevenção, entrega e operação.
- Escolher evidências que representem a experiência do usuário.

## Confiabilidade e disponibilidade

Um sistema confiável produz o resultado correto de maneira consistente.
Disponibilidade mede a proporção de tempo em que o serviço permanece utilizável.
As duas propriedades não são sinônimas.

Uma API pode responder rapidamente com status `200` e calcular um total
incorreto. Ela está disponível do ponto de vista da rede, mas não é confiável.
Também pode recusar corretamente uma entrada inválida com `400`; essa resposta
não representa indisponibilidade.

```text
disponibilidade = tempo operacional / tempo total observado
```

Na prática, a equipe precisa definir o que conta como operacional. Responder
abaixo de uma meta de latência, concluir a transação e produzir o estado correto
podem fazer parte do indicador.

## Meta e orçamento de indisponibilidade

| Meta | Indisponibilidade aproximada por ano | Por mês |
|---:|---:|---:|
| 99% | 3 dias, 15 h e 39 min | 7 h e 18 min |
| 99,9% | 8 h e 45 min | 43 min |
| 99,99% | 52 min | 4 min e 23 s |
| 99,999% | 5 min e 15 s | 26 s |

Esse tempo funciona como um orçamento de indisponibilidade. Metas maiores exigem
redundância, automação e resposta a incidentes mais rigorosas. O custo aumenta,
por isso o número deve refletir impacto de negócio e expectativa dos usuários.

No checkout, uma medida útil combina disponibilidade com correção: percentual
de confirmações concluídas sem duplicar pagamento ou deixar pedido inconsistente.

## Confiabilidade ao longo do ciclo

```mermaid
flowchart LR
    A[Requisito mensurável] --> B[Testes e contratos de erro]
    B --> C[Integração e entrega contínuas]
    C --> D[Verificação do deploy]
    D --> E[Logs, métricas e rastreamento]
    E --> F[Incidente e aprendizado]
    F --> B
```

| Etapa | Pergunta | Evidência |
|---|---|---|
| Desenvolvimento | A regra conhecida continua correta? | Testes automatizados |
| Integração | A mudança pode entrar na versão principal? | Pipeline aprovado |
| Entrega | O artefato certo foi implantado com segurança? | Tag, verificação e rollback |
| Operação | O usuário recebe o resultado esperado? | Sinais técnicos e de negócio |
| Aprendizado | A mesma falha será detectada mais cedo? | Novo teste, alerta ou decisão |

Confiabilidade não é um componente adicionado no final. Cada etapa reduz uma
classe de risco e produz informação para a próxima.

## Escolha a subaula

| Se o problema está em... | Estude primeiro |
|---|---|
| Regressões, respostas imprevisíveis ou operações repetidas | Testes, erros e idempotência |
| Mudanças manuais, falhas de deploy ou diagnóstico lento | Entrega e observabilidade |

<div class="grid cards" markdown>

-   :material-test-tube:{ .lg .middle } **04.1: Testes, erros e idempotência**

    Proteja as regras do pedido e mantenha contratos previsíveis diante de falhas.

    [Estudar prevenção e tratamento de falhas](aula-04-testes-erros.md)

-   :material-chart-timeline-variant:{ .lg .middle } **04.2: Entrega e observabilidade**

    Automatize a promoção do artefato e observe o checkout em execução.

    [Estudar entrega e observabilidade](aula-04-entrega-observabilidade.md)

</div>

!!! warning "A porcentagem não substitui o cenário"
    Uma meta de 99,9% é incompleta sem população, janela, operação medida e
    definição de sucesso. A métrica deve representar um resultado importante
    para o usuário, não apenas a saúde de uma máquina.
