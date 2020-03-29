import os

from pyramid.config import Configurator


def get_from_env_or_settings(settings_name, settings, env_name=None, default=None):
    if not env_name:
        env_name = settings_name.upper().replace('.', '_')

    return os.environ.get(env_name, settings.get(settings_name, default))


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')
    config.scan()
    return config.make_wsgi_app()
