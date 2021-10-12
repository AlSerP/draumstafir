from django.urls import path

from . import views

urlpatterns = [
    path('upload', views.UploadImageView.as_view(), name="upload"),
    path('<int:pk>/', views.ImageView.as_view(), name='image_show'),
    path('<int:pk>/edit/', views.ImageUpdateView.as_view(), name='image_edit'),
    path('<int:pk>/delete/', views.ImageDeleteView.as_view(), name='image_delete'),
]