from django.urls import path, re_path
from . import views
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Documentation')

urlpatterns = [
  path('album/<int:id>', views.album_id),
  path('artist/<int:id>', views.artist_id),
  path('search/', views.search_songs_by_author),
  path('login/', views.login),
  path('logout/', views.login),
  re_path(r'^docs/', schema_view)
]