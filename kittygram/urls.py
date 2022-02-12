from django.urls import include, path

from cats.views import APICAT

urlpatterns = [
   path('cats/', APICAT.as_view()),
]


