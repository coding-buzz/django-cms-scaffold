from __future__ import unicode_literals

import os

from django.core.management.base import BaseCommand
from django.conf import settings

from scaffold.management.exceptions import ScaffoldException
import scaffold.management.logger as logger


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--app', type=str)

    def handle(self, *args, **options):
        try:
            app = options.get('app', None)
            app_path = self._get_app_path(app)
            logger.info('initializing ' + app)
            logger.info('app\'s path: ' + app_path)
            self._create_plugins_file(app_path)
        except ScaffoldException as e:
            logger.error(unicode(e))
            return

    @staticmethod
    def _get_app_path(app):
        if app is None or not len(app.strip()):
            raise ScaffoldException('app name cannot be empty')
        path = os.path.join(settings.BASE_DIR, app)
        if not os.path.isdir(path):
            raise ScaffoldException('app directory {} does not exist'.format(path))
        return path

    @staticmethod
    def _create_plugins_file(app_path):
        file_path = os.path.join(app_path, 'cms_plugins.py')
        logger.info('creating file cms_plugins.py'.format(file_path))
        if not os.path.exists(file_path):
            open(file_path, 'w').close()
            logger.info('file {} has been created'.format(file_path))
        else:
            logger.warn('file {} already exists'.format(file_path))
