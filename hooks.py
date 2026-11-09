"""Build hooks for the blog.

The blog plugin creates a page per archive year and per category, but no
landing page for either, and it offers no option to produce one. These hooks
generate both from the views the plugin has already built, so a new year or a
new category needs no file edited.

NOTE: This reads the blog plugin's view objects. A material release that
changes them fails the build rather than producing a wrong page.
"""

from mkdocs.plugins import event_priority
from mkdocs.structure.nav import Section

from material.plugins.blog.structure import Archive, Category

BLOG_PLUGIN = "material/blog"

# Marker each landing page carries in place of its generated list.
MARKERS = {
    "archive.md": ("<!-- pw:archive -->", Archive),
    "categories.md": ("<!-- pw:categories -->", Category),
}


def _configured_title(config, src_uri):
    """Return the nav label mkdocs.yml gives a source file, if it gives one."""
    for entry in config.nav or []:
        if not isinstance(entry, dict):
            continue
        for title, target in entry.items():
            if target == src_uri:
                return title
    return None


def _generated_section(item):
    """Report whether an item is a plugin-built Archive or Categories section.

    Matches on the children's type rather than the section title, so it does
    not depend on the site's language.
    """
    if not isinstance(item, Section) or not item.children:
        return False
    return all(isinstance(c, Archive) for c in item.children) or all(
        isinstance(c, Category) for c in item.children
    )


def _render(views, page):
    """Return a markdown list of views, linked by source path.

    Linking to each view's markdown source lets mkdocs resolve the URL and
    warn if a link breaks, rather than computing a relative path here.
    """
    lines = []
    for view in views:
        count = len(view.posts)
        noun = "post" if count == 1 else "posts"
        lines.append(f"- [{view.name}]({view.file.src_uri}) &mdash; {count} {noun}")
    return "\n".join(lines) if lines else "Nothing here yet."


# Runs after the blog plugin, which registers its own handlers at -50.
@event_priority(-100)
def on_nav(nav, config, files):
    """Relabel the blog index and drop the plugin's generated nav sections.

    The landing pages generated below take those sections' place, so leaving
    them in would list every year and category twice.
    """
    blog = config.plugins[BLOG_PLUGIN].blog

    # The plugin replaces the index page with its own view, which does not
    # carry the label nav gives it. Page.title is a weak property, so the
    # configured label can be put back.
    title = _configured_title(config, blog.file.src_uri)
    if title:
        blog.title = title

    nav.items[:] = [item for item in nav.items if not _generated_section(item)]
    for item in nav.items:
        if getattr(item, "children", None):
            item.children[:] = [c for c in item.children if not _generated_section(c)]
    return nav


@event_priority(-100)
def on_page_markdown(markdown, page, config, files):
    """Replace a landing page's marker with its generated list."""
    entry = MARKERS.get(page.file.src_uri)
    if entry is None:
        return None

    marker, kind = entry
    if marker not in markdown:
        return None

    views = [v for v in config.plugins[BLOG_PLUGIN].blog.views if isinstance(v, kind)]
    if kind is Archive:
        views = sorted(views, key=lambda v: v.name, reverse=True)
    return markdown.replace(marker, _render(views, page))
