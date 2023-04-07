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
denuncia2011 = CantidadesDenunciasPorComisionDeDelitos2011[0]
denuncia2012 = CantidadesDenunciasPorComisionDeDelitos2012[0]
denuncia2013 = CantidadesDenunciasPorComisionDeDelitos2013[0]
denuncia2014 = CantidadesDenunciasPorComisionDeDelitos2014[0]
denuncia2015 = CantidadesDenunciasPorComisionDeDelitos2015[0]
denuncia2016 = CantidadesDenunciasPorComisionDeDelitos2016[0]
denuncia2017 = CantidadesDenunciasPorComisionDeDelitos2017[0]
promediofinal = round((denuncia2011 + denuncia2012 + denuncia2013 + denuncia2014 + denuncia2015 + denuncia2016 + denuncia2017)/7)
denuncia2018 = round(promediofinal * (1 + (asciiNombre + asciiApellido) / 50000))
print('Denuncias de delitos contra la libertad')
denunciaDel2011Al2018 = [denuncia2011, denuncia2012, denuncia2013, denuncia2014, denuncia2015, denuncia2016, denuncia2017, denuncia2018]

for inicio in range(len(denunciaDel2011Al2018)-1):
    for inicio2 in range(len(denunciaDel2011Al2018)-1):
        if denunciaDel2011Al2018[inicio2] > denunciaDel2011Al2018[inicio2+1]:
            aux = denunciaDel2011Al2018[inicio2]
            denunciaDel2011Al2018[inicio2] = denunciaDel2011Al2018[inicio2+1]
            denunciaDel2011Al2018[inicio2+1] = aux

            promedioFinal = años[inicio2]
            años[inicio2] = años[inicio2+1]
            años[inicio2+1] = promedioFinal
            
for inicio in range(len(años)-1,-1,-1):
    print(años[inicio],'= ',denunciaDel2011Al2018[inicio])
