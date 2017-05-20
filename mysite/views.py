from django.http import Http404, HttpResponse
import datetime

def hello(request):
    return HttpResponse("<strong>Hello World</strong>")


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>UTC time is now %s</body></html>" % now
    html += "<p><html><body><strong>A2 time is now %s</strong></body></html></p>" % (now + datetime.timedelta(hours=-4))
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    now = datetime.datetime.now()
    dt = now + datetime.timedelta(hours=offset)
    html = "<html><body>The UTC time is currently:%s</body></html>" %(now)
    html += "<p><body>In %s hour(s) the UTC time will be: %s</body></p>" %(offset, dt)
    return HttpResponse(html)
