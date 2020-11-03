from django.urls import path
from . import views
urlpatterns=[
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blogdetail/<int:id>', views.blog_details, name='view_blog_detail'),

]