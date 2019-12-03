from django.urls import path
from controle.produto import views as v

app_name='produto'

urlpatterns=[
    path('', v.produto_list, name='produto_list'),
]