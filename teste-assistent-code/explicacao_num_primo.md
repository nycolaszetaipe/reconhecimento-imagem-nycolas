# Explicação do código Python para verificar número primo

A função `is_prime(n)` recebe um número inteiro `n` e retorna `True` se o número for primo, ou `False` caso contrário.

## Como funciona

1. `if n <= 1:`
   - Números menores ou iguais a 1 não são considerados primos.
   - Nesse caso, a função retorna `False`.

2. `if n <= 3:`
   - Os números 2 e 3 são primos.
   - Se `n` for 2 ou 3, a função retorna `True`.

3. `if n % 2 == 0 or n % 3 == 0:`
   - Se `n` for divisível por 2 ou por 3, então não é primo.
   - A função retorna `False` para esses casos.

4. O laço `while i * i <= n:`
   - O valor de `i` começa em 5.
   - A verificação usa `i * i <= n` porque, se nenhum divisor for encontrado até a raiz quadrada de `n`, então `n` é primo.

5. `if n % i == 0 or n % (i + 2) == 0:`
   - O algoritmo testa divisores do tipo `i` e `i + 2`.
   - Isso cobre combinações de números da forma 6k - 1 e 6k + 1, que são os únicos candidatos possíveis além de 2 e 3.

6. `i += 6`
   - Após testar `i` e `i + 2`, o valor de `i` avança de 6 em 6.
   - Isso evita testar números que já foram excluídos por serem múltiplos de 2 ou 3.

7. `return True`
   - Se nenhum divisor for encontrado até a raiz quadrada de `n`, a função conclui que `n` é primo.

## Resumo

- A função trata casos especiais de forma rápida: números menores ou iguais a 1, e os primeiros primos 2 e 3.
- Em seguida, descarta múltiplos de 2 e 3.
- Por fim, verifica apenas os candidatos que podem ser primos, usando um passo de 6 em 6.
- Isso torna a função eficiente e correta para verificar primalidade de inteiros positivos.
