"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from cocktail.events import when
from woost.admin.sections import CRUD
from woost.admin.sections.contentsection import ContentSection
from woost.extensions.sitemap.sitemap import SiteMap


@when(ContentSection.declared)
def add_sections(e):
    e.source.append(CRUD("sitemaps", model = SiteMap))

