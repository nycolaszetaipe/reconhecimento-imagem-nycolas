def is_prime(number):
    """
    Verifica se um número inteiro é primo.

    Um número primo é um número natural maior que 1 que não tem divisores positivos
    além de 1 e ele mesmo.

    Args:
        number (int): O número a ser verificado.

    Returns:
        bool: True se o número for primo, False caso contrário.

    Raises:
        TypeError: Se o input não for um inteiro.
        ValueError: Se o número for negativo.

    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(4)
        False
    """
    if not isinstance(number, int):
        raise TypeError("O input deve ser um inteiro.")

    if number < 0:
        raise ValueError("O número deve ser não-negativo.")

    # Casos especiais: números menores ou iguais a 1 não são primos
    if number <= 1:
        return False

    # 2 e 3 são primos
    if number <= 3:
        return True

    # Elimina múltiplos de 2 e 3
    if number % 2 == 0 or number % 3 == 0:
        return False

    # Verifica divisores da forma 6k ± 1 até a raiz quadrada de number
    divisor = 5
    while divisor * divisor <= number:
        if number % divisor == 0 or number % (divisor + 2) == 0:
            return False
        divisor += 6

    return True


if __name__ == "__main__":
    # Exemplos de uso
    test_numbers = [1, 2, 3, 4, 17, 18, 19, 20, 23, 29, 30]
    for num in test_numbers:
        result = is_prime(num)
        print(f"{num} é primo? {result}")