# Aula 02 — Manutenibilidade

[Baixar o PDF original](../assets/pdfs/2026-2/aula-02-manutenibilidade.pdf){ .md-button }

## Objetivos

- Relacionar manutenibilidade ao custo e ao risco de uma mudança.
- Identificar acoplamento, baixa coesão, duplicação e complexidade.
- Usar SOLID como ferramenta de raciocínio, sem tratá-lo como objetivo final.
- Reconhecer quando Strategy, Factory e outros padrões reduzem o raio de mudança.

## O que significa manter um sistema?

Um sistema manutenível permite entender, localizar, modificar, testar e corrigir
comportamentos sem efeitos cascata. O objetivo é tornar mudanças futuras mais
previsíveis, seguras e baratas.

| Propriedade | Sinal desejável |
|---|---|
| Acoplamento | Poucas dependências entre módulos |
| Coesão | Responsabilidades relacionadas permanecem juntas |
| Testabilidade | Comportamentos podem ser verificados isoladamente |
| Localidade | Uma regra muda em poucos lugares |
| Clareza | Dependências e responsabilidades ficam explícitas |

## Como sistemas se tornam difíceis de mudar

- **Acoplamento alto:** uma alteração exige conhecer vários módulos.
- **Complexidade alta:** existem caminhos demais para entender e testar.
- **Duplicação:** a mesma regra evolui de formas diferentes.
- **Dependências frágeis:** detalhes externos contaminam o domínio.

O efeito econômico forma um ciclo: mais tempo para entender gera maior risco de
alteração, que gera mais defeitos e retrabalho, reduzindo a velocidade do time.

## Métricas úteis

Complexidade ciclomática, complexidade cognitiva, acoplamento, coesão, ciclos de
dependência, duplicação, *code smells*, *lead time* e *change failure rate* ajudam
a formular perguntas. Nenhuma delas, sozinha, prova que o sistema é manutenível.

## SOLID em uma frase por princípio

| Princípio | Pergunta prática |
|---|---|
| SRP | Quantas razões diferentes fazem este módulo mudar? |
| OCP | Um novo comportamento exige alterar todos os existentes? |
| LSP | Uma implementação substituta preserva o contrato esperado? |
| ISP | Cada consumidor depende apenas das operações que usa? |
| DIP | O domínio depende de abstrações ou de detalhes externos? |

### Exemplo: Strategy

Condicionais crescentes para PIX, cartão e boleto misturam seleção e execução.
Uma estratégia cria um contrato comum e permite adicionar meios de pagamento sem
alterar o fluxo central.

```java
public interface ProcessadorPagamento {
    Resultado processar(Pagamento pagamento);
}

public final class ProcessadorPix implements ProcessadorPagamento {
    public Resultado processar(Pagamento pagamento) {
        return Resultado.aprovado("pix");
    }
}
```

### Exemplo: Factory

Uma fábrica concentra a criação das estratégias. O restante da aplicação recebe
um processador pronto e não precisa conhecer detalhes de construção.

```java
public ProcessadorPagamento criar(TipoPagamento tipo) {
    return switch (tipo) {
        case PIX -> new ProcessadorPix();
        case CREDITO -> new ProcessadorCredito();
        case BOLETO -> new ProcessadorBoleto();
    };
}
```

!!! warning "Padrão não é decoração"
    Um padrão vale a pena quando resolve um problema recorrente e reduz o custo de
    mudança. Aplicá-lo sem necessidade pode apenas adicionar indireção.

## Perguntas de revisão

1. Como acoplamento e coesão afetam o raio de uma mudança?
2. Por que SOLID é uma ferramenta e não o objetivo do design?
3. Quando Strategy é preferível a uma sequência de condicionais?
4. Que problema Factory resolve sem substituir Strategy?
5. Por que uma única métrica não mede toda a manutenibilidade?
