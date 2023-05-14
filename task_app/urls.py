from django.urls import path
from.views import *
urlpatterns=[
    path('userview/',userview.as_view(),name='userview'),
    path('postview/',post_allview.as_view(),name='postallview'),
    path('postview/<int:id>',postview.as_view(),name='postview'),
    path('likeview/',likeallview.as_view(),name='likeallview'),
    path('likeview/<int:id>',likeview.as_view(),name='likeview'),
    
]