import string
from collections import Counter

def word_count(text: str) -> dict[str, int]:
    clean_text = text.translate(str.maketrans("", "", string.punctuation)).lower()
    words = clean_text.split()
    return dict(Counter(words))


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)
    return Counter(counts).most_common(k)