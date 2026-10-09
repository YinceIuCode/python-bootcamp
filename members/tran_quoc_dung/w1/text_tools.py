def word_count(text: str) -> dict[str, int]:
    special = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','','.']
    normalize_string = "".join([char for char in text if char not in special]).lower().split(" ")
    
    return dict(sorted(dict(sorted({word : normalize_string.count(word) for word in normalize_string}.items(), key = lambda dict_key : dict_key[0])).items(), key = lambda dict_key : dict_key[1]))
    
def top_k(text: str, k: int) -> list[tuple[str, int]]:
    return [word for word in list(word_count(text).items()) if word[1] >= k]

print(top_k("Git is fast. Git is fun!", 2))
print(top_k("Git is fast. Git is fun!", 1))
