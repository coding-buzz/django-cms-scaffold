from __future__ import unicode_literals

import os

import scaffold.management.logger as logger


def create_file(file_path, default_content):
    logger.info('creating file {}'.format(file_path))
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write(default_content)
        logger.info('file {} has been created'.format(file_path))
    else:
        logger.warn('file {} already exists, skipping'.format(file_path))


def create_dir(dir_path):
    logger.info('creating directory {}'.format(dir_path))
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        logger.info('directory {} has been created'.format(dir_path))
    else:
        logger.warn('directory {} already exists, skipping'.format(dir_path))
