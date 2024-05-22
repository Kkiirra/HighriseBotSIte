from django.urls import path
from .views import SigninView, signup

urlpatterns = [
    path('signin/', SigninView.as_view(), name='signin'),
    path('signup/', signup, name='signup'),

]
