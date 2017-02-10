"""Carbon Sphinx Theme"""

import os


__all__ = ['get_html_templates_path', 'get_html_theme_path']


def get_html_theme_path():
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def get_html_templates_path():
    return os.path.join(
        os.path.abspath(os.path.dirname((__file__))),
        'templates',
    )
