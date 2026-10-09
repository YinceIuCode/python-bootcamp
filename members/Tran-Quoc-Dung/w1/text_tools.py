def word_count(text: str) -> dict[str, int]:
    special=['!','@','#','$','%','^','&','*','(',')','-','_','+','=','','.']
    return dict(sorted(sorted(dict((word, "".join([char for char in text if char not in special]).lower().split(" ").count(word)) for word in "".join([char for char in text if char not in special]).lower().split(" ")).items(), key = lambda dict_key : dict_key[0]), key = lambda dict_key : dict_key[1]))
    
def top_k(text: str, k: int) -> list[tuple[str, int]]:
    return [word for word in list(word_count(text).items()) if word[1] >= k]

print(top_k("Git is fast. Git is fun!", 2))
<<<<<<< HEAD
print(top_k("Git is fast. Git is fun!", 1))
=======
print(top_k("Git is fast. Git is fun!", 1))
>>>>>>> cf1984e (feat: adding w1-2 homework file text_tools.py)
