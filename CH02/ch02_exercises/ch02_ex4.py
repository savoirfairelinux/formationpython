def compter_letters(s: str):
    d = {}
    for c in s:
        d[c] = (d[c] or 0) + 1
    return d

print(compter_lettres('mississippi'))