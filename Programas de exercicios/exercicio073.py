#ordenando tuplas
times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio',
         'São Paulo', 'Atlético-MG', 'Atlético-PR', 'Cruzeiro',
         'Botafogo', 'Santos', 'Bahia', 'Corinthians', 'Ceará',
         'Fluminense', 'Vasco', 'Chapecoense', 'América-MG',
         'Sport', 'Vitória', 'Paraná Clube')
print(f'Times do Brasileirão {times}')
print('-=' * 50)
print(f'Os 5 primeiros times são {times[:5]}')
print('-=' * 50)
print(f'Os quatros últimos times são {times[-4:]}')
print('-=' * 50)
print(f'Os times em ordem alfabetica {sorted(times)}')
print('-=' * 50)
print(f'A Chapecoense está na {times.index("Chapecoense")+1}ª posição')