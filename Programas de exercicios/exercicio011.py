#programa que lê a altura e a largura em metros, calcule sua area e a quantidade de tinta nessesária para pintala, sabendo que cada litro de tinta pinta 2 metros quadrados
print ('para sabermos quantos litro de tinta, primeiro precisa: ')
la = float(input('largura de sua parede em metros: '))
al = float(input('altura da parede em metros: '))
l = (al*la)/2
print ('sua parede precisa de {} litros de tinta '.format(l))


