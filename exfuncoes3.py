s = input()
n = input()
m = input()

n = int(n)


def estilo(simbolo, numero, mensagem):
    res = str(f"{numero * simbolo}{mensagem}{numero * simbolo}")
    return res


print(estilo(s, n, m))
