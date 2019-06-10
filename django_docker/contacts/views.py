from django.shortcuts import render

# Create your views here.


def contact(request):
    return render(request, 'contacts/index.html', {'title': 'Jinja II'})
