from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:poll_id>/', views.poll),
    path('<int:poll_id>/questions/', views.questions),
    path('<int:poll_id>/questions/<int:que_id>', views.question),
    path('<int:poll_id>/questions/<int:que_id>/accept', views.accept_answer),
    path('<int:poll_id>/questions/<int:que_id>/answer-err', views.answer_err),
]
