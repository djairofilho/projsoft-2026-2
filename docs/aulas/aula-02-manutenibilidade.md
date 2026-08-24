# Aula 02 — Manutenibilidade

Manutenibilidade aparece no esforço necessário para entender, modificar, testar
e corrigir um sistema. O objetivo não é produzir um código bonito de forma
abstrata, mas tornar as próximas mudanças previsíveis, seguras e baratas.

## Material original

<iframe
  class="pdf-preview"
  src="../../assets/pdfs/2026-2/aula-02-manutenibilidade.pdf"
  title="Visualização do PDF da Aula 02: Manutenibilidade">
</iframe>

<div class="pdf-preview-actions" markdown>
[Abrir ou baixar o PDF](../assets/pdfs/2026-2/aula-02-manutenibilidade.pdf){ .md-button .md-button--primary }

<p class="pdf-preview-note">18 páginas. O visualizador usa o leitor de PDF do navegador.</p>
</div>

## Objetivos

- Relacionar manutenibilidade ao custo e ao risco de mudança.
- Identificar acoplamento, coesão, duplicação e complexidade.
- Interpretar métricas sem transformá-las em objetivos isolados.
- Usar SOLID para analisar responsabilidades e dependências.
- Aplicar Strategy e Factory quando o problema justificar a abstração.

## O que significa manter um sistema?

Uma mudança pequena expõe a qualidade do design. Se alterar uma regra exige abrir
muitos arquivos, conhecer detalhes internos e repetir testes manuais, o sistema
tem baixa manutenibilidade.

O material divide o trabalho de manutenção em quatro capacidades:

| Capacidade | Resultado esperado |
|---|---|
| Entender | Encontrar onde uma regra ou comportamento está implementado |
| Modificar | Fazer a mudança sem espalhar alterações pelo sistema |
| Testar | Validar o novo comportamento com baixo esforço |
| Corrigir | Diagnosticar e resolver defeitos sem efeitos em cascata |

Essas capacidades se reforçam. Responsabilidades claras facilitam a localização
da regra; dependências explícitas permitem isolar o comportamento; testes rápidos
reduzem a incerteza da alteração.

## Por que o custo de mudança aumenta?

Quatro problemas aparecem com frequência:

- **acoplamento alto:** uma parte conhece detalhes demais de outras partes;
- **complexidade alta:** há caminhos e estados demais para compreender e testar;
- **duplicação:** a mesma regra precisa ser alterada em vários lugares;
- **dependências frágeis:** detalhes externos vazam para o núcleo da aplicação.

O resultado forma um ciclo econômico:

```text
mais tempo para entender
        ↓
mais risco para alterar
        ↓
mais defeitos e retrabalho
        ↓
menor velocidade do time
```

Uma entrega lenta nem sempre indica falta de esforço. Pode indicar que cada
alteração exige pagar juros de decisões anteriores.

## Propriedades desejáveis no design

### Baixo acoplamento e alta coesão

Acoplamento mede o quanto módulos dependem uns dos outros. Coesão indica o quanto
as responsabilidades de um módulo pertencem ao mesmo propósito. O objetivo é
reduzir conhecimento entre partes e manter juntas as regras que mudam pelo mesmo
motivo.

Baixo acoplamento não significa ausência de dependências. Uma aplicação precisa
colaborar com banco, mensageria e serviços externos. A diferença é tornar essas
relações pequenas, explícitas e substituíveis.

### Responsabilidades claras

Um módulo deve ter um propósito que possa ser explicado sem uma lista de funções
desconexas. Uma classe que calcula preço, persiste pedido, envia e-mail e gera PDF
mistura regras com motivos de mudança distintos.

Separar `PricingService`, `OrderRepository` e `NotificationService` não é apenas
organização. Cada mudança passa a ter um destino mais previsível e testes mais
focados.

### Testabilidade e mudanças localizadas

Um comportamento testável recebe suas dependências e expõe um resultado
observável. Se uma regra só pode ser verificada com banco, rede e interface em
execução, o retorno de cada alteração fica lento e frágil.

Uma mudança localizada afeta poucas partes. Isso reduz o raio de impacto, melhora
a revisão de código e simplifica a reversão quando algo falha.

## Como medir manutenibilidade

Nenhuma métrica responde sozinha se um sistema é manutenível. O valor está em
combinar sinais técnicos e sinais do processo.

| Dimensão | Exemplos | Pergunta que ajuda a responder |
|---|---|---|
| Complexidade | Ciclomática e cognitiva | Quantos caminhos ou conceitos precisam ser acompanhados? |
| Estrutura | Acoplamento, coesão e ciclos | A mudança atravessa muitos módulos? |
| Código | Duplicação, tamanho e *code smells* | Há indícios de responsabilidade difusa? |
| Fluxo | *Lead time* e frequência de entrega | Quanto tempo uma mudança leva até chegar ao usuário? |
| Estabilidade | Defeitos e *change failure rate* | Quantas mudanças causam falha ou retrabalho? |

Métricas podem ser manipuladas quando viram metas. Reduzir o tamanho médio de
classes, por exemplo, pode gerar muitas classes pequenas sem melhorar o design.
Use a tendência e o contexto para investigar, não para substituir julgamento.

## Ferramentas de manutenibilidade

O material organiza as ferramentas em grupos complementares:

- código bem estruturado, Clean Code, SOLID e padrões de projeto;
- testes de unidade, integração e ponta a ponta;
- análise estática, identificação de *smells* e falhas de segurança;
- observabilidade para diagnosticar o comportamento em execução;
- métricas de engenharia para acompanhar o efeito no fluxo do time.

Uma ferramenta cobre apenas parte do problema. Alta cobertura não garante bons
testes; análise estática não detecta todas as decisões inadequadas; um padrão de
projeto aplicado sem necessidade pode piorar a compreensão.

## SOLID como ferramenta de raciocínio

SOLID reúne cinco princípios para pensar mudança, responsabilidade e dependência.
Eles não são uma certificação de qualidade nem exigem uma classe para cada linha.

### S: Single Responsibility Principle

Uma classe ou módulo deve possuir uma responsabilidade coesa e um conjunto
coerente de motivos para mudar. A pergunta prática é: quantas razões diferentes
podem exigir alteração aqui?

Se `OrderService` calcula preço, salva no banco e envia e-mail, mudanças de regra
comercial, persistência e comunicação competem no mesmo lugar. Separar as
responsabilidades reduz interferência e permite testar cada uma diretamente.

### O: Open/Closed Principle

O design deve permitir extensão sem transformar cada comportamento novo em uma
alteração espalhada. “Fechado para modificação” não significa nunca tocar no
código. Significa criar um ponto estável de extensão quando existe variação real.

Em pagamentos, uma estratégia por método permite adicionar uma nova opção sem
reescrever o fluxo que seleciona e executa a cobrança.

### L: Liskov Substitution Principle

Uma implementação substituta deve preservar o contrato esperado. Se uma subclasse
exige tratamento especial, rejeita operações válidas do tipo base ou muda o
significado da resposta, a abstração é enganosa.

O contrato inclui mais que a assinatura: condições de entrada, resultado, erros e
efeitos observáveis também precisam ser compatíveis.

### I: Interface Segregation Principle

Um consumidor deve depender apenas das operações que usa. Interfaces grandes
obrigam implementações a criar métodos vazios, lançar exceções inesperadas ou
conhecer capacidades irrelevantes.

Interfaces menores devem refletir papéis do domínio, não uma divisão mecânica de
cada método em um arquivo.

### D: Dependency Inversion Principle

Regras centrais devem depender de abstrações estáveis. Banco de dados, cliente
HTTP e mensageria são detalhes que implementam contratos definidos pelo caso de
uso. Isso permite trocar infraestrutura e testar o domínio com implementações
controladas.

Injeção de dependência é um mecanismo comum para montar essas relações. Ela ajuda
a aplicar o princípio, mas usar um framework de injeção não garante um bom limite
arquitetural.

## Padrão Strategy

Strategy resolve uma família de comportamentos intercambiáveis. Sem ele, uma
condicional tende a crescer sempre que surge PIX, cartão, boleto ou outro método.

```java
public interface PaymentStrategy {
    PaymentResult pay(Payment payment);
}

public final class PixStrategy implements PaymentStrategy {
    @Override
    public PaymentResult pay(Payment payment) {
        return PaymentResult.approved("pix");
    }
}
```

O fluxo depende do contrato e cada estratégia concentra sua regra. Isso se
conecta ao princípio aberto/fechado e melhora a testabilidade.

Strategy vale a pena quando os comportamentos variam, crescem ou precisam ser
selecionados em execução. Para duas condições estáveis e triviais, a indireção
pode custar mais do que ajuda.

## Padrão Factory

Factory concentra a criação de objetos. Ela evita que vários pontos conheçam
classes concretas e regras de construção.

```java
public PaymentStrategy create(PaymentMethod method) {
    return switch (method) {
        case PIX -> new PixStrategy();
        case CREDIT_CARD -> new CreditCardStrategy();
        case BOLETO -> new BoletoStrategy();
    };
}
```

Strategy e Factory resolvem problemas diferentes. Strategy organiza a execução
de comportamentos; Factory organiza a escolha e a construção das implementações.
É comum usá-las juntas, mas uma não substitui a outra.

## Outros padrões citados

| Padrão ou técnica | Intenção principal |
|---|---|
| Repository | Isolar o acesso e a persistência de dados |
| Injeção de dependência | Fornecer colaboradores sem construí-los internamente |
| Decorator | Acrescentar comportamento ao redor de outro objeto |
| Builder | Construir objetos complexos passo a passo |
| Observer e Listener | Reagir a eventos sem acoplamento direto entre emissores e interessados |
| Composite | Tratar objetos individuais e composições por um contrato comum |
| Adapter | Traduzir uma interface externa para o contrato esperado |

!!! warning "Padrões não são regras universais"
    Um padrão é útil quando nomeia e resolve um problema recorrente. Aplicá-lo
    antes de existir variação, dependência ou complexidade pode apenas adicionar
    arquivos e indireções.

## Síntese

Manutenibilidade é custo e risco de mudança. Acoplamento, coesão, complexidade,
testabilidade e localidade ajudam a explicar esse custo. SOLID orienta perguntas
sobre responsabilidades e dependências; padrões oferecem soluções conhecidas;
métricas mostram se as decisões realmente melhoraram o sistema.
