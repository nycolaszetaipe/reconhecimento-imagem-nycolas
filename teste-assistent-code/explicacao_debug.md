# Explicação de debug.py

Este arquivo documenta os erros encontrados em `debug.py` e explica por que cada problema ocorria.

## 1. Erro de sintaxe no prompt de entrada de dados

Linha original:
```python
item1 = float(input(Preço do item 1? ))
```

- Causa: o texto do prompt não estava entre aspas.
- Resultado: `SyntaxError` porque o Python interpretou `Preço` como um nome de variável.
- Correção: colocar a string entre aspas:
```python
item1 = float(input("Preço do item 1? "))
```

## 2. Conversão de tipo incorreta do desconto

Linha original:
```python
desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)
```

- Causa: `input()` retorna uma string.
- Resultado: `TypeError` ao tentar dividir a string por 100.
- Correção: converter o valor para número, por exemplo `float`:
```python
desconto_percentual = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_percentual / 100)
```

## 3. Formatação de string incorreta na impressão

Linha original:
```python
print(" Item 2:        R$ {total_item2:.2f}")
```

- Causa: a string não era uma f-string.
- Resultado: foi exibido literalmente `{total_item2:.2f}` em vez do valor formatado.
- Correção: usar f-string corretamente:
```python
print(f" Item 2:        R$ {total_item2:.2f}")
```

## 4. Erro de indentação no bloco condicional

Linha original:
```python
if desconto_cupom > 0: 
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

- Causa: o `print()` dentro do `if` não estava indentado.
- Resultado: `IndentationError` no Python.
- Correção: identar o bloco de código dentro do `if`:
```python
if desconto_percentual > 0:
    print(f" Desconto ({desconto_percentual:.0f}%): -R$ {desconto:.2f}")
```

## 5. Melhoria de legibilidade e robustez

No código corrigido, foram aplicadas as seguintes melhorias:

- Função `format_currency(value)` para formatar valores monetários de forma consistente.
- Função `main()` para organizar o fluxo do programa.
- Conversão explícita de `input()` para `int` e `float`.
- Uso de nomes de variáveis mais claros: `desconto_percentual` em vez de `desconto_cupom`.
- Impressão com `f-strings` para exibir valores formatados.
- Mantido o cálculo final:
  - `subtotal = total_item1 + total_item2 + total_item3`
  - `imposto = subtotal * 0.10`
  - `total = subtotal + imposto - desconto`

## Código corrigido

```python
def format_currency(value):
    return f"R$ {value:.2f}"


def main():
    cliente = input("Qual é seu nome? ")

    qtd1 = int(input("Quantidade do item 1: "))
    item1 = float(input("Preço do item 1? "))

    qtd2 = int(input("Quantidade do item 2: "))
    item2 = float(input("Preço do item 2? "))

    qtd3 = int(input("Quantidade do item 3: "))
    item3 = float(input("Preço do item 3? "))

    total_item1 = qtd1 * item1
    total_item2 = qtd2 * item2
    total_item3 = qtd3 * item3

    subtotal = total_item1 + total_item2 + total_item3
    imposto = subtotal * 0.10

    desconto_percentual = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
    desconto = subtotal * (desconto_percentual / 100)

    total = subtotal + imposto - desconto

    linha = "=" * 31
    separador = "-" * 31

    print(linha)
    print(f" Cliente: {cliente}")
    print(linha)
    print(f" Item 1:        {format_currency(total_item1)}")
    print(f" Item 2:        {format_currency(total_item2)}")
    print(f" Item 3:        {format_currency(total_item3)}")
    print(separador)
    print(f" Subtotal:      {format_currency(subtotal)}")
    print(f" Imposto (10%): {format_currency(imposto)}")
    if desconto_percentual > 0:
        print(f" Desconto ({desconto_percentual:.0f}%): -{format_currency(desconto)}")
    print(linha)
    print(f" TOTAL:         {format_currency(total)}")
    print(linha)


if __name__ == "__main__":
    main()
```

## Conclusão

Os erros originais eram causados por:
- sintaxe incorreta no prompt de `input()`;
- falta de conversão de tipos em `desconto_cupom`;
- uso incorreto de formatação de strings;
- indentação inválida no bloco `if`.

Após as correções, o programa está funcional e legível.
