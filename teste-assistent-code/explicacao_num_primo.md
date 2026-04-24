# Explicação do Código Python para Verificar Número Primo

Este documento explica o funcionamento da função `is_prime(number)` implementada em Python, que verifica se um número inteiro é primo.

## O que é um Número Primo?

Um número primo é um número natural maior que 1 que possui apenas dois divisores positivos distintos: 1 e ele mesmo. Exemplos: 2, 3, 5, 7, 11, etc.

## Estrutura da Função

A função `is_prime(number)` segue uma abordagem eficiente baseada no algoritmo de verificação de primalidade, otimizado para eliminar candidatos desnecessários.

### 1. Validação de Entrada

```python
if not isinstance(number, int):
    raise TypeError("O input deve ser um inteiro.")

if number < 0:
    raise ValueError("O número deve ser não-negativo.")
```

- **Propósito**: Garante que o input seja válido antes de prosseguir.
- **Por que?**: Evita erros inesperados e melhora a robustez do código.

### 2. Casos Especiais

```python
if number <= 1:
    return False

if number <= 3:
    return True
```

- **Números ≤ 1**: Não são primos por definição.
- **2 e 3**: São os únicos primos pares e ímpares consecutivos, tratados diretamente.

### 3. Eliminação de Múltiplos de 2 e 3

```python
if number % 2 == 0 or number % 3 == 0:
    return False
```

- **Lógica**: Qualquer número divisível por 2 ou 3 (exceto 2 e 3) não é primo.
- **Eficiência**: Remove rapidamente a maioria dos candidatos compostos.

### 4. Verificação de Divisores Potenciais

```python
divisor = 5
while divisor * divisor <= number:
    if number % divisor == 0 or number % (divisor + 2) == 0:
        return False
    divisor += 6
```

- **Algoritmo**: Testa apenas números da forma 6k ± 1 (como 5, 7, 11, 13, etc.).
- **Razão**: Todos os primos maiores que 3 podem ser expressos nessa forma.
- **Otimização**: Incrementa o divisor em 6 para pular múltiplos de 2 e 3.
- **Condição de parada**: `divisor * divisor <= number` (até a raiz quadrada).

### 5. Conclusão

```python
return True
```

- Se nenhum divisor for encontrado, o número é primo.

## Exemplo de Execução

```python
if __name__ == "__main__":
    test_numbers = [1, 2, 3, 4, 17, 18, 19, 20, 23, 29, 30]
    for num in test_numbers:
        result = is_prime(num)
        print(f"{num} é primo? {result}")
```

Saída esperada:
```
1 é primo? False
2 é primo? True
3 é primo? True
4 é primo? False
17 é primo? True
18 é primo? False
19 é primo? True
20 é primo? False
23 é primo? True
29 é primo? True
30 é primo? False
```

## Complexidade e Eficiência

- **Tempo**: O(√n), onde n é o número testado.
- **Espaço**: O(1), constante.
- **Vantagens**: Eficiente para números grandes, evita verificações desnecessárias.

## Boas Práticas Aplicadas (Clean Code)

- **Nomes descritivos**: `number` em vez de `n`, `divisor` em vez de `i`.
- **Docstring completa**: Inclui descrição, argumentos, retornos, exceções e exemplos.
- **Tratamento de erros**: Validação de entrada com exceções apropriadas.
- **Comentários**: Explicam a lógica sem ser redundante.
- **Legibilidade**: Código estruturado e fácil de seguir.
- **Testes**: Bloco `if __name__ == "__main__"` para demonstração.

Esta implementação é robusta, eficiente e segue princípios de código limpo.
