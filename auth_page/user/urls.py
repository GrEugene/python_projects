from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('check_customer_url/', views.valid_customer, name='validation'),
    
    path('<int:question_id>/results/', views.results, name='results'),
    
    path('<int:question_id>/vote/', views.vote, name='vote'),
]