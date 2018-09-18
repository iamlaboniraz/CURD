from django.shortcuts import render,redirect
from django.views import View
from .models import BookList
# Create your views here.
def index(request):
	books=BookList.objects.all()
	return render(request,'index.html',{'books':books})

class CreateData(View):
	def get(self, request):	
		return render(request,'add_book.html')

	def post(self, request):
		print(request.POST)
		Title = request.POST.GET['Title']
		Price = request.POST.GET['Price']
		Author = request.POST.GET['Author']
		book_details = BookList(Title=Title, Price=Price, Author=Author)
		print(book_details)
		book_details.save()
		return redirect('/')	

	



def edit(request,id):	
	books=BookList.objects.get(pk=id)
	context={
	'books': books
	}
	return render(request,'edit.html',context)
	
def update(request,id):	
	books=BookList.objects.get(pk=id)
	books.Title = request.GET['Title']
	books.Price = request.GET['Price']
	books.Author = request.GET['Author']
	books.save()
	return redirect('/')


def delete(request,id):	
	books=BookList.objects.get(pk=id)
	books.delete()
	return redirect('/')