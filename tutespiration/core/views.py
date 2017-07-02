import json
import random
import requests

from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.utils.html import mark_safe

from .models import Quote, Photo, Inspiration

API_CLIENT_ID = 'd3a7d14e9e0385eac98efe3dd409dc0c5027a0dc464535d58fccbb6ce429beec'


class PostMixin(object):
    def post(self, request, *args, **kwargs):
        query = request.POST['query']
        quote = self.get_quote(query)
        if not quote:
            return self.render_to_response(self.get_context_data(noquote=True))

        font_index, font = Inspiration.get_random_font()

        try:
            photo = self.get_photo()
        except:
            return self.render_to_response(self.get_context_data(fail=True))

        insp = Inspiration.objects.create(font_index=font_index,
                photo=photo,
                quote=quote)

        permalink = '/{pk}'.format(pk=insp.pk)

        return self.render_to_response(self.get_context_data(
            quote=quote,
            font=mark_safe(font),
            client_id=API_CLIENT_ID,
            font_index=font_index,
            permalink=permalink,
            photo=photo))


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


class Tutespiration(PostMixin, TemplateView):
    template_name = 'tutespiration.html'

    def get_response(self):
        api_url = 'https://api.unsplash.com/photos/random'
        params = dict(
            orientation='landscape',
            client_id=API_CLIENT_ID,
        )
        headers = {'Accept-Version': 'v1'}

        resp = requests.get(url=api_url, params=params, headers=headers)
        resp.raise_for_status()
        data = json.loads(resp.text)

        return data


    def get_photo(self):
        data = self.get_response()
        photo = Photo.objects.create(alt_text=data['description'],
            image_url=data['links']['download'],
            credit_userid=data['user']['username'],
            credit_name=data['user']['name'],
            photo_id=data['id'])
        return photo


    def get_quote(self, query):
        quotes = Quote.objects.filter(text__icontains=query)
        num = quotes.count()
        if num:
            which = random.randint(0, num - 1)
            return quotes[which]
        else:
            return None


class CitableTutespiration(PostMixin, DetailView):
    template_name = 'tutespiration.html'
    model = Inspiration

    def get_context_data(self, **kwargs):
        context = super(CitableTutespiration, self).get_context_data(**kwargs)
        inspiration = self.get_object()
        context['permalink'] = self.get_object().get_absolute_url()

        context['font_index'] = inspiration.font_index
        context['font'] = mark_safe(inspiration.font)
        context['quote'] = inspiration.quote
        context['photo'] = inspiration.photo
        return context
