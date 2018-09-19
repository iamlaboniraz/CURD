from django.shortcuts import render, redirect
from django.views import View
from .models import BookList


# Create your views here.
def index(request):
    books = BookList.objects.all()
    return render(request, 'index.html', {'books': books})


class CreateData(View):
    """
     Always use class method in views
     . Don't upload virtual environment github and don't delete .gitignore file from root directory
    """
    def get(self, request):
        return render(request, 'add_book.html')

    def post(self, request):
        print(request.POST)
        title = request.POST.get('title') # do not use camelcase variable name
        price = request.POST.get('price')
        author = request.POST.get('author')

        book_details = BookList(Title=title, Price=price, Author=author)
        print(book_details)
        book_details.save()
        return redirect('/')




def edit(request, id):
    books = BookList.objects.get(pk=id)
    context = {
        'books': books
    }
    return render(request, 'edit.html', context)


def update(request, id):
    books = BookList.objects.get(pk=id)
    books.Title = request.GET['Title']
    books.Price = request.GET['Price']
    books.Author = request.GET['Author']
    books.save()
    return redirect('/')


def delete(request, id):
    books = BookList.objects.get(pk=id)
    books.delete()
    return redirect('/')
