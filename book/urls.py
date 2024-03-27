from django.urls import path
from .views import *

urlpatterns = [
    path('', landing, name = 'landing'),
    path('detail/<int:id>/', detail_view, name = 'detail'),
    path('review/', review_view, name = 'review' ),
]