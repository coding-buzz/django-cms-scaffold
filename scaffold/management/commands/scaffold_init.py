from __future__ import unicode_literals

import os

from django.core.management.base import BaseCommand
from django.conf import settings

from scaffold.management.exceptions import ScaffoldException
import scaffold.management.logger as logger
import scaffold.management.file_manager as file_manager
import scaffold.management.default_file_contents as default_contents


class Command(BaseCommand):

    _DIRS_TO_CREATE = [
        'templates/{app_name}',
        'templates/{app_name}/plugins',
        'templates/{app_name}/partials',
        'static/{app_name}',
        'static/{app_name}/images',
        'static/{app_name}/js',
        'static/{app_name}/js/vendor',
        'static/{app_name}/scss',
        'static/{app_name}/scss/plugins',
        'static/{app_name}/scss/general',
    ]

    _FILES_TO_CREATE = [
        {
            'path': 'models.py',
            'content': default_contents.MODELS_PY
        }, {
            'path': 'cms_plugins.py',
            'content': default_contents.CMS_PLUGINS_PY
        }, {
            'path': 'static/{app_name}/scss/general/fonts.scss',
            'content': ''
        }, {
            'path': 'static/{app_name}/scss/general/base.scss',
            'content': ''
        }, {
            'path': 'static/{app_name}/scss/app.scss',
            'content': default_contents.APP_SCSS
        }, {
            'path': 'templates/{app_name}/partials/_js.html',
            'content': default_contents.JS_HTML
        }
    ]

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.app_path = None
        self.app = None

    def add_arguments(self, parser):
        parser.add_argument('--app', type=str)

    def handle(self, *args, **options):
        try:
            self.app = options.get('app', '')
            self.app_path = self._get_app_path(self.app)
        except ScaffoldException as e:
            logger.error(unicode(e))
            return

        logger.info('initializing ' + self.app)
        logger.info('app\'s path: ' + self.app_path)

        for dir_path in self._DIRS_TO_CREATE:
            self._create_directory(dir_path)

        for file_element in self._FILES_TO_CREATE:
            self._create_file(file_element)

    @staticmethod
    def _get_app_path(app):
        if app is None or not len(app.strip()):
            raise ScaffoldException('app name cannot be empty')
        path = os.path.join(settings.BASE_DIR, app)
        if not os.path.isdir(path):
            raise ScaffoldException('app directory {} does not exist'.format(path))
        return path

    def _create_file(self, file_element):
        file_manager.create_file(
            file_path=os.path.join(self.app_path, file_element['path'].format(app_name=self.app)),
            default_content=file_element['content'].format(app_name=self.app)
        )

    def _create_directory(self, dir_element):
        dir_path = os.path.join(self.app_path, dir_element.format(app_name=self.app))
        file_manager.create_dir(dir_path)
