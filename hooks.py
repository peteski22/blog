"""Build hooks for the blog.

The blog plugin creates a page per archive year and per category, but no
landing page for either, and it offers no option to produce one. These hooks
generate both from the views the plugin has already built, so a new year or a
new category needs no file edited.

NOTE: This reads the blog plugin's view objects. A material release that
changes them fails the build rather than producing a wrong page.
"""

from enum import Enum

from mkdocs.plugins import event_priority, get_plugin_logger
from mkdocs.structure.nav import Section

from material.plugins.blog.structure import Archive, Category

BLOG_PLUGIN = "material/blog"

log = get_plugin_logger(__name__)


class Landing(Enum):
    """A generated landing page, keyed by the source file it is built from.

    Each member carries the marker its page holds and the view type whose
    entries fill it, so a page cannot exist without both.
    """

    ARCHIVE = ("archive.md", "<!-- pw:archive -->", Archive)
    CATEGORIES = ("categories.md", "<!-- pw:categories -->", Category)

    def __new__(cls, src_uri, marker, view_type):
        member = object.__new__(cls)
        member._value_ = src_uri
        member.src_uri = src_uri
        member.marker = marker
        member.view_type = view_type
        return member

    @classmethod
    def for_source(cls, src_uri):
        """Return the landing page built from a source file, or None."""
        try:
            return cls(src_uri)
        except ValueError:
            return None

    def sorted(self, views):
        """Return the views for this page in the order it should list them.

        Archives read newest first, by the most recent post each one holds.
        Categories keep the order the blog plugin already sorted them into.
        """
        if self is not Landing.ARCHIVE:
            return list(views)
        return sorted(views, key=_newest_post, reverse=True)


def _configured_title(nav, src_uri):
    """Return the nav label mkdocs.yml gives a source file, if it gives one.

    Walks nested sections, because nav entries may hold their own lists.
    """
    for entry in nav or []:
        if isinstance(entry, list):
            title = _configured_title(entry, src_uri)
            if title:
                return title
        elif isinstance(entry, dict):
            for label, target in entry.items():
                if target == src_uri:
                    return label
                if isinstance(target, list):
                    title = _configured_title(target, src_uri)
                    if title:
                        return title
    return None


def _drop_generated_sections(nav):
    """Remove the plugin's own view sections and report which types went.

    Returns the set of view types whose section was removed, so the caller can
    tell the difference between nothing to do and a nav it no longer matches.
    """
    removed = set()

    def prune(items):
        kept = []
        for item in items:
            view_type = _generated_section(item)
            if view_type:
                removed.add(view_type)
                continue
            if getattr(item, "children", None):
                item.children[:] = prune(item.children)
            kept.append(item)
        return kept

    nav.items[:] = prune(nav.items)
    return removed


def _generated_section(item):
    """Return the view type a plugin-built section holds, or None.

    Matches on the children's type rather than the section title, so it does
    not depend on the site's language.
    """
    if not isinstance(item, Section) or not item.children:
        return None
    for view_type in (Archive, Category):
        if all(isinstance(child, view_type) for child in item.children):
            return view_type
    return None


def _newest_post(view):
    """Return the creation date of the most recent post in a view."""
    return max(post.config.date.created for post in view.posts)


def _render(views):
    """Return a markdown list of views, linked by source path.

    Linking to each view's markdown source lets mkdocs resolve the URL and
    warn if a link breaks, rather than computing a relative path here.
    """
    lines = []
    for view in views:
        count = len(view.posts)
        noun = "post" if count == 1 else "posts"
        lines.append(f"- [{view.name}]({view.file.src_uri}) ({count} {noun})")
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
    title = _configured_title(config.nav, blog.file.src_uri)
    if title:
        blog.title = title
    else:
        log.warning(
            "No nav label is configured for %s, so the blog index will be "
            "named after its heading", blog.file.src_uri
        )

    present = {type(view) for view in blog.views} & {Archive, Category}
    for view_type in sorted(present - _drop_generated_sections(nav), key=str):
        log.warning(
            "No generated %s section was found in the navigation, so the "
            "header may list those entries twice", view_type.__name__.lower()
        )
    return nav


@event_priority(-100)
def on_page_markdown(markdown, page, config, files):
    """Replace a landing page's marker with its generated list."""
    landing = Landing.for_source(page.file.src_uri)
    if landing is None:
        return None

    if landing.marker not in markdown:
        log.warning(
            "%s does not contain %s, so its list was not generated",
            landing.src_uri, landing.marker
        )
        return None

    views = [
        view
        for view in config.plugins[BLOG_PLUGIN].blog.views
        if isinstance(view, landing.view_type)
    ]
    return markdown.replace(landing.marker, _render(landing.sorted(views)))
