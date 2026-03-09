# ruff: noqa: E501, TRY003, EM102

from __future__ import annotations

from collections.abc import Mapping
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any

from django.urls import reverse

SUPPORTED_PUBLIC_LANGUAGES = ("en", "es")
DEFAULT_PUBLIC_LANGUAGE = "en"
VISIBLE_CASE_STUDY_SLUGS = ("aire", "osoigo", "atempora", "enact")
CASE_STUDY_ROUTE_NAMES = {
    "aire": "case-study-aire",
    "osoigo": "case-study-osoigo",
    "enact": "case-study-enact",
    "atempora": "case-study-atempora",
    "embever": "case-study-embever",
}


@dataclass(frozen=True)
class LocalizedText:
    translations: Mapping[str, str]

    def resolve(self, language_code: str) -> str:
        return self.translations[normalize_public_language(language_code)]


class ContentError(ValueError):
    """Raised when the structured content is inconsistent."""


def text(**translations: str) -> LocalizedText:
    translation_keys = set(translations)
    expected_keys = set(SUPPORTED_PUBLIC_LANGUAGES)
    if translation_keys != expected_keys:
        missing = sorted(expected_keys - translation_keys)
        extra = sorted(translation_keys - expected_keys)
        details = []
        if missing:
            details.append(f"missing={','.join(missing)}")
        if extra:
            details.append(f"extra={','.join(extra)}")
        raise ContentError(
            f"Invalid translation keys for content entry ({'; '.join(details)})",
        )
    return LocalizedText(translations)


SITE_UI = {
    "meta": {
        "title": text(
            en="Leo Hakim | Backend & Cloud Engineer",
            es="Leo Hakim | Ingeniería Backend y Cloud",
        ),
        "description": text(
            en=(
                "Personal website of Leonardo Hakim: backend engineering, cloud "
                "architecture, and client-ready success stories."
            ),
            es=(
                "Sitio profesional de Leonardo Hakim: ingeniería backend, "
                "arquitectura cloud y casos de éxito para clientes."
            ),
        ),
        "og_title": text(
            en="Leo Hakim | Backend & Cloud Engineer",
            es="Leo Hakim | Ingeniería Backend y Cloud",
        ),
        "og_description": text(
            en=(
                "Success stories and services focused on reliable product delivery "
                "and business outcomes."
            ),
            es=(
                "Casos de éxito y servicios enfocados en entrega confiable e "
                "impacto de negocio."
            ),
        ),
        "twitter_title": text(
            en="Leo Hakim | Backend & Cloud Engineer",
            es="Leo Hakim | Ingeniería Backend y Cloud",
        ),
        "twitter_description": text(
            en=(
                "Backend and cloud engineering profile with clear success stories "
                "and delivery experience."
            ),
            es=(
                "Perfil de ingeniería backend y cloud con casos de éxito claros y "
                "experiencia real de entrega."
            ),
        ),
    },
    "brand": {
        "name": "LEONARDO HAKIM",
        "subtitle": text(
            en="Backend . Cloud . Reliability",
            es="Backend . Cloud . Confianza",
        ),
    },
    "navigation": {
        "aria_label": text(en="Primary", es="Principal"),
        "toggle_label": text(en="Toggle navigation", es="Abrir menú"),
        "links": [
            {"label": text(en="Home", es="Inicio"), "route_name": "home"},
            {
                "label": text(en="Case Studies", es="Casos de éxito"),
                "route_name": "case-studies",
            },
            {"label": text(en="Services", es="Servicios"), "route_name": "services"},
            {"label": text(en="Writing", es="Contenido"), "route_name": "writing"},
            {"label": text(en="About", es="Sobre mí"), "route_name": "about"},
        ],
        "primary_cta": {
            "label": text(en="Contact", es="Contacto"),
            "route_name": "contact",
        },
    },
    "language_switcher": {
        "form_label": text(en="Change language", es="Cambiar idioma"),
        "select_label": text(en="Language", es="Idioma"),
    },
    "common": {
        "read_more": text(en="Read more", es="Ver más"),
    },
    "footer": {
        "navigation_title": text(en="Navigation", es="Navegación"),
        "contact_title": text(en="Contact", es="Contacto"),
        "summary": text(
            en=(
                "Backend, platform, and cloud consultant working where product, "
                "operations, and infrastructure need clearer technical decisions."
            ),
            es=(
                "Consultor de backend, plataformas y cloud. Trabajo donde producto, "
                "operación e infraestructura necesitan decisiones técnicas más claras."
            ),
        ),
        "links": [
            {
                "label": text(en="Case studies", es="Casos"),
                "route_name": "case-studies",
            },
            {"label": text(en="Email", es="Email"), "url": "mailto:work@leohakim.dev"},
            {"label": text(en="Contact", es="Contacto"), "route_name": "contact"},
        ],
        "copyright": text(
            en="Copyright {year} Leonardo Hakim. All rights reserved.",
            es="Copyright {year} Leonardo Hakim. Todos los derechos reservados.",
        ),
    },
    "case_study": {
        "back_link": text(
            en="Back to case studies ->",
            es="Volver a casos de éxito ->",
        ),
        "context_label": text(en="Context", es="Contexto"),
        "role_label": text(en="My role", es="Mi rol"),
        "approach_label": text(en="Approach", es="Enfoque"),
        "result_label": text(en="Result", es="Resultado"),
        "business_value_label": text(en="Business value", es="Valor de negocio"),
        "simple_stack_label": text(en="Simple stack", es="Stack simple"),
        "card_cta": text(en="View full story ->", es="Ver historia completa ->"),
    },
    "default_content_message": text(
        en="Use this document as a way to quick start any new project.",
        es="Usa este documento como punto de partida para tu proyecto.",
    ),
}


PAGES = {
    "home": {
        "meta": {
            "title": text(
                en="Leonardo Hakim | Clear engineering for digital products",
                es="Leonardo Hakim | Ingeniería clara para productos digitales",
            ),
            "description": text(
                en=(
                    "Backend, platform, and cloud consulting for products that need "
                    "more reliability, safer delivery, and clearer technical decisions as they grow."
                ),
                es=(
                    "Consultoría en backend, plataformas y cloud para productos que "
                    "necesitan más confiabilidad, entregas más seguras y decisiones técnicas más claras al crecer."
                ),
            ),
            "og_title": text(
                en="Leonardo Hakim | Clear engineering for products under real pressure",
                es="Leonardo Hakim | Ingeniería clara para productos con presión real",
            ),
            "og_description": text(
                en=(
                    "Backend, platform, and cloud work for teams that need safer "
                    "systems, clearer decisions, and less fragile delivery."
                ),
                es=(
                    "Backend, plataformas y cloud para equipos que necesitan sistemas "
                    "más seguros, decisiones más claras y delivery menos frágil."
                ),
            ),
        },
        "badge": text(
            en="Clear engineering for products that need to scale",
            es="Ingeniería clara para productos que necesitan escalar",
        ),
        "title": text(
            en="Clear engineering for products that need to scale without becoming fragile.",
            es="Ingeniería clara para productos que necesitan escalar sin volverse frágiles.",
        ),
        "lead": text(
            en=(
                "Backend, platform, and cloud work for teams that need more reliability, "
                "safer delivery, and clearer technical decisions."
            ),
            es=(
                "Backend, plataformas y cloud para equipos que necesitan más "
                "confiabilidad, entregas más seguras y decisiones técnicas más claras."
            ),
        ),
        "supporting": text(
            en=(
                "I work where backend, product, operations, and infrastructure start "
                "colliding: high-traffic media, live platforms, complex SaaS, and systems "
                "that can no longer depend on improvisation."
            ),
            es=(
                "Trabajo donde backend, producto, operación e infraestructura empiezan "
                "a chocar: medios de alto tráfico, plataformas en producción, SaaS "
                "complejos y sistemas que ya no pueden depender de la improvisación."
            ),
        ),
        "primary_cta": {
            "label": text(en="Start by email", es="Escribir por email"),
            "route_name": "contact",
        },
        "secondary_cta": {
            "label": text(en="See real case studies", es="Ver casos reales"),
            "route_name": "case-studies",
        },
        "portrait_alt": text(
            en="Portrait of Leonardo Hakim",
            es="Retrato de Leonardo Hakim",
        ),
        "hero_list_title": text(en="Why teams bring me in", es="Por qué me buscan"),
        "hero_highlights": [
            text(
                en="Reliable systems for products already under real demand.",
                es="Sistemas confiables para productos que ya están bajo demanda real.",
            ),
            text(
                en="Clearer technical decisions across backend, product, and operations.",
                es="Decisiones más claras entre backend, producto y operación.",
            ),
            text(
                en="Engineering that helps teams grow without making the platform fragile.",
                es="Ingeniería que permite crecer sin volver frágil la plataforma.",
            ),
        ],
        "selected_work_label": text(en="Selected work", es="Experiencia seleccionada"),
        "help_label": text(en="How I can help", es="Cómo puedo ayudarte"),
        "help_title": text(
            en="Senior technical support for products that already have real pressure",
            es="Soporte técnico senior para productos que ya tienen presión real",
        ),
        "help_intro": text(
            en=(
                "I am most useful when the challenge is not just building features, "
                "but making the system safer to operate and easier to evolve."
            ),
            es=(
                "Aporto más cuando el problema no es solo construir features, sino "
                "volver el sistema más seguro de operar y más claro de evolucionar."
            ),
        ),
        "help_areas": [
            {
                "title": text(
                    en="Stabilize products that are already feeling pressure",
                    es="Estabilizar productos que ya sienten la presión",
                ),
                "description": text(
                    en=(
                        "When the backend starts slowing product and operations down, "
                        "I help restore predictability and reduce risk."
                    ),
                    es=(
                        "Cuando el backend empieza a frenar producto y operación, ayudo "
                        "a recuperar previsibilidad y bajar riesgo."
                    ),
                ),
            },
            {
                "title": text(
                    en="Modernize critical backend without blocking delivery",
                    es="Modernizar backend crítico sin frenar la entrega",
                ),
                "description": text(
                    en=(
                        "I improve fragile areas of the system while keeping service "
                        "continuity and the team moving."
                    ),
                    es=(
                        "Mejora de áreas frágiles del sistema manteniendo continuidad "
                        "de servicio y avance del equipo."
                    ),
                ),
            },
            {
                "title": text(
                    en="Turn complex product rules into workable systems",
                    es="Convertir reglas complejas en sistemas que se pueden operar",
                ),
                "description": text(
                    en=(
                        "I design clearer domain and platform decisions so growth does "
                        "not create chaos later."
                    ),
                    es=(
                        "Diseño decisiones de dominio y plataforma más claras para "
                        "crecer sin volver al caos."
                    ),
                ),
            },
        ],
        "featured_label": text(en="Featured cases", es="Casos destacados"),
        "featured_title": text(
            en="Selected work across production reliability, product architecture, and delivery",
            es="Trabajo seleccionado en confiabilidad en producción, arquitectura de producto y delivery",
        ),
        "featured_intro": text(
            en=(
                "Four cases that show how I work when backend, operations, and product "
                "complexity need to be aligned instead of improvised."
            ),
            es=(
                "Cuatro casos que muestran cómo trabajo cuando backend, operación y "
                "complejidad de producto necesitan alinearse en lugar de improvisarse."
            ),
        ),
        "featured_cta": {
            "label": text(en="View case studies", es="Ver casos de estudio"),
            "route_name": "case-studies",
        },
        "closing_label": text(
            en="Selected engagements",
            es="Colaboraciones seleccionadas",
        ),
        "closing_title": text(
            en=(
                "If your product is working but the technical base is getting harder "
                "to trust, let's talk."
            ),
            es=(
                "Si tu producto ya funciona pero la base técnica empieza a ser difícil "
                "de confiar, conversemos."
            ),
        ),
        "closing_body": text(
            en=(
                "Available for selected consulting, implementation, and fractional senior "
                "engagements in Spanish and English."
            ),
            es=(
                "Disponible para colaboraciones seleccionadas de consultoría, "
                "implementación y acompañamiento senior en español e inglés."
            ),
        ),
        "closing_primary_cta": {
            "label": text(en="Write by email", es="Escribir por email"),
            "route_name": "contact",
        },
        "closing_secondary_cta": {
            "label": text(en="View case studies", es="Ver casos de estudio"),
            "route_name": "case-studies",
        },
    },
    "about": {
        "meta": {
            "title": text(
                en="About Leonardo Hakim | leohakim.dev",
                es="Sobre Leonardo Hakim | leohakim.dev",
            ),
            "description": text(
                en=(
                    "Backend, platform, and cloud consultant working at the intersection "
                    "of product, operations, and infrastructure."
                ),
                es=(
                    "Consultor de backend, plataformas y cloud trabajando en la "
                    "intersección entre producto, operación e infraestructura."
                ),
            ),
        },
        "eyebrow": text(en="About", es="Sobre mí"),
        "title": text(
            en="I work where backend, product, operations, and infrastructure need to stop pulling in different directions.",
            es="Trabajo donde backend, producto, operación e infraestructura necesitan dejar de tirar para lados distintos.",
        ),
        "lead": text(
            en=(
                "I have over 10 years of software engineering experience, with a strong "
                "focus on backend, platforms, infrastructure, and the operational side of real products."
            ),
            es=(
                "Tengo más de 10 años de experiencia en ingeniería de software, con foco "
                "fuerte en backend, plataformas, infraestructura y la operación real de productos digitales."
            ),
        ),
        "supporting": text(
            en=(
                "My value is not only in building backend code. It is in helping teams make "
                "clearer decisions when technical debt, fragile systems, complex product rules, "
                "or delivery pressure start slowing everything down."
            ),
            es=(
                "Mi valor no está solo en escribir backend. Está en ayudar a equipos a tomar "
                "mejores decisiones cuando la deuda técnica, la fragilidad operativa, la complejidad "
                "de producto o la presión de entrega empiezan a frenar todo."
            ),
        ),
        "focus_cards": [
            {
                "title": text(en="Reliable systems", es="Sistemas confiables"),
                "body": text(
                    en=(
                        "I work best when a product can no longer depend on improvisation "
                        "and needs a safer technical base."
                    ),
                    es=(
                        "Trabajo mejor cuando un producto ya no puede depender de la "
                        "improvisación y necesita una base técnica más segura."
                    ),
                ),
            },
            {
                "title": text(
                    en="Complex product logic",
                    es="Lógica de producto compleja",
                ),
                "body": text(
                    en="I help turn messy business rules into backend structures teams can actually build and operate.",
                    es="Ayudo a convertir reglas de negocio desordenadas en estructuras backend que el equipo realmente pueda construir y operar.",
                ),
            },
            {
                "title": text(
                    en="Delivery and infrastructure",
                    es="Delivery e infraestructura",
                ),
                "body": text(
                    en=(
                        "I also work on the operational layer: deployment, runtime decisions, "
                        "and the systems teams rely on to move with confidence."
                    ),
                    es=(
                        "También trabajo sobre la capa operativa: despliegue, decisiones de runtime "
                        "y sistemas de apoyo para que el equipo avance con más confianza."
                    ),
                ),
            },
        ],
        "collaboration_title": text(en="How I collaborate", es="Cómo colaboro"),
        "collaboration_points": [
            text(
                en="Direct communication with both technical and non-technical stakeholders.",
                es="Comunicación directa con perfiles técnicos y no técnicos.",
            ),
            text(
                en="Priority on reducing risk before chasing optimization for its own sake.",
                es="Prioridad en bajar riesgo antes de perseguir optimización por sí sola.",
            ),
            text(
                en="Clear tradeoffs, realistic execution, and strong ownership.",
                es="Tradeoffs claros, ejecución realista y ownership fuerte.",
            ),
            text(
                en="Available for selected consulting, implementation, and fractional senior engagements.",
                es="Disponible para colaboraciones seleccionadas de consultoría, implementación y acompañamiento senior.",
            ),
            text(
                en="Working languages: native Spanish and professional English.",
                es="Idiomas de trabajo: español nativo e inglés profesional.",
            ),
        ],
        "primary_cta": {
            "label": text(en="View real case studies", es="Ver casos reales"),
            "route_name": "case-studies",
        },
        "secondary_cta": {
            "label": text(
                en="Let's talk about your project",
                es="Hablemos de tu proyecto",
            ),
            "route_name": "contact",
        },
    },
    "services": {
        "meta": {
            "title": text(en="Services | leohakim.dev", es="Servicios | leohakim.dev"),
            "description": text(
                en="Technical consulting, stabilization, architecture work, and fractional senior support.",
                es="Consultoría técnica, estabilización, arquitectura y acompañamiento senior fractional.",
            ),
        },
        "eyebrow": text(en="Services", es="Servicios"),
        "title": text(
            en="Senior technical support for teams that need clearer decisions, safer systems, and less fragile delivery.",
            es="Soporte técnico senior para equipos que necesitan decisiones más claras, sistemas más seguros y delivery menos frágil.",
        ),
        "lead": text(
            en=(
                "Best fit for products already in motion: SaaS, media, platforms with live traffic, "
                "or systems where backend and operations are starting to hurt product delivery."
            ),
            es=(
                "Especialmente útil en productos que ya están en marcha: SaaS, media, plataformas "
                "con tráfico real o sistemas donde backend y operación empiezan a frenar al producto."
            ),
        ),
        "service_cards": [
            {
                "title": text(
                    en="Technical assessment and prioritization",
                    es="Diagnóstico y priorización técnica",
                ),
                "body": text(
                    en="A clear view of what is fragile, what is slowing the team down, and what should be addressed first.",
                    es="Una lectura clara de qué está frágil, qué está frenando al equipo y qué conviene resolver primero.",
                ),
                "bullets": [
                    text(
                        en="Architecture and system health review.",
                        es="Estado real del sistema y de la arquitectura.",
                    ),
                    text(
                        en="Technical debt and operational risk map.",
                        es="Mapa de deuda técnica y riesgo operativo.",
                    ),
                    text(
                        en="Practical next steps tied to business impact.",
                        es="Siguientes pasos concretos conectados al impacto de negocio.",
                    ),
                ],
            },
            {
                "title": text(
                    en="Stabilization and implementation",
                    es="Estabilización e implementación",
                ),
                "body": text(
                    en="Backend, infrastructure, and delivery work focused on making the platform safer to run and easier to evolve.",
                    es="Trabajo sobre backend, infraestructura y entrega para que la plataforma sea más segura de operar y más clara de evolucionar.",
                ),
                "bullets": [
                    text(
                        en="Critical backend refactoring and architecture hardening.",
                        es="Refactorización crítica de backend y hardening de arquitectura.",
                    ),
                    text(
                        en="Reliability, performance, and operational improvements.",
                        es="Mejoras de confiabilidad, performance y operación.",
                    ),
                    text(
                        en="Safer rollout and better delivery practices.",
                        es="Entrega más controlada para reducir riesgo técnico.",
                    ),
                ],
            },
            {
                "title": text(
                    en="Senior fractional support",
                    es="Acompañamiento senior fractional",
                ),
                "body": text(
                    en="A strong external senior profile for teams that need help deciding, aligning, and executing without adding unnecessary management layers.",
                    es="Un perfil senior externo para equipos que necesitan ayuda para decidir, alinear y ejecutar sin sumar capas innecesarias de gestión.",
                ),
                "bullets": [
                    text(
                        en="Technical leadership support and decision follow-through.",
                        es="Soporte de liderazgo técnico y seguimiento de decisiones.",
                    ),
                    text(
                        en="Architecture, delivery, and operational guidance.",
                        es="Guía sobre arquitectura, delivery y operación.",
                    ),
                    text(
                        en="Team enablement so improvements last beyond the engagement.",
                        es="Enablement del equipo para que las mejoras se sostengan en el tiempo.",
                    ),
                ],
            },
        ],
        "engagement_title": text(en="Engagement models", es="Modalidades"),
        "engagement_body": text(
            en="Consulting, high-value implementation, temporary technical leadership, or fractional senior support depending on the problem and the stage of the product.",
            es="Consultoría, implementación de alto valor, liderazgo técnico temporal o acompañamiento senior fractional según el problema y la etapa del producto.",
        ),
        "primary_cta": {
            "label": text(en="Start by email", es="Escribir por email"),
            "route_name": "contact",
        },
        "secondary_cta": {
            "label": text(en="View success stories", es="Ver casos de éxito"),
            "route_name": "case-studies",
        },
    },
    "writing": {
        "meta": {
            "title": text(en="Writing | leohakim.dev", es="Contenido | leohakim.dev"),
            "description": text(
                en="Practical writing about backend, product architecture, and operating real systems.",
                es="Contenido práctico sobre backend, arquitectura de producto y operación de sistemas reales.",
            ),
        },
        "eyebrow": text(en="Writing", es="Contenido"),
        "title": text(
            en="Practical writing about backend, delivery, product architecture, and operating real systems.",
            es="Contenido práctico sobre backend, delivery, arquitectura de producto y operación de sistemas reales.",
        ),
        "lead": text(
            en="No hype. Just concrete tradeoffs, lessons from production, and decisions that teams can actually use.",
            es="Sin hype. Solo tradeoffs concretos, aprendizajes de producción y decisiones que un equipo realmente puede usar.",
        ),
        "topics_title": text(en="Main topics", es="Temas principales"),
        "topics": [
            text(
                en="Making backend systems easier to trust under real operational pressure.",
                es="Volver más confiables sistemas backend bajo presión operativa real.",
            ),
            text(
                en="Turning technical debt into clearer priorities and tradeoffs.",
                es="Convertir deuda técnica en prioridades y tradeoffs más claros.",
            ),
            text(
                en="Designing architecture that helps product, operations, and teams grow together.",
                es="Diseñar arquitectura que ayude a crecer a producto, operación y equipo a la vez.",
            ),
        ],
    },
    "contact": {
        "meta": {
            "title": text(en="Contact | leohakim.dev", es="Contacto | leohakim.dev"),
            "description": text(
                en="Send a short brief about your product, backend, or infrastructure challenge.",
                es="Envíame un resumen breve de tu desafío de producto, backend o infraestructura.",
            ),
        },
        "eyebrow": text(en="Contact", es="Contacto"),
        "title": text(
            en="Send a short project brief and I will tell you if I can help.",
            es="Envíame un resumen corto de tu proyecto y te diré si puedo ayudarte.",
        ),
        "lead": text(
            en="Email is the best first step. If it makes sense, we can move to a call afterwards.",
            es="El email es el mejor primer paso. Si tiene sentido, después pasamos a una llamada.",
        ),
        "primary_panel": {
            "title": text(en="Preferred contact options", es="Canales de contacto"),
            "body": text(
                en="The more useful first message usually includes product stage, current technical pain, and what outcome would make the engagement worthwhile.",
                es="El mejor primer mensaje suele incluir etapa del producto, dolor técnico actual y qué resultado haría valiosa la colaboración.",
            ),
            "primary_cta": {
                "label": text(en="Write by email", es="Escribir por email"),
                "url": "mailto:work@leohakim.dev?subject=Project%20Inquiry",
            },
            "secondary_cta": {
                "label": text(en="Optional intro call", es="Llamada inicial opcional"),
                "url": "https://cal.leohakim.dev/",
            },
        },
        "secondary_panel": {
            "title": text(en="What we can cover first", es="Qué podemos ver primero"),
            "items": [
                text(
                    en="What is fragile today in backend, infrastructure, or delivery.",
                    es="Qué está frágil hoy en backend, infraestructura o delivery.",
                ),
                text(
                    en="What has become harder to trust as the product grows.",
                    es="Qué se volvió más difícil de confiar a medida que el producto creció.",
                ),
                text(
                    en="What kind of support you need: audit, implementation, or ongoing senior help.",
                    es="Qué tipo de ayuda necesitas: auditoría, implementación o acompañamiento senior.",
                ),
            ],
            "email": "work@leohakim.dev",
        },
    },
    "cv": {
        "meta": {
            "title": text(en="CV | leohakim.dev", es="CV | leohakim.dev"),
            "description": text(
                en="Executive summary of backend, platform, and infrastructure work under real operational pressure.",
                es="Resumen ejecutivo de trabajo en backend, plataformas e infraestructura bajo presión operativa real.",
            ),
        },
        "eyebrow": "CV",
        "title": text(
            en="Executive summary of backend, platform, and infrastructure work in products that need reliability under real pressure.",
            es="Resumen ejecutivo de trabajo en backend, plataformas e infraestructura para productos que necesitan confiabilidad bajo presión real.",
        ),
        "lead": text(
            en="Over 10 years of software engineering experience, with work across high-traffic media, live platforms, complex SaaS, and multi-team technical environments.",
            es="Más de 10 años de experiencia en ingeniería de software, con trabajo en media de alto tráfico, plataformas en producción, SaaS complejos y entornos técnicos multi-equipo.",
        ),
        "focus_cards": [
            {
                "title": text(
                    en="Reliability and stabilization",
                    es="Confiabilidad y estabilización",
                ),
                "body": text(
                    en="I work on systems that already have real load, operational pressure, or technical fragility.",
                    es="Trabajo sobre sistemas que ya tienen carga real, presión operativa o fragilidad técnica.",
                ),
            },
            {
                "title": text(en="Product architecture", es="Arquitectura de producto"),
                "body": text(
                    en="I help turn complex rules and messy flows into backend structures teams can build without chaos.",
                    es="Ayudo a convertir reglas complejas y flujos desordenados en estructuras backend que el equipo pueda construir sin caos.",
                ),
            },
            {
                "title": text(
                    en="Delivery and infrastructure",
                    es="Delivery e infraestructura",
                ),
                "body": text(
                    en="Backend work connected to deployment, runtime, and operational decisions, not isolated from them.",
                    es="Trabajo de backend conectado con despliegue, runtime y operación, no aislado de esas capas.",
                ),
            },
        ],
        "availability_title": text(en="Available for", es="Disponible para"),
        "availability_items": [
            text(
                en="Technical consulting for fragile or hard-to-scale products.",
                es="Consultoría técnica para productos frágiles o difíciles de escalar.",
            ),
            text(
                en="High-value implementation in backend, platform, and delivery work.",
                es="Implementación de alto valor en backend, plataforma y delivery.",
            ),
            text(
                en="Temporary technical leadership or fractional senior support.",
                es="Liderazgo técnico temporal o acompañamiento senior fractional.",
            ),
        ],
        "primary_cta": {
            "label": text(en="Contact", es="Contactar"),
            "route_name": "contact",
        },
        "secondary_cta": {
            "label": text(en="View case studies", es="Ver casos"),
            "route_name": "case-studies",
        },
    },
    "playbook": {
        "meta": {
            "title": text(en="Playbook | leohakim.dev", es="Playbook | leohakim.dev"),
            "description": text(
                en="A practical process for reducing technical risk and improving reliability over time.",
                es="Un proceso práctico para reducir riesgo técnico y mejorar la confiabilidad de forma continua.",
            ),
        },
        "eyebrow": "Playbook",
        "title": text(
            en="How I work when a product cannot keep depending on improvisation.",
            es="Cómo trabajo cuando un producto ya no puede seguir dependiendo de la improvisación.",
        ),
        "lead": text(
            en="A practical process focused on business risk, technical stability, and continuous improvement.",
            es="Un proceso práctico con foco en riesgo de negocio, estabilidad técnica y mejora continua.",
        ),
        "steps": [
            {
                "title": text(
                    en="1. Understand business and real risks",
                    es="1. Entender el negocio y riesgos reales",
                ),
                "body": text(
                    en="I start by identifying what can hurt operations, customer trust, or delivery first, not by making a generic technical wishlist.",
                    es="Empiezo por identificar qué puede afectar primero la operación, la confianza del cliente o la capacidad de entrega, no por armar una wishlist técnica genérica.",
                ),
            },
            {
                "title": text(
                    en="2. Prioritize what impacts first",
                    es="2. Priorizar lo que impacta primero",
                ),
                "body": text(
                    en="The goal is to avoid scattered effort and focus on the smallest set of changes with the highest practical value.",
                    es="La idea es evitar esfuerzos dispersos y enfocar el trabajo en el conjunto mínimo de cambios con mayor valor real.",
                ),
            },
            {
                "title": text(
                    en="3. Implement with stability in mind",
                    es="3. Implementar con foco en estabilidad",
                ),
                "body": text(
                    en="Implementation happens in controlled stages so the team can keep moving while risk is reduced.",
                    es="La implementación se hace por etapas controladas para que el equipo pueda seguir avanzando mientras baja el riesgo.",
                ),
            },
            {
                "title": text(
                    en="4. Measure and improve continuously",
                    es="4. Medir y mejorar continuamente",
                ),
                "body": text(
                    en="I prefer evidence over slogans: what changed, what still hurts, and what should be adjusted next.",
                    es="Prefiero evidencia antes que slogans: qué cambió, qué sigue doliendo y qué conviene ajustar después.",
                ),
            },
        ],
        "primary_cta": {
            "label": text(en="Start a conversation", es="Iniciar conversación"),
            "route_name": "contact",
        },
    },
    "speaking": {
        "meta": {
            "title": text(en="Speaking | leohakim.dev", es="Charlas | leohakim.dev"),
            "description": text(
                en="Talks about real-world backend, delivery pressure, and architecture decisions that have to survive production.",
                es="Charlas sobre backend real, presión de delivery y decisiones de arquitectura que tienen que sobrevivir en producción.",
            ),
        },
        "eyebrow": text(en="Speaking", es="Charlas"),
        "title": text(
            en="Talks about real-world backend, delivery pressure, and architecture decisions that have to survive production.",
            es="Charlas sobre backend real, presión de delivery y decisiones de arquitectura que tienen que sobrevivir en producción.",
        ),
        "lead": text(
            en="Available in Spanish and English for conferences, communities, and in-company sessions.",
            es="Disponible en español e inglés para conferencias, comunidades y espacios internos.",
        ),
        "topic_cards": [
            {
                "title": text(
                    en="Real scalability in production",
                    es="Escalabilidad real en producción",
                ),
                "body": text(
                    en="Lessons from systems where reliability, delivery speed, and operational pressure have to coexist.",
                    es="Aprendizajes de sistemas donde confiabilidad, velocidad de entrega y presión operativa tienen que convivir.",
                ),
            },
            {
                "title": text(
                    en="Technical debt without smoke",
                    es="Deuda técnica sin humo",
                ),
                "body": text(
                    en="Practical ways to reduce fragility and make technical debt manageable without empty narratives.",
                    es="Formas prácticas de bajar fragilidad y volver manejable la deuda técnica sin relatos vacíos.",
                ),
            },
            {
                "title": text(
                    en="Architecture that supports business",
                    es="Arquitectura que acompaña al negocio",
                ),
                "body": text(
                    en="How to connect engineering decisions with product constraints, operations, and business priorities.",
                    es="Cómo conectar decisiones de ingeniería con restricciones de producto, operación y prioridades del negocio.",
                ),
            },
        ],
        "primary_cta": {
            "label": text(en="Invite me to speak", es="Invitar a charla"),
            "route_name": "contact",
        },
        "secondary_cta": {
            "label": text(en="View case studies", es="Ver casos"),
            "route_name": "case-studies",
        },
    },
    "case_studies": {
        "meta": {
            "title": text(
                en="Success stories | leohakim.dev",
                es="Casos de éxito | leohakim.dev",
            ),
            "description": text(
                en="Selected case studies across production reliability, product architecture, and technical delivery.",
                es="Casos seleccionados sobre confiabilidad en producción, arquitectura de producto y delivery técnico.",
            ),
        },
        "eyebrow": text(en="Case studies", es="Casos de éxito"),
        "title": text(
            en="Real systems. Real constraints. Clear outcomes.",
            es="Sistemas reales. Restricciones reales. Resultados claros.",
        ),
        "lead": text(
            en="Four selected cases that show how I work when backend, operations, and product complexity need to be aligned instead of improvised.",
            es="Cuatro casos seleccionados que muestran cómo trabajo cuando backend, operación y complejidad de producto necesitan alinearse en lugar de improvisarse.",
        ),
        "additional_experience_title": text(
            en="Additional experience",
            es="Experiencia adicional",
        ),
        "additional_experience_body": text(
            en="I also have selected backend and cloud experience in IoT-related contexts, but I keep that work more generic publicly when the available detail is limited or sensitive.",
            es="También tengo experiencia adicional en backend y cloud en contextos ligados a IoT, pero prefiero contarla de forma más genérica cuando el detalle disponible es limitado o sensible.",
        ),
    },
}


CASE_STUDIES = {
    "aire": {
        "name": "Aire de Santa Fe",
        "route_name": "case-study-aire",
        "kind": text(en="Case study", es="Caso de estudio"),
        "meta": {
            "title": text(
                en="Case study: Aire de Santa Fe | leohakim.dev",
                es="Caso de estudio: Aire de Santa Fe | leohakim.dev",
            ),
            "description": text(
                en="Backend, push notifications, and operating foundations for a high-traffic news app.",
                es="Backend, notificaciones push y base operativa para una app de noticias de alto tráfico.",
            ),
        },
        "hero_summary": text(
            en="Backend, push notifications, and operating foundations for a high-traffic news app that needed more reliability before it could grow with confidence.",
            es="Backend, notificaciones push y base operativa para una app de noticias de alto tráfico que necesitaba más confiabilidad antes de crecer con seguridad.",
        ),
        "home_summary": text(
            en="Backend, push, and operating foundations for a high-traffic media app that needed more predictable delivery.",
            es="Backend, push y base operativa para una app de medios de alto tráfico que necesitaba más previsibilidad.",
        ),
        "index_summary": text(
            en="Backend, push, and operating foundations for a high-traffic news app that needed more predictable delivery.",
            es="Backend, push y base operativa para una app de noticias de alto tráfico que necesitaba más previsibilidad.",
        ),
        "context": text(
            en="A news product with millions of visits, editorial peaks, and push distribution needs. The challenge was not just serving endpoints, but creating a backend that could support real traffic, real operations, and future product evolution without too much fragility.",
            es="Un producto de noticias con millones de visitas, picos editoriales y necesidades reales de distribución por push. El desafío no era solo servir endpoints, sino construir un backend capaz de sostener tráfico real, operación editorial y evolución de producto sin demasiada fragilidad.",
        ),
        "role": text(
            en="I was directly responsible for backend, API, push flows, the internal panel, part of the deployment setup, and the operational decisions needed to make the system more workable day to day.",
            es="Tuve responsabilidad directa sobre backend, API, flujos de push, panel interno, parte del despliegue y las decisiones operativas necesarias para volver el sistema más trabajable en el día a día.",
        ),
        "approach": [
            {
                "title": text(
                    en="1. Decouple sensitive flows:",
                    es="1. Desacoplar flujos sensibles:",
                ),
                "body": text(
                    en="I designed backend operations around asynchronous tasks so push and operational work would not overload user-facing flows.",
                    es="Diseñé la operación del backend alrededor de tareas asíncronas para que el push y otros procesos sensibles no cargaran de más los flujos de cara al usuario.",
                ),
            },
            {
                "title": text(
                    en="2. Reduce pressure on the origin:",
                    es="2. Reducir presión sobre el origen:",
                ),
                "body": text(
                    en="I defined a hybrid caching approach with Firestore for high-demand content and clearer expiration rules for news delivery.",
                    es="Definí una estrategia híbrida de caché con Firestore para contenido de alta consulta y reglas más claras de expiración para la entrega de noticias.",
                ),
            },
            {
                "title": text(
                    en="3. Make operations easier to run:",
                    es="3. Hacer la operación más gobernable:",
                ),
                "body": text(
                    en="I kept the internal tooling simple and treated push as an operable system, with room for tracing and future metrics instead of one-off sending.",
                    es="Mantuve las herramientas internas simples y traté el push como un sistema operable, con espacio para trazabilidad y métricas futuras en lugar de simples envíos aislados.",
                ),
            },
        ],
        "result": text(
            en="The platform gained a more predictable base for editorial and product operations. Content delivery, internal workflows, and backend evolution started from a much more controlled place.",
            es="La plataforma ganó una base más predecible para la operación editorial y de producto. La entrega de contenido, los flujos internos y la evolución del backend empezaron a partir de un lugar mucho más controlado.",
        ),
        "business_value": text(
            en="In a media product under real traffic, better backend predictability means less operational friction and a stronger base for engagement, editorial continuity, and future monetization work.",
            es="En un producto media con tráfico real, una mayor previsibilidad del backend significa menos fricción operativa y una base más fuerte para engagement, continuidad editorial y trabajo futuro de monetización.",
        ),
        "simple_stack": text(
            en="Django and DRF for the API and internal tools, Celery and Redis for background work, PostgreSQL for core data, Firebase for push delivery, and Firestore for cache in high-demand content flows.",
            es="Django y DRF para la API y las herramientas internas, Celery y Redis para trabajo en segundo plano, PostgreSQL para datos centrales, Firebase para la entrega de push y Firestore para caché en flujos de contenido de alta consulta.",
        ),
        "note": text(
            en="Some parts, such as deeper metrics and more advanced segmentation, are still evolving and are not presented here as finished work.",
            es="Algunas partes, como métricas más profundas y segmentación más avanzada, siguen en evolución y no se presentan aquí como trabajo cerrado.",
        ),
        "primary_cta": {
            "label": text(
                en="Talk about a similar challenge",
                es="Hablar de un desafío similar",
            ),
            "route_name": "contact",
        },
        "secondary_cta": {
            "label": text(en="View services", es="Ver servicios"),
            "route_name": "services",
        },
    },
    "osoigo": {
        "name": "Osoigo",
        "route_name": "case-study-osoigo",
        "kind": text(en="Case study", es="Caso de estudio"),
        "meta": {
            "title": text(
                en="Case study: Osoigo | leohakim.dev",
                es="Caso de estudio: Osoigo | leohakim.dev",
            ),
            "description": text(
                en="Sensitive backend work for a live participation platform with messaging and permission-based flows.",
                es="Trabajo sobre áreas sensibles del backend de una plataforma participativa viva.",
            ),
        },
        "hero_summary": text(
            en="Sensitive backend work for a live participation platform where messaging, permissions, and continuity could not be treated lightly.",
            es="Trabajo sobre áreas sensibles del backend de una plataforma participativa viva, donde mensajería, permisos y continuidad no se podían tratar a la ligera.",
        ),
        "home_summary": text(
            en="Sensitive backend areas reinforced so a live participation platform could keep evolving with less risk.",
            es="Refuerzo de áreas sensibles del backend para que una plataforma viva pudiera seguir evolucionando con menos riesgo.",
        ),
        "index_summary": text(
            en="Sensitive backend work so a live participation platform could keep evolving with less operational risk.",
            es="Trabajo sobre áreas sensibles del backend para que una plataforma viva pudiera seguir evolucionando con menos riesgo operativo.",
        ),
        "context": text(
            en="This was a live platform with interaction, messaging, and permission-based flows, where touching the wrong backend pieces could easily increase fragility instead of helping the product move forward.",
            es="Era una plataforma en producción, con interacción, mensajería y flujos basados en permisos, donde tocar ciertas piezas del backend sin criterio suficiente podía aumentar la fragilidad en lugar de ayudar al producto a avanzar.",
        ),
        "role": text(
            en="I worked on backend areas tied to conversations, messages, endpoints, signals and emails, asynchronous tasks, and part of the technical-operational layer around deployment and infrastructure.",
            es="Trabajé sobre backend en áreas ligadas a conversaciones, mensajes, endpoints, señales y emails, tareas asíncronas y parte de la capa técnico-operativa asociada al despliegue y la infraestructura.",
        ),
        "approach": [
            {
                "title": text(
                    en="1. Reinforce sensitive backend paths:",
                    es="1. Reforzar recorridos sensibles del backend:",
                ),
                "body": text(
                    en="I helped strengthen conversation, message, and related backend flows so they could be touched with less risk.",
                    es="Ayudé a reforzar flujos de conversaciones, mensajes y áreas relacionadas para que pudieran evolucionar con menos riesgo.",
                ),
            },
            {
                "title": text(
                    en="2. Reduce ambiguity in sensitive behavior:",
                    es="2. Reducir ambigüedad en comportamientos sensibles:",
                ),
                "body": text(
                    en="Testing, signals, emails, and asynchronous work all benefited from clearer handling in areas where small changes could have outsized effects.",
                    es="Testing, señales, emails y trabajo asíncrono se beneficiaron de un manejo más claro en áreas donde pequeños cambios podían tener efectos desproporcionados.",
                ),
            },
            {
                "title": text(
                    en="3. Support continuity while the product kept moving:",
                    es="3. Sostener continuidad mientras el producto seguía avanzando:",
                ),
                "body": text(
                    en="Part of the work was also technical-operational: helping the platform keep evolving without turning each sensitive change into unnecessary risk.",
                    es="Parte del aporte también fue técnico-operativo: ayudar a que la plataforma siguiera evolucionando sin volver cada cambio sensible en un riesgo innecesario.",
                ),
            },
        ],
        "result": text(
            en="The work helped reduce fragility in sensitive areas and made it easier to keep evolving a live system without increasing risk every time key pieces changed.",
            es="El trabajo ayudó a reducir fragilidad en áreas sensibles y a que fuera más fácil seguir evolucionando un sistema vivo sin aumentar el riesgo cada vez que se tocaban piezas clave.",
        ),
        "business_value": text(
            en="On a platform like this, safer evolution matters as much as new features. Lower operational risk protects continuity for both the team and the product.",
            es="En una plataforma así, evolucionar con más seguridad importa tanto como sacar nuevas funcionalidades. Menor riesgo operativo protege la continuidad tanto del equipo como del producto.",
        ),
        "simple_stack": text(
            en="Django and DRF for the backend, PostgreSQL for core data, Celery plus queues for background work, and container-based deployment and runtime tooling to support continuity and safer releases.",
            es="Django y DRF para el backend, PostgreSQL para los datos centrales, Celery y colas para trabajo en segundo plano, y tooling de despliegue y runtime basado en contenedores para sostener continuidad y releases más seguros.",
        ),
        "note": text(
            en="Some institutional and product details are intentionally kept broad here to avoid exposing sensitive internal context.",
            es="Algunos detalles institucionales y de producto se mantienen intencionalmente amplios para no exponer contexto interno sensible.",
        ),
        "primary_cta": {
            "label": text(
                en="Talk about a similar challenge",
                es="Hablar de un desafío similar",
            ),
            "route_name": "contact",
        },
        "secondary_cta": {
            "label": text(en="View services", es="Ver servicios"),
            "route_name": "services",
        },
    },
    "enact": {
        "name": "ENACT",
        "route_name": "case-study-enact",
        "kind": text(en="Technical case", es="Caso técnico"),
        "meta": {
            "title": text(
                en="Case study: ENACT | leohakim.dev",
                es="Caso de estudio: ENACT | leohakim.dev",
            ),
            "description": text(
                en="Infrastructure, deployment, and runtime coordination work in a multi-team international environment.",
                es="Trabajo de infraestructura, despliegue y coordinación de runtime en un entorno internacional multi-equipo.",
            ),
        },
        "hero_summary": text(
            en="Infrastructure, deployment, and runtime coordination work in a multi-team international environment that needed repeatability more than improvisation.",
            es="Trabajo de infraestructura, despliegue y coordinación de runtime en un entorno internacional multi-equipo que necesitaba repetibilidad más que improvisación.",
        ),
        "home_summary": text(
            en="Infrastructure and deployment work in a multi-team international environment that needed repeatability.",
            es="Infraestructura y despliegue en un entorno internacional multi-equipo que necesitaba repetibilidad.",
        ),
        "index_summary": text(
            en="Infrastructure and deployment work in a multi-team international environment that needed repeatability.",
            es="Trabajo de infraestructura y despliegue en un entorno internacional multi-equipo que necesitaba repetibilidad.",
        ),
        "context": text(
            en="This was a shared technical environment with distributed ownership, multiple teams, and sensitive deployment pieces such as ingress, TLS, secrets, and service exposure.",
            es="Era un entorno técnico compartido, con ownership distribuido, múltiples equipos y piezas sensibles de despliegue como ingress, TLS, secretos y exposición de servicios.",
        ),
        "role": text(
            en="My contribution focused on infrastructure, deployments, technical integration, and runtime documentation so teams could work with a more repeatable and less informal operational base.",
            es="Mi aporte se centró en infraestructura, despliegues, integración técnica y documentación de runtime para que los equipos trabajaran con una base operativa más repetible y menos informal.",
        ),
        "approach": [
            {
                "title": text(
                    en="1. Make configuration repeatable:",
                    es="1. Volver repetible la configuración:",
                ),
                "body": text(
                    en="I worked with declarative manifests and configuration so deployment did not depend so heavily on tacit knowledge.",
                    es="Trabajé con manifests y configuración declarativa para que el despliegue no dependiera tanto de conocimiento tácito.",
                ),
            },
            {
                "title": text(
                    en="2. Standardize sensitive infrastructure pieces:",
                    es="2. Estandarizar piezas sensibles de infraestructura:",
                ),
                "body": text(
                    en="TLS, ingress, namespaces, secrets, and service exposure needed consistent handling to reduce avoidable friction between teams.",
                    es="TLS, ingress, namespaces, secretos y exposición de servicios necesitaban un tratamiento consistente para reducir fricción evitable entre equipos.",
                ),
            },
            {
                "title": text(
                    en="3. Lower reliance on informal coordination:",
                    es="3. Bajar la dependencia de coordinación informal:",
                ),
                "body": text(
                    en="Documentation and runtime guidance helped make integration and deployment work more predictable across organizations.",
                    es="La documentación y la guía de runtime ayudaron a volver más predecible el trabajo de integración y despliegue entre organizaciones.",
                ),
            },
        ],
        "result": text(
            en="The environment gained predictability. Deployment and integration work relied less on ad hoc coordination and more on repeatable technical decisions.",
            es="El entorno ganó previsibilidad. El despliegue y la integración dependieron menos de coordinación ad hoc y más de decisiones técnicas repetibles.",
        ),
        "business_value": text(
            en="In a multi-partner setting, lowering friction and reducing avoidable deployment risk is already meaningful business value because it protects continuity across shared work.",
            es="En un entorno multi-partner, bajar fricción y reducir riesgo evitable de despliegue ya es valor de negocio porque protege la continuidad del trabajo compartido.",
        ),
        "simple_stack": text(
            en="Kubernetes, declarative deployment configuration, ingress and TLS tooling, runtime documentation, and the practical work needed to make shared environments easier to operate.",
            es="Kubernetes, configuración declarativa de despliegue, tooling de ingress y TLS, documentación de runtime y el trabajo práctico necesario para volver más operables los entornos compartidos.",
        ),
        "note": text(
            en="This is intentionally presented as a technical case. Internal architecture and partner-level details are kept broad on purpose.",
            es="Esto se presenta intencionalmente como un caso técnico. La arquitectura interna y los detalles a nivel partner se mantienen amplios a propósito.",
        ),
        "primary_cta": {
            "label": text(
                en="Talk about a similar challenge",
                es="Hablar de un desafío similar",
            ),
            "route_name": "contact",
        },
        "secondary_cta": {
            "label": text(en="Back to case studies", es="Volver a casos"),
            "route_name": "case-studies",
        },
    },
    "atempora": {
        "name": "Atempora",
        "route_name": "case-study-atempora",
        "kind": text(
            en="Product architecture case",
            es="Caso de arquitectura de producto",
        ),
        "meta": {
            "title": text(
                en="Case study: Atempora | leohakim.dev",
                es="Caso de estudio: Atempora | leohakim.dev",
            ),
            "description": text(
                en="Product architecture for a SaaS with scheduling, credits, payments, and complex rules.",
                es="Arquitectura de producto para un SaaS con agenda, créditos, pagos y reglas complejas.",
            ),
        },
        "hero_summary": text(
            en="A product architecture case for a SaaS with scheduling, credits, payments, and complex rules that could not be improvised without creating expensive debt later.",
            es="Un caso de arquitectura de producto para un SaaS con agenda, créditos, pagos y reglas complejas que no se podían improvisar sin generar deuda cara después.",
        ),
        "home_summary": text(
            en="Product architecture for a SaaS with scheduling, payments, and complex rules that could not be improvised.",
            es="Arquitectura de producto para un SaaS con agenda, pagos y reglas complejas que no se podían improvisar.",
        ),
        "index_summary": text(
            en="Product architecture for a SaaS with scheduling, payments, and complex rules that could not be improvised.",
            es="Arquitectura de producto para un SaaS con agenda, pagos y reglas complejas que no se podían improvisar.",
        ),
        "context": text(
            en="The product combines sessions, credits, payments, cancellations, currencies, settlements, and multi-tenant rules. The risk was ending up with an MVP that looked functional on the surface but was inconsistent underneath.",
            es="El producto combina sesiones, créditos, pagos, cancelaciones, monedas, liquidaciones y reglas multi-tenant. El riesgo era terminar con un MVP que pareciera funcional por fuera pero fuera inconsistente por dentro.",
        ),
        "role": text(
            en="As founder and backend/product architect, I focused on designing the domain, the API, and the core rules before the product scaled on top of ambiguous assumptions.",
            es="Como fundador y arquitecto de backend/producto, me centré en diseñar el dominio, la API y las reglas centrales antes de que el producto creciera sobre supuestos ambiguos.",
        ),
        "approach": [
            {
                "title": text(
                    en="1. Model business rules before screens:",
                    es="1. Modelar reglas de negocio antes que pantallas:",
                ),
                "body": text(
                    en="The first job was to define what sessions, credits, cancellations, usage rules, and settlements really meant instead of letting the implementation guess.",
                    es="El primer trabajo fue definir qué significaban realmente sesiones, créditos, cancelaciones, reglas de uso y liquidaciones en lugar de dejar que la implementación lo adivinara.",
                ),
            },
            {
                "title": text(
                    en="2. Separate key concepts on purpose:",
                    es="2. Separar conceptos clave a propósito:",
                ),
                "body": text(
                    en="Credits were decoupled from money, sessions and slots were modeled explicitly, and multi-tenant plus settlement logic were treated as first-class concerns instead of future patches.",
                    es="Los créditos se desacoplaron del dinero, sesiones y slots se modelaron de forma explícita, y la lógica multi-tenant y de liquidaciones se trató como algo central y no como un parche futuro.",
                ),
            },
            {
                "title": text(
                    en="3. Build the API around real product constraints:",
                    es="3. Construir la API alrededor de restricciones reales del producto:",
                ),
                "body": text(
                    en="The goal was not just cleaner code, but a backend structure the product could keep extending without contradictions becoming structural debt.",
                    es="El objetivo no era solo un código más limpio, sino una estructura backend que el producto pudiera seguir extendiendo sin que las contradicciones se convirtieran en deuda estructural.",
                ),
            },
        ],
        "result": text(
            en="The most important result is clarity. The product now has a much more coherent base for implementation, with fewer dangerous ambiguities in the core rules that matter most.",
            es="El resultado más importante es la claridad. El producto ahora tiene una base mucho más coherente para implementarse, con menos ambigüedades peligrosas en las reglas centrales que más importan.",
        ),
        "business_value": text(
            en="In a product like this, good architecture is business value. It reduces the chance of expensive rewrites, inconsistent behavior, and avoidable friction once the MVP starts growing.",
            es="En un producto así, una buena arquitectura ya es valor de negocio. Reduce la posibilidad de reescrituras caras, comportamientos inconsistentes y fricción evitable cuando el MVP empiece a crecer.",
        ),
        "simple_stack": text(
            en="Django and DRF for the backend and API, PostgreSQL plus queues for the core logic, React for the product interface, and payment/video providers connected to the domain rather than driving it.",
            es="Django y DRF para backend y API, PostgreSQL y colas para la lógica central, React para la interfaz de producto, y proveedores de pago/video conectados al dominio en lugar de definirlo.",
        ),
        "note": text(
            en="This is presented as a product architecture case and an example of capability, not as a finished commercial success story.",
            es="Esto se presenta como un caso de arquitectura de producto y una prueba de capacidad, no como una success story comercial ya cerrada.",
        ),
        "primary_cta": {
            "label": text(
                en="Talk about a similar challenge",
                es="Hablar de un desafío similar",
            ),
            "route_name": "contact",
        },
        "secondary_cta": {
            "label": text(en="View services", es="Ver servicios"),
            "route_name": "services",
        },
    },
    "embever": {
        "name": "Embever",
        "route_name": "case-study-embever",
        "kind": text(en="Public summary", es="Resumen público"),
        "meta": {
            "title": text(
                en="Case study: Embever | leohakim.dev",
                es="Caso de estudio: Embever | leohakim.dev",
            ),
            "description": text(
                en="A brief public note about backend and asynchronous work in a cloud and IoT-related context.",
                es="Una nota pública breve sobre trabajo de backend y procesos asíncronos en un contexto ligado a cloud e IoT.",
            ),
        },
        "hero_summary": text(
            en="A deliberately brief public note about backend and asynchronous work in a cloud and IoT-related context where reliability and traceability mattered.",
            es="Una nota pública intencionalmente breve sobre trabajo de backend y procesos asíncronos en un contexto ligado a cloud e IoT donde importaban la confiabilidad y la trazabilidad.",
        ),
        "home_summary": text(
            en="Backend and asynchronous work in a cloud and IoT-related context where operational trust mattered.",
            es="Trabajo de backend y asincronía en un contexto ligado a cloud e IoT donde la confianza operativa importaba.",
        ),
        "index_summary": text(
            en="Backend and asynchronous work in a cloud and IoT-related context where operational trust mattered.",
            es="Trabajo de backend y asincronía en un contexto ligado a cloud e IoT donde la confianza operativa importaba.",
        ),
        "context": text(
            en="The project involved backend services and sensitive flows where observability, operational trust, and asynchronous processing were important to day-to-day work.",
            es="El trabajo involucró servicios backend y flujos sensibles donde la observabilidad, la confianza operativa y el procesamiento asíncrono eran importantes para el día a día.",
        ),
        "role": text(
            en="I prefer not to turn this into a full public case study until I can recover more precise detail and separate what is safe to publish from what is not.",
            es="Prefiero no convertirlo en un caso público completo hasta poder recuperar más detalle preciso y separar mejor qué es publicable y qué no.",
        ),
        "approach": [
            {
                "title": text(
                    en="1. Backend and async processes:",
                    es="1. Backend y procesos asíncronos:",
                ),
                "body": text(
                    en="work around services and flows where reliability and traceability could not be treated casually.",
                    es="trabajo sobre servicios y flujos donde la confiabilidad y la trazabilidad no se podían tratar de forma liviana.",
                ),
            },
            {
                "title": text(en="2. Operational trust:", es="2. Confianza operativa:"),
                "body": text(
                    en="focus on making the backend base more trustworthy for sensitive daily operations.",
                    es="foco en volver más confiable la base backend para operaciones sensibles del día a día.",
                ),
            },
            {
                "title": text(
                    en="3. Public detail kept intentionally broad:",
                    es="3. Detalle público intencionalmente amplio:",
                ),
                "body": text(
                    en="until more exact material is recovered, this remains supporting experience rather than a flagship case.",
                    es="hasta recuperar material más exacto, esto queda como experiencia de apoyo y no como un caso principal.",
                ),
            },
        ],
        "result": text(
            en="A public summary of backend work in a sensitive cloud and IoT setting, intentionally scoped to what can be stated safely today.",
            es="Un resumen público de trabajo de backend en un contexto sensible de cloud e IoT, limitado intencionalmente a lo que hoy se puede afirmar con seguridad.",
        ),
        "business_value": text(
            en="This still helps represent relevant experience, but I do not treat it as a flagship proof point until I can support it with more concrete public detail.",
            es="Sigue siendo experiencia relevante, pero no la trato como una prueba principal hasta poder sostenerla con más detalle público concreto.",
        ),
        "simple_stack": text(
            en="Backend services, asynchronous processes, operational visibility, and the reliability work needed in systems connected to sensitive technical flows.",
            es="Servicios backend, procesos asíncronos, visibilidad operativa y el trabajo de confiabilidad necesario en sistemas conectados a flujos técnicos sensibles.",
        ),
        "note": text(
            en="This remains supporting experience rather than a flagship public case until more exact and publishable detail is recovered.",
            es="Esto sigue siendo experiencia de apoyo y no un caso público principal hasta recuperar más detalle preciso y publicable.",
        ),
        "primary_cta": {
            "label": text(
                en="Talk about a similar challenge",
                es="Hablar de un desafío similar",
            ),
            "route_name": "contact",
        },
        "secondary_cta": {
            "label": text(en="Back to case studies", es="Volver a casos"),
            "route_name": "case-studies",
        },
    },
}


def normalize_public_language(language_code: str | None) -> str:
    if not language_code:
        return DEFAULT_PUBLIC_LANGUAGE
    normalized = language_code.replace("_", "-").split("-", 1)[0].lower()
    if normalized in SUPPORTED_PUBLIC_LANGUAGES:
        return normalized
    return DEFAULT_PUBLIC_LANGUAGE


def _resolve_localized_value(value: Any, language_code: str) -> Any:
    if isinstance(value, LocalizedText):
        return value.resolve(language_code)
    if isinstance(value, Mapping):
        return {
            key: _resolve_localized_value(item, language_code)
            for key, item in value.items()
        }
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return [_resolve_localized_value(item, language_code) for item in value]
    return value


def _resolve_links(value: Any) -> Any:
    if isinstance(value, Mapping):
        resolved = {
            key: _resolve_links(item)
            for key, item in value.items()
            if key not in {"route_name", "case_slug", "url"}
        }
        if "route_name" in value:
            resolved["href"] = reverse(value["route_name"])
        elif "case_slug" in value:
            resolved["href"] = reverse(CASE_STUDY_ROUTE_NAMES[value["case_slug"]])
        elif "url" in value:
            resolved["href"] = value["url"]
        return resolved
    if isinstance(value, list):
        return [_resolve_links(item) for item in value]
    return value


def _build_case_card(
    case_slug: str,
    language_code: str,
    *,
    summary_key: str,
) -> dict[str, Any]:
    case = _resolve_localized_value(CASE_STUDIES[case_slug], language_code)
    return {
        "title": case["name"],
        "summary": case[summary_key],
        "href": reverse(CASE_STUDY_ROUTE_NAMES[case_slug]),
    }


def get_site_ui(language_code: str | None) -> dict[str, Any]:
    language = normalize_public_language(language_code)
    ui = _resolve_localized_value(SITE_UI, language)
    ui = _resolve_links(ui)
    ui["current_language"] = language
    return ui


def get_page_content(page_key: str, language_code: str | None) -> dict[str, Any]:
    if page_key not in PAGES:
        raise KeyError(f"Unknown page key: {page_key}")

    language = normalize_public_language(language_code)
    page = _resolve_localized_value(PAGES[page_key], language)
    page = _resolve_links(page)

    if page_key == "home":
        page["trust_logos"] = [
            {
                "name": CASE_STUDIES[slug]["name"],
                "href": reverse(CASE_STUDY_ROUTE_NAMES[slug]),
            }
            for slug in VISIBLE_CASE_STUDY_SLUGS
        ]
        page["featured_cases"] = [
            _build_case_card(slug, language, summary_key="home_summary")
            for slug in VISIBLE_CASE_STUDY_SLUGS
        ]
    elif page_key == "case_studies":
        page["cases"] = [
            _build_case_card(slug, language, summary_key="index_summary")
            for slug in VISIBLE_CASE_STUDY_SLUGS
        ]

    page["language_code"] = language
    return page


def get_case_study_content(case_slug: str, language_code: str | None) -> dict[str, Any]:
    if case_slug not in CASE_STUDIES:
        raise KeyError(f"Unknown case study slug: {case_slug}")

    language = normalize_public_language(language_code)
    case = _resolve_localized_value(CASE_STUDIES[case_slug], language)
    case = _resolve_links(case)
    case["language_code"] = language
    return case


def _validate_content() -> None:
    route_names = set(CASE_STUDY_ROUTE_NAMES.values())
    for slug, case in CASE_STUDIES.items():
        if case["route_name"] not in route_names:
            raise ContentError(f"Case study {slug} points to an unknown route name")

    for slug in VISIBLE_CASE_STUDY_SLUGS:
        if slug not in CASE_STUDIES:
            raise ContentError(f"Visible case study {slug} is missing from content")


_validate_content()
