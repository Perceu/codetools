from django.urls import path
from codetools.knowledge.views import apis, open_source_tools, yt_channels

app_name = "knowledge"

urlpatterns = [
    path('apis', apis, name="apis"),
    path('open-source-tools', open_source_tools, name="open-source-tools"),
    path('yt-channels', yt_channels, name="yt-channels"),
]
