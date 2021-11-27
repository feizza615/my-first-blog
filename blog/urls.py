from django.urls import path,include
from . import views
from rest_framework import routers
#from . import PostViewSet
from blog.views import PostViewSet




router = routers.DefaultRouter()
router.register(r'post', PostViewSet)

urlpatterns = [
   path('',include(router.urls)),
   path('',views.post_list,name='post_list')
]
