from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
import datetime

# Create your views here.

def index(request):
    return HttpResponse("hello world")


def addBook(request):
    book1 = Book(name="Alchemist", pageNumber=45,genre="Fiction", publishDate="1999-03-25")
    book1.save()
    book2 = Book(name="Seven Habbits", pageNumber=105,genre="Motivational", publishDate="1992-07-31")
    book2.save()
    return HttpResponse("Going to add new book, added")


def allBooks(request):
    bookList=Book.objects.all()
    for eachElement in bookList:
        if(eachElement.publishDate >= datetime.date(2018,1,1)):
            print(eachElement.name)
    return HttpResponse("All Books")



def changeGenre(request):
    bookList=Book.objects.all()
    for eachElement in bookList:
        if(eachElement.publishDate >= datetime.date(2018,1,1)):
            print(eachElement.name)
            eachElement.genre = "fiction"
            print(eachElement.genre)
    return HttpResponse("Genre Changed")