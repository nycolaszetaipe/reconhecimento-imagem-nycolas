# Teste Assistente Code - Exemplos de Python

Este projeto contém exemplos educacionais de código Python, com foco em debug, boas práticas (Clean Code) e otimização de algoritmos. É um conjunto de exercícios com explicações detalhadas sobre correção de erros e refatoração.

## 📁 Estrutura do Projeto

```
teste-assistent-code/
├── README.md                      # Este arquivo
├── debug.py                       # Código corrigido de cálculo de compras
├── explicacao_debug.md           # Documentação dos erros em debug.py
├── num.primos.py                 # Algoritmo para verificar números primos
├── explicacao_num_primo.md       # Documentação do algoritmo de primalidade
├── refatoracao.py                # Código refatorado para calcular estatísticas
└── explicacao_refatoracao.md     # Documentação da refatoração
```

## 🎯 Conteúdo

### 1. Debug de Código - Cálculo de Compras

**Arquivo**: [debug.py](debug.py)

Um programa que calcula o total de uma compra com três itens, aplicando imposto (10%) e desconto (cupom).

#### Erros Encontrados e Corrigidos:

1. **Erro de Sintaxe** - String sem aspas no prompt `input()`
2. **Erro de Tipo** - Conversão de string para número não realizada
3. **Erro de Formatação** - F-string não prefixada com `f`
4. **Erro de Indentação** - Bloco dentro de `if` não indentado

#### Principais Correções:

- ✅ Conversão explícita de `input()` para `int` e `float`
- ✅ Uso correto de f-strings para formatação
- ✅ Indentação adequada em blocos condicionais
- ✅ Função auxiliar `format_currency()` para consistência
- ✅ Melhor organização com função `main()`

Para mais detalhes, veja [explicacao_debug.md](explicacao_debug.md)

---

### 2. Verificação de Números Primos

**Arquivo**: [num.primos.py](num.primos.py)

Algoritmo otimizado para verificar se um número é primo.

#### Características:

- **Tempo**: O(√n) - muito eficiente para números grandes
- **Espaço**: O(1) - uso constante de memória
- **Validação**: Trata tipos incorretos e números negativos
- **Docstring**: Completa com exemplos de uso

#### Estratégia do Algoritmo:

1. Casos especiais: números ≤ 1 retornam `False`
2. Números 2 e 3 retornam `True` (primos base)
3. Elimina múltiplos de 2 e 3 imediatamente
4. Verifica divisores da forma 6k ± 1 até √n

#### Exemplo de Uso:

```python
from num.primos import is_prime

numeros = [2, 3, 4, 17, 20, 23, 29]
for num in numeros:
    print(f"{num} é primo? {is_prime(num)}")
```

Para mais detalhes, veja [explicacao_num_primo.md](explicacao_num_primo.md)

---

### 3. Refatoração - Cálculo de Estatísticas

**Arquivo**: [refatoracao.py](refatoracao.py)

Função refatorada que calcula estatísticas de uma lista de números seguindo princípios de Clean Code.

#### Funcionalidades:

- Calcula **total** (soma)
- Calcula **média** aritmética
- Encontra **valor máximo**
- Encontra **valor mínimo**
- **Validação** de entrada (lista vazia)
- **Verificação** de tipos (todos números)

#### Exemplo de Uso:

```python
from refatoracao import calculate_list_statistics

numeros = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
total, media, maximo, minimo = calculate_list_statistics(numeros)

print(f"Total: {total}")
print(f"Média: {media}")
print(f"Maior: {maximo}")
print(f"Menor: {minimo}")
```

Para mais detalhes, veja [explicacao_refatoracao.md](explicacao_refatoracao.md)

---

## 🚀 Como Usar

### Executar o programa de debug (cálculo de compras):

```bash
python debug.py
```

Será solicitado:
- Nome do cliente
- Quantidade e preço de 3 itens
- Percentual do desconto (opcional)

### Executar verificação de números primos:

```bash
python num.primos.py
```

Mostra se os números `[1, 2, 3, 4, 17, 18, 19, 20, 23, 29, 30]` são primos.

### Executar cálculo de estatísticas:

```bash
python refatoracao.py
```

Calcula e exibe estatísticas da lista `[23, 7, 45, 2, 67, 12, 89, 34, 56, 11]`.

---

## 📚 Conceitos de Clean Code Aplicados

### 1. **Nomes Descritivos**
- Variáveis e funções com nomes que explicam sua função
- Exemplos: `format_currency()`, `calculate_list_statistics()`, `is_prime()`

### 2. **Funções Pequenas e Focadas**
- Cada função tem uma responsabilidade clara
- Evita código duplicado

### 3. **Validação de Entrada**
- Trata tipos incorretos com `isinstance()`
- Valida dados vazios
- Levanta exceções apropriadas (`TypeError`, `ValueError`)

### 4. **Documentação**
- Docstrings completas com descrição, argumentos, retorno e exemplos
- Comentários que explicam o "por quê", não o "o quê"

### 5. **Uso de Funções Built-in**
- `sum()`, `max()`, `min()`, `len()` em vez de loops manuais
- Código mais legível e eficiente

### 6. **F-strings Modernas**
- Formatação clara e pythônica
- Melhor legibilidade que `format()` ou `%`

### 7. **Bloco Principal**
```python
if __name__ == "__main__":
    # Código de execução
```
- Permite importar módulos sem executar código automaticamente
- Facilita testes e reutilização

---

## 🧪 Exemplos de Saída

### Debug.py
```
===============================
 Cliente: João Silva
===============================
 Item 1:        R$ 50.00
 Item 2:        R$ 75.50
 Item 3:        R$ 25.00
-------------------------------
 Subtotal:      R$ 150.50
 Imposto (10%): R$ 15.05
 Desconto (10%): -R$ 15.05
===============================
 TOTAL:         R$ 150.50
===============================
```

### Num.primos.py
```
1 é primo? False
2 é primo? True
3 é primo? True
4 é primo? False
17 é primo? True
20 é primo? False
23 é primo? True
```

### Refatoracao.py
```
Total: 346
Média: 34.6
Maior: 89
Menor: 2
```

---

## 🔍 Lições Aprendidas

Este projeto demonstra:

1. ✅ Como identificar e corrigir erros comuns em Python
2. ✅ Importância de validação de entrada
3. ✅ Como otimizar algoritmos (complexidade O(√n) vs O(n))
4. ✅ Princípios de Clean Code aplicáveis em produção
5. ✅ Uso de docstrings e documentação clara
6. ✅ Formatação e apresentação de dados

---

## 📖 Documentação Adicional

Cada arquivo Python possui uma documentação markdown associada:

- [explicacao_debug.md](explicacao_debug.md) - Análise detalhada dos 5 erros corrigidos
- [explicacao_num_primo.md](explicacao_num_primo.md) - Algoritmo de primalidade explicado passo a passo
- [explicacao_refatoracao.md](explicacao_refatoracao.md) - Clean Code e refatoração linha a linha

---

## 💡 Dicas de Uso

1. **Para Aprendizado**: Leia as documentações `.md` antes de ver o código.
2. **Para Prática**: Tente recriar os erros originais e depois corrigi-los.
3. **Para Implementação**: Adapte o padrão de estrutura para seus projetos.
4. **Para Otimização**: Estude o algoritmo de números primos e aplique em outros contextos.

---

## 🔧 Requisitos

- Python 3.6+
- Nenhuma dependência externa (biblioteca padrão apenas)

---

## 📝 Licença

Este projeto é fornecido como material educacional.

---

## ✨ Autor

Desenvolvido como exemplo educacional para demonstração de boas práticas em Python e Clean Code.

