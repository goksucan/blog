from django.contrib import admin
from django.urls import path, include 
from core import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from core.models import Post

from core.sitemaps import CategorySitemap, PostSitemap

sitemaps = {"category": CategorySitemap, "post": PostSitemap}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps} ),
    path('', views.index, name='index' ),
    path('robots.txt', views.robots_txt, name='robots_txt' ),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('<slug:category_slug>/<slug:slug>/', views.post_detail, name = 'post_detail'),
    path('<slug:slug>/', views.category, name = 'category_detail'),
    path('tag/<tag>', views.tag, name='tag'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
