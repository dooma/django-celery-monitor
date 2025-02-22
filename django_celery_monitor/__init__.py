# -*- coding: utf-8 -*-
"""Celery monitor for Django."""
# :copyright: (c) 2016, Ask Solem.
#             All rights reserved.
# :license:   BSD (3 Clause), see LICENSE for more details.

from __future__ import absolute_import, unicode_literals

import re

from collections import namedtuple

__version__ = '1.2.0'
__author__ = 'Jannis Leidel'
__contact__ = 'jannis@leidel.info'
__homepage__ = 'https://github.com/jazzband/django-celery-monitor'
__docformat__ = 'restructuredtext'

# -eof meta-

version_info_t = namedtuple('version_info_t', (
    'major', 'minor', 'micro', 'releaselevel', 'serial',
))

# bumpversion can only search for {current_version}
# so we have to parse the version here.
_temp = re.match(
    r'(\d+)\.(\d+).(\d+)(.+)?', __version__).groups()
VERSION = version_info = version_info_t(
    int(_temp[0]), int(_temp[1]), int(_temp[2]), _temp[3] or '', '')
del(_temp)
del(re)

__all__ = []

default_app_config = 'django_celery_monitor.apps.CeleryMonitorConfig'
