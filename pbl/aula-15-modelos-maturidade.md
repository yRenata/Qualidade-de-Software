# Aula 15 – Modelos de Maturidade

## Integrantes

- Renata G. Bueno

---

# 1. Diagnóstico de Maturidade

| Critério | Sim | Parcial | Não |
|-----------|-----|----------|-----|
| Os requisitos são documentados? | | X | |
| Existe controle de mudanças? | | | X |
| Há atividades de teste definidas? | X | | |
| Os defeitos são registrados? | | X | |
| O processo de desenvolvimento é conhecido por toda a equipe? | X | | |
| As tarefas são planejadas e acompanhadas regularmente? | X | | |
| Existe padronização para implementação de funcionalidades? | | X | |
| Os testes são executados antes da entrega das funcionalidades? | X | | |
| Há revisão de código ou validação por outro integrante da equipe? | | | X |
| A equipe utiliza ferramentas para gerenciamento das atividades? | X | | |
| Os artefatos do projeto são organizados e versionados? | X | | |
| Existe rastreabilidade entre requisitos e funcionalidades? | | X | |
| A equipe realiza retrospectivas ou reuniões de melhoria? | | X | |
| Existem métricas para acompanhar a qualidade? | | | | X |

### Nível de maturidade estimado

**Nível do CMMI ou MPS.BR...**

### Justificativa

A equipe opera em um Nível Gerenciado, evidenciado pela existência de um fluxo de trabalho estruturado que inclui desde o refinamento de user stories até o monitoramento pós-lançamento. Utilizamos práticas como Code Review, testes unitários, testes de interface (acessibilidade) e homologação com stakeholders. As oportunidades de melhoria residem na formalização da rastreabilidade total entre os requisitos e o código, bem como na adoção de métricas quantitativas de qualidade para medir o desempenho de cada ciclo.

---

# 2. Lacunas Identificadas

| Lacuna | Impacto |
|---------|----------|
| Ausência de métricas de qualidade | Dificulta o acompanhamento objetivo da saúde do projeto e a identificação de gargalos. |
| Rastreabilidade parcial | A falta de um vínculo claro entre requisitos e funcionalidades dificulta o controle de mudanças e a análise de impacto. |
| Revisão de código informal | Torna difícil analisar o histórico de falhas e aprender com erros recorrentes para prevenir retrabalho.   |
| Documentação de Requisitos | O fluxograma mostra "Análise", mas a formalização desses requisitos em ferramentas de rastreabilidade ainda é um ponto de atenção. |
| Métricas de Qualidade | O fluxo termina em "Monitoramento pós-lançamento", mas não há menção explícita de coleta de dados ou métricas para melhoria do processo. |
| Gestão de Mudanças | Embora o fluxo seja claro, o histórico de porquê certas decisões de design ou código foram tomadas nem sempre é rastreável. | 

---

# 3. Propostas de Melhoria

| Melhoria | Benefício |
|-----------|-----------|
| Definir métricas básicas de qualidade | Permitirá um acompanhamento mais preciso da evolução do projeto e da eficácia das entregas.   |
| Padronizar revisões de código | Garantirá maior controle sobre as mudanças e garantirá que todos os requisitos sejam testados e entregues.   |
| Melhorar a rastreabilidade entre requisitos e funcionalidades | Facilitará a análise de causa raiz, reduzindo a recorrência de problemas técnicos no LocalEats. |
| Implementar Rastreabilidade (RTM) | Garantir que cada User Story tenha um link direto para o código e para o caso de teste correspondente. |
| Definir KPIs de Processo | Monitorar métricas como Cycle Time (tempo de entrega) e taxa de reabertura de bugs para embasar decisões. |
| Centralização da Documentação | Manter o "Processo LocalEats" documentado em uma Wiki ou repositório centralizado, garantindo que o conhecimento não dependa apenas da memória da equipe. |

---

## Conclusão

O processo atual do LocalEats demonstra maturidade ao incorporar práticas de revisão e testes no ciclo de vida. Para evoluir para níveis superiores, devemos transitar de uma execução baseada em consenso para uma baseada em dados, implementando indicadores de desempenho e documentação formal que garantam a repetibilidade do sucesso independente de quem executa a tarefa.