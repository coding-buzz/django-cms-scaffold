from __future__ import unicode_literals

import os

from tests.base import BaseTest
from scaffold.management.commands.scaffold_init import Command as InitCommand

from mock import patch


class ScaffoldInitTest(BaseTest):

    @patch('scaffold.management.logger.error')
    def test_missing_app_init(self, error_logger):
        command = InitCommand()
        options = {
            'app': 'missing-app'
        }
        command.handle(**options)
        expected_log = 'app directory {} does not exist'.format(
            os.path.join(self.TEST_PROJECT_DIR, 'missing-app')
        )
        error_logger.assert_called_with(expected_log)

    @patch('scaffold.management.logger.info')
    def test_fresh_app_init(self, info_logger):
        command = InitCommand()
        options = {
            'app': self.TEST_APP_NAME
        }
        command.handle(**options)
        expected_info_logs = [
            'initializing {}'.format(self.TEST_APP_NAME),
            'app\'s path: {}'.format(self.TEST_APP_DIR),
            'creating file cms_plugins.py',
            'file {} has been created'.format(os.path.join(self.TEST_APP_DIR, 'cms_plugins.py')),
        ]
        info_logs = map(lambda x: unicode(x[0][0]), info_logger.call_args_list)
        self.assertListEqual(info_logs, expected_info_logs)
