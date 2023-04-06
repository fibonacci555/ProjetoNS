from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', Index.as_view(), name='blog-home'),

    path('Aveiro/', Aveiro.as_view(), name='Aveiro'),
    path('Beja/', Beja.as_view(), name='Beja'),
    path('Braga/', Braga.as_view(), name='Braga'),
    path('Braganca/', Braganca.as_view(), name='Braganca'),
    path('Castelo Branco/', CasteloBranco.as_view(), name='CasteloBranco'),
    path('Coimbra/', Coimbra.as_view(), name='Coimbra'),
    path('Evora/', Evora.as_view(), name='Evora'),
    path('Faro/', Faro.as_view(), name='Faro'),
    path('Guarda/', Guarda.as_view(), name='Guarda'),
    path('Leiria/', Leiria.as_view(), name='Leiria'),
    path('Lisboa/', Lisboa.as_view(), name='Lisboa'),
    path('Portalegre/', Portalegre.as_view(), name='Portalegre'),
    path('Porto/', Porto.as_view(), name='Porto'),
    path('Santarem/', Santarem.as_view(), name='Santarem'),
    path('Setubal/', Setubal.as_view(), name='Setubal'),
    path('Viana do Castelo/', VianaDoCastelo.as_view(), name='VianaDoCastelo'),
    path('Vila Real/', VilaReal.as_view(), name='VilaReal'),
    path('Viseu/', Viseu.as_view(), name='Viseu'),



    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new', PostCreateView.as_view(), name='post-create'),    # default path blog/post_form.html
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]
    

