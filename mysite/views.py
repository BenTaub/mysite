# from django.template.loader import get_template
# from django.template import Context
from django.shortcuts import render
from django.http import Http404, HttpResponse
import datetime
from mysite.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})



def hello(request):
    html = "<strong>Hello World</strong>"
    html += display_meta(request=request)
    return HttpResponse(html)
    # return HttpResponse("<strong>Hello World</strong>")


def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})

    # t = get_template('current_datetime.html')
    # html = t.render(Context({'current_date': now}))

    # html = "<html><body>UTC time is now %s</body></html>" % now
    # html += "<p><html><body><strong>A2 time is now %s</strong></body></html></p>" % (now + datetime.timedelta(hours=-4))

    # return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    now = datetime.datetime.now()
    dt = now + datetime.timedelta(hours=offset)
    return render(request=request, template_name='hours_ahead.html',
                  context={'hour_offset': offset, 'next_time': dt, 'now': now})
    # html = "<html><body>The UTC time is currently:%s</body></html>" %(now)
    # html += "<p><body>In %s hour(s) the UTC time will be: %s</body></p>" %(offset, dt)
    # return HttpResponse(html)

def display_meta(request):
    keys = list(request.META.keys())
    values = request.META
    # values = dict(request.META.items())
    keys.sort()
    html = []
    for this_key in keys:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (this_key, values[this_key]))
    return '<table>%s</table>' % '\n' .join(html)
