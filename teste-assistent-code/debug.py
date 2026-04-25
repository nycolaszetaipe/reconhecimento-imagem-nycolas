# debug.py corrigido

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
