<<<<<<< HEAD
#debemos declarar la vista que queremos mostrar
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    #hace referencia a lo que queres cargar cuando carguemos la clase
    template_name = 'index.html'
=======
from django.shortcuts import render
from django.views.generic import TemplateView

"""
    todos estos se encuentran en django.views.generic

    DetaileView: solo muestra un valor de la base de datos
    ListView: listar todos los objetos de un modelo particular
    CreateView: crea un objeto
    UpdateView: actualiza un objeto
    DelateView: borra un objeto
    TemplateView: solamente muestra un template

    estas son unas vistas que ya estan en django que ya tienen todo el código necesario
    para la cumplir con esas funcionalidades
"""
#views basadas en clases 


class Index(TemplateView):
    template_name = "index.html"

class Services(TemplateView):
    template_name = "pages/services.html"

class Blog(TemplateView):
    template_name = "pages/blog.html"

class Contact(TemplateView):
    template_name = "pages/contact.html"
>>>>>>> 4eefce52db50dc5bbfe09e3089238d20f06acde5
