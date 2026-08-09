"""A podpack site, and the worked output of following creating-a-site.md.

It exists to demonstrate the one thing podpack's own repository cannot: a site
installing an app from outside itself. podpack is a framework and installs no
app; this is a site, and installing apps is what a site is for.
"""

import podpack


def create_app():
    return podpack.create_app(site_package="podpack_demo")
