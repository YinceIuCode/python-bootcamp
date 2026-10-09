import re
from collections import Counter

def word_count(text: str, k: int) -> list[tuple[str, int]]:
    words = re.findall(r'\b\w+\b', text.lower())
    counts = Counter(words)
    return counts.most_common(k)