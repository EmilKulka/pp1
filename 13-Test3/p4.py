def f(d):
    Numery_rejestracyjne = []
    for i in range(len(d)):
        for j in range(len(d[i])):
            if d[i][j] == "in":
                Numery_rejestracyjne.append(d[i][0])
            if d[i][j] == "out":
                Numery_rejestracyjne.remove(d[i][0])
    Numery_rejestracyjne.sort()
    return Numery_rejestracyjne



print(f([["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"],
["BA111","in"],["BA123","out"],["KR234","in"]]))

