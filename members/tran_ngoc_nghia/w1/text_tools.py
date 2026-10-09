def word_count(text: str) -> dict[str, int]:
    result = {}

    text = text.lower()

    text_list = text.split()

    for word in text_list:
        word = word.strip(".,!?;:\"'()[]{}")
        result[word] = result.get(word, 0) + 1

    return result


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)

    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:k]


if __name__ == "__main__":
    print(word_count("Git is fun. Git is fast!"))
    print(top_k("Git is fun. Git is fast!", 2))