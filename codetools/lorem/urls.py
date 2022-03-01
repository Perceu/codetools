from django.urls import path
from codetools.lorem.views import lorem_excel, lorem_ipsum, lorem_pixel, lorem_pdf, lorem_doc, lorem_pixel_index, lorem_docs_index

app_name = "lorem"

urlpatterns = [
    path('ipsum', lorem_ipsum, name="ipsum"),
    path('pixel', lorem_pixel, name="pixel"),
    path('pixel-index', lorem_pixel_index, name="pixel-index"),
    path('docs-index', lorem_docs_index, name="docs-index"),
    path('pdf', lorem_pdf, name="pdf"),
    path('doc', lorem_doc, name="doc"),
    path('xlsx', lorem_excel, name="xlsx"),
]
