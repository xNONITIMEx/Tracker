from django.urls import path
from .views import urlpatterns, activate

app_name = 'user'
urlpatterns = urlpatterns + [
    path('activate/<uidb64>/<token>', activate, name='activate')
]
