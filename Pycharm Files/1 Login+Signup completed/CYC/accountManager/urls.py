from django.conf.urls import url,include
from accountManager.views import tokenLoginFunction,signUpFunction,usualLoginFunction


urlpatterns = [
    url(r'^tokenlogin/',tokenLoginFunction),
    url(r'^usuallogin/',usualLoginFunction),
    url(r'^signup/',signUpFunction),
]
