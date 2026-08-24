# Aula 04 — Confiabilidade

Confiabilidade é a capacidade de o software funcionar corretamente e de forma
consistente. Ela depende de decisões tomadas durante desenvolvimento, manutenção
e operação, não apenas da infraestrutura onde o sistema executa.

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
- Entender o papel de testes e tratamento de erros.
- Relacionar CI/CD e automação à redução de falhas.
- Definir sinais úteis para monitorar aplicação e infraestrutura.

## Confiabilidade e disponibilidade

Um sistema confiável produz o resultado correto de maneira consistente.
Disponibilidade mede a proporção de tempo em que o serviço permanece utilizável.
Taxa de respostas bem-sucedidas também pode compor essa avaliação.

As duas propriedades não são sinônimas. Uma API pode responder rapidamente com
status `200` e calcular um saldo incorreto. Ela está disponível do ponto de vista
da rede, mas não é confiável. Também pode recusar corretamente uma entrada inválida
com `400`; essa resposta não representa uma falha de disponibilidade.

Uma forma simples de calcular disponibilidade é:

```text
disponibilidade = tempo operacional / tempo total observado
```

Na prática, a definição precisa dizer o que conta como operacional. Responder
abaixo de uma meta de latência, atender uma região específica e concluir uma
transação podem fazer parte do indicador.

## Metas de disponibilidade

Plataformas públicas costumam manter páginas de status para comunicar incidentes
e histórico de operação. Uma meta percentual pode parecer próxima de 100%, mas
cada casa decimal reduz muito o tempo tolerado de falha.

| Meta | Nome comum | Indisponibilidade aproximada por ano | Por mês |
|---:|---|---:|---:|
| 99% | dois noves | 3 dias, 15 h e 39 min | 7 h e 18 min |
| 99,9% | três noves | 8 h e 45 min | 43 min |
| 99,99% | quatro noves | 52 min | 4 min e 23 s |
| 99,999% | cinco noves | 5 min e 15 s | 26 s |
| 99,9999% | seis noves | 31 s | 2,6 s |

Esse tempo funciona como um orçamento de indisponibilidade. Se a meta mensal de
99,9% já consumiu 40 minutos, restam poucos minutos antes de violá-la.

Metas maiores exigem redundância, automação, observação e resposta a incidentes
mais rigorosas. O custo aumenta, por isso o número deve refletir impacto de negócio
e expectativa dos usuários. Buscar seis noves para um sistema interno pouco usado
pode consumir recursos que trariam mais valor em outro lugar.

## Como aumentar a confiabilidade

O material organiza as práticas em testes, tratamento de erros, integração
contínua, entrega contínua, automação e monitoramento. Elas formam uma cadeia:
prevenir defeitos, detectar problemas cedo, impedir uma entrega inadequada e
observar o comportamento real.

## Testes de software

Testar é verificar se o software funciona de acordo com o comportamento
especificado. Testes manuais ajudam na exploração, mas são caros para repetir.
Testes automatizados oferecem retorno frequente e consistente.

| Nível | Escopo | Falha que ajuda a localizar |
|---|---|---|
| Unidade | Regra ou componente isolado | Erro de lógica local |
| Integração | Colaboração com banco, fila ou serviço | Contrato ou configuração incompatível |
| Ponta a ponta | Fluxo completo como o usuário o executa | Falha entre várias camadas |

JUnit e Mockito são comuns no ecossistema Java; `pytest` em Python; Selenium em
fluxos de navegador. A ferramenta é secundária. O conjunto de testes deve cobrir
riscos importantes, executar com estabilidade e indicar claramente o que quebrou.

Mais testes não garantem mais confiabilidade. Testes que nunca falham diante de um
defeito, dependem de ordem ou oscilam sem mudança reduzem a confiança no pipeline.

## Tratamento de erros

Linguagens oferecem mecanismos como `try` e `catch`, e frameworks fornecem
validação de entrada. Tratar um erro não significa esconder a exceção. É preciso
decidir onde recuperar, onde converter para uma resposta conhecida e onde
interromper o fluxo.

Uma boa resposta serve a dois públicos:

- pessoas precisam de uma mensagem clara e uma ação possível;
- sistemas precisam de status e estrutura estáveis para decidir o próximo passo.

Em uma API HTTP, o código informa a categoria do resultado:

| Situação | Código comum | Significado para o consumidor |
|---|---:|---|
| Entrada inválida | `400` | Corrigir os dados antes de repetir |
| Identidade ausente ou inválida | `401` | Autenticar novamente |
| Operação não permitida | `403` | A identidade não possui autorização |
| Recurso inexistente | `404` | O identificador não foi encontrado |
| Conflito com o estado atual | `409` | Reavaliar o estado antes de repetir |
| Falha inesperada do servidor | `500` | A operação não pôde ser concluída |

Retornar `200` com uma mensagem de erro no corpo prejudica monitoramento e força
cada integração a interpretar texto. Retornar `500` para uma validação também é
incorreto, pois sugere que repetir sem alterar a entrada pode funcionar.

```java
try {
    return service.create(request);
} catch (DuplicateResourceException error) {
    throw new ResponseStatusException(HttpStatus.CONFLICT, error.getMessage());
}
```

O exemplo mostra a tradução de uma condição conhecida. Falhas inesperadas ainda
devem ser registradas com contexto útil, sem vazar segredo ou dado pessoal para a
resposta.

## Integração contínua

Integração contínua, ou CI, usa um repositório central e práticas que integram
mudanças pequenas com frequência. Apenas armazenar código no Git não basta. A
mudança precisa receber validação automática e retorno rápido.

Ao abrir ou atualizar um pull request, o pipeline pode:

1. instalar dependências em um ambiente limpo;
2. compilar a aplicação;
3. executar testes automatizados;
4. verificar cobertura e análise estática;
5. impedir a integração se uma política falhar.

O ambiente limpo reduz o risco de o software funcionar apenas na máquina de quem
desenvolveu. O bloqueio automático também evita depender da memória de uma pessoa
para repetir todas as verificações.

## Entrega contínua

Entrega contínua, ou CD, mantém o software pronto para ser implantado por um
processo simples e reproduzível. O pipeline deve parar quando encontra um
problema, evitando promover um artefato que falhou em uma etapa anterior.

```text
pull request
    ↓
testes e análise
    ↓
integração na branch principal
    ↓
imagem Docker versionada
    ↓
publicação no registro
    ↓
deploy e verificação
```

GitHub Actions, Jenkins e CircleCI são ferramentas possíveis. Entre as tarefas
citadas no material estão executar testes em pull requests, verificar cobertura,
criar e publicar imagens Docker, notificar usuários e automatizar o deploy.

Automação melhora repetibilidade e rastreabilidade, mas também precisa ser
testada. Permissões excessivas, dependências sem versão e ausência de estratégia
de reversão transformam o pipeline em uma nova fonte de risco.

## Monitoramento

Monitorar é observar o sistema depois que ele entra em execução. Aplicação,
servidor, banco de dados e integrações externas podem falhar de formas diferentes,
então é preciso combinar sinais.

| Sinal | Pergunta respondida | Exemplo |
|---|---|---|
| Logs | O que aconteceu em um evento específico? | Erro com identificador da requisição |
| Métricas | O comportamento mudou ao longo do tempo? | Latência, erros e uso de CPU |
| Rastreamento | Onde uma requisição distribuída gastou tempo? | Chamada lenta a um serviço externo |
| Alerta | É necessário agir agora? | Taxa de erro acima do limite por cinco minutos |

Grafana pode visualizar métricas; Logstash participa de pipelines de logs;
Datadog oferece recursos gerenciados de observabilidade. A ferramenta não define
o que importa. Os sinais devem estar ligados a efeitos para o usuário e a ações
que a equipe consegue executar.

!!! example "API de pagamentos"
    Além de CPU e memória, uma API de pagamentos deve acompanhar taxa de aprovação,
    respostas por código HTTP, latência por integração, transações duplicadas e
    divergências de estado. Métricas apenas de infraestrutura não revelam uma
    cobrança incorreta.

## Confiabilidade ao longo do ciclo

As práticas se complementam:

- testes previnem regressões conhecidas;
- tratamento de erros mantém contratos previsíveis;
- CI detecta problemas antes da integração;
- CD reduz variação e trabalho manual no deploy;
- monitoramento revela o que os testes não anteciparam;
- incidentes geram aprendizado para novos testes, alertas e decisões.

Confiabilidade não é um componente que se adiciona no final. É uma propriedade
construída e medida durante todo o ciclo de vida do software.
