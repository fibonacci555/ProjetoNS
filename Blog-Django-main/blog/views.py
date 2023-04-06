from django.http import request
from django.shortcuts import render
from .models import Post
from users.models import *
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)

class Index(ListView):
    def get(self,request):

        return render(request, 'blog/index.html')
    def post(self,request):
        return render(request, 'blog/index.html')
    



class Aveiro(View):
    def get(self,request):
        distrito = "Aveiro"
        list = Profile.objects.filter(distrito="Aveiro")
        context = {
            'profile_list' : list,
            'dist': distrito,
        }
        return render(request, 'blog/Aveiro.html',context)
    def post(self,request):
        return render(request, 'blog/Aveiro.html')

class Beja(View):
    def get(self,request):
        distrito = "Beja"
        list = Profile.objects.filter(distrito="Beja")
        context = {
            'profile_list' : list,
            'dist': distrito,
        }
        return render(request, 'blog/Beja.html',context)
    def post(self,request):
        return render(request, 'blog/Beja.html')

class Braga(View):
    def get(self,request):
        distrito = "Braga"
        list = Profile.objects.filter(distrito="Braga")
        context = {
            'profile_list' : list,
            'dist': distrito,
        }
        return render(request, 'blog/Braga.html',context)
    def post(self,request):
        return render(request, 'blog/Braga.html')

class Braganca(View):
    def get(self,request):
        distrito = "Bragança"
        list = Profile.objects.filter(distrito="Braganca")
        context = {
            'profile_list' : list,
            'dist': distrito,
        }
        return render(request, 'blog/Braganca.html',context)
    def post(self,request):
        return render(request, 'blog/Braganca.html')

class CasteloBranco(View):
    def get(self,request):
        distrito = "Castelo Branco"
        list = Profile.objects.filter(distrito="CasteloBranco")
        context = {
            'profile_list' : list,
            'dist': distrito,
        }
        return render(request, 'blog/CasteloBranco.html',context)
    def post(self,request):
        return render(request, 'blog/CasteloBranco.html')

class Coimbra(View):
    def get(self,request):
        distrito = "Coimbra"
        list = Profile.objects.filter(distrito="Coimbra")
        context = {
            'profile_list' : list,
            'dist': distrito,
        }
        return render(request, 'blog/Coimbra.html',context)
    def post(self,request):
        return render(request, 'blog/Coimbra.html')

class Evora(View):
    def get(self,request):
        distrito = "Évora"
        list = Profile.objects.filter(distrito="Evora")
        context = {
            'profile_list' : list,
            'dist': distrito,
        }
        return render(request, 'blog/Evora.html',context)
    def post(self,request):
        return render(request, 'blog/Evora.html')

class Faro(View):
    def get(self,request):
        distrito = "Faro"
        list = Profile.objects.filter(distrito="Faro")
        context = {
            'profile_list' : list,
            'dist': distrito,
        }
        return render(request, 'blog/Faro.html',context)
    def post(self,request):
        return render(request, 'blog/Faro.html')

class Guarda(View):
    def get(self,request):
        distrito = "Guarda"
        list = Profile.objects.filter(distrito="Guarda")
        context = {
            'profile_list' : list,
            'dist': distrito,
        }
        return render(request, 'blog/Guarda.html',context)
    def post(self,request):
        return render(request, 'blog/Guarda.html')

class Leiria(View):
    def get(self,request):
        distrito = "Leiria"
        list = Profile.objects.filter(distrito="Leiria")
        context = {
            'profile_list' : list,
            'dist': distrito,
        }
        return render(request, 'blog/Leiria.html',context)
    def post(self,request):
        return render(request, 'blog/Leiria.html')

class Lisboa(View):
    def get(self,request):
        distrito = "Lisboa"
        list = Profile.objects.filter(distrito="Lisboa")
        context = {
            'profile_list' : list,
            'dist': distrito,
        }
        return render(request, 'blog/Lisboa.html',context)
    def post(self,request):
        return render(request, 'blog/Lisboa.html')

class Portalegre(View):
    def get(self,request):
        distrito = "Portalegre"
        list = Profile.objects.filter(distrito="Portalegre")
        context = {
            'profile_list' : list,
            'dist': distrito,
        }
        return render(request, 'blog/Portalegre.html',context)
    def post(self,request):
        return render(request, 'blog/Portalegre.html')

class Porto(View):
    def get(self,request):
        distrito = "Porto"
        list = Profile.objects.filter(distrito="Porto")
        context = {
            'profile_list' : list,
            'dist': distrito,
        }
        return render(request, 'blog/Porto.html',context)
    def post(self,request):
        return render(request, 'blog/Porto.html')

class Santarem(View):
    def get(self,request):
        distrito = "Santarém"
        list = Profile.objects.filter(distrito="Santarem")
        context = {
            'profile_list' : list,
            'dist': distrito,
        }
        return render(request, 'blog/Santarem.html',context)
    def post(self,request):
        return render(request, 'blog/Santarem.html')
    
class Setubal(View):
    def get(self,request):
        distrito = "Setúbal"
        list = Profile.objects.filter(distrito="Setubal")
        context = {
            'profile_list' : list,
            'dist': distrito,
        }
        return render(request, 'blog/Setubal.html',context)
    def post(self,request):
        return render(request, 'blog/Setubal.html')

class VianaDoCastelo(View):
    def get(self,request):
        distrito = "Viana Do Castelo"
        list = Profile.objects.filter(distrito="VianaDoCastelo")
        context = {
            'profile_list' : list,
            'dist': distrito,
        }
        return render(request, 'blog/VianaDoCastelo.html',context)
    def post(self,request):
        return render(request, 'blog/VianaDoCastelo.html')

class VilaReal(View):
    def get(self,request):
        distrito = "Vila Real"
        list = Profile.objects.filter(distrito="VilaReal")
        context = {
            'profile_list' : list,
            'dist': distrito,
        }
        return render(request, 'blog/VilaReal.html',context)
    def post(self,request):
        return render(request, 'blog/VilaReal.html')

class Viseu(View):
    def get(self,request):
        distrito = "Viseu"
        list = Profile.objects.filter(distrito="Viseu")
        context = {
            'profile_list' : list,
            'dist': distrito,
        }
        return render(request, 'blog/Viseu.html',context)
    def post(self,request):
        return render(request, 'blog/Viseu.html')


class PostDetailView(DetailView):
    model = Post
   
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):                 # method used to set author to current logged User
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):                 # method used to set author to current logged user
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'   #  used to redirect to home page after deletion the post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
 