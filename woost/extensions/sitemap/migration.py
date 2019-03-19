"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from cocktail.persistence import migration_step

@migration_step
def prefix_members(e):

    from woost.models import Publishable

    for pub in Publishable.select():
        for key in ("priority", "change_frequency"):
            old_key = "sitemap_" + key
            try:
                value = getattr(pub, old_key)
            except KeyError:
                pass
            else:
                delattr(pub, old_key)
                setattr(pub, "x_sitemap_" + key, value)

