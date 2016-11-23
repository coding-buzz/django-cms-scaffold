from __future__ import unicode_literals

import os

from tests.base_test import BaseTest
from scaffold.management.commands.scaffold_init import Command as InitCommand
import scaffold.management.default_file_contents as default_contents

from mock import patch


class FreshAppInitTest(BaseTest):

    @patch('scaffold.management.logger.info')
    def test_fresh_app_init(self, info_logger):
        command = InitCommand()
        options = {
            'app': self.TEST_APP_NAME
        }
        command.handle(**options)

        self._check_plugins_file()
        self._check_templates_dir()
        self._check_models_file()

        static_dir_path = os.path.join(self.TEST_APP_DIR, 'static', self.TEST_APP_NAME)

        self._check_static_dir(static_dir_path)
        self._check_js_dir(static_dir_path)
        self._check_scss_dir(static_dir_path)

        info_logger.assert_called()

    def _check_plugins_file(self):
        plugins_file_path = os.path.join(self.TEST_APP_DIR, 'cms_plugins.py')
        self.assertTrue(os.path.isfile(plugins_file_path), 'missing cms_plugins.py file')
        with open(plugins_file_path, 'r') as f:
            content = f.read()
            self.assertEqual(content, default_contents.CMS_PLUGINS_PY, 'wrong content of cms_plugins.py file')

    def _check_templates_dir(self):
        templates_dir_path = os.path.join(self.TEST_APP_DIR, 'templates', self.TEST_APP_NAME)
        self.assertTrue(os.path.isdir(templates_dir_path), 'missing templates directory')

        plugins_dir_path = os.path.join(templates_dir_path, 'plugins')
        self.assertTrue(os.path.isdir(plugins_dir_path), 'missing templates/plugins directory')

        partials_dir_path = os.path.join(templates_dir_path, 'partials')
        self.assertTrue(os.path.isdir(partials_dir_path), 'missing templates/partials directory')

        js_html_file_path = os.path.join(partials_dir_path, '_js.html')
        with open(js_html_file_path, 'r') as f:
            content = f.read()
            self.assertEqual(content,
                             default_contents.JS_HTML.format(app_name=self.TEST_APP_NAME),
                             'wrong content of _js.html file')

    def _check_models_file(self):
        models_file_path = os.path.join(self.TEST_APP_DIR, 'models.py')
        self.assertTrue(os.path.isfile(models_file_path), 'missing models.py files')
        with open(models_file_path, 'r') as f:
            content = f.read()
            self.assertEqual(content, default_contents.MODELS_PY, 'wrong content of models.py file')

    def _check_static_dir(self, static_dir_path):
        self.assertTrue(os.path.isdir(static_dir_path), 'missing static/<app_name> directory')

    def _check_js_dir(self, static_dir_path):
        js_dir_path = os.path.join(static_dir_path, 'js')
        self.assertTrue(os.path.isdir(js_dir_path), 'missing static/<app_name>/js directory')
        js_vendor_dir_path = os.path.join(js_dir_path, 'vendor')
        self.assertTrue(os.path.isdir(js_vendor_dir_path), 'missing static/<app_name>/js/vendor directory')

    def _check_scss_dir(self, static_dir_path):
        scss_dir_path = os.path.join(static_dir_path, 'scss')
        self.assertTrue(os.path.isdir(scss_dir_path), 'missing static/<app_name>/scss directory')

        scss_plugins_dir_path = os.path.join(scss_dir_path, 'plugins')
        self.assertTrue(os.path.isdir(scss_plugins_dir_path), 'missing static/<app_name>/scss/plugins directory')

        scss_general_dir_path = os.path.join(scss_dir_path, 'general')
        self.assertTrue(os.path.isdir(scss_general_dir_path), 'missing static/<app_name>/scss/general directory')

        app_scss_file_path = os.path.join(scss_dir_path, 'app.scss')
        with open(app_scss_file_path, 'r') as f:
            content = f.read()
            self.assertEqual(content, default_contents.APP_SCSS, 'wrong content of app.scss file')
