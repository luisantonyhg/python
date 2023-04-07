# APELLIDOS: HUAMANI GONZALES
# NOMBRES: LUIS ANTONY
# ÚLTIMO DIGITO DNI: 2



DescripcionDenunciasPorComisionDeDelitos = ['Número de denuncias por comisión de delitos', 'Denuncias de delitos contra el patrimonio', 'Denuncias de delitos contra la vida, el cuerpo y la salud', 'Denuncias de delitos contra la seguridad pública', 'Denuncias de delitos contra la libertad'] 
CantidadesDenunciasPorComisionDeDelitos2011 = [240438, 168618, 28486, 15932, 15812] 
CantidadesDenunciasPorComisionDeDelitos2012 = [271813, 185357, 39744, 14839, 17848] 
CantidadesDenunciasPorComisionDeDelitos2013 = [299474, 204935, 33613, 28175, 18459] 
CantidadesDenunciasPorComisionDeDelitos2014 = [326578, 224753, 36643, 30388, 19379] 
CantidadesDenunciasPorComisionDeDelitos2015 = [349323, 242697, 37057, 40150, 18730] 
CantidadesDenunciasPorComisionDeDelitos2016 = [355876, 242653, 44342, 38150, 20428] 
CantidadesDenunciasPorComisionDeDelitos2017 = [399869, 265219, 50597, 49385, 22660]

valorMinimo2011Al2017 = 999999
valor_max_del_pat_2011_2017 = 0
print('Denuncias de delitos contra el patrimonio')
print('2011 =',CantidadesDenunciasPorComisionDeDelitos2011[1])
print('2012 =',CantidadesDenunciasPorComisionDeDelitos2012[1])
print('2013 =',CantidadesDenunciasPorComisionDeDelitos2013[1])
print('2014 =',CantidadesDenunciasPorComisionDeDelitos2014[1])
print('2015 =',CantidadesDenunciasPorComisionDeDelitos2015[1])
print('2016 =',CantidadesDenunciasPorComisionDeDelitos2016[1])
print('2017 =',CantidadesDenunciasPorComisionDeDelitos2017[1])
denunciaDel2011al2017 = [CantidadesDenunciasPorComisionDeDelitos2011[1],CantidadesDenunciasPorComisionDeDelitos2012[1],CantidadesDenunciasPorComisionDeDelitos2013[1],CantidadesDenunciasPorComisionDeDelitos2014[1],CantidadesDenunciasPorComisionDeDelitos2015[1],CantidadesDenunciasPorComisionDeDelitos2016[1],CantidadesDenunciasPorComisionDeDelitos2017[1]]
promedioFinal = 0
contador = 0
for inicio in denunciaDel2011al2017:
    contador += 1
    promedioFinal += inicio
    if valorMinimo2011Al2017 > inicio:
        valorMinimo2011Al2017 = inicio
    if valor_max_del_pat_2011_2017 < inicio:
        valor_max_del_pat_2011_2017 = inicio
print('El promedio es:',round(promedioFinal/contador, 2))
print('El valor mínimo es:',valorMinimo2011Al2017)
print('El valor máximo es:',valor_max_del_pat_2011_2017)
print()

valor_min_del_vid_2011_2017 = 999999
valor_max_del_vid_2011_2017 = 0
print('Denuncias de delitos contra la vida, el cuerpo y la salud')
print('2011 =',CantidadesDenunciasPorComisionDeDelitos2011[2])
print('2012 =',CantidadesDenunciasPorComisionDeDelitos2012[2])
print('2013 =',CantidadesDenunciasPorComisionDeDelitos2013[2])
print('2014 =',CantidadesDenunciasPorComisionDeDelitos2014[2])
print('2015 =',CantidadesDenunciasPorComisionDeDelitos2015[2])
print('2016 =',CantidadesDenunciasPorComisionDeDelitos2016[2])
print('2017 =',CantidadesDenunciasPorComisionDeDelitos2017[2])
del_vid_2011_2017 = [CantidadesDenunciasPorComisionDeDelitos2011[2],CantidadesDenunciasPorComisionDeDelitos2012[2],CantidadesDenunciasPorComisionDeDelitos2013[2],CantidadesDenunciasPorComisionDeDelitos2014[2],CantidadesDenunciasPorComisionDeDelitos2015[2],CantidadesDenunciasPorComisionDeDelitos2016[2],CantidadesDenunciasPorComisionDeDelitos2017[2]]
promedio = 0
cont = 0
for i in del_vid_2011_2017:
    cont += 1
    promedio += i
    if valor_min_del_vid_2011_2017 > i:
        valor_min_del_vid_2011_2017 = i
    if valor_max_del_vid_2011_2017 < i:
        valor_max_del_vid_2011_2017 = i
print('El promedio es:',round(promedio/cont, 2))
print('El valor mínimo es:',valor_min_del_vid_2011_2017)
print('El valor máximo es:',valor_max_del_vid_2011_2017)
print()

valor_min_del_seg_2011_2017 = 999999
valor_max_del_seg_2011_2017 = 0
print('Denuncias de delitos contra la seguridad pública')
print('2011 =',CantidadesDenunciasPorComisionDeDelitos2011[3])
print('2012 =',CantidadesDenunciasPorComisionDeDelitos2012[3])
print('2013 =',CantidadesDenunciasPorComisionDeDelitos2013[3])
print('2014 =',CantidadesDenunciasPorComisionDeDelitos2014[3])
print('2015 =',CantidadesDenunciasPorComisionDeDelitos2015[3])
print('2016 =',CantidadesDenunciasPorComisionDeDelitos2016[3])
print('2017 =',CantidadesDenunciasPorComisionDeDelitos2017[3])
del_seg_2011_2017 = [CantidadesDenunciasPorComisionDeDelitos2011[3],CantidadesDenunciasPorComisionDeDelitos2012[3],CantidadesDenunciasPorComisionDeDelitos2013[3],CantidadesDenunciasPorComisionDeDelitos2014[3],CantidadesDenunciasPorComisionDeDelitos2015[3],CantidadesDenunciasPorComisionDeDelitos2016[3],CantidadesDenunciasPorComisionDeDelitos2017[3]]
promedio = 0
cont = 0
for i in del_seg_2011_2017:
    cont += 1
    promedio += i
    if valor_min_del_seg_2011_2017 > i:
        valor_min_del_seg_2011_2017 = i
    if valor_max_del_seg_2011_2017 < i:
        valor_max_del_seg_2011_2017 = i
print('El promedio es:',round(promedio/cont, 2))
print('El valor mínimo es:',valor_min_del_seg_2011_2017)
print('El valor máximo es:',valor_max_del_seg_2011_2017)
