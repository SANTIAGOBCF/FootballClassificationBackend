from django.urls import path
from dashboard import views
urlpatterns = [
    path('result/',views.result,name="result" ),
]