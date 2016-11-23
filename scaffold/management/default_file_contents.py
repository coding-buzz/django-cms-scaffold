from __future__ import unicode_literals


MODELS_PY = '''from cms.models.pluginmodel import CMSPlugin
'''


CMS_PLUGINS_PY = '''from cms.plugin_base import CMSPluginBase
'''


APP_SCSS = '''@import 'general/base';
@import 'general/fonts';
'''


JS_HTML = '''{{% load static %}}


{{# scripts here #}}
{{# example: <script src="{{% static '{app_name}/js/main.js' %}}"></script> #}}
'''
