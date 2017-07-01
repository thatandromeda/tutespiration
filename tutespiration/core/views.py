import json
import random
import requests

from django.views.generic import TemplateView
from django.utils.html import mark_safe
from .models import Quote

API_CLIENT_ID = 'd3a7d14e9e0385eac98efe3dd409dc0c5027a0dc464535d58fccbb6ce429beec'

class Tutespiration(TemplateView):
    template_name = 'tutespiration.html'
    fonts = ["'Kaushan Script', cursive", "'Sue Ellen Francisco', cursive",
             "'Qwigley', cursive", "'Shadows Into Light', cursive"]

    def get_photo(self):
        api_url = 'https://api.unsplash.com/photos/random'
        params = dict(
            orientation='landscape',
            client_id=API_CLIENT_ID,
        )
        headers = {'Accept-Version': 'v1'}

        resp = requests.get(url=api_url, params=params, headers=headers)
        resp.raise_for_status()

        data = json.loads(resp.text)
        photo = {}
        photo['alt_text'] = data['description']
        photo['image_url'] = data['links']['download']
        photo['credit_userid'] = data['user']['username']
        photo['credit_name'] = data['user']['name']
        return photo


    def get_quote(self, query):
        quotes = Quote.objects.filter(text__icontains=query)
        num = quotes.count()
        which = random.randint(0, num)
        return quotes[which]


    def post(self, request, *args, **kwargs):
        query = request.POST['query']
        quote = self.get_quote(query)
        font = random.choice(self.fonts)
        return self.render_to_response(self.get_context_data(
            quote=quote,
            font=mark_safe(font),
            client_id=API_CLIENT_ID,
            ** self.get_photo()))

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
