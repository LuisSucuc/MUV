
#MENU DE SELECCIÓN
def index():
    return dict()

#VELOCIDAD FINAL
def velo_fin():
    #Diseño SQLFactory
    formulario = SQLFORM.factory(
        Field('velo_ini', requires = IS_DECIMAL_IN_RANGE(error_message="Ingresa un numero")),
        Field('aceleracion', requires = IS_DECIMAL_IN_RANGE(error_message="Ingresa un numero")),
        Field('tiempo', requires = IS_DECIMAL_IN_RANGE(error_message="Ingresa un numero"))
        )

    if formulario.process().accepted:

        Vo = formulario.vars.velo_ini
        a  = formulario.vars.aceleracion
        t  = formulario.vars.tiempo

        #Formula y redondeo
        Vf = Vo + a*t
        Vf = round( Vf, 2 )

        #Resultado
        resultado = 'Vf = ' + str(Vf)

        #Envio de datos
        redirect(URL('calcular', 'resultado', vars={'Vo': Vo, 'a': a, 'resultado': resultado }))
        #db.persona.insert(velo_fin = formulario.vars., velo_fin = formulario.vars., velo_fin = formulario.vars., velo_fin = formulario.vars.,)
    elif formulario.errors:
        response.flash = 'El formulario contiene errores'
    return dict(formulario = formulario)


#VELOCIDAD INICIAL
def velo_ini():
    #Diseño SQLFactory
    formulario = SQLFORM.factory(
        Field('velo_fin', requires = IS_DECIMAL_IN_RANGE(error_message="Ingresa un numero")),
        Field('aceleracion', requires = IS_DECIMAL_IN_RANGE(error_message="Ingresa un numero")),
        Field('tiempo', requires = IS_DECIMAL_IN_RANGE(error_message="Ingresa un numero")),
        )

    if formulario.process().accepted:

        Vf = formulario.vars.velo_fin
        a  = formulario.vars.aceleracion
        t  = formulario.vars.tiempo

        #Formula y redondeo
        Vo = Vf - a*t
        Vo = round( Vo, 2 )

        #Resultado
        resultado = 'Vo = ' + str(Vo)

        #Envio de datos
        redirect(URL('calcular', 'resultado', vars={'Vo': Vo, 'a': a, 'resultado': resultado }))

    elif formulario.errors:
        response.flash = 'El formulario contiene errores'
    return dict(formulario = formulario)

def distancia():
    #Diseño SQLFactory
    formulario = SQLFORM.factory(
        Field('velo_ini', requires = IS_DECIMAL_IN_RANGE(error_message="Ingresa un numero")),
        Field('aceleracion', requires = IS_DECIMAL_IN_RANGE(error_message="Ingresa un numero")),
        Field('tiempo', requires = IS_DECIMAL_IN_RANGE(error_message="Ingresa un numero")),
        )

    if formulario.process().accepted:

        Vo = formulario.vars.velo_ini
        a  = formulario.vars.aceleracion
        t  = formulario.vars.tiempo

        #Formula y redondeo
        x =  Vo*t  +  (a*t*t)/2
        x = round( x, 2 )

        #Resultado
        resultado = 'x = ' + str(x)

        #Envio de datos
        redirect(URL('calcular', 'resultado', vars={'Vo': Vo, 'a': a, 'resultado': resultado }))

    elif formulario.errors:
        response.flash = 'El formulario contiene errores'
    return dict(formulario = formulario)

def aceleracion():
    #Diseño SQLFactory
    formulario = SQLFORM.factory(
        Field('velo_fin', requires = IS_DECIMAL_IN_RANGE(error_message="Ingresa un numero")),
        Field('velo_ini', requires = IS_DECIMAL_IN_RANGE(error_message="Ingresa un numero")),
        Field('tiempo', requires = IS_DECIMAL_IN_RANGE(error_message="Ingresa un numero")),
        )

    if formulario.process().accepted:

        Vf = formulario.vars.velo_fin
        Vo = formulario.vars.velo_ini
        t  = formulario.vars.tiempo

        #Formula y redondeo
        a = (Vf-Vo)/t
        a = round( a, 2 )

        #Resultado
        resultado = 'a = ' + str(a)

        #Envio de datos
        redirect(URL('calcular', 'resultado', vars={'Vo': Vo, 'a': a, 'resultado': resultado }))

    elif formulario.errors:
        response.flash = 'El formulario contiene errores'
    return dict(formulario = formulario)

#TIEMPO ---- ---- ----
def tiempo():
    #Diseño SQLFactory
    formulario = SQLFORM.factory(
        Field('velo_fin', requires = IS_DECIMAL_IN_RANGE(error_message="Ingresa un numero")),
        Field('velo_ini', requires = IS_DECIMAL_IN_RANGE(error_message="Ingresa un numero")),
        Field('aceleracion', requires = IS_DECIMAL_IN_RANGE(error_message="Ingresa un numero")),
        )

    if formulario.process().accepted:

        Vf = formulario.vars.velo_fin
        Vo = formulario.vars.velo_ini
        a  = formulario.vars.aceleracion
        
        #Formula y redondeo
        t = (Vf-Vo)/a
        t = round( t, 2 )

        #Resultado
        resultado = 't = ' + str(t)

        #Envio de datos
        redirect(URL('calcular', 'resultado', vars={'Vo': Vo, 'a': a, 'resultado': resultado }))

    elif formulario.errors:
        response.flash = 'El formulario contiene errores'
    return dict(formulario = formulario)

def resultado():
    Vo = request.vars.Vo
    a = request.vars.a
    resultado = request.vars.resultado
    return dict(Vo = Vo, a = a, resultado = resultado)

@cache.action()
def download():
    return response.download(request, db)
