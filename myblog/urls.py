from django.conf.urls import url
from myblog.views import stub_view
# import the new view
from myblog.views import list_view
# import the view
from myblog.views import detail_view

urlpatterns = [
    url(r'^$',
        list_view,
        name="blog_index"),
    url(r'^posts/(?P<post_id>\d+)/$',
        detail_view,
        name='blog_detail'),
]

