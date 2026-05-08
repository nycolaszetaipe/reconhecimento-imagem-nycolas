# debug.py corrigido

def format_currency(value):
    """Formata valores numéricos para o padrão de moeda brasileiro."""
    return f"R$ {value:.2f}"


def main():
    # ENTRADA DE DADOS
    # Correção de caracteres especiais para garantir compatibilidade
    cliente = input("Qual é seu nome? ")

    qtd1 = int(input("Quantidade do item 1: "))
    item1 = float(input("Preço do item 1? "))

    qtd2 = int(input("Quantidade do item 2: "))
    item2 = float(input("Preço do item 2? "))

    qtd3 = int(input("Quantidade do item 3: "))
    item3 = float(input("Preço do item 3? "))

    # CÁLCULOS DOS ITENS
    total_item1 = qtd1 * item1
    total_item2 = qtd2 * item2
    total_item3 = qtd3 * item3

    subtotal = total_item1 + total_item2 + total_item3
    imposto = subtotal * 0.10

    # DESCONTO
    # Conversão de input (string) para float para permitir cálculos matemáticos 
    desconto_input = input("Você tem um cupom de desconto? (Digite o percentual ou 0): ")
    desconto_percentual = float(desconto_input)
    desconto = subtotal * (desconto_percentual / 100)

    # TOTAL FINAL
    total = subtotal + imposto - desconto

    # EXIBIÇÃO
    linha = "=" * 31
    separador = "-" * 31

    print(linha)
    print(f" Cliente: {cliente}")
    print(linha)
    # Uso da função auxiliar para manter o código limpo (Clean Code)
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