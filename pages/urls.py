from django.urls import path
from .views import HomePageView, AboutPageView, ProjectPageView, BlogPageView, ContactPageView,ProjectDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about-me/', AboutPageView.as_view(), name='about-me'),
    path('my-project/', ProjectPageView.as_view(), name='my-project'),
    path('my-project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('blog/', BlogPageView.as_view(), name='blog'),
    path('contact-me/', ContactPageView.as_view(), name='contact-me'),
]
