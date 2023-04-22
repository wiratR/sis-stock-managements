from django.urls import path
from . import views

app_name = 'tracks'

urlpatterns = [
    path('', views.TrackListView.as_view(), name='all'),
    path('tracks/<int:pk>/detail', views.TrackDetailView.as_view(), name='track_detail'),
    path('tracks/create/', views.TrackCreateView.as_view(), name='track_create'),
    path('tracks/<int:pk>/update/', views.TrackUpdateView.as_view(), name='track_update'),
    path('tracks/<int:pk>/delete/', views.TrackDeleteView.as_view(), name='track_delete'),
]