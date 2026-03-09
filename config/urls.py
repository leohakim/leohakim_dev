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
        ]
        if is_en:
            context["hero_highlights"] = [
                "Reliable systems for products already under real demand.",
                "Clearer technical decisions across backend, product, and operations.",
                "Engineering that helps teams grow without making the platform fragile.",  # noqa: E501
            ]
            context["help_areas"] = [
                {
                    "title": "Stabilize products that are already feeling pressure",
                    "description": (
                        "When the backend starts slowing product and operations "
                        "down, I help restore predictability and reduce risk."
                    ),
                },
                {
                    "title": "Modernize critical backend without blocking delivery",
                    "description": (
                        "I improve fragile areas of the system while keeping "
                        "service continuity and the team moving."
                    ),
                },
                {
                    "title": "Turn complex product rules into workable systems",
                    "description": (
                        "I design clearer domain and platform decisions so "
                        "growth does not create chaos later."
                    ),
                },
            ]
            context["featured_cases"] = [
                {
                    "title": "Aire de Santa Fe",
                    "summary": (
                        "Backend, push, and operating foundations for a "
                        "high-traffic media app that needed more predictable delivery."
                    ),
                    "href": reverse("case-study-aire"),
                },
                {
                    "title": "Osoigo",
                    "summary": (
                        "Sensitive backend areas reinforced so a live "
                        "participation platform could keep evolving with less risk."
                    ),
                    "href": reverse("case-study-osoigo"),
                },
                {
                    "title": "Atempora",
                    "summary": (
                        "Product architecture for a SaaS with scheduling, "
                        "payments, and complex rules that could not be improvised."
                    ),
                    "href": reverse("case-study-atempora"),
                },
                {
                    "title": "ENACT",
                    "summary": (
                        "Infrastructure and deployment work in a multi-team "
                        "international environment that needed repeatability."
                    ),
                    "href": reverse("case-study-enact"),
                },
            ]
            context["social_links"] = [
                {"label": "Case studies", "href": reverse("case-studies")},
                {"label": "Email", "href": "mailto:work@leohakim.dev"},
                {"label": "Contact", "href": reverse("contact")},
            ]
        else:
            context["hero_highlights"] = [
                "Sistemas confiables para productos que ya están bajo demanda real.",
                "Decisiones más claras entre backend, producto y operación.",
                "Ingeniería que permite crecer sin volver frágil la plataforma.",
            ]
            context["help_areas"] = [
                {
                    "title": "Estabilizar productos que ya sienten la presión",
                    "description": (
                        "Cuando el backend empieza a frenar producto y "
                        "operación, ayudo a recuperar previsibilidad y bajar riesgo."
                    ),
                },
                {
                    "title": "Modernizar backend crítico sin frenar la entrega",
                    "description": (
                        "Mejora de áreas frágiles del sistema manteniendo "
                        "continuidad de servicio y avance del equipo."
                    ),
                },
                {
                    "title": "Convertir reglas complejas en sistemas que se pueden operar",  # noqa: E501
                    "description": (
                        "Diseño decisiones de dominio y plataforma más claras "
                        "para crecer sin volver al caos."
                    ),
                },
            ]
            context["featured_cases"] = [
                {
                    "title": "Aire de Santa Fe",
                    "summary": (
                        "Backend, push y base operativa para una app de "
                        "medios de alto tráfico que necesitaba más previsibilidad."
                    ),
                    "href": reverse("case-study-aire"),
                },
                {
                    "title": "Osoigo",
                    "summary": (
                        "Refuerzo de áreas sensibles del backend para que "
                        "una plataforma viva pudiera seguir evolucionando con menos riesgo."  # noqa: E501
                    ),
                    "href": reverse("case-study-osoigo"),
                },
                {
                    "title": "Atempora",
                    "summary": (
                        "Arquitectura de producto para un SaaS con agenda, "
                        "pagos y reglas complejas que no se podían improvisar."
                    ),
                    "href": reverse("case-study-atempora"),
                },
                {
                    "title": "ENACT",
                    "summary": (
                        "Infraestructura y despliegue en un entorno "
                        "internacional multi-equipo que necesitaba repetibilidad."
                    ),
                    "href": reverse("case-study-enact"),
                },
            ]
            context["social_links"] = [
                {"label": "Casos", "href": reverse("case-studies")},
                {"label": "Email", "href": "mailto:work@leohakim.dev"},
                {"label": "Contacto", "href": reverse("contact")},
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
