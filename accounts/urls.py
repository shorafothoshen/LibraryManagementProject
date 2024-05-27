from django.urls import path
from . import views

urlpatterns = [
    path("signup/",views.SignUpClassView.as_view(), name="signup"),
    path("login/",views.LoginClassView.as_view(),name="Login"),
    path("profile/",views.Profileview.as_view(), name="Profile"),
    path("update/",views.UpdateViewClass.as_view(), name="update"),
    path("logout/",views.UserLogoutView.as_view(), name="Logout"),
]
