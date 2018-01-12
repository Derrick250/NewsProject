

from django.conf.urls import url
from project.snippets import views

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),

    url(r'^users/$', views.user_list),
    url(r'^users/(?P<pk>[0-9]+)/$', views.user_detail),

    url(r'^articles/$', views.article_list),
    url(r'^articles/(?P<pk>[0-9]+)/$', views.article_detail),

    url(r'^comments/$', views.comment_list),
    url(r'^comments/(?P<pk>[0-9]+)/$', views.comment_detail),

    url(r'^usertags/$', views.usertag_list),
    url(r'^usertags/(?P<pk>[0-9]+)/$', views.usertag_detail),

    url(r'^articletags/$', views.articletag_list),
    url(r'^articletags/(?P<pk>[0-9]+)/$', views.articletag_detail)
]