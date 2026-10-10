def word_count(s: str) -> dict[str, int]:
	count = {};
	wl = s.lower().split()
	for item in wl:
		item = ''.join([char for char in item if char.isalnum()])
		count[item] = count.get(item,0) + 1
	return count

def top_k (s: str,k: int) -> list[tuple[str, int]]:
	s_count = word_count(s)
	k_list = []
	i = 0;
	for key in sorted(s_count, key=s_count.get,reverse=True):
		k_list.append((key,s_count[key]))
		i += 1
		if i == k:
			break
	return k_list
