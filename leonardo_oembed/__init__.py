
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

default_app_config = 'leonardo_oembed.Config'

try:
    from local_settings import APPS
except ImportError:
    pass

class Default(object):

    optgroup = 'Oembed'

    if 'leonardo_oembed' in APPS:
        apps = [
            'feincms_oembed',
            'leonardo_oembed',
        ]

        widgets = [
            'leonardo_oembed.models.OembedWidget',
            'leonardo_oembed.models.FeedWidget'
        ]

        config = {
            'Web': {
                'EMBEDLY_KEY': ('62809705-1', _('Embedly API key')),
            }
        }


class Config(AppConfig, Default):
    name = 'leonardo_oembed'
    verbose_name = ("Leonardo OEmbed")

default = Default()
