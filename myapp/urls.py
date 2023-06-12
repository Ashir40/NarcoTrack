from django.urls import path, include, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register, name='register'),
    path('profile', views.create_profile, name='profile'),
    path('patient_data', views.patient_data, name = "patient_data"),
    path('patient_delete/<str:id>/', views.patient_delete, name = "patient_delete"),
    path('show_profile', views.show_profile, name='show_profile'),
    path('centers', views.centers, name = 'centers'),
    path('center_detail/<str:id>/', views.center_detail, name = 'center_detail'),
    path('create_center', views.create_center, name= 'create_center'),
    path('search_by_cnic', views.search_by_cnic, name= 'search_by_cnic'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('quiz', views.quiz, name='quiz'),
    
] 