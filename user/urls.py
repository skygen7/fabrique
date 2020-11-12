from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('poll-error', views.person_poll_error),
    path('<person_id>', views.person),
    path('<person_id>/polls', views.person_polls),
    path('<person_id>/polls/<poll_id>', views.person_answers),
]
