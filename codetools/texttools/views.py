from codetools.core.base.views.generic import TemplateMediaView


# Create your views here.

class CaseTextView(TemplateMediaView):
    template_name = "case-text.html"

    class Media:
        js = (
            'vendor/react.production.min.js',
            'vendor/react-dom.production.min.js',
            'vendor/babel.min.js',
        )
        babels = (
            'js/case-text.js', 
        )