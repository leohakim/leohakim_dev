from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views import defaults as default_views
from django.views.i18n import set_language

from leohakim_dev.public_views import CaseStudiesIndexView
from leohakim_dev.public_views import CaseStudyView
from leohakim_dev.public_views import HomePageView
from leohakim_dev.public_views import LocalizedPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path(
        "about/",
        LocalizedPageView.as_view(
            template_name="pages/about.html",
            page_key="about",
        ),
        name="about",
    ),
    path("case-studies/", CaseStudiesIndexView.as_view(), name="case-studies"),
    path(
        "case-studies/aire/",
        CaseStudyView.as_view(case_slug="aire"),
        name="case-study-aire",
    ),
    path(
        "case-studies/osoigo/",
        CaseStudyView.as_view(case_slug="osoigo"),
        name="case-study-osoigo",
    ),
    path(
        "case-studies/enact/",
        CaseStudyView.as_view(case_slug="enact"),
        name="case-study-enact",
    ),
    path(
        "case-studies/atempora/",
        CaseStudyView.as_view(case_slug="atempora"),
        name="case-study-atempora",
    ),
    path(
        "case-studies/embever/",
        CaseStudyView.as_view(case_slug="embever"),
        name="case-study-embever",
    ),
    path(
        "services/",
        LocalizedPageView.as_view(
            template_name="pages/services.html",
            page_key="services",
        ),
        name="services",
    ),
    path(
        "writing/",
        LocalizedPageView.as_view(
            template_name="pages/writing.html",
            page_key="writing",
        ),
        name="writing",
    ),
    path(
        "contact/",
        LocalizedPageView.as_view(
            template_name="pages/contact.html",
            page_key="contact",
        ),
        name="contact",
    ),
    path(
        "cv/",
        LocalizedPageView.as_view(template_name="pages/cv.html", page_key="cv"),
        name="cv",
    ),
    path(
        "playbook/",
        LocalizedPageView.as_view(
            template_name="pages/playbook.html",
            page_key="playbook",
        ),
        name="playbook",
    ),
    path(
        "speaking/",
        LocalizedPageView.as_view(
            template_name="pages/speaking.html",
            page_key="speaking",
        ),
        name="speaking",
    ),
    path("set-language/", set_language, name="set_language"),
    path(settings.ADMIN_URL, admin.site.urls),
    path("users/", include("leohakim_dev.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]

if settings.DEBUG:
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
