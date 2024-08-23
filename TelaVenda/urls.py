from django.urls import path
from.import views

urlpatterns = [
    path('TelaVenda/', views.TelaVenda, name="TelaVenda"),
]
