import random

from django.views.generic import TemplateView
from django.utils.html import mark_safe
from .models import Quote


class Tutespiration(TemplateView):
    template_name = 'tutespiration.html'
    fonts = ["'Kaushan Script', cursive", "'Sue Ellen Francisco', cursive",
             "'Qwigley', cursive", "'Shadows Into Light', cursive"]

    def post(self, request, *args, **kwargs):
        query = request.POST['query']
        quote = Quote.objects.filter(text__icontains=query).first()
        font = random.choice(self.fonts)
        return self.render_to_response(self.get_context_data(
            quote=quote,
            font=mark_safe(font)))

    def render_to_response(self, context, **response_kwargs):
        """
        From django.views.generic.edit.FormView
        """
        response_kwargs.setdefault('content_type', self.content_type)
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            using=self.template_engine,
            **response_kwargs
        )
