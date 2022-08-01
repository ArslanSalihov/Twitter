from unicodedata import name
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete_post, name='delete'),
    path('search/', views.search, name='search_results'),
    path('register', views.register, name='register' ),
    path('login', views.register, name='login' ),
    path('regorlog', views.regorlog, name='regorlog' ),
    path('favourite', views.favourite, name='favourite'),
    path('favourite/add/<int:post_id>', views.add_to_favourite, name='add_to_favourite'),
    path('favourite/delete/<int:post_id>', views.delete_favourite, name='delete_favourite'),
    path('post/<int:id>/comment', views.comment, name='comment'),
    path('post_detail/<int:post_id>', views.post_detail, name='post_detail'),
]