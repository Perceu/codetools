from django.views.generic import TemplateView

class TemplateMediaView(TemplateView):

    class Media:
        js = []
        babels = []
        css = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.Media:
            context['media'] = {}
            context['media']['js'] = self.Media.js if hasattr(self.Media, 'js') else []
            context['media']['babels'] = self.Media.babels if hasattr(self.Media, 'babels') else []
            context['media']['css'] = self.Media.css if hasattr(self.Media, 'css') else {}

        return context