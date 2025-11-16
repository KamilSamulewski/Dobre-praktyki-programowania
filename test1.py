import re

import pytest


def is_palindrome(text: str) -> bool:
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n musi być >= 0")
    if n in (0, 1):
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def count_vowels(text: str) -> int:
    vowels = set("aeiouy")
    return sum(1 for ch in text.lower() if ch in vowels)


def calculate_discount(price: float, discount: float) -> float:
    if not 0 <= discount <= 1:
        raise ValueError("discount musi być w zakresie 0–1")
    return price * (1 - discount)


def flatten_list(nested_list: list) -> list:
    result = []
    for el in nested_list:
        if isinstance(el, list):
            result.extend(flatten_list(el))
        else:
            result.append(el)
    return result


def word_frequencies(text: str) -> dict:
    cleaned = re.sub(r"[^\w\s]", "", text.lower())
    words = cleaned.split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


