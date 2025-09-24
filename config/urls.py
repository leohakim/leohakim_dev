from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.utils.translation import gettext_lazy as _
from django.views import defaults as default_views
from django.views.generic import TemplateView
from django.views.i18n import set_language


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
        context["trust_logos"] = ["Aire de Santa Fe", "RTVE", "ENACT"]
        context["hero_kpis"] = [
            {"value": "135+", "label": _("systems assessed")},
            {"value": "22%", "label": _("avg. cost savings")},
            {"value": "99.95%", "label": _("uptime maintained")},
        ]
        context["service_offerings"] = [
            {
                "title": _("Reliability Accelerator"),
                "items": [
                    _("SLOs & incident review"),
                    _("Runbooks ready for on-call"),
                    _("Observability deep dive"),
                ],
            },
            {
                "title": _("Cloud Architecture Sprint"),
                "items": [
                    _("Kubernetes & Terraform audits"),
                    _("CI/CD hardening"),
                    _("Security & compliance guardrails"),
                ],
            },
            {
                "title": _("FinOps Optimization"),
                "items": [
                    _("Usage profiling"),
                    _("Right-sizing & autoscaling"),
                    _("Alerts on spend anomalies"),
                ],
            },
        ]
        context["case_study_summary"] = _(
            "Migrated legacy workloads to Kubernetes with Terraform, "
            "introduced SLO-driven on-call, and removed single points of failure.",
        )
        context["case_study_metrics"] = [
            {"value": "-42%", "label": _("p95 latency")},
            {"value": "99.95%", "label": _("uptime")},
            {"value": "-28%", "label": _("cloud spend")},
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
