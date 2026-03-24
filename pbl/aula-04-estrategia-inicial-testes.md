# Estratégia Inicial de Testes – LocalEats

## 1. Funcionalidades
- Recomendações personalizadas
- Busca por restaurantes
- Vizualizar cardápio e avaliações
- Salvar favoritos


---

## 2. Níveis de Teste

### Funcionalidade: Recomendações Personalizadas
- Unitário: validar lógica de recomendação
- Integração: uso de dados do usuário
- Sistema: sistema sugere restaurantes
- Aceitação: usuário recebe sugestões relevantes

### Funcionalidade: Busca por restaurantes
- Unitário: valida filtros (preço, localização, tipo)
- Integração: conexão com banco de restaurantes
- Sistema: usuário realiza bysca e recebe resultados coerentes
- Aceitação: usuário encontra restaurantes conforme seus requisitos

### Funcionalidade: Vizualizar Cardápio e Avaliações
- Unitário: valida exibição de dados
- Integração: integração com banco de dados de avaliações
- Sistema: usuário acessa restaurante e visualiza informações completas
- Aceitação: usuário entende cardápio e avaliações sem problemas

### Funcionalidade: Salvar Favoritos
- Unitário: validar inclusão/remoção de fav.
- Integração: salvar dados no banco
- Sistema: usuário adiciona e visualiza favoritos
- Aceitação: usuário cpnsegue acessar seus favoritos

---

## 3. Prioridades e Riscos

Alta prioridade:
- Busca por restaurantes → principal funcionalidade
- Vizualização do cardápio → essencial para o usuário

Justificativa:
Falhas nessas áreas impedem o uso da plataforma.

Média prioridade:
- Recomendações personalizadas → chance de gerar mais lucro

Justificativa: Afetam a experiência e pequena porcentagem do lucro.

Baixa prioridade: 
- Favoritos → não impede uso

Justificativa:
Não impede o uso do sistema, apenas gera desconforto em alguns usuários.

---

## 4. Pirâmide de Testes

- Maior foco: Testes unitários
- Médio foco: Testes de integração
- Menor foco: Testes de sistema e aceitação

Justificativa:
Testes unitários são mais rápidos, baratos e de certa maneira mais eficazes.
Testes de integração dão garantia de que os componentes funcionem juntos.
Testes de sistema são caros e lentos, usados apenas para validar principais fluxos.

---

## 5. Testes em Produção

- Uso de monitoramento de erros (logs)
- Testes A/B para novas funções
- Coleta de feedback dos usuários
- Aplicar em: Recomendações personalizadas e UX.

Justificativa:
Permite identificar e relatar problemas reais de uso e do sistema.