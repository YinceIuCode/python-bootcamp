"""Module for counting word frequencies and finding top-k frequent words in text."""


def word_count(text: str) -> dict[str, int]:
    """Count the occurrences of each word in a given text, ignoring case and punctuation.

    Args:
        text: The input string to process.

    Returns:
        A dictionary mapping each cleaned word to its frequency count.
    """
    result: dict[str, int] = {}
    text_lower = text.lower()
    text_list = text_lower.split()

    for word in text_list:
        cleaned_word = word.strip(".,!?;:\"'()[]{}")
        if cleaned_word:  # just a note that this line has been change for your safety
            result[cleaned_word] = result.get(cleaned_word, 0) + 1

    return result


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Find the top-k most frequent words in a text, sorted by frequency descending and then alphabetically.

    Args:
        text: The input string to process.
        k: The maximum number of top words to return.

    Returns:
        A list of tuples containing words and their corresponding counts.
    """
    counts = word_count(text)
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:k]


if __name__ == "__main__":
    print(word_count("Git is fun. Git is fast!"))
    print(top_k("Git is fun. Git is fast!", 2))
