from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from django.views.i18n import set_language


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        is_en = self.request.LANGUAGE_CODE.startswith("en")
        context["trust_logos"] = [
            {"name": "Aire de Santa Fe", "url": "/case-studies/aire/"},
            {"name": "Osoigo", "url": "/case-studies/osoigo/"},
            {"name": "ENACT", "url": "/case-studies/enact/"},
            {"name": "Atempora", "url": "/case-studies/atempora/"},
            {"name": "Embever", "url": "/case-studies/embever/"},
        ]
        if is_en:
            context["hero_highlights"] = [
                "Stabilize products that grew fast and became hard to operate.",
                "Translate technical complexity into decisions people can understand.",
                "Build practical roadmaps for product, platform, and team growth.",
            ]
            context["signature_blocks"] = [
                {
                    "title": "Product stabilization",
                    "description": (
                        "I help teams reduce operational noise and recover confidence "
                        "in day-to-day delivery."
                    ),
                },
                {
                    "title": "Backend modernization",
                    "description": (
                        "I redesign critical backend areas so products can evolve "
                        "without breaking what already works."
                    ),
                },
                {
                    "title": "Technical leadership support",
                    "description": (
                        "I align technical and non-technical stakeholders "
                        "to keep projects moving with clarity."
                    ),
                },
            ]
            context["featured_cases"] = [
                {
                    "title": "Aire de Santa Fe",
                    "context": (
                        "Media platform with high traffic and campaigns "
                        "that needed more predictable operations."
                    ),
                    "outcome": (
                        "A stronger publishing and notification flow with "
                        "clearer operational decisions."
                    ),
                    "href": "/case-studies/aire/",
                },
                {
                    "title": "Osoigo",
                    "context": (
                        "Participation platform that needed a more robust base "
                        "for product evolution."
                    ),
                    "outcome": (
                        "Lower operational risk and cleaner delivery flow "
                        "for continuous improvement."
                    ),
                    "href": "/case-studies/osoigo/",
                },
                {
                    "title": "ENACT",
                    "context": (
                        "Multi-team international initiative with complex "
                        "coordination requirements."
                    ),
                    "outcome": (
                        "Stable cross-team delivery and shared working rules "
                        "for reliable execution."
                    ),
                    "href": "/case-studies/enact/",
                },
                {
                    "title": "Atempora",
                    "context": (
                        "Product with complex scheduling and payment rules "
                        "that impacted users and operations."
                    ),
                    "outcome": (
                        "Simpler product logic, clearer operation, and a stronger "
                        "base for future growth."
                    ),
                    "href": "/case-studies/atempora/",
                },
            ]
            context["work_steps"] = [
                {
                    "step": "Step 1",
                    "title": "Understand your context",
                    "description": (
                        "We align on business goals, current bottlenecks, "
                        "and the risks that matter most."
                    ),
                },
                {
                    "step": "Step 2",
                    "title": "Prioritize for impact",
                    "description": (
                        "We define a realistic plan focused on visible gains "
                        "for product and operations."
                    ),
                },
                {
                    "step": "Step 3",
                    "title": "Execute with quality and rhythm",
                    "description": (
                        "Implementation happens with close follow-up, clear "
                        "communication, and controlled delivery."
                    ),
                },
                {
                    "step": "Step 4",
                    "title": "Transfer and continuity",
                    "description": (
                        "Your team keeps the improvements with practical "
                        "documentation and clear ownership."
                    ),
                },
            ]
            context["focus_areas"] = [
                "Media and content products",
                "Collaborative and civic platforms",
                "Complex service operations",
                "IoT and integration-heavy products",
            ]
            context["social_links"] = [
                {"label": "Case studies", "href": "/case-studies/"},
                {"label": "Email", "href": "mailto:work@leohakim.dev"},
                {"label": "Book intro call", "href": "https://cal.leohakim.dev/"},
            ]
        else:
            context["hero_highlights"] = [
                (
                    "Estabilizar productos que crecieron rapido "
                    "y se volvieron dificiles de operar."
                ),
                "Traducir complejidad tecnica en decisiones faciles de entender.",
                "Armar una hoja de ruta practica para producto, plataforma y equipo.",
            ]
            context["signature_blocks"] = [
                {
                    "title": "Estabilizacion de producto",
                    "description": (
                        "Ayudo a bajar ruido operativo y recuperar confianza "
                        "en la entrega del dia a dia."
                    ),
                },
                {
                    "title": "Modernizacion de backend",
                    "description": (
                        "Rediseno partes criticas del backend para evolucionar "
                        "producto sin romper lo que ya funciona."
                    ),
                },
                {
                    "title": "Acompanamiento de liderazgo tecnico",
                    "description": (
                        "Alineo equipos tecnicos y no tecnicos para avanzar "
                        "con claridad y foco."
                    ),
                },
            ]
            context["featured_cases"] = [
                {
                    "title": "Aire de Santa Fe",
                    "context": (
                        "Plataforma media con alto trafico y campanas "
                        "que necesitaban una operacion mas previsible."
                    ),
                    "outcome": (
                        "Se ordeno el flujo de publicacion y notificaciones "
                        "para operar con mas confianza."
                    ),
                    "href": "/case-studies/aire/",
                },
                {
                    "title": "Osoigo",
                    "context": (
                        "Plataforma participativa que necesitaba una base "
                        "mas robusta para evolucionar."
                    ),
                    "outcome": (
                        "Se redujo riesgo operativo y se logro "
                        "una entrega continua mas ordenada."
                    ),
                    "href": "/case-studies/osoigo/",
                },
                {
                    "title": "ENACT",
                    "context": (
                        "Iniciativa internacional con varios equipos y "
                        "necesidad de coordinar entregas complejas."
                    ),
                    "outcome": (
                        "Se logro una entrega estable entre equipos "
                        "con reglas comunes de trabajo."
                    ),
                    "href": "/case-studies/enact/",
                },
                {
                    "title": "Atempora",
                    "context": (
                        "Producto con reglas complejas de agenda y pagos "
                        "que afectaban operacion y experiencia."
                    ),
                    "outcome": (
                        "Se simplifico la logica de producto para operar "
                        "con mas claridad y sostener crecimiento."
                    ),
                    "href": "/case-studies/atempora/",
                },
            ]
            context["work_steps"] = [
                {
                    "step": "Paso 1",
                    "title": "Entender el contexto",
                    "description": (
                        "Alineamos objetivos de negocio, cuellos de botella "
                        "actuales y riesgos prioritarios."
                    ),
                },
                {
                    "step": "Paso 2",
                    "title": "Priorizar impacto",
                    "description": (
                        "Definimos un plan realista, con foco "
                        "en mejoras visibles para producto y operacion."
                    ),
                },
                {
                    "step": "Paso 3",
                    "title": "Ejecutar con calidad y ritmo",
                    "description": (
                        "La implementacion avanza con seguimiento cercano, "
                        "comunicacion clara y entrega controlada."
                    ),
                },
                {
                    "step": "Paso 4",
                    "title": "Transferencia y continuidad",
                    "description": (
                        "Tu equipo mantiene las mejoras con documentacion "
                        "practica y ownership claro."
                    ),
                },
            ]
            context["focus_areas"] = [
                "Productos media y contenido",
                "Plataformas colaborativas y civicas",
                "Operaciones de servicios complejos",
                "Productos IoT con multiples integraciones",
            ]
            context["social_links"] = [
                {"label": "Casos", "href": "/case-studies/"},
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
