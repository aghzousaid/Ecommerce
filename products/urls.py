
from django.conf.urls import url

from products.views import *

urlpatterns = [
    url(r'^products/$', ProductListView.as_view()),
    url(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
]

