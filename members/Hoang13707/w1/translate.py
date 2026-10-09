from typing import Union

def reverse_sequence(data: Union[list, str]) -> Union[list, str]:
    return data[::-1]


def reverse_in_place(data: list) -> None:
    data.reverse()


def primes_up_to(n: int) -> list[int]:
    primes = []
    for is_prime in range(2, n + 1):
        if all(is_prime % i != 0 for i in range(2, int(is_prime ** 0.5) + 1)):
            primes.append(is_prime)
    return primes