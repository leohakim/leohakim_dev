# Sitemap (v1)

- Home

- Case Studies (Aire · ENACT · Atempora)

- Services (SRE/DevOps · Cloud Architecture · Cost Optimization)

- About (bio corta, valores, stack, certificaciones)

- Writing (blog / notas técnicas / talks)

- Contact (CTA + calendly/mail)

- [Optional] Speaking (charlas, workshops)


---

# Wireframes (texto + layout)

## 1) Home

### Mobile (single column)

```less
[Topbar]  leohakim.dev     [☰]

[HERO]
  — Badge: SRE / Cloud Architect
  — H1: “I design reliable, fast & cost-efficient systems.”
  — Sub: Django & Kubernetes | Push at scale | Observability | Terraform
  — Primary CTA: [Work with me]  Secondary: [View case studies]
  — Trust bar (logos chico): Aire · Osoigo · ENACT · (otros)

[VALUE PROPS - 3 cards]
  (1) Reliability: SLOs, error budgets, HA/DR
  (2) Performance: latencia, caching smart, CDN
  (3) Cost: right-sizing, autoscaling, FinOps simple

[FEATURED CASE STUDY]
  — Thumb + título (Aire)
  — Problem → Approach → Result (3 bullets + métrica)
  — CTA: [Read case study]

[SERVICES SNAPSHOT] (3 bloques con ícono)
  — SRE/DevOps
  — Cloud Architecture
  — Cost Optimization
  CTA: [See all services]

[BLOG HIGHLIGHTS]
  — 2–3 posts con títulos accionables

[ABOUT MINI]
  — Foto chica + 2 párrafos humanos
  — Chips: Django, DRF, K8s, Terraform, AWS/GCP, Prometheus/Otel

[CTA FINAL]
  — “Tell me about your system”
  — [Contact]  [Download CV]

[FOOTER]  Links + socials

```

### Desktop (grid 12)

```java
Header sticky
 ├─ Logo (izq)       ├─ Nav: Home | Case Studies | Services | Writing | About | Contact

HERO (full width, 2 col)
 ├─ Col izq: H1 + sub + CTAs + chips
 └─ Col der: imagen/ilustración técnica (diagrama simple)

Trust bar (fila de logos en gris)

3 Value Props (3 columnas)

Featured Case Study (2 col: imagen / texto + CTA)

Services snapshot (3 tarjetas)

Blog highlights (3 tarjetas)

About mini (2 col: foto / texto)

CTA final (banda con fondo suave)

```

**Copy sugerido HERO**

- H1: “Reliable systems, lower latency, smarter costs.”
- Sub: “SRE & Cloud Architect. I help teams ship resilient backends on AWS/GCP with Kubernetes, Terraform, and solid observability.”
- CTA primario: “Start a project” · Secundario: “See case studies”

---

## 2) Case Studies (listing)

```
[Header]

[Intro]
  — H1: Case Studies
  — Sub: “Problems, constraints, outcomes. Measurable impact.”

[Grid de tarjetas 2–3 col]
  — Aire: Push a escala, audiencias, cache/CDN, métricas (open rate, p50/p95)
  — ENACT: K8s multi-servicio, IaC, seguridad, CI/CD
  — Atempora: multi-tenant, core sesiones/créditos, compliance, escalabilidad

[Filtro chips]
  — Domain: Media, SaaS
  — Tech: k8s, Terraform, DRF, Redis, Prometheus

```

### Template de Case Study (detalle)

```
[Hero con título + 3 KPIs]
  — p95 ↓ 42% | Uptime 99.95% | Coste -28%

[Contexto]
  — Problema / objetivos / restricciones

[Arquitectura]
  — Diagrama (imagen) + descripción (componentes clave)
  — Decisiones (ADR corto): por qué K8s/Terraform/Redis, etc.

[Observabilidad]
  — SLIs/SLOs, alertas, dashboards (screenshots borrosos)

[Entrega]
  — CI/CD (canary, rollbacks), feature flags si aplica

[Resultados]
  — Métricas antes/después (latencia, costos, confiabilidad)

[Stack y rol]
  — Tu rol exacto + tecnologías

[CTA]
  — “Want results like these?” → Contacto

```

---

## 3) Services

```
[H1] Services for reliable & cost-efficient systems

[Cards]
  1) SRE/DevOps
     — SLOs, incident response, HA/DR, runbooks, post-mortems
     — Observabilidad: Prometheus, Grafana, Loki, OpenTelemetry
     — Entregable: playbook + dashboards + alertas

  2) Cloud Architecture
     — K8s (EKS/GKE), Terraform/Helm, redes, secretos, IAM
     — CI/CD: blue/green, canary, rollbacks

  3) Cost Optimization
     — Profiling, cache & CDN strategy, autoscaling, storage tiers
     — Informes y ahorro objetivo (10–30%)

[Paquetes/engagements]
  — Audit (1–2 semanas)
  — Implementation (4–8 semanas)
  — Ongoing SRE (retainer mensual)

[CTA] Book a 30-min intro call

```

---

## 4) About

```
[H1] About Leo Hakim

[Bio corta]
  — 2–3 párrafos orientados a impacto (no historia larga)
  — Filosofía: “reliability first”, “measure to improve”, “costs are a feature”

[Highlights]
  — 20+ años software · Django/DRF · K8s · Terraform · AWS/GCP
  — Liderazgo técnico, equipos cross-funcionales

[Certificaciones & formación]
  — (espacio para AWS/GCP cuando la tengas)
  — Cursos clave (SRE, observabilidad)

[Foto humana + link a LinkedIn]

```

---

## 5) Writing

```
[H1] Writing

[Filtros]
  — SRE, DevOps, Django, Arquitectura

[Listado]
  — Títulos útiles (no clickbait), fechas limpias
  — CTA al final: suscripción o contacto

```

---

## 6) Contact

```
[H1] Let’s make your system reliable

[2 columnas en desktop]
  — Col izq: Form (nombre, email, mensaje) + GDPR breve
  — Col der: “Prefer to talk?” → Calendly / Email directo

[CTA secundario]
  — “Download my 1-page SRE checklist” (lead magnet futuro)

```

---

# Componentes reutilizables (design system básico)

- **Chips** de tecnología/tema
- **Badges** (SRE / Cloud Architect)
- **Cards** (case study, blog, servicio)
- **Stat/KPI** (p50/95/99, uptime, ahorro %)
- **CTAs** primario/secundario
- **Trust bar** de logos (en gris)
- **Code block** estilizado para snippets

---

# Tono y microcopy

- Claro, directo, orientado a **problema → solución → impacto**.
- Evitar jerga innecesaria. Resaltar **métricas** siempre.

**Ejemplos:**

- “Cut p95 by 42% with targeted caching + CDN rules.”
- “From ad-hoc deploys to safe canary releases in 2 weeks.”
- “Error budget policies that your business can understand.”

---

# SEO & performance (checklist rápido)

- H1 único por página + meta-titles orientados a “SRE / Cloud Architect”
- Hero con **value proposition** y **nicho** (Media & SaaS)
- Imágenes **lazy-loaded**, formatos modernos, compresión
- Lighthouse 95+ (no librerías pesadas, usar Tailwind)
- Schema.org (Person, BlogPosting, Organization si aplica)
- OpenGraph para compartir case studies
