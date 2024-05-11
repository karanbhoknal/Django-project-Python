from django.urls import path
from . import views 


urlpatterns = [
    path('',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('crudadd/',views.create_view,name='create_view'),
    path('crudlist/',views.list_view,name='list_view'),
    path('userlist/',views.register_view,name='register_view'),
    path('basic/',views.basic,name='basic'),
    path('overview/',views.overview,name='overview'),
    path('Variable/',views.Variable,name='Variable'),
    path('Loops/',views.Loops,name='Loops'),
    path('condition/',views.condition,name='condition'),
    path('function/',views.function,name='function'),
    path('keywords/',views.keywords,name='keywords'),
    path('tuple/',views.tuple,name='tuple'),
    path('set/',views.set,name='set'),
    path('module/',views.module,name='module'),
    path('directory/',views.directory,name='directory'),
    path('dictionary/',views.dictionary,name='dictionary'),
    path('forget/',views.forget,name='forget'),
    
    
    
]