from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import home, PostDetailView

urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('pricing.html', views.pricing, name="pricing"),
    path('about.html', views.about, name="about"),

    # projects
    path('post/<int:pk>', PostDetailView.as_view(), name="post-detail"),
   
]
#THIS PATH IS IMPORTANT TO RENDER OUR IMG IN OUR ADMIN
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
