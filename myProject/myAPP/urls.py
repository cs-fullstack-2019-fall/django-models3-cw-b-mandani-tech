from  django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Book/add/',views.addBook),
    path('allBooks/',views.allBooks),
    path('changeGenre/',views.changeGenre)

]