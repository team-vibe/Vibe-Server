from . import views
from django.urls import path


urlpatterns = [
    path('', views.index),
    path('restaurant-search/<str:query>/', views.get_restaurants),
    path('restaurant-search/website/<str:id>/', views.get_website_link),
    path('event-search/<str:query>/', views.get_events),
    path('event-search/<str:query>/<str:eventcode>/', views.get_events_by_code),
]