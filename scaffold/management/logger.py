from __future__ import unicode_literals, print_function


_COLORS = {
    'INFO': '\033[92m',
    'ERROR': '\033[91m',
    'WARN': '\033[93m',
    'END': '\033[0m'
}


def info(message):
    print(_COLORS['INFO'] + '[INFO] ' + str(message) + _COLORS['END'])


def error(message):
    print(_COLORS['ERROR'] + '[ERROR] ' + str(message) + _COLORS['END'])


def warn(message):
    print(_COLORS['WARN'] + '[WARN] ' + str(message) + _COLORS['END'])
