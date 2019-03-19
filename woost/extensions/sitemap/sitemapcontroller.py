#-*- coding: utf-8 -*-
u"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
import cherrypy
from woost import app
from woost.controllers.publishablecontroller import PublishableController


class SitemapController(PublishableController):

    def _produce_content(self, **kwargs):
        cherrypy.response.headers["Content-Type"] = "text/xml"
        for fragment in app.publishable.generate_sitemap():
            yield fragment

