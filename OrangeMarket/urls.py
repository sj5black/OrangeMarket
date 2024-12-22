from django.contrib import admin
from django.urls import path, include
from articles import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("home/", views.home, name="home"),
    path("articles/", include("articles.urls")),
    path("users/", include("users.urls")),
    path("accounts/", include("accounts.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)