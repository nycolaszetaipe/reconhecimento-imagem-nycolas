def calculate_list_statistics(numbers):
    """
    Calcula estatísticas básicas de uma lista de números.

    Args:
        numbers (list): Uma lista de números (int ou float).

    Returns:
        tuple: (total, average, maximum, minimum)

    Raises:
        ValueError: Se a lista estiver vazia.
        TypeError: Se a lista contiver elementos não numéricos.
    """
    if not numbers:
        raise ValueError("A lista não pode estar vazia.")

    # Verifica se todos os elementos são números
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("Todos os elementos da lista devem ser números.")

    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return total, average, maximum, minimum


if __name__ == "__main__":
    # Exemplo de uso
    numbers = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    total, average, maximum, minimum = calculate_list_statistics(numbers)

    print(f"Total: {total}")
    print(f"Média: {average}")
    print(f"Maior: {maximum}")
    print(f"Menor: {minimum}")