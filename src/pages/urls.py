from django.urls import path
from . import views
urlpatterns = [
        path('doctorpage',views.doctorpage,name='doctorpage'),
        path('studentpage',views.studentpage,name='studentpage'),
]