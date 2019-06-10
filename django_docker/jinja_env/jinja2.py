from django.templatetags.static import static
from django.urls import reverse

from jinja2 import Environment

# "globals" is a Jinja Template Variables' Dictionary.


class JinjaEnvironment(Environment):

    def __init__(self, **kwargs):
        super(JinjaEnvironment, self).__init__(**kwargs)
        self.globals['static'] = static
        self.globals['url'] = reverse
