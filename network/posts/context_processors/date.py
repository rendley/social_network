import datetime


def year(request):
    context = {'year': datetime.datetime.now().year}
    return context
