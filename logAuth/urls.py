from django.urls import path
from . import views

urlpatterns = [
    path('log', views.login1, name="login-add"),
    path('register', views.register1),
    path('unlog', views.logout1, name="unlog"),
    path('profily/<str:online>', views.profilize, name="profil"),
    path('add/<str:profil>/<str:online>', views.add, name="add"),
    path('', views.index, name="home"), 
    path('pay/<str:online>', views.payment, name="pay"),
    path('share/<str:online>', views.share, name="share"),
    path('dashboard/<str:profil>/<str:category>', views.dashboard, name="dashboard"),
    path('reseting', views.reset, name="reseting"),
    path('change/<str:email>', views.changePwd, name="change"),
    path('choose', views.PrefChoice, name="choose"),
    
    
]

#input type="file" name="photo" id="id_photo"