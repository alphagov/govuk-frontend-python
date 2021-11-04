
from flask.templating import Environment as FlaskEnvironment
from jinja2 import select_autoescape
from govuk_frontend_jinja.templates import Environment as NunjucksEnvironment
from govuk_frontend_jinja.templates import NunjucksExtension, NunjucksUndefined


class Environment(NunjucksEnvironment, FlaskEnvironment):
    pass


def init_govuk_frontend(app):
    """Use the govuk_frontend_jinja Jinja environment in a Flask app

    >>> from flask import Flask
    >>> app = Flask("cheeseshop_service")
    >>> init_govuk_frontend(app)
    """
    app.jinja_environment = Environment
    app.select_jinja_autoescape = select_autoescape(("html", "htm", "xml", "xhtml", "njk"))
    app.jinja_env.add_extension(extension=NunjucksExtension)
    app.jinja_env.undefined = NunjucksUndefined
    # jinja_options = app.jinja_options.copy()
    # jinja_options["undefined"] = NunjucksUndefined
    # app.jinja_options = jinja_options
    return app
