def concatenate(s1: str, s2: str) -> str:
    comb = s1 + s2
    if len(comb) > 10:
        return ("Too long!")
    else:
        return comb    




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
