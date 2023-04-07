# APELLIDOS: HUAMANI GONZALES
# NOMBRES: LUIS ANTONY
# ÚLTIMO DIGITO DNI: 2
asciiNombre = 786
asciiApellido = 1225
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
print(DescripcionDenunciasPorComisionDeDelitos[0])
print('2011 =',denuncia2011)
print('2012 =',denuncia2012)
print('2013 =',denuncia2013)
print('2014 =',denuncia2014)
print('2015 =',denuncia2015)
print('2016 =',denuncia2016)
print('2017 =',denuncia2017)
print('2018 =',denuncia2018)
denunciaDel2011al2018 = [denuncia2011, denuncia2012, denuncia2013, denuncia2014, denuncia2015, denuncia2016, denuncia2017, denuncia2018]
total = 0
for inicio in denunciaDel2011al2018:
    total += inicio
print('La suma total de los valores correspondientes a "Número de denuncias por comisión de delitos", desde al año 2011 hasta el año 2018 es:',total)   
print('En comparación al año 2017, en el año 2018 disminuyó el "Número de denuncias por comisión de delitos", siendo la cantidad:',denuncia2018)


