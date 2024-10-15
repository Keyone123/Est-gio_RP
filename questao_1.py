def fibonacci_sequence(limite):
    if limite == 0:
        return 0
    elif limite == 1:
        return 1
    else:
        return fibonacci_sequence(limite - 1) + fibonacci_sequence(limite - 2)


def is_fibonacci_sequence(num):
    fib = fibonacci_sequence(num)
    if num in [fibonacci_sequence(i) for i in range(num)]:
        return f'{num} pertence a sequência de Fibonacci'
    else:
        return f'{num} não pertence a sequência de Fibonacci'

num = int(input('Digite um número: '))
print(is_fibonacci_sequence(num))
