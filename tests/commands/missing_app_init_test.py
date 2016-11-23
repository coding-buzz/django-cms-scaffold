from __future__ import unicode_literals

import os

from tests.base_test import BaseTest
from scaffold.management.commands.scaffold_init import Command as InitCommand

from mock import patch


class MissingAppInitTest(BaseTest):

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
