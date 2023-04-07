texto = '''Un equipo internacional de investigadores no solo creó todo un universo virtual. También lo puso gratuitamente a disposición de todas las personas con acceso a internet.

Uchuu, un término que significa universo en japonés, es la simulación más realista del cosmos lograda hasta la fecha.

El proyecto fue desarrollado por el Observatorio Astronómico Nacional de Japón (NAOJ) en colaboración con el Instituto de Astrofísica de Andalucía (IAA-CSIC), el Centro de Supercomputación de Galicia (CESGA) y la RedIRIS, la red académica y de investigación española.'''

contador = { 'minusculas': 0 , 'mayusculas' : 0}
for i in texto:
    if i.isupper():
        contador['mayusculas'] += 1
    elif i.islower():
        contador['minusculas'] += 1
        
print(contador)