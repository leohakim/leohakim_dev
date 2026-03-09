from __future__ import annotations

from django.http import Http404
from django.views.generic import TemplateView

from leohakim_dev.content import get_case_study_content
from leohakim_dev.content import get_page_content


class LocalizedPageView(TemplateView):
    page_key: str | None = None

    def get_page_key(self) -> str:
        if not self.page_key:
            msg = "page_key must be defined"
            raise ValueError(msg)
        return self.page_key

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = get_page_content(
            self.get_page_key(),
            getattr(self.request, "LANGUAGE_CODE", None),
        )
        return context


class HomePageView(LocalizedPageView):
    template_name = "pages/home.html"
    page_key = "home"


class CaseStudiesIndexView(LocalizedPageView):
    template_name = "pages/case_studies.html"
    page_key = "case_studies"


class CaseStudyView(TemplateView):
    template_name = "pages/case_study.html"
    case_slug: str | None = None

    def get_case_slug(self) -> str:
        if not self.case_slug:
            msg = "case_slug must be defined"
            raise ValueError(msg)
        return self.case_slug

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["case"] = get_case_study_content(
                self.get_case_slug(),
                getattr(self.request, "LANGUAGE_CODE", None),
            )
        except KeyError as exc:
            raise Http404(str(exc)) from exc
        return context
