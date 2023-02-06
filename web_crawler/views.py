from http import HTTPStatus

from django.views.generic import FormView, View, TemplateView
from django.http.response import JsonResponse


from .forms import WebCrawlerForm
from .crawler import Crawler


class HomePage(FormView):
    http_method_names = ["get"]
    template_name = "home.html"
    form_class = WebCrawlerForm


class NestedView(TemplateView):
    http_method_names = ["get"]
    template_name = "nested.html"


class CrawlerView(View):
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        form: WebCrawlerForm = WebCrawlerForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get("url")
            links = Crawler(url=url).crawl()
            return JsonResponse(data=dict(links=links, url=url))
        return JsonResponse(data=form.errors, status=HTTPStatus.BAD_REQUEST)
