# Aula 17 – Integração Contínua, Qualidade Automatizada, Métricas e Gestão de Defeitos

## Integrantes

- Renata G. Bueno


---

## 1. Repositório da Atividade

| Item | Descrição |
|--------|--------|
| Nome do repositório | localeats-ci-laboratorio |
| Link do repositório | https://github.com/yRenata/localeats-ci-laboratorio |

### Estrutura de Diretórios

```text
localeats-ci-laboratorio/
├── .github/
│   └── workflows/
│       └── quality.yml
├── tests/
│   ├── test_order.py
│   ├── test_order_bdd.py
│   ├── features/
│   │   └── order_total.feature
│   └── steps/
│       └── test_order_steps.py
├── order.py
├── pytest.ini
└── requirements.txt
```

---

## 2. Planejamento da Funcionalidade

| Item | Descrição |
|--------|--------|
| Título da Issue | Implementar cálculo do valor total do pedido |
| Objetivo da funcionalidade | Calcular automaticamente a soma dos itens do pedido |
| Link da Issue | https://github.com/yRenata/localeats-ci-laboratorio/issues/1 |

---

## 3. Teste Automatizado

| Item | Descrição |
|--------|--------|
| Tipo de teste | Unitário |
| Objetivo do teste | Verificar o cálculo correto do valor total, comportamento com lista vazia, aplicação de descontos e tratamento de erros (valores negativos e strings). | https://github.com/yRenata/localeats-ci-laboratorio/blob/feature/order-total/tests/test_order.py |

```python
import pytest
from order import calculate_total, apply_discount

def test_calculate_total():
    assert calculate_total([10, 20, 30]) == 60

def test_calculate_total_lista_vazia():
    assert calculate_total([]) == 0

def test_apply_discount():
    assert apply_discount(100, 10) == 90

def test_calculate_total_nao_deve_aceitar_valores_negativos():
    with pytest.raises(ValueError, match="Os valores dos itens não podem ser negativos"):
        calculate_total([-10, 20, 30])

def test_calculate_total_nao_deve_aceitar_strings():
    with pytest.raises(TypeError, match="Todos os itens devem ser numéricos"):
        calculate_total(["abc", 20, 30])
```

---

## 4. Pipeline de Integração Contínua

| Item | Descrição |
|--------|--------|
| Nome do workflow | Quality Check |
| Evento que dispara a execução | push e pull_request |
| Link para o workflow | https://github.com/yRenata/localeats-ci-laboratorio/blob/feature/order-total/tests/.github/workflows/quality.yml |
| Link da execução | https://github.com/yRenata/localeats-ci-laboratorio/actions |

```yaml
name: Quality Check

on:
  push:
  pull_request:

jobs:
  tests:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - run: pip install pytest pytest-bdd

      - run: pytest
```

---

## 5. Indicadores de Qualidade

| Indicador | Valor |
|------------|---------|
| Quantidade de testes executados | 8 |
| Quantidade de testes aprovados | 8 |
| Quantidade de testes com falha | 0 |
| Status final do pipeline | Sucesso |

---

## 6. Registro de Defeito

| Item | Descrição |
|--------|--------|
| Título do defeito | Erro no cálculo do valor total |
| Severidade | Alta |
| Link da Issue | https://github.com/yRenata/localeats-ci-laboratorio/issues/2 |

O defeito foi simulado alterando a função para retornar um valor incorreto. O problema foi identificado pela falha do teste automatizado durante a execução do pipeline. Após corrigir a implementação, os testes voltaram a ser aprovados.