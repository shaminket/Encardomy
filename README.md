# Encardomy — Plataforma Web Multipágina Oficial
> **Servicios Académicos Inteligentes | Velocidad de IA + Revisión Humana Experta**

Este proyecto constituye el sitio web completo y multipágina de **Encardomy**, desarrollado bajo la identidad visual del manual de marca oficial y la metodología 3P de **15 secciones individuales aplicadas a cada servicio**.

---

## 🎨 Identidad Visual y Sistema de Diseño

- **Paleta de Color Oficial**:
  - **Azul Eléctrico (`#2D7FF9`)**: Acciones primarias, botones de llamada a la acción (CTA), estados activos y barras de progreso.
  - **Azul Marino (`#123B6A`)**: Títulos de jerarquía principal, encabezados, barras de navegación y pie de página.
  - **Blanco (`#FFFFFF`)**: Fondo dominante para limpieza visual y alto contraste.
  - **Verde Menta (`#31C98D`)**: Sello de verificación humana, confirmaciones de éxito y beneficios clave.
  - **Gris Grafito (`#40464F`)**: Texto regular, párrafos descriptivos y legibilidad continua.
  - **Superficie Clara (`#EEF2F7`) / Azul Muy Claro (`#DCEEFF`)**: Fondos de tarjetas secundarias, badges de categoría e inputs de formulario.
- **Tipografías**:
  - **Sora**: Encabezados, títulos de sección, números de metodología, botones y métricas.
  - **Inter**: Párrafos, listas descriptivas, campos de formulario y tablas técnicas.
- **Cuadrícula & Espaciado**: Sistema de múltiplos de **8px** (`8, 16, 24, 32, 40, 48, 64, 80, 96 px`).
- **Accesibilidad (WCAG AA)**: Áreas táctiles mínimas de **44px** en todos los botones e interactivos, contraste cromático verificado y soporte para lectores de pantalla.
- **Mobile-First**: Experiencia nativa y fluida en teléfonos móviles con menú drawer accesible y barra flotante inferior rápida.

---

## 🧭 Arquitectura Multipágina

El flujo de usuario sigue estrictamente la jerarquía:

```text
Inicio (index.html)
  └── Categorías / Catálogo (categorias.html)
        └── Categoría filtrada (?cat=estudiar, ?cat=mejorar, etc.)
              └── Página individual de servicio (/servicios/*.html)
                    └── Modal / Flujo de Compra y Cotización por WhatsApp
```

---

## 📂 Catálogo de 5 Categorías & 12 Servicios

| Categoría | Servicio | Archivo | Entregables Clave |
| :--- | :--- | :--- | :--- |
| **Estudiar** | Resumen Académico | `servicios/resumen.html` | Síntesis conceptual, glosario y Flash Summary |
| **Estudiar** | Guía de Estudio | `servicios/guia-de-estudio.html` | Temario desglosado con preguntas razonadas |
| **Estudiar** | Flashcards | `servicios/flashcards.html` | Mazos para Anki (.apkg), Quizlet y PDF |
| **Estudiar** | Examen de Práctica | `servicios/examen-de-practica.html` | Simulacro con solucionario y ponderaciones |
| **Mejorar** | Corrección Académica | `servicios/correccion-academica.html` | Ortotipografía, APA 7 y Control de Cambios |
| **Mejorar** | Edición Natural | `servicios/edicion-natural.html` | Humanización de textos y cadencia orgánica |
| **Mejorar** | Mejora de Trabajo | `servicios/mejora-de-trabajo.html` | Diagnóstico de rúbrica y enriquecimiento |
| **Crear** | Documento Académico | `servicios/documento-academico.html` | Borrador base con citas reales verificadas |
| **Crear** | Investigación | `servicios/investigacion.html` | Marco teórico y base de datos de referencias |
| **Diseñar** | Presentación Visual | `servicios/presentacion.html` | Diapositivas PPTX / Canva con notas de orador |
| **Diseñar** | Infografía | `servicios/infografia.html` | Láminas PDF vectoriales 300 DPI y PNG 4K |
| **Proyectos** | Proyecto Encardomy | `servicios/proyecto-encardomy.html` | Acompañamiento integral end-to-end |

---

## 📐 Metodología de las 15 Secciones (Aplicada a Cada Servicio)

Cada una de las páginas individuales contiene las 15 secciones estructuradas:

1. **Portada**: Titular de alto impacto, subtítulo, promesa directa, badge de categoría y botón de cotización rápida.
2. **Oferta**: Lista detallada de entregables, componentes incluidos y garantías de calidad.
3. **Imágenes y videos**: Muestras visuales de formatos, diseño editorial y esquemas conceptuales.
4. **Diferenciador**: Por qué Encardomy supera a la IA genérica sin filtro (velocidad + verificación humana, cero promesas falsas de 'indetectable').
5. **Beneficios**: 4 ventajas concretas orientadas a ahorro de tiempo, notas y tranquilidad mental.
6. **Video review de influencer**: `[Placeholder: Video Review de Creador / Estudiante de Prepa & Universidad]`.
7. **Características**: Ficha técnica con plazos de entrega, formatos (.docx, .pdf, .pptx), fuentes aceptadas y revisiones.
8. **Sobre empresa/creador**: Filosofía de Encardomy y origen enfocado en estudiantes de 15 a 25 años.
9. **Autoridad**: `[Placeholder: Rigor metodológico y alianzas académicas en desarrollo]`.
10. **Objeciones**: Respuestas directas a dudas sobre ética académica, plagio, alucinaciones de IA y revisiones.
11. **Unboxing**: Desglose gráfico de qué archivos recibe el alumno en su bandeja de entrega.
12. **¿Para quién es?**: Definición clara de para quién es ideal y para quién NO es.
13. **Prueba social**: `[Placeholder: Testimonios de alumnos verificados en proceso de recolección activa]`.
14. **¿Cómo comprar?**: Guía paso a paso de 3 etapas con cotización previa por WhatsApp.
15. **FAQ**: Acordeón interactivo con preguntas y respuestas específicas del servicio.

---

## 🚀 Cómo Visualizar y Probar el Sitio

Abre directamente `index.html` en tu navegador o ejecuta el servidor local de Python:

```bash
cd /Users/shaminket/.gemini/users/user1/encardomy-web
python3 -m http.server 8000
```

Y visita en tu navegador:
👉 `http://localhost:8000`
