"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from woost.models import ExtensionAssets, Configuration, Controller

def install():
    """Creates the assets required by the sitemap extension."""

    assets = ExtensionAssets("sitemap")

    # Sitemap controller
    Configuration.instance.default_sitemap_controller = assets.require(
        Controller,
        "sitemap_controller",
        title = assets.TRANSLATIONS,
        python_name =
            "woost.extensions.sitemap.sitemapcontroller.SitemapController"
    )

