from django.conf.urls import url,include
from home.views import Homeview
from . import views


urlpatterns = [
    url(r'create/',views.post, name='create_post' ),
    url(r'addprofile/',views.newprofile, name='newprofile'),
    url(r'profile/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(), name='album_profile'),

    url(r'^',Homeview.as_view(), name='home' ),



]