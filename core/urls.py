from django.urls import path
from .views import make_conference

urlpatterns = [
    path('', make_conference, name='make_conference'),
    # path('', create_conference, name='create_conference'),
    # path('conference/', conference, name='conference'),
]
