def compter_lettres(s: str):
    d = {}
    for c in s:
        d[c] = (d[c] if c in d else 0) + 1
    return d

print(compter_lettres('mississippi'))