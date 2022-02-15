from django.contrib.auth import views
from django.urls import path
from .views import PostList, PostCreate, Logout, PostUpdate, PostDelet, Profile

app_name = 'account'
urlpatterns = [
    path('', PostList, name='home'),
    path('create/', PostCreate.as_view(), name='Post-create'),
    path('create/<int:pk>', PostUpdate.as_view(), name='Post-Update'),
    path('profile/', Profile.as_view(), name='profile'),
    path('delete/<int:pk>', PostDelet.as_view(), name='Post-Delete'),
    path('logout/', Logout, name='logout'),
]