from django.conf.urls import url
from django.contrib import admin

from fasttrack.views import *


admin.site.site_header = '패스트트랙'

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Custom Views
    url(r'^', HomeTemplateView.as_view(), name="home"),
]
