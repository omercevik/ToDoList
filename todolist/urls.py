from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name="home"),
    path('todolist/<list_id>', views.todolist, name="todolist"),
    path('lists/', views.lists, name="lists"),
    path('delete_list/<list_id>', views.delete_list, name="delete_list"),
    path('order/<list_id>/<order_by_what>', views.order, name="order"),
    path('home/', views.home, name="home"),
    path('delete/<list_id>/<returnId>', views.delete, name="delete"),
    path('cross_off/<list_id>/<returnId>', views.cross_off, name="cross_off"),
    path('uncross/<list_id>/<returnId>', views.uncross, name="uncross"),
    path('register/', views.register, name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='home'), name="logout"),
]
