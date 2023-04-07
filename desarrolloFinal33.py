# APELLIDOS: HUAMANI GONZALES
# NOMBRES: LUIS ANTONY
# ÚLTIMO DIGITO DNI: 2
asciiNombre = 786
asciiApellido = 1225
años = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
DescripcionDenunciasPorComisionDeDelitos = ['Número de denuncias por comisión de delitos', 'Denuncias de delitos contra el patrimonio', 'Denuncias de delitos contra la vida, el cuerpo y la salud', 'Denuncias de delitos contra la seguridad pública', 'Denuncias de delitos contra la libertad'] 
CantidadesDenunciasPorComisionDeDelitos2011 = [240438, 168618, 28486, 15932, 15812] 
CantidadesDenunciasPorComisionDeDelitos2012 = [271813, 185357, 39744, 14839, 17848] 
CantidadesDenunciasPorComisionDeDelitos2013 = [299474, 204935, 33613, 28175, 18459] 
CantidadesDenunciasPorComisionDeDelitos2014 = [326578, 224753, 36643, 30388, 19379] 
CantidadesDenunciasPorComisionDeDelitos2015 = [349323, 242697, 37057, 40150, 18730] 
CantidadesDenunciasPorComisionDeDelitos2016 = [355876, 242653, 44342, 38150, 20428] 
CantidadesDenunciasPorComisionDeDelitos2017 = [399869, 265219, 50597, 49385, 22660]
del_2011 = CantidadesDenunciasPorComisionDeDelitos2011[4]
del_2012 = CantidadesDenunciasPorComisionDeDelitos2012[4]
del_2013 = CantidadesDenunciasPorComisionDeDelitos2013[4]
del_2014 = CantidadesDenunciasPorComisionDeDelitos2014[4]
del_2015 = CantidadesDenunciasPorComisionDeDelitos2015[4]
del_2016 = CantidadesDenunciasPorComisionDeDelitos2016[4]
del_2017 = CantidadesDenunciasPorComisionDeDelitos2017[4]
promedio = round((del_2011 + del_2012 + del_2013 + del_2014 + del_2015 + del_2016 + del_2017)/7)
del_2018 = round(promedio * (1 + (asciiNombre + asciiApellido) / 50000))
print('Denuncias de delitos contra la libertad')
del_2011_2018 = [del_2011, del_2012, del_2013, del_2014, del_2015, del_2016, del_2017, del_2018]

for i in range(len(del_2011_2018)-1):
    for j in range(len(del_2011_2018)-1):
        if del_2011_2018[j] > del_2011_2018[j+1]:
            aux = del_2011_2018[j]
            del_2011_2018[j] = del_2011_2018[j+1]
            del_2011_2018[j+1] = aux

            aux2 = años[j]
            años[j] = años[j+1]
            años[j+1] = aux2
            
for i in range(len(años)-1,-1,-1):
    print(años[i],'= ',del_2011_2018[i])
