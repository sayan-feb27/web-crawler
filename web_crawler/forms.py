from django.forms import Form, URLField
from django.forms.widgets import URLInput


class WebCrawlerForm(Form):
    url = URLField(
        label="url",
        required=True,
        widget=URLInput(
            attrs={"class": "input is-primary", "x-model": "url"}
        )
    )
