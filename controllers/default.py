

def index():
    response.flash = T("¡Bienvenido!")
    return dict()


def user():
    return dict(form=auth())


@cache.action()
def download():
    return response.download(request, db)


def call():
    return service()
