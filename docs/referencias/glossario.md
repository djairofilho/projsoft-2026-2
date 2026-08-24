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

**Rede Docker**
: Rede virtual que conecta containers e controla quais participantes conseguem
  se comunicar. Uma rede criada pelo usuário oferece nome próprio, isolamento e
  descoberta de containers por nome. Consulte a
  [referência rápida de Docker](docker.md#redes-docker).

**Driver de rede**
: Implementação usada pelo Docker para oferecer conectividade. O driver define
  onde a rede existe e como o tráfego circula; `bridge` é o driver comum para
  containers executados no mesmo host.

**Bridge**
: Rede privada criada no host Docker. A `bridge` padrão recebe containers que não
  informam uma rede, enquanto uma bridge criada pelo usuário permite organizar
  uma aplicação e resolver participantes pelo nome do container.

**Descoberta por nome**
: Capacidade de um container localizar outro pelo nome, como `banco`, sem fixar
  seu endereço IP interno. Está disponível nas redes Docker criadas pelo usuário.

**Publicação de porta**
: Mapeamento de uma porta da máquina para uma porta do container, configurado com
  `-p PORTA_HOST:PORTA_CONTAINER`. Publicar uma porta permite acesso externo e é
  diferente de conectar containers à mesma rede.

**Variável de ambiente**
: Par nome e valor fornecido ao processo no momento da execução. Em Docker, pode
  ser definida com `-e NOME=VALOR`, herdada com `-e NOME` ou carregada por
  `--env-file`. Não deve ser tratada como armazenamento seguro de segredos.

**Arquivo de ambiente**
: Arquivo de linhas `NOME=VALOR` fornecido com `--env-file`. Um exemplo pode ser
  versionado com valores fictícios, mas arquivos com credenciais reais devem
  permanecer fora do repositório.

**Docker Compose**
: Ferramenta que define e executa uma aplicação com vários containers a partir
  de um arquivo `compose.yaml`. Consulte a
  [referência rápida de Docker Compose](docker-compose.md).

**Arquivo Compose**
: Documento YAML que descreve serviços, redes, volumes e outras opções da
  aplicação. O nome preferencial é `compose.yaml`.

**Serviço Compose**
: Componente definido em `services` que descreve como criar um ou mais containers
  com a mesma imagem e configuração. Na rede do projeto, o nome do serviço também
  funciona como hostname.

**Volume nomeado**
: Armazenamento gerenciado pelo Docker e identificado por nome. Seu ciclo de vida
  é separado do container, permitindo recriar um serviço sem perder os dados.

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
