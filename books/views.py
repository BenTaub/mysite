from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book

# Create your views here.
def search_form(request):
    return render(request, 'search_form.html')


def search(request):
    error = False
    if 'q' in request.GET:
    # if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html', {'books': books, 'query': q})
        # message = 'You searched for: %r<p>and picked color code %r<\p>' % (request.GET['q'], request.GET['color_pick'])
    # else:
    return render(request, 'search_form.html', {'error': error})
        # message = 'You submitted an empty form.'
    # return HttpResponse(message)
