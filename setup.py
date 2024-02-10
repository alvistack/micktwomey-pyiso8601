# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['iso8601']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'iso8601',
    'version': '2.1.0',
    'description': 'Simple module to parse ISO 8601 dates',
    'author': 'Michael Twomey',
    'author_email': 'mick@twomeylee.name',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/micktwomey/pyiso8601',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
