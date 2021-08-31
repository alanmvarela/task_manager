from django.urls import path
from .views import CreateCardView

app_name = 'api'

urlpatterns = [
    path('', CreateCardView.as_view(), name='create_card')
]