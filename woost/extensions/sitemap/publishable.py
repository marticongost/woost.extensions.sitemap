#-*- coding: utf-8 -*-
"""

@author:		Martí Congost
@contact:		marti.congost@whads.com
@organization:	Whads/Accent SL
@since:			February 2010
"""
from decimal import Decimal
from cocktail.translations import translations
from cocktail import schema
from woost.models import Publishable, URI

translations.load_bundle("woost.extensions.sitemap.publishable")

URI.default_sitemap_indexable = False

Publishable.add_member(
    schema.String("x_sitemap_change_frequency",
        enumeration = [
            "always",
            "hourly",
            "daily",
            "weekly",
            "monthly",
            "yearly",
            "never"
        ],
        member_group = "meta.robots",
        text_search = False,
        listed_by_default = False
    ),
    append = True
)

Publishable.add_member(
    schema.Decimal("x_sitemap_priority",
        min = 0,
        max = 1,
        listed_by_default = False,
        member_group = "meta.robots"
    ),
    append = True
)

