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
    assert normalize_public_language("it-it") == "it"
    assert normalize_public_language("it") == "it"
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
    assert page["featured_cases"][0]["kind"] == "Caso de estudio"


def test_home_page_content_includes_best_fit_items():
    page = get_page_content("home", "en")
    expected_best_fit_items = [
        "Growth-stage SaaS",
        "Media and live platforms",
        "Teams that need strong seniority",
    ]

    assert page["ideal_for_label"] == "Best fit"
    assert len(page["ideal_for_items"]) == len(expected_best_fit_items)
    for expected, current in zip(
        expected_best_fit_items,
        page["ideal_for_items"],
        strict=True,
    ):
        assert expected in current


def test_cv_page_content_matches_latest_profile_version():
    page = get_page_content("cv", "en")

    assert "15+ years of experience" in page["lead"]
    assert page["snapshot_items"][0] == (
        "15+ years building production systems with Python and Django"
    )
    assert page["best_fit_title"] == "Recent experience"
    assert page["versions_panel"]["title"] == "Selected project"
    assert page["availability_title"] == "Education and languages"


def test_case_study_content_resolves_case_specific_ctas():
    case = get_case_study_content("atempora", "en")

    assert case["kind"] == "Product architecture case"
    assert case["primary_cta"]["href"] == reverse("contact")
    assert case["secondary_cta"]["href"] == reverse("services")


def test_case_study_content_includes_factual_summary_cards():
    case = get_case_study_content("aire", "es")

    assert [fact["label"] for fact in case["facts"]] == [
        "Sector",
        "Rol",
        "Foco principal",
    ]
    assert "alto tráfico" in case["facts"][0]["value"]


def test_case_study_content_supports_italian():
    case = get_case_study_content("aire", "it")

    assert case["kind"] == "Caso di studio"
    assert "notifiche push" in case["hero_summary"]
    assert case["facts"][0]["label"] == "Settore"


def test_writing_page_content_includes_positioning_and_formats():
    page = get_page_content("writing", "en")
    expected_titles = [
        "Production notes",
        "Architecture essays",
        "Team decision guides",
    ]

    assert "Selective writing" in page["positioning_title"]
    assert [card["title"] for card in page["format_cards"]] == expected_titles


def test_speaking_page_content_supports_italian_formats():
    page = get_page_content("speaking", "it")
    expected_titles = [
        "Talk per conferenze",
        "Sessioni per community",
        "Talk interni per team",
    ]

    assert page["formats_title"] == "Formati che funzionano bene"
    assert [card["title"] for card in page["format_cards"]] == expected_titles


def test_site_ui_resolves_navigation_and_footer_links():
    site_ui = get_site_ui("es")

    assert site_ui["navigation"]["links"][0]["label"] == "Inicio"
    assert site_ui["navigation"]["links"][0]["href"] == reverse("home")
    assert site_ui["footer"]["links"][1]["href"] == "mailto:work@leohakim.dev"


def test_site_ui_supports_italian_labels():
    site_ui = get_site_ui("it")

    assert site_ui["navigation"]["links"][1]["label"] == "Casi di studio"
    assert site_ui["navigation"]["primary_cta"]["label"] == "Contatto"
