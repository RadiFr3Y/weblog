from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import aboutView, indexView, contactView, singleView, workView, SlugView
from django.urls import reverse

def get_absolute_url(self):
    return reverse('post_detail_url', kwargs={'slug': self.slug})

app_name = 'page'
urlpatterns = [
    path('', indexView, name = 'index'),
    path('contact/', contactView, name = 'contact'),
    path('work/', workView, name = 'work'),
    path('single/', singleView, name = 'single'),
    path('about/', aboutView, name = 'about'),
    path('<slug:slug>', SlugView, name='slug')
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)