from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home),
    path('aboutus/',views.about,name='aboutus'),
    path('services/',views.services,name='services'),
    path('seosem/',views.seosem,name='seosem'),
    path('digitalmarketing/',views.digitalmarketing,name='digitalmarketing'),
    path('graphicsdesigning/',views.graphicsservices,name='graphicsdesigning'),
    path('webdesigning&development/',views.webservices,name='webdesigning'),
    path('contentwriting/',views.contentservices,name='contentservices'),
    path('videoediting/',views.videoediting,name='videoediting'),
    path('contactus/',views.contactus,name='contactus'),
    path('blog/',views.blog,name='blog'),
    path('blog/<int:pk>/',views.blogdetail,name='blogdetail'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('portfolio/<slug:data>/',views.portfolio,name='portfoliofilteration'),
    path('terms&Condition/',views.termsandCondition,name='termsandCondition'),
    path('privacy&Policy/',views.privacy,name='privacy'),
    path('FAQ?/',views.faq,name='FAQ'),
    path('thankyou/',views.thanks,name='thankyou'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
