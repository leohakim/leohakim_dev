from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.urls import reverse
from django.views import defaults as default_views
from django.views.generic import TemplateView
from django.views.i18n import set_language


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        is_en = self.request.LANGUAGE_CODE.startswith("en")
        context["trust_logos"] = [
            {"name": "Aire de Santa Fe", "url": reverse("case-study-aire")},
            {"name": "Osoigo", "url": reverse("case-study-osoigo")},
            {"name": "ENACT", "url": reverse("case-study-enact")},
            {"name": "Atempora", "url": reverse("case-study-atempora")},
            {"name": "Embever", "url": reverse("case-study-embever")},
        ]
        if is_en:
            context["hero_highlights"] = [
                "Systems that stay reliable under pressure.",
                "Technical debt turned into operational strength.",
                "Engineering decisions that impact revenue and growth.",
            ]
            context["help_areas"] = [
                {
                    "title": "Stabilize fast-growing products",
                    "description": (
                        "Reduce incidents and improve day-to-day reliability "
                        "in products under real demand."
                    ),
                },
                {
                    "title": "Modernize without business disruption",
                    "description": (
                        "Upgrade critical backend areas while keeping service "
                        "continuity and delivery pace."
                    ),
                },
                {
                    "title": "Scale with clear architecture",
                    "description": (
                        "Build a predictable technical base that supports "
                        "growth without chaos."
                    ),
                },
            ]
            context["featured_cases"] = [
                {
                    "title": "Aire de Santa Fe",
                    "summary": (
                        "High-traffic media environment improved with more "
                        "predictable operations."
                    ),
                    "href": reverse("case-study-aire"),
                },
                {
                    "title": "Osoigo",
                    "summary": (
                        "Civic participation platform stabilized to operate "
                        "safely at scale."
                    ),
                    "href": reverse("case-study-osoigo"),
                },
                {
                    "title": "ENACT",
                    "summary": (
                        "International multi-team project coordinated "
                        "with safer technical delivery."
                    ),
                    "href": reverse("case-study-enact"),
                },
                {
                    "title": "Atempora",
                    "summary": (
                        "Complex SaaS rules and flows reorganized for "
                        "clearer operations."
                    ),
                    "href": reverse("case-study-atempora"),
                },
            ]
            context["social_links"] = [
                {"label": "Case studies", "href": reverse("case-studies")},
                {"label": "Email", "href": "mailto:work@leohakim.dev"},
                {"label": "Book intro call", "href": "https://cal.leohakim.dev/"},
            ]
        else:
            context["hero_highlights"] = [
                "Sistemas que dejan de fallar bajo presión.",
                "Deuda técnica convertida en ventaja operativa.",
                "Decisiones técnicas con impacto comercial real.",
            ]
            context["help_areas"] = [
                {
                    "title": "Estabilizar productos que crecieron rápido",
                    "description": (
                        "Reducir incidentes y mejorar confiabilidad diaria "
                        "en productos bajo demanda real."
                    ),
                },
                {
                    "title": "Modernizar backend sin frenar el negocio",
                    "description": (
                        "Actualizar áreas críticas manteniendo continuidad "
                        "de servicio y ritmo de entrega."
                    ),
                },
                {
                    "title": "Escalar con arquitectura clara y predecible",
                    "description": (
                        "Construir una base técnica ordenada para crecer "
                        "sin volver al caos operativo."
                    ),
                },
            ]
            context["featured_cases"] = [
                {
                    "title": "Aire de Santa Fe",
                    "summary": (
                        "Entorno media de alto tráfico mejorado con una "
                        "operación más predecible."
                    ),
                    "href": reverse("case-study-aire"),
                },
                {
                    "title": "Osoigo",
                    "summary": (
                        "Plataforma cívica estabilizada para operar a escala "
                        "con menor riesgo."
                    ),
                    "href": reverse("case-study-osoigo"),
                },
                {
                    "title": "ENACT",
                    "summary": (
                        "Proyecto internacional coordinado con "
                        "entrega técnica más segura."
                    ),
                    "href": reverse("case-study-enact"),
                },
                {
                    "title": "Atempora",
                    "summary": (
                        "Reglas y flujos complejos de SaaS ordenados para "
                        "operar con más claridad."
                    ),
                    "href": reverse("case-study-atempora"),
                },
            ]
            context["social_links"] = [
                {"label": "Casos", "href": reverse("case-studies")},
                {"label": "Email", "href": "mailto:work@leohakim.dev"},
                {"label": "Agendar llamada", "href": "https://cal.leohakim.dev/"},
            ]
        return context


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path(
        "about/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    path(
        "case-studies/",
        TemplateView.as_view(template_name="pages/case_studies.html"),
        name="case-studies",
    ),
    # Case studies detail pages
    path(
        "case-studies/aire/",
        TemplateView.as_view(template_name="pages/case_studies/aire.html"),
        name="case-study-aire",
    ),
    path(
        "case-studies/osoigo/",
        TemplateView.as_view(template_name="pages/case_studies/osoigo.html"),
        name="case-study-osoigo",
    ),
    path(
        "case-studies/enact/",
        TemplateView.as_view(template_name="pages/case_studies/enact.html"),
        name="case-study-enact",
    ),
    path(
        "case-studies/atempora/",
        TemplateView.as_view(template_name="pages/case_studies/atempora.html"),
        name="case-study-atempora",
    ),
    path(
        "case-studies/embever/",
        TemplateView.as_view(template_name="pages/case_studies/embever.html"),
        name="case-study-embever",
    ),
    path(
        "services/",
        TemplateView.as_view(template_name="pages/services.html"),
        name="services",
    ),
    path(
        "writing/",
        TemplateView.as_view(template_name="pages/writing.html"),
        name="writing",
    ),
    path(
        "contact/",
        TemplateView.as_view(template_name="pages/contact.html"),
        name="contact",
    ),
    path(
        "cv/",
        TemplateView.as_view(template_name="pages/cv.html"),
        name="cv",
    ),
    path(
        "playbook/",
        TemplateView.as_view(template_name="pages/playbook.html"),
        name="playbook",
    ),
    path(
        "speaking/",
        TemplateView.as_view(template_name="pages/speaking.html"),
        name="speaking",
    ),
    path("set-language/", set_language, name="set_language"),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("leohakim_dev.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    # ...
    # Media files
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [
            path("__debug__/", include(debug_toolbar.urls)),
            *urlpatterns,
        ]
