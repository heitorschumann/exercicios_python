f, o, p, d = map(int, input().split())
esmeraldas = 0
esmeraldas += f
esmeraldas += 2 * p
esmeraldas = (esmeraldas * 2) * o
esmeraldas = (esmeraldas * 4) * d

print(esmeraldas)
