from django.contrib import admin
from django.urls import path, include
from account.views import signup, activate

app_name = 'main'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('webapp.urls')),
    path('account/', include('account.urls'), name="mailaccount"),
    path('signup/', signup, name="signup"),
    path('activate/<uidb64>/<token>', activate, name="activate"),
    path('comment/', include('comment.urls')),
]

