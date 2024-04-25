# Crie uma tupla preenchida com os 10 filmes mais assistidos de todos os tempos, e depois mostre:
#
# Apenas os 3 primeiros mais assistidos
# Os últimos 2 mais assistidos
# A lista em ordem alfabética
# Em que posição está “O rei leão”

# 9. Os Vingadores (2012) – US$ 1.520 bilhões
# 8. O Rei Leão (2019) – US$ 1.663 bilhões
# 7. Jurassic World (2015) – US$ 1.671 bilhões
# 6. Homem-Aranha: Sem Volta Para Casa (2021) – US$ 1.921 bilhões
# 5. Vingadores: Guerra Infinita (2018) – US$ 2.052 bilhões
# 4. Star Wars: O Despertar da Força (2015) – US$ 2.071 bilhões
# 3. Titanic (1997) – US$ 2.264 bilhões
# 2. Avatar: O Caminho da Água (2022) – US$ 2.320 bilhões
# 1. Vingadores: Ultimato (2019) – US$ 2.799 bilhões
# 0. Avatar (2009) – US$ 4.03 bilhões

filmes = ('Avatar', 'Vingadores: Ultimato', 'Avatar: O Caminho da Água', 'Titanic',
          'Star Wars: O Despertar da Força', 'Vingadores: Guerra Infinita', 'Homem-Aranha',
          'Jurassic World', 'O Rei Leão', 'Os Vingadores')


for ele in range(0, 3):
    print(filmes[ele])

print('===============')

for ele in range(8, len(filmes)):
    print(filmes[ele])

print('===============')

print(sorted(filmes))

print('===============')

for ele in range(8, len(filmes), 4):
    print(filmes[ele])

