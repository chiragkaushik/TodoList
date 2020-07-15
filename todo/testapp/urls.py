from django.conf.urls import url
from testapp import urls
from . import views
urlpatterns = [
    url(r'^users/', views.user_list ),
    url(r'^detail/(?P<id>[0-9]+)/', views.user_detail),
    url(r'^generic/users/(?P<id>[0-9]+)/', views.GenericUserAPIView.as_view()),
    url(r'^generic/access/(?P<id>[0-9]+)/', views.GenericAccessAPIView.as_view()),
    url(r'^generic/todolist/(?P<id>[0-9]+)/', views.GenericTodoListAPIView.as_view()),
    url(r'^generic/todoitem/(?P<id>[0-9]+)/', views.GenericTodoItemAPIView.as_view()),

]