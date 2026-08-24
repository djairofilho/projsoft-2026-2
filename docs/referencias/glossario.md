# Glossário

## Arquitetura e qualidade

**Arquitetura de software**
: Decisões estruturais usadas para atender requisitos de qualidade dentro de
  restrições.

**Requisito funcional**
: Comportamento que o sistema deve oferecer.

**Requisito de qualidade**
: Condição de operação ou propriedade esperada, como segurança, desempenho ou
  manutenibilidade. Veja como especificá-lo na
  [Aula 01.1](../aulas/aula-01-requisitos-qualidade.md).

**Cenário de qualidade**
: Descrição verificável de fonte, estímulo, ambiente, artefato, resposta e medida.

**Restrição**
: Limite de prazo, custo, tecnologia, regulação ou capacidade da equipe que reduz
  o conjunto de alternativas viáveis.

**Decisão arquitetural**
: Escolha estrutural registrada com contexto, alternativas, consequências e
  evidências. Veja a [Aula 01.2](../aulas/aula-01-decisoes-arquiteturais.md).

**Trade-off**
: Consequência de obter um benefício enquanto se aceita outro custo ou risco.

**Confiabilidade**
: Capacidade de produzir resultados corretos e consistentes.

**Disponibilidade**
: Proporção de tempo em que um serviço permanece utilizável.

**SLI**
: Indicador que mede um aspecto do serviço, como proporção de checkouts
  concluídos corretamente.

**SLO**
: Meta definida para um SLI em uma janela de tempo.

**Orçamento de indisponibilidade**
: Parcela tolerada de resultados fora da meta durante a janela do SLO.

**Escalabilidade**
: Capacidade de manter o serviço quando carga ou volume variam.

## Design e evolução

**Acoplamento**
: Grau de dependência entre componentes.

**Coesão**
: Grau em que as responsabilidades de um componente pertencem ao mesmo propósito.

**SOLID**
: Cinco princípios para raciocinar sobre responsabilidades, extensão, contratos,
  interfaces e dependências.

**Strategy**
: Padrão que encapsula comportamentos intercambiáveis sob um contrato comum.

**Factory**
: Padrão que concentra a criação de objetos e esconde seus detalhes dos
  consumidores.

**Repository**
: Contrato que expressa operações de persistência na linguagem da aplicação e
  isola detalhes do banco de dados.

**Injeção de Dependência**
: Técnica que fornece colaboradores a um objeto externamente, tornando relações
  explícitas e substituíveis.

**Adapter**
: Padrão que traduz um contrato externo para a interface esperada pela aplicação.

**Decorator**
: Padrão que acrescenta comportamento ao redor de um objeto que preserva o mesmo
  contrato.

**Observer e Listener**
: Padrão em que interessados reagem a eventos sem que o publicador conheça cada
  implementação.

**Builder**
: Padrão que organiza a construção gradual e nomeada de objetos complexos.

**Composite**
: Padrão que permite tratar elementos individuais e composições por um contrato
  comum.

## Entrega e operação

**Imagem Docker**
: Pacote imutável que contém aplicação e dependências.

**Container**
: Execução isolada de uma imagem.

**Idempotência**
: Propriedade que permite repetir uma operação lógica sem produzir um novo efeito.
  Veja a [Aula 04.1](../aulas/aula-04-testes-erros.md).

**Integração contínua (CI)**
: Integração frequente de código acompanhada por validações automáticas.

**Entrega contínua (CD)**
: Processo reproduzível que mantém o software pronto para entrega ou automatiza
  sua publicação.

**Observabilidade**
: Capacidade de compreender o estado interno de um sistema a partir de sinais como
  logs, métricas e rastreamento. Veja a
  [Aula 04.2](../aulas/aula-04-entrega-observabilidade.md).

## Recursos de estudo

**Biblioteca Telles**
: Biblioteca do Insper que reúne o catálogo e o acesso institucional às bases de
  dados. O login remoto nas bases digitais é feito pelo OpenAthens.

**O’Reilly Learning**
: Plataforma de livros, cursos e vídeos técnicos disponível aos usuários
  elegíveis do Insper por acesso institucional. Veja o passo a passo e os livros
  indicados na página de
  [bibliografia e acesso à O’Reilly](bibliografia.md).
