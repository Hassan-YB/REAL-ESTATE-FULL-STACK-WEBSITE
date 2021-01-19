from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin 

urlpatterns = [
     path('',views.index,name='index'),
     path('agent_profile/',views.agent_profile,name='agent_profile'),
     path('contact/',views.contact,name='contact'),
     path('details/',views.details,name='details'),
     path('index_map/',views.index_map,name='index_map'),
     path('pricing/',views.pricing,name='pricing'),
     path('registration/',views.registration,name='registration'),
     path('results_grid/',views.results_grid,name='results_grid'),
     path('results/',views.results,name='results'),
     path('search_users/',views.search_users,name='search_users'),
     path('submit/',views.submit,name='submit'),
     path('signup/',views.signup,name='signup'),
     path('<int:id>/',views.detail,name='detail'),


 ]  

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
        