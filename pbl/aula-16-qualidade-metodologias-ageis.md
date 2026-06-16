# Aula 16 – Qualidade em Metodologias Ágeis

## Integrantes

- Renata G. Bueno


---

# 1. Análise de Práticas Ágeis no Processo

| Prática | Existe no processo? | Como é aplicada atualmente? | Pode ser melhorada? |
|----------|----------|----------|----------|
| Planejamento iterativo | Sim | Criação de user stories | Sim, com maior formalização dos requisitos.  |
| Priorização de funcionalidades | Parcial  | Baseada em feedbacks e metas.  | Sim, usando critérios objetivos de valor de negócio.  |
| Entregas incrementais | Sim  | Deploy de novas funções do app.  | Sim, automatizando testes para acelerar o ciclo.  |
| Feedback frequente | Sim  | Coleta após monitoramento pós-lançamento.  | Sim, integrando o cliente durante o desenvolvimento.  |
| Trabalho colaborativo | Sim | Integração entre design (Figma) e código.  | Sim, via Pair Programming para revisão técnica.  |
| Controle visual das atividades |Sim  | Utilização de ferramentas de gestão.  | Sim, com quadros Kanban mais detalhados (WIP).  |
| Melhoria contínua | Parcial  | Revisão baseada em experiência da equipe.  | Sim, através de retrospectivas formais e métricas.  |

### Conclusão

O processo atual possui boa base colaborativa, mas padece de informalidade na documentação e rastreabilidade. A maior oportunidade reside em transitar da execução baseada em consenso para uma baseada em dados, implementando métricas que permitam medir a qualidade de forma contínua, reduzindo retrabalho e aumentando a previsibilidade das entregas.

---

# 2. Propostas de Melhoria Ágil

| Melhoria Proposta | Metodologia Relacionada | Benefício Esperado |
|------------------|------------------------|--------------------|
| Implementar Code Review  | XP (Pair Programming)  | Aumento da qualidade do código e compartilhamento de conhecimento.    |
| Adotar TDD  | XP (Engenharia)  | Redução de bugs e garantia de que o código atende aos requisitos desde o início.  |
| Uso de Métricas de Fluxo  | Kanban  | Melhor identificação de gargalos para otimização do processo.  |
| Reuniões Diárias  | Scrum  | Alinhamento rápido e identificação imediata de impedimentos.  |

---

# 3. Definition of Ready (DoR)

Uma funcionalidade estará pronta para desenvolvimento quando:

1. A user story e o objetivo de negócio estão claramente definidos.
2. Os critérios de aceitação foram totalmente especificados.
3. Dependências externas foram mapeadas e resolvidas.
4. O esforço foi estimado pela equipe técnica.
5. Todas as dúvidas e ambiguidades pendentes foram eliminadas.

---

# 4. Definition of Done (DoD)

Uma funcionalidade será considerada concluída quando:

1. O código foi revisado por outro integrante (ex: Code Review).
2. Os testes unitários e de integração foram executados com sucesso.
3. A interface foi validada contra o protótipo e requisitos de acessibilidade.
4. A funcionalidade foi homologada com o Product Owner ou cliente.
5. O código está integrado à branch principal e testado no ambiente de staging.