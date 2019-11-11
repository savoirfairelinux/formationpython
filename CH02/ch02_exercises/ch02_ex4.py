def compter_lettres(s: str):
    d = {}
    for c in s:
        d[c] = (d[c] if c in d else 0) + 1
    return d

def compter_lettres2(s: str):
    return {c: s.count(c) for c in s}

print(compter_lettres2('mississippi'))