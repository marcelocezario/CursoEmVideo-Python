altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))
area = altura * largura

print('Para pintar essa parede ({}m²), é necessário {} litros de tinta'.format(area,area/2))