import re
from http import HTTPStatus

import pytest
from django.urls import reverse

PUBLIC_ROUTE_NAMES = [
    "home",
    "about",
    "case-studies",
    "case-study-aire",
    "case-study-osoigo",
    "case-study-enact",
    "case-study-atempora",
    "case-study-embever",
    "services",
    "writing",
    "contact",
    "cv",
    "playbook",
    "speaking",
]


@pytest.mark.parametrize(
    "route_name",
    PUBLIC_ROUTE_NAMES,
)
def test_public_pages_return_200(client, route_name):
    response = client.get(reverse(route_name))
    assert response.status_code == HTTPStatus.OK


@pytest.mark.parametrize("route_name", PUBLIC_ROUTE_NAMES)
def test_public_pages_change_content_with_language(client, route_name):
    response_en = client.get(reverse(route_name), HTTP_ACCEPT_LANGUAGE="en")
    response_es = client.get(reverse(route_name), HTTP_ACCEPT_LANGUAGE="es")

    assert response_en.status_code == HTTPStatus.OK
    assert response_es.status_code == HTTPStatus.OK

    text_en = response_en.content.decode("utf-8", errors="ignore")
    text_es = response_es.content.decode("utf-8", errors="ignore")

    assert '<html lang="en">' in text_en
    assert '<html lang="es">' in text_es
    assert re.search(r">\s*Home\s*<", text_en)
    assert re.search(r">\s*Inicio\s*<", text_es)


def test_home_navigation_labels_follow_selected_language(client):
    response_en = client.get(reverse("home"), HTTP_ACCEPT_LANGUAGE="en")
    response_es = client.get(reverse("home"), HTTP_ACCEPT_LANGUAGE="es")

    text_en = response_en.content.decode("utf-8", errors="ignore")
    text_es = response_es.content.decode("utf-8", errors="ignore")

    assert re.search(r">\s*Home\s*<", text_en)
    assert re.search(r">\s*Case Studies\s*<", text_en)
    assert re.search(r">\s*Services\s*<", text_en)
    assert re.search(r">\s*Contact\s*<", text_en)

    assert re.search(r">\s*Inicio\s*<", text_es)
    assert re.search(r">\s*Casos de éxito\s*<", text_es)
    assert re.search(r">\s*Servicios\s*<", text_es)
    assert re.search(r">\s*Contacto\s*<", text_es)


def test_set_language_switches_rendered_site_language(client):
    response = client.post(
        reverse("set_language"),
        data={"language": "es", "next": reverse("home")},
        follow=True,
    )

    assert response.status_code == HTTPStatus.OK
    text = response.content.decode("utf-8", errors="ignore")

    assert '<html lang="es">' in text
    assert re.search(r">\s*Inicio\s*<", text)
