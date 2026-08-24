# Aula 01 — Introdução

Esta aula apresenta a ideia central da disciplina: implementar as funções de um
sistema é apenas parte do problema. Arquitetura começa quando precisamos garantir
que essas funções continuem corretas sob carga, falhas, ataques, mudanças e
restrições reais de custo e prazo.

## Material original

<iframe
  class="pdf-preview"
  src="../../assets/pdfs/2026-2/aula-01-introducao.pdf"
  title="Visualização do PDF da Aula 01: Introdução">
</iframe>

<div class="pdf-preview-actions" markdown>
[Abrir ou baixar o PDF](../assets/pdfs/2026-2/aula-01-introducao.pdf){ .md-button .md-button--primary }

<p class="pdf-preview-note">37 páginas. O visualizador usa o leitor de PDF do navegador.</p>
</div>

## Objetivos

- Diferenciar requisitos funcionais de requisitos de qualidade.
- Entender arquitetura como decisão estrutural sob restrições.
- Reconhecer confiabilidade, escalabilidade, segurança e manutenibilidade.
- Avaliar benefícios, custos e riscos de uma decisão arquitetural.
- Entender o papel humano na decisão mesmo com o apoio de IA.

## O CRUD é necessário, mas não diferencia o sistema

Muitas aplicações começam com as mesmas quatro operações: criar, consultar,
atualizar e excluir dados. Um comércio eletrônico, um banco, uma rede social, um
sistema acadêmico e uma plataforma de reservas podem ser descritos como conjuntos
de CRUDs. Isso não significa que sejam arquiteturalmente equivalentes.

O que diferencia esses sistemas é o contexto em que as operações precisam
funcionar:

- muitos usuários agindo ao mesmo tempo;
- grande volume de dados e de requisições;
- picos e quedas bruscas de demanda;
- necessidade de operar continuamente;
- dependência de serviços externos;
- ataques e tentativas de fraude;
- perda financeira quando algo falha;
- evolução constante por várias equipes.

Cadastrar um pagamento é um requisito funcional. Impedir que ele seja cobrado
duas vezes quando a rede oscila é um requisito de qualidade. O primeiro descreve
o comportamento; o segundo define as condições nas quais esse comportamento deve
ser confiável.

| Tipo de requisito | Pergunta principal | Exemplo |
|---|---|---|
| Funcional | O que o sistema faz? | Realizar uma compra |
| Qualidade | Como e sob quais condições ele faz? | Processar a compra uma única vez, mesmo após uma repetição |

Um requisito de qualidade deve ser verificável. “O sistema será rápido” é vago.
“95% das consultas responderão em até 300 ms com 500 usuários simultâneos” oferece
carga, métrica e limite. Esses dados orientam o design e permitem validar a
decisão depois.

## Requisitos de qualidade

O material destaca quatro grupos que serão aprofundados na disciplina. Eles se
relacionam com observabilidade, usabilidade, rastreabilidade e custo, entre outros
atributos.

### Confiabilidade

Confiabilidade é a capacidade de executar corretamente e retornar um resultado
consistente para a transação. Ela envolve disponibilidade, resiliência, tolerância
a falhas, recuperação e consistência.

Algumas técnicas possíveis:

- **idempotência:** repetir a mesma operação não produz um segundo efeito;
- **timeout:** uma chamada deixa de esperar após um limite conhecido;
- **retry:** uma falha transitória pode ser repetida com uma política controlada;
- **circuit breaker:** chamadas para um serviço degradado são interrompidas antes
  de sobrecarregar ainda mais o sistema;
- **replicação e backup:** dados e serviços podem sobreviver à perda de uma
  instância;
- **testes:** regras e integrações são verificadas de forma repetível.

Essas técnicas não devem ser aplicadas isoladamente. Um `retry` sem idempotência
pode duplicar uma cobrança; sem limite e espera progressiva, também pode ampliar
uma indisponibilidade.

### Escalabilidade

Escalabilidade é manter um desempenho aceitável quando a carga varia. Os sinais
mais comuns são latência, volume processado por intervalo, capacidade, uso de
recursos e comportamento durante picos.

| Técnica | Benefício esperado | Custo ou risco introduzido |
|---|---|---|
| Cache | Reduz latência e carga no banco | Invalidação e dados desatualizados |
| Fila | Absorve picos e desacopla etapas | Processamento assíncrono e observação mais difícil |
| Balanceador | Distribui requisições | Novo componente operacional |
| Particionamento | Distribui dados e escrita | Consultas e consistência mais complexas |
| gRPC | Comunicação eficiente entre serviços | Mais contrato e ferramentas específicas |

Escalar não significa apenas adicionar máquinas. Antes disso, é preciso saber
qual recurso está saturado e qual meta deixou de ser atendida.

### Segurança

Segurança atravessa todo o ciclo de engenharia, do código à operação. Ela inclui:

- autenticação para identificar quem faz a requisição;
- autorização para limitar o que a identidade pode fazer;
- confidencialidade para impedir leitura indevida;
- integridade para detectar ou evitar alteração;
- auditoria e rastreabilidade de ações relevantes;
- privacidade e tratamento adequado de dados pessoais;
- recuperação após um incidente.

OAuth 2.0, tokens com validade curta, limitação de requisições, gestão de segredos
e verificação de dependências são mecanismos possíveis. Nenhum deles substitui a
análise de ameaças do fluxo completo. Um token tecnicamente seguro ainda pode ser
exposto em logs, por exemplo.

### Manutenibilidade

Manutenibilidade é a facilidade de entender, alterar, testar e corrigir o sistema.
Boas práticas, padrões de projeto, testes e um processo de engenharia consistente
ajudam a manter mudanças localizadas e previsíveis.

Ela também é uma propriedade econômica. Quando uma regra está duplicada ou os
módulos são fortemente acoplados, uma mudança pequena exige mais análise, cria
mais risco e aumenta o retrabalho. A [Aula 02](aula-02-manutenibilidade.md)
aprofunda esses mecanismos.

### Atributos que atravessam os quatro grupos

Observabilidade aparece repetidamente porque não é possível garantir uma
propriedade que a equipe não consegue enxergar. Logs, métricas e rastreamento
ajudam a saber se a aplicação está correta, rápida e segura. Eles também reduzem
o tempo para entender uma falha.

Usabilidade trata da capacidade de pessoas concluírem suas tarefas de maneira
eficaz. Rastreabilidade liga uma ação ao contexto que a produziu, o que ajuda em
auditoria e diagnóstico. Custo limita todas as alternativas: uma solução pode
atender tecnicamente aos requisitos e ainda ser inviável para a organização.

Esses atributos não formam departamentos isolados. Uma fila pode melhorar a
absorção de picos e a tolerância a falhas, mas dificulta rastrear uma operação por
várias etapas. Uma auditoria muito detalhada pode ajudar na investigação e, se
registrar dados demais, criar um risco de privacidade.

## Do requisito para uma decisão

Uma sequência útil para sair de uma preocupação vaga e chegar ao design é:

```text
cenário de negócio
    ↓
requisito mensurável
    ↓
restrições conhecidas
    ↓
alternativas e trade-offs
    ↓
decisão e mecanismo
    ↓
medição em execução
```

Considere uma conta que não pode ficar inconsistente. Primeiro, a equipe descreve
o cenário de falha e o estado correto esperado. Depois, define como medir
divergências e quais limites são aceitáveis. Só então compara transação,
idempotência, compensação ou outro mecanismo compatível com a arquitetura. Pular
diretamente para uma tecnologia impede saber se ela resolve o problema certo.

## Não existe solução perfeita

Requisitos de qualidade disputam recursos e introduzem consequências. Essa troca
é o *trade-off*. Uma linguagem pode oferecer vantagens técnicas, mas ser uma má
escolha se ninguém da equipe souber mantê-la. Uma plataforma gerenciada pode
reduzir trabalho operacional, mas ter custo proibitivo. Criptografia adicional
pode melhorar a proteção e aumentar a latência.

Uma decisão precisa considerar, no mínimo:

1. o requisito de qualidade que deve melhorar;
2. a evidência que mostrará se houve melhora;
3. as restrições de prazo, custo, equipe e tecnologia;
4. as alternativas viáveis;
5. os benefícios, custos e novos riscos de cada alternativa;
6. a forma de observar o resultado e revisar a escolha.

!!! example "Exemplo de decisão"
    Uma API sofre picos curtos de leitura. Adicionar cache pode reduzir a latência,
    mas algumas informações precisam refletir alterações imediatamente. Em vez de
    armazenar todas as respostas, a equipe pode limitar o cache a dados estáveis,
    definir tempo de expiração e medir taxa de acerto e desatualização. A decisão
    fica ligada ao problema e pode ser verificada.

## O que é arquitetura de software?

As definições apresentadas no material convergem em alguns pontos: estrutura de
alto nível, decomposição e composição de elementos, comunicação, distribuição,
características de qualidade e decisões importantes.

Uma definição operacional para a disciplina é:

> Arquitetura de software é tomar decisões estruturais para que um sistema atenda
> seus requisitos de qualidade dentro das restrições existentes.

O arquiteto não escolhe apenas tecnologias. Ele identifica forças em conflito,
torna hipóteses explícitas, compara alternativas, registra consequências e ajuda
a equipe a verificar se a arquitetura continua adequada durante a evolução do
sistema.

O trabalho também envolve comunicação. Uma decisão que existe apenas na cabeça
de uma pessoa não orienta implementação nem operação. Diagramas, contratos,
registros de decisão e exemplos executáveis tornam o raciocínio acessível às
equipes que serão afetadas.

Restrições fazem parte da arquitetura. Prazo de entrega, orçamento, regras
regulatórias, tecnologia já adotada, experiência da equipe e dependências externas
delimitam o espaço de solução. Ignorá-las não produz uma arquitetura mais pura;
produz uma proposta que talvez não possa ser executada.

Uma decisão é arquitetural quando alterá-la depois custa caro ou afeta muitas
partes. O formato dos serviços, a estratégia de persistência, os limites entre
módulos e o modelo de comunicação costumam ter esse peso. Um detalhe local de
implementação normalmente não tem.

## IA como apoio à engenharia

A IA acelera implementação, exploração de alternativas e produção de testes. Ela
também pode reduzir erros mecânicos. Ainda assim, não conhece automaticamente
todas as restrições do negócio, os riscos aceitos pela organização nem a
capacidade operacional da equipe.

Por isso, a decisão final continua exigindo julgamento humano. Uma sugestão deve
ser confrontada com evidências, custos e consequências. A IA funciona melhor como
instrumento de análise do que como fonte de autoridade arquitetural.

## Trilha da disciplina

Depois desta introdução, o curso aprofunda requisitos de qualidade e mecanismos
para implementá-los:

1. manutenibilidade, padrões, testes e processo de engenharia;
2. confiabilidade, tratamento de erros, CI/CD e monitoramento;
3. escalabilidade, processamento e infraestrutura;
4. segurança, autenticação, autorização e práticas ao longo do ciclo.

Docker aparece como base operacional para empacotar e executar a aplicação de
forma reproduzível. O trabalho da disciplina conecta essas decisões em um projeto
que evolui durante o semestre.
