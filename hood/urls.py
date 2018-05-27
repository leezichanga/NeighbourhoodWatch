from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.index,name='index'),
    url(r'^new/',views.create_profile,name='new_profile'),
    url(r'^profile/',views.view_profile,name='profile'),
    url(r'^view_your_hood/',views.view_hood,name='hood'),
    url(r'^businesses/',views.view_business,name='biz'),
    url(r'^searched/', views.search_results, name='search_results'),
    url(r'^post/',views.new_post,name='post'),
    ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
