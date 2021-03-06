from django.urls import path, re_path

from . import views

urlpatterns = [
    path('upload', views.UploadImageView.as_view(), name="upload"),
    # path('all', views.AllImagesView.as_view(), name="all_images"),
    path('show', views.AllImagesView.as_view(), name="all_images"),
    # path('shaw', views.AllImagesView.as_view(), name="all_images"),
    path('<int:pk>/', views.ImageView.as_view(), name='image_show'),
    path('<int:pk>/edit', views.ImageUpdateView.as_view(), name='image_edit'),
    path('<int:pk>/delete', views.ImageDeleteView.as_view(), name='image_delete'),
    path('<int:pk>/comment', views.UploadCommentView.as_view(), name='comment_upload'),
    path('<int:pk>/like', views.like_image, name='like'),
    path('<int:pk>/dislike', views.dislike_image, name='dislike'),
    path('<int:pk>/<str:tag>/delete', views.delete_tag, name='tag_delete'),
]
