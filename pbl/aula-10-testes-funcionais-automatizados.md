# 🧩 Atividade PBL – Aula 10  
## Testes Funcionais Automatizados – LocalEats

---

## 👥 Integrante(s)
- Renata G. Bueno

---

## 🔹 1. Fluxo funcional escolhido

### 📌 Fluxo:
Login de usuário

🔎 **Descrição**  
Permite que o usuário faça autenticação no sistema utilizando e-mail e senha.

🎯 **Importância**  
O login é um fluxo essencial, pois sem ele o usuário não consegue acessar as funcionalidades principais da plataforma.

---

## 🔹 2. Teste com Codegen

### 💻 Comando utilizado

```bash
playwright codegen https://local-eats-unisenac.vercel.app/
```

### 🔗 Link para o código gerado

👉 https://github.com/seu-repositorio/tests/codegen_login.py

### 🧠 Observações

- O Codegen facilitou a criação inicial do teste 
- O código gerado automaticamente ficou muito extenso  
- Foi necessário ajustar seletores e organizar melhor o código
- Alguns elementos precisaram de seletores mais específicos 

---

## 🔹 3. Teste automatizado com Pytest

### 🔗 Link para o teste

👉 https://github.com/seu-repositorio/tests/test_login.py

### 📌 O que o teste faz?

- Abre a aplicação no navegador
- Preenche os campos de login 
- Realiza a autenticação do usuário
- Verifica se o login foi realizado corretamente 

---

## 🔹 4. Refatoração com Page Object Model (POM)

### 🔗 Link para Page Object

👉 https://github.com/seu-repositorio/pages/login_page.py

### 🔗 Link para teste refatorado

👉 https://github.com/seu-repositorio/tests/test_login.py

### 🧠 Melhorias realizadas

- Separação da lógica da interface e do teste  
- Melhor organização do código  
- Facilidade para manutenção futura
- Reaproveitamento dos métodos criados

---

## 🔹 5. Execução dos testes

### ▶️ Comando

```bash
pytest
```

### 📊 Resultado

- Total de testes: 1  
- Testes passaram: 1  
- Testes falharam: 0  

### 📸 Evidência

![alt text](image.png)

---

## 🔹 6. Análise crítica

- Seletores genéricos causaram falhas
- Foi necessário utilizar id e class
- O Codegen gera código pouco organizado

---

## 🔹 7. Reflexão

- Pequenos detalhes impactam os testes  
- Devem focar em fluxos críticos  
- Aumentam a confiança no sistema  

---

## 💡 Conclusão

Com essa atividade foi possível desenvolver e automatizar o fluxo de login utilizando Playwright e Pytest. Além da criação do teste automatizado, também foi necessário ajustar seletores, corrigir falhas e refatorar o código utilizando Page Object Model.

A prática mostrou a importância da automação de testes para validar funcionalidades importantes do sistema, além de demonstrar como boas práticas ajudam a tornar os testes mais organizados, reutilizáveis e fáceis de manter.