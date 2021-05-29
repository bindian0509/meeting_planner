from django.urls import path
from meetings.views import room
from . import views

urlpatterns = [
    path('meetings/<int:id>', views.detail, name='detail'),
    path('rooms/<int:id>', room, name='room'),
    path('rooms', views.rooms_list, name='rooms'),
    path('new', views.new, name='new'),
]
