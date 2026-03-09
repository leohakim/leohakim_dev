from django.conf import settings
from django.urls import reverse

from leohakim_dev.content import SUPPORTED_PUBLIC_LANGUAGES
from leohakim_dev.content import get_case_study_content
from leohakim_dev.content import get_page_content
from leohakim_dev.content import get_site_ui
from leohakim_dev.content import normalize_public_language


def test_public_content_languages_match_django_languages():
    configured_languages = {code for code, _ in settings.LANGUAGES}
    assert configured_languages == set(SUPPORTED_PUBLIC_LANGUAGES)


def test_normalize_public_language_supports_variants_and_fallback():
    assert normalize_public_language("en-us") == "en"
    assert normalize_public_language("es-ar") == "es"
    assert normalize_public_language("it") == "en"
    assert normalize_public_language(None) == "en"


def test_home_page_content_resolves_featured_case_links():
    page = get_page_content("home", "es")

    assert (
        page["title"]
        == "Ingeniería clara para productos que necesitan escalar sin volverse "
        "frágiles."
    )
    assert [case["title"] for case in page["featured_cases"]] == [
        "Aire de Santa Fe",
        "Osoigo",
        "Atempora",
        "ENACT",
    ]
    assert page["featured_cases"][0]["href"] == reverse("case-study-aire")


def test_case_study_content_resolves_case_specific_ctas():
    case = get_case_study_content("atempora", "en")

    assert case["kind"] == "Product architecture case"
    assert case["primary_cta"]["href"] == reverse("contact")
    assert case["secondary_cta"]["href"] == reverse("services")


def test_site_ui_resolves_navigation_and_footer_links():
    site_ui = get_site_ui("es")

    assert site_ui["navigation"]["links"][0]["label"] == "Inicio"
    assert site_ui["navigation"]["links"][0]["href"] == reverse("home")
    assert site_ui["footer"]["links"][1]["href"] == "mailto:work@leohakim.dev"
