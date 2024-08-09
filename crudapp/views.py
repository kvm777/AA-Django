from django.shortcuts import render

# Create your views here.


def crudIndex(request):
    return render(request, "crudapp/crud-index.html")




""""
templates
    - firstapp
    - crudapp
    - accounts
    index.html


"""