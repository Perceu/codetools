from django.urls import path
from codetools.texttools.views import CaseTextView

app_name = "texttools"

urlpatterns = [
    path('cases', CaseTextView.as_view(), name="cases"),
]
