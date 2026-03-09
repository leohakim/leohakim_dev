from __future__ import annotations

from django.utils import timezone

from leohakim_dev.content import get_site_ui


def site_ui(request):
    ui = get_site_ui(getattr(request, "LANGUAGE_CODE", None))
    ui["footer"]["copyright_text"] = ui["footer"]["copyright"].format(
        year=timezone.now().year,
    )
    return {"site_ui": ui}
