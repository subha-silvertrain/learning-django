from django.urls import path

from . import views

# if you add a url here, it would go to localhost/polls/results for example if you added results

urlpatterns = [
    path("", views.index, name="index"),
]