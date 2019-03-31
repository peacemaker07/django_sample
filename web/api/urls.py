from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from api.views import BookViewSet, BookBulkView

router = DefaultRouter(trailing_slash=False)
router.register(r'books/?', BookViewSet)


app_name = 'api'
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^books/bulk', BookBulkView.as_view())
]
