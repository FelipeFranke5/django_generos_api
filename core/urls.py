from django.contrib import admin
from django.urls import path
from genres import views as genre_views


urlpatterns = [
    path("admin/", admin.site.urls),
]

genre_urlpatterns = [
    path("genres/", genre_views.genre_view, name="genres"),
    path("genres/<int:pk>/", genre_views.genre_detail, name="genre_detail"),
]

urlpatterns += genre_urlpatterns
