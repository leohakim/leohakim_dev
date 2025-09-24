# ADR Contexto Adicional — Rediseño leohakim.dev

Este documento complementa los wireframes y sitemap existentes, y establece las **reglas contextuales** y lineamientos clave para el desarrollo del nuevo sitio web en Windsurf.

---

## 🎯 Objetivo

- Crear un sitio **profesional, moderno y minimalista**, con foco en **confiabilidad técnica** y **claridad comunicativa**.
- Comunicar la propuesta de valor: **SRE / Cloud Architect**, con experiencia en **medios y SaaS**, mostrando casos de éxito, servicios y escritos técnicos.
- Garantizar un desarrollo **limpio, escalable y seguro**, con tiempos de carga rápidos (Lighthouse 95+).

---

## 📐 Principios de Diseño

- **UI limpia y moderna**: TailwindCSS como base, sin Bootstrap.
- **Mobile-first**: layouts adaptados desde pantallas pequeñas hacia desktop.
- **Consistencia visual**:
  - Paleta minimalista (blanco, gris suave, azul/acento).
  - Uso de tipografías claras y legibles (ej. Inter, Roboto o Source Sans).
  - Espaciado generoso y jerarquía tipográfica bien definida.

- **Microcopy orientado a impacto**: siempre **problema → solución → métrica**.
- **Imágenes**: livianas, SVG/PNG optimizados, con alt-text descriptivo.

---

## ⚙️ Lineamientos Técnicos

- **Stack Frontend**:
  - **TailwindCSS** para estilos.
  - **AlpineJS / HTMX** en caso de interactividad ligera.
  - **Next.js opcional** para blog / rendimiento futuro.

- **Performance**:
  - Lazy-load en imágenes.
  - Pre-render de contenido crítico.
  - Lighthouse ≥ 95.
  - Uso de imágenes modernas (WebP/AVIF).

- **Accesibilidad**:
  - Contraste AA mínimo.
  - Navegación con teclado.
  - Etiquetas `aria-*` donde corresponda.

---

## 🔒 Seguridad

- HTTPS obligatorio.
- Headers de seguridad (CSP, X-Frame-Options, etc.).
- Formularios con validación y protección anti-spam (honeypot o hCaptcha).

---

## 📑 Secciones y Contenido Clave

Basado en el **Wireframe**:contentReference[oaicite:1]{index=1}:

- **Home**: Hero fuerte, valor inmediato, CTA claro.
- **Case Studies**: foco en métricas, arquitectura y resultados medibles.
- **Services**: tarjetas con entregables concretos y engagement models.
- **About**: bio profesional + highlights técnicos.
- **Writing**: artículos orientados a SEO y autoridad técnica.
- **Contact**: formulario simple + integración con Calendly.

---

## 🛠️ Desarrollo en Windsurf

### Reglas principales
1. Siempre responder en español.
2. Mantener **código limpio** y documentado.
3. Usar componentes reutilizables (cards, chips, CTAs, trust bars).
4. Evitar dependencias innecesarias.
5. Priorización: **claridad > estética compleja**.
6. Revisar cada cambio con criterios: **escalabilidad, seguridad, performance**.

---

## 📈 SEO y Branding

- Meta titles y descripciones optimizados: `SRE / Cloud Architect | Leo Hakim`.
- Estructura semántica correcta (`<h1>`, `<h2>`, `<section>`).
- OpenGraph + Twitter Cards para case studies.
- Schema.org (Person, BlogPosting).

---

## ✅ Entregables Esperados

- Plantilla base en TailwindCSS.
- Layouts responsivos (Home, Case Studies, Services, About, Writing, Contact).
- Sistema de componentes.
- Checklist de performance, seguridad y SEO cumplido.

---

**Autor**: Leo Hakim
**Fecha**: Septiembre 2025
**Repositorio**: [leohakim.dev](https://leohakim.dev)
