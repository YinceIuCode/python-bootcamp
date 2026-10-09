import string 

def word_count(text:str) -> dict[str, int]:
    text = text.lower()
    translator = str.maketrans("","",string.punctuation)
    clean_word = text.translate(translator)

    words = clean_word.split()

    counts = {}
    for word in words:
        if word.islower():
            counts[word] = counts.get(word, 0) + 1

    return counts

def get_count(item:tuple[str,int]) -> int:
    return item[1]
    
def top_k (text:str, k:int) -> list[tuple[str, int]]:
    counts = word_count(text)
    sorted_items = sorted(counts.items(), key=get_count, reverse=True)
    return sorted_items[:k]

# print(word_count("Git is fun. Git is fast!"))
# print(top_k("Git is fun. Git is fast!", 2))

