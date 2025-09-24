---
trigger: always_on
---

0) Idioma, tono y enfoque

Idioma obligatorio: responder siempre en español (variante neutra).

Tono: claro, profesional, directo; evitar jerga innecesaria.

Enfoque: priorizar código limpio, escalable, seguro y moderno, con UI limpia y profesional.

1) Alcance del proyecto

Estructura de contenidos: respetar el sitemap y wireframes (Home, Case Studies, Services, About, Writing, Contact, y opcional Speaking). No agregar secciones fuera de alcance sin justificar.

Wireframes

Componentes reutilizables: chips, badges, cards, KPI/stats, CTAs, trust bar, code blocks estilizados. Diseñar como un design system básico.

Wireframes

2) Tecnología y arquitectura front

Stack por defecto: Django templates, HTMX + AlpineJS sin dependencias pesadas.

Estilos: Tailwind CSS (sin Bootstrap). Permitir dark mode mediante class y tokens (CSS variables).

Iconos: Lucide/Heroicons en SVG inline (sin librerías pesadas).

JS: evitar plugins de terceros salvo necesidad clara; cero jQuery.

Imágenes: formatos modernos (AVIF/WebP), lazy-loading, sizes y srcset correctos.

Fuentes: system fonts por defecto; si se usa fuente externa, display=swap y preload sólo de variantes utilizadas.

3) Calidad de código

Convención:

JS: ESLint (base eslint:recommended, @typescript-eslint si aplica) + Prettier.

CSS: reglas Tailwind preferidas; estilos utilitarios → componentes (@apply) cuando haya repetición.

Estructura: separar UI (presentacional) y contenido/datos.

Accesibilidad (A11y):

Contraste AA, navegación por teclado, aria-*, alt en imágenes, :focus-visible.

Semántica: un H1 por página; landmarks (header, nav, main, footer).

Testing ligero:

Prueba de enlaces rotos (crawler simple).

Lighthouse objetivo ≥ 95 en Performance/Best Practices/SEO/Accessibility.

4) Seguridad

Formularios (Contact): sanitizar inputs; usar honeypot o turnstile; nunca exponer claves.

5) Performance & escalabilidad

Presupuesto de rendimiento:

JS inicial ≤ 120 KB gzip; CSS ≤ 50 KB.

TTFB en páginas estáticas < 200 ms (CDN).

Imágenes optimizadas y responsive.

Caching: Cache-Control + ETags; assets con hash y immutable; HTML con revalidación si ISR.

CDN: servir estáticos por CDN; habilitar compresión (brotli/gzip).

Medición: añadir build step que reporte tamaños de bundles y fallar si exceden el presupuesto.

6) SEO & analítica

On-page SEO: meta-title/description por página; schema.org (Person, BlogPosting, Organization cuando aplique); OpenGraph + Twitter cards.

URLs limpias y sitemap.xml + robots.txt.

Blog/Writing: títulos útiles, fechas limpias, sin clickbait; canonical correcto.

Wireframes

Sin trackers intrusivos; analítica ligera (p. ej., Plausible/Umami).

7) UI/UX

HERO Home: valor claro + CTAs (“Work with me / Ver casos”). Trust bar de logos en gris.

Wireframes

Case Studies: plantilla con KPIs (p95, uptime, coste), problema → solución → impacto, diagrama de arquitectura y resultados. CTA final a contacto.

Wireframes

Services: 3 tarjetas (SRE/DevOps, Cloud Architecture, Cost Optimization) con entregables claros y paquetes (Audit / Implementation / Ongoing SRE).

Wireframes

About: bio corta orientada a impacto, highlights y foto humana.

Wireframes

Contact: formulario + alternativa Calendly/email; mini GDPR.

Wireframes

Microcopy: “problema → solución → impacto”, siempre que se pueda con métricas.

Wireframes

8) Entregables que debe producir Windsurf por defecto

Para cada cambio o feature:

Resumen de decisiones (1–3 bullets).

Diff/patch claro (archivos tocados).

Checklist de A11y/Performance/SEO/Security aplicadas.

Cómo testear (pasos reproducibles).

Al crear una página o componente nuevo: incluir ejemplo de uso + variaciones (estados vacíos, loading, error).

9) Do / Don’t

Do:

Tailwind; SVG inline; imágenes AVIF/WebP; a11y AA; Lighthouse ≥95; CSP estricta; contenido del wireframe.

Wireframes

Don’t:

No Bootstrap ni jQuery.

No librerías pesadas para cosas simples (carouseles, modales).

No inline styles salvo critical CSS justificado.

No tracking agresivo ni popups invasivos.

10) Definition of Done (DoD)

Página/feature compila, pasa lint/tests, cumple presupuesto de rendimiento, sin errores a11y obvios, cumple SEO básico, y respeta sitemap + wireframes y design system.

Wireframes

11) Plantilla de respuesta que debe usar Windsurf (siempre)

Formato de salida:

Contexto & objetivo (1–2 líneas).

Decisiones clave (bullets).

Cambios propuestos (lista de archivos + breve razón).

Diffs (solo las partes relevantes).

Checks (A11y/Perf/SEO/Sec).

Cómo probar (pasos y comandos).
