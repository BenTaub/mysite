# views.py
from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book

# Create your views here.
def search_form(request):
    return render(request, 'search_form.html')


def search(request):
    # error = False
    errors = []
    if 'q' in request.GET:
    # if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term')
            # error = True
        elif len(q) > 20:
            errors.append('You entered: ' + q)
            errors.append('Please enter no more than 20 characters')
            # error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html', {'books': books, 'query': q})
        # message = 'You searched for: %r<p>and picked color code %r<\p>' % (request.GET['q'], request.GET['color_pick'])
    # else:
    return render(request, 'search_form.html', {'errors': errors})
        # message = 'You submitted an empty form.'
    # return HttpResponse(message)
