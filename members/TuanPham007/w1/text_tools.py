from collections import Counter
import re

def word_count(text: str) -> dict[str, int]:
    words = re.findall(r'\b\w+\b', text.lower())
    return dict(Counter(words))

def top_k(text: str, k: int) -> list[tuple[str, int]]:
    words = re.findall(r'\b\w+\b', text.lower())
    counts = Counter(words)
    return counts.most_common(k)