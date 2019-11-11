from collections import defaultdict

def compter_lettres(s: str):
    d = {}
    for c in s:
        d[c] = (d[c] if c in d else 0) + 1
    return d

def compter_lettres2(s: str):
    return {c: s.count(c) for c in s}

def compter_lettres3(s: str):
    d = defaultdict(lambda: 0)
    for c in s:
        d[c] += 1
    return dict(d)

print(compter_lettres3('mississippi'))