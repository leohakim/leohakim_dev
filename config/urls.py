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
        context["skills"] = [
            "Django",
            "DRF",
            "K8s",
            "Terraform",
            "AWS",
            "GCP",
            "Prometheus",
            "OpenTelemetry",
        ]
        context["trust_logos"] = [
            {"name": "Aire de Santa Fe", "url": "/case-studies/aire/"},
            {"name": "Osoigo", "url": "/case-studies/osoigo/"},
            {"name": "ENACT", "url": "/case-studies/enact/"},
            {"name": "Atempora", "url": "/case-studies/atempora/"},
        ]
        if is_en:
            context["hero_kpis"] = [
                {"value": "20+", "label": "years in software engineering"},
                {"value": "5", "label": "public success stories"},
                {"value": "3", "label": "focus areas: product, platform, growth"},
            ]
            context["signature_blocks"] = [
                {
                    "title": "Technical depth",
                    "summary": (
                        "Success stories with real context, "
                        "decisions, and delivery journey."
                    ),
                    "stat": "Execution quality",
                },
                {
                    "title": "Business outcomes",
                    "summary": (
                        "Clear communication of what changed and why it mattered."
                    ),
                    "stat": "Business clarity",
                },
                {
                    "title": "Professional visibility",
                    "summary": (
                        "Assets ready for clients, recruiters, "
                        "and leadership conversations."
                    ),
                    "stat": "Trust and positioning",
                },
            ]
            context["visibility_sprint"] = [
                {
                    "step": "Week 1",
                    "title": "Clarify your message",
                    "description": (
                        "Define a positioning statement people understand in seconds."
                    ),
                },
                {
                    "step": "Week 2",
                    "title": "Publish proof of work",
                    "description": (
                        "Turn real projects into clear and credible success stories."
                    ),
                },
                {
                    "step": "Week 3",
                    "title": "Build content cadence",
                    "description": (
                        "Create a practical rhythm for LinkedIn and website updates."
                    ),
                },
                {
                    "step": "Week 4",
                    "title": "Improve conversion",
                    "description": (
                        "Guide profile visitors into conversations "
                        "and new opportunities."
                    ),
                },
            ]
            context["featured_cases"] = [
                {
                    "title": "Aire de Santa Fe",
                    "summary": (
                        "Media product with high traffic needs "
                        "and a stronger operating model."
                    ),
                    "kpi": "Stability and campaign performance improved",
                    "href": "/case-studies/aire/",
                },
                {
                    "title": "Osoigo / ENACT",
                    "summary": (
                        "Collaborative platform strengthened "
                        "for growth and operational confidence."
                    ),
                    "kpi": "More predictable delivery",
                    "href": "/case-studies/osoigo/",
                },
                {
                    "title": "Atempora",
                    "summary": (
                        "Complex product rules simplified for teams and end users."
                    ),
                    "kpi": "Clearer operations and product evolution",
                    "href": "/case-studies/atempora/",
                },
            ]
            context["collaboration_models"] = [
                {
                    "title": "Profile upgrade sprint",
                    "duration": "2-3 weeks",
                    "description": (
                        "Refine your professional message "
                        "and upgrade your web presence."
                    ),
                    "href": "/contact/",
                    "cta": "Start this sprint",
                },
                {
                    "title": "Delivery and impact package",
                    "duration": "4-8 weeks",
                    "description": (
                        "Improve product and platform execution, "
                        "then communicate outcomes."
                    ),
                    "href": "/services/",
                    "cta": "Explore this engagement",
                },
                {
                    "title": "Technical authority advisory",
                    "duration": "Monthly",
                    "description": (
                        "Ongoing support for positioning, storytelling, and growth."
                    ),
                    "href": "/speaking/",
                    "cta": "See this model",
                },
            ]
            context["channel_playbook"] = [
                {
                    "channel": "LinkedIn",
                    "format": "Lessons from real projects in plain language",
                    "frequency": "2 posts per week",
                },
                {
                    "channel": "Case studies",
                    "format": "Challenge -> approach -> outcome",
                    "frequency": "1 in-depth story per month",
                },
                {
                    "channel": "Speaking",
                    "format": "Talks about execution and product growth",
                    "frequency": "1 proposal per month",
                },
                {
                    "channel": "Direct outreach",
                    "format": "CV one-pager + selected case links",
                    "frequency": "Every strategic opportunity",
                },
            ]
            context["quick_assets"] = [
                {
                    "title": "Success stories",
                    "description": (
                        "Real projects explained in client-friendly language."
                    ),
                    "href": "/case-studies/",
                    "cta": "Open success stories",
                },
                {
                    "title": "CV one-pager",
                    "description": (
                        "Short professional profile for recruiters and clients."
                    ),
                    "href": "/cv/",
                    "cta": "Open CV",
                },
                {
                    "title": "Speaking profile",
                    "description": (
                        "Topics and sessions to build technical credibility."
                    ),
                    "href": "/speaking/",
                    "cta": "Open speaking page",
                },
            ]
            context["social_links"] = [
                {"label": "Website", "href": "/"},
                {"label": "Email", "href": "mailto:work@leohakim.dev"},
                {"label": "Book intro call", "href": "https://cal.leohakim.dev/"},
            ]
        else:
            context["hero_kpis"] = [
                {"value": "20+", "label": "anos en ingenieria de software"},
                {"value": "5", "label": "casos de exito publicados"},
                {"value": "3", "label": "focos: producto, plataforma, crecimiento"},
            ]
            context["signature_blocks"] = [
                {
                    "title": "Profundidad tecnica",
                    "summary": (
                        "Casos reales con contexto, decisiones y camino de ejecucion."
                    ),
                    "stat": "Calidad de ejecucion",
                },
                {
                    "title": "Resultado de negocio",
                    "summary": (
                        "Explicacion clara de que cambio y por que fue relevante."
                    ),
                    "stat": "Claridad para negocio",
                },
                {
                    "title": "Visibilidad profesional",
                    "summary": (
                        "Activos listos para clientes, recruiters "
                        "y conversaciones de liderazgo."
                    ),
                    "stat": "Confianza y posicionamiento",
                },
            ]
            context["visibility_sprint"] = [
                {
                    "step": "Semana 1",
                    "title": "Claridad de mensaje",
                    "description": (
                        "Definir una propuesta de valor que se entienda en segundos."
                    ),
                },
                {
                    "step": "Semana 2",
                    "title": "Publicar pruebas reales",
                    "description": (
                        "Convertir proyectos reales en casos creibles "
                        "y faciles de entender."
                    ),
                },
                {
                    "step": "Semana 3",
                    "title": "Crear cadencia de contenido",
                    "description": (
                        "Establecer una rutina practica para LinkedIn "
                        "y actualizaciones web."
                    ),
                },
                {
                    "step": "Semana 4",
                    "title": "Mejorar conversion",
                    "description": (
                        "Guiar visitantes del perfil hacia "
                        "conversaciones y oportunidades."
                    ),
                },
            ]
            context["featured_cases"] = [
                {
                    "title": "Aire de Santa Fe",
                    "summary": (
                        "Producto media con alto trafico "
                        "y necesidad de mayor estabilidad."
                    ),
                    "kpi": "Mejoro estabilidad y rendimiento de campanas",
                    "href": "/case-studies/aire/",
                },
                {
                    "title": "Osoigo / ENACT",
                    "summary": (
                        "Plataforma colaborativa fortalecida "
                        "para crecimiento y continuidad."
                    ),
                    "kpi": "Entregas mas predecibles",
                    "href": "/case-studies/osoigo/",
                },
                {
                    "title": "Atempora",
                    "summary": (
                        "Reglas complejas de producto simplificadas "
                        "para equipos y usuarios."
                    ),
                    "kpi": "Operacion mas clara y sostenible",
                    "href": "/case-studies/atempora/",
                },
            ]
            context["collaboration_models"] = [
                {
                    "title": "Sprint de posicionamiento",
                    "duration": "2-3 semanas",
                    "description": (
                        "Ajuste de mensaje profesional y mejora de presencia digital."
                    ),
                    "href": "/contact/",
                    "cta": "Empezar este sprint",
                },
                {
                    "title": "Paquete de ejecucion e impacto",
                    "duration": "4-8 semanas",
                    "description": (
                        "Mejorar producto y plataforma, "
                        "y comunicar resultados logrados."
                    ),
                    "href": "/services/",
                    "cta": "Explorar esta colaboracion",
                },
                {
                    "title": "Advisory de autoridad tecnica",
                    "duration": "Mensual",
                    "description": (
                        "Acompanamiento continuo para posicionamiento y crecimiento."
                    ),
                    "href": "/speaking/",
                    "cta": "Ver este modelo",
                },
            ]
            context["channel_playbook"] = [
                {
                    "channel": "LinkedIn",
                    "format": "Aprendizajes de proyectos reales en lenguaje claro",
                    "frequency": "2 publicaciones por semana",
                },
                {
                    "channel": "Casos de exito",
                    "format": "Desafio -> enfoque -> resultado",
                    "frequency": "1 historia en profundidad por mes",
                },
                {
                    "channel": "Speaking",
                    "format": "Charlas sobre ejecucion y crecimiento de producto",
                    "frequency": "1 propuesta por mes",
                },
                {
                    "channel": "Outreach directo",
                    "format": "CV one-pager + enlaces seleccionados",
                    "frequency": "En cada oportunidad estrategica",
                },
            ]
            context["quick_assets"] = [
                {
                    "title": "Casos de exito",
                    "description": "Proyectos reales explicados para clientes.",
                    "href": "/case-studies/",
                    "cta": "Abrir casos de exito",
                },
                {
                    "title": "CV one-pager",
                    "description": "Perfil corto para recruiters y clientes.",
                    "href": "/cv/",
                    "cta": "Abrir CV",
                },
                {
                    "title": "Perfil de speaking",
                    "description": "Temas y sesiones para reforzar autoridad tecnica.",
                    "href": "/speaking/",
                    "cta": "Abrir speaking",
                },
            ]
            context["social_links"] = [
                {"label": "Web", "href": "/"},
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
