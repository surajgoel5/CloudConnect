from django.urls import path
from . import views

urlpatterns = [
path('',views.index,name='index'),
path('getbuttonvalue/<int:button_id>/', views.getButtonVal, name='getButtonVal'),
path('getbuttonlastedited/<int:button_id>/', views.getButtonLastEdited, name='getButtonLastEdited'),
path('switchbutton/<int:button_id>/', views.switchButton, name='switchButton'),
path('turnonbutton/<int:button_id>/', views.turnOnButton, name='turnOnButton'),
path('turnoffbutton/<int:button_id>/', views.turnOffButton, name='turnOffButton'),
]