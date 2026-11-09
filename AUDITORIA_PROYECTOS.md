# AUDITORÍA, SEPARACIÓN DE PROYECTOS Y ARQUITECTURA DE ENCARDOMY

**Fecha de auditoría:** 9 de noviembre de 2026  
**Ecosistema matriz:** ShaMinKet  
**Proyecto auditado:** Encardomy (`https://encardomy.shaminket.com`)  
**Directorio de trabajo:** `/Users/shaminket/Desktop/Encardomy`

## 1. Identificación de cada proyecto en el ecosistema ShaMinKet

Durante la revisión exhaustiva de los repositorios locales en `/Users/shaminket/.gemini/users/user1/` y las carpetas de Google Drive del usuario, se identificaron **cinco proyectos independientes** desarrollados bajo el paraguas de **ShaMinKet**, los cuales poseen propósitos, audiencias y arquitecturas completamente distintas:

| Proyecto | Dominio / Ubicación identificada | Naturaleza del proyecto | Relación con Encardomy |
| :--- | :--- | :--- | :--- |
| **Proyecto A: Encardomy** | `https://encardomy.shaminket.com` · Carpeta activa: `/Users/shaminket/Desktop/Encardomy` · Drive: `Encardomy/` (`Identidad visual/Identidad.png`, `Trabajos hechos/`) | **Negocio educativo y comercial** que ofrece productos, servicios académicos (presentaciones 20×20, impresión de documentos, boletos y cobertura de obras teatrales), metodologías propias (`1 + 3 = 1`) y recursos de estudio para cualquier estudiante o autodidacta. | **Es el proyecto objetivo de este desarrollo.** |
| **Proyecto B: 415 (Minweb 415)** | `https://415.shaminket.com` · Carpetas locales: `Enp4/`, `Enp4_backup_completo/`, `fotografia-encardomy/` | **Herramienta interna de organización escolar** exclusiva para los 56 alumnos del Grupo 415 (Secciones A y B) de la ENP Plantel 4 "Vidal Castañeda y Nájera" (UNAM). | **Proyecto independiente.** Aunque en su código antiguo llevaba el subtítulo *"ENCARDOMY MINWEB 415"*, NO es el sitio comercial de Encardomy y su contenido escolar interno jamás debe mezclarse en Encardomy. |
| **Proyecto C: Citador Académico ShaMinKet** | Carpeta local: `citador-shaminket/` | **Utilidad web académica** para generar referencias bibliográficas y citas en el texto en 6 formatos (APA 7, MLA 9, Chicago 17, Harvard, IEEE y Vancouver) a partir de enlaces o imágenes. | Herramienta transversal del ecosistema ShaMinKet útil para cualquier estudiante; puede referenciarse o integrarse como recurso educativo general si se autoriza, sin atarlo a ningún grupo escolar. |
| **Proyecto D: Kallos (Corrector de Texto)** | Carpeta local: `corrector-texto/` | **Herramienta de ortografía, gramática y estilo** con métricas de legibilidad, riqueza léxica y tiempo de lectura en español. | Herramienta transversal de estudio y redacción para cualquier estudiante o redactor. |
| **Proyecto E: KINSHOMAT** | Carpeta local: `kinshomat-web/` · Drive: `Kinshomat/KINSHOMAT - Documento Maestro del Proyecto` | **Proyecto narrativo, audiovisual y comunitario** enfocado en introspección, soledad, nostalgia y conexión emocional. | **Totalmente independiente.** No guarda relación funcional ni comercial con Encardomy. |

### Nota transparente sobre acceso al servidor externo
- Al intentar consultar en vivo el dominio externo `https://encardomy.shaminket.com` mediante el navegador web integrado, el servidor externo no devolvió páginas indexadas públicamente.
- La causa raíz del error en la iteración anterior fue asumir que los respaldos locales en `Enp4/` y `Enp4_backup_completo/` (cuyo encabezado decía *"ENCARDOMY MINWEB 415"*) correspondían al sitio comercial `encardomy.shaminket.com`, cuando en realidad correspondían a `https://415.shaminket.com` (**Proyecto B: 415**).

## 2. Objetivo y público de los proyectos principales (Encardomy vs. 415)

### Proyecto A: Encardomy (`https://encardomy.shaminket.com`)
- **Objetivo principal:** Funcionar como un **negocio educativo comercial independiente y escalable** capaz de vender servicios y productos educativos, convertir visitantes en clientes, comunicar con claridad su propuesta de valor (*"Trabajos • Proyectos • Presentaciones • Más — Rápido | Confiable | Hecho para estudiantes"*), posicionar la marca Encardomy, impulsar su canal de YouTube y fidelizar a una audiencia general.
- **Público objetivo:**
  - Estudiantes de cualquier institución educativa (UNAM, IPN o cualquier escuela de nivel medio superior y superior).
  - Personas autodidactas que desean aprender por su cuenta.
  - Personas que buscan materiales, herramientas de estudio, presentaciones de alto impacto o servicios académicos confiables.

### Proyecto B: 415 (`https://415.shaminket.com`)
- **Objetivo principal:** Facilitar la organización diaria, consulta de horarios SIHO, seguimiento de tareas, avisos, exámenes y comunicación interna de un único grupo escolar.
- **Público objetivo:** Exclusivamente los integrantes del **Grupo 415 (Secciones A y B)** de la Escuela Nacional Preparatoria Plantel 4 de la UNAM. No es una tienda ni una plataforma comercial abierta al público.

## 3. Funciones correspondientes a cada proyecto

| Categoría | Funciones que pertenecen a **ENCARDOMY** (Proyecto A) | Funciones que pertenecen exclusivamente a **415** (Proyecto B) |
| :--- | :--- | :--- |
| **Propuesta y Catálogo Comercial** | Presentación de la marca Encardomy, catálogo de servicios por línea institucional o general (Impresión de hojas y documentos, Realización de presentaciones 20 × 20 a $100 MXN, Venta de boletos y cobertura de obras teatrales con fotografías, videos y resumen), flujo claro de solicitud/compra. | Ninguna función comercial abierta al público general. |
| **Recursos Educativos Abiertos** | Metodología propia de exposición de alto impacto **1 + 3 = 1** (Gancho + 3 Pilares + Cierre y regla visual 70/15/15), guías generales de estudio y acceso a utilidades académicas universales (procesamiento de documentos PDF, citación APA 7, revisión de textos). | Ninguna dirigida al público externo. |
| **Contenido Audiovisual y Comunidad** | Promoción del **canal de YouTube de Encardomy**, presentación de videos educativos y llamadas a la acción para suscribirse y aprender. | No aplica. |
| **Atención al Cliente y Confianza** | Página **Nosotros** (identidad, misión, metodología de trabajo de Encardomy), **Preguntas Frecuentes** de compradores, **Contacto** directo para cotizaciones/pedidos (WhatsApp oficial `+52 55 7198 5641` y formulario de encargo) y **Marco Legal** propio de Encardomy (`legal.html`). | Buzón interno de sugerencias del grupo 415 y reportes de la Sección B. |
| **Gestión Escolar Interna** | **Ninguna.** Encardomy no gestiona horarios de salones, pase de lista ni tareas de un grupo. | Horario semanal SIHO del Grupo 415, monitor de clase en vivo y tolerancias, directorio de los 15 profesores del Grupo 415, avisos de materias del 415, tareas y exámenes del 415, agenda de Fotografía del 2º Periodo ENP 4, registro de clases perdidas y espacio de la Sección B. |

## 4. Contenido incorrectamente mezclado en la iteración previa

En los archivos `/Users/shaminket/Desktop/Encardomy/index.html`, `/Users/shaminket/Desktop/Encardomy/js/recovered-data.js` y `/Users/shaminket/Desktop/Encardomy/js/app.js` se habían incorporado por error los siguientes elementos exclusivos del **Proyecto B (415)**:

1. **Horario Semanal Oficial SIHO del Grupo 415**, monitor de clase en curso, reloj/simulador escolar y selector de **Sección A / Sección B**.
2. **Directorio de los 15 profesores del Grupo 415** de la ENP 4 (nombres de docentes y salones B-112, B-109, CC-2, etc.).
3. **Avisos, tareas y exámenes internos del Grupo 415** (fechas de exámenes de octubre 2026, entregas en Classroom del grupo 415, paquetes internos de copias del grupo 415).
4. **Gestor de trabajos necesarios de Historia Universal III** del Grupo 415.
5. **Módulos de Clases Perdidas (Inasistencias) y Comunidad Sección B** del Grupo 415.
6. **Agenda Interactiva de Fotografía del 2º Periodo (Salón B301, ENP 4)** y nota interna de evaluación de la profesora Eza.
7. **Textos legales de la "Minweb 415"** que describían a la plataforma como *"una herramienta web escolar desarrollada exclusivamente para los estudiantes del Grupo 415"*, en lugar de reflejar la naturaleza comercial y educativa general de **Encardomy**.

## 5. Elementos que deben conservarse (y justificación)

1. **Identidad Visual Oficial de Encardomy (`Identidad.png` — Concepto 3: Cursor Inteligente):**
   - **Paleta cromática oficial:** Azul Eléctrico (`#207FF9`), Azul Marino (`#12396A`), Blanco Puro (`#FFFFFF`), Verde Menta (`#31C9BD`), Gris Grafito (`#40464F`) y Gris Claro (`#EEF2F7`).
   - **Tipografías oficiales:** `Sora` (títulos, subtítulos, encabezados y logotipo) e `Inter` (cuerpo de texto, botones e información).
   - **Activos gráficos:** Logotipo oficial de Encardomy (`encardomy.png` e isotipo vectorial SVG del documento con esquina doblada en verde menta, letra "E" y cursor), junto con los logotipos institucionales (`unam.png` e `ipn.png`) para identificar sus líneas de servicios sin limitar la marca a un grupo escolar.
   - **Eslogan y descriptores de marca confirmados en `Identidad.png`:** *"TRABAJOS • PROYECTOS • PRESENTACIONES • MÁS"* y *"RÁPIDO | CONFIABLE | HECHO PARA ESTUDIANTES"*, además del identificador `@encardomy`.
2. **Catálogo de Servicios y Productos Confirmados de Encardomy:**
   - **Impresión de hojas y documentos:** Servicio de impresión de hojas y documentos (Precio: sujeto a cotización / no definido, sin inventar tarifas).
   - **Realización de presentaciones 20 × 20 (Formato PechaKucha):** Diseño y estructuración profesional de presentaciones de 20 diapositivas × 20 segundos (Precio confirmado: **$100 MXN**).
   - **Venta de boletos para obras teatrales (Línea IPN / Cultural):** Paquete integral que incluye venta de boletos, entrega de fotografías, entrega de videos y un resumen de la obra (Precio: **Variable**).
3. **Recursos Educativos Universales (con justificación comercial y de valor):**
   - **Metodología de Exposición 1 + 3 = 1** (documentada en Drive en `Metodologias./Metodologia 1 - 3 = 1 - Manual Visual de Exposicion.pdf`, creada por Diego en 2021 y actualizada en octubre de 2026): Aporta un altísimo valor educativo para cualquier visitante que desee aprender a exponer sin leer ni memorizar, y funciona como embudo comercial natural hacia el servicio de **Realización de presentaciones 20 × 20 ($100 MXN)**.
   - **Utilidades de documentos PDF (Motor PDF24):** Reutilizable únicamente como herramienta educativa general para que cualquier estudiante o autodidacta comprima, una, divida o convierta sus archivos PDF de estudio, eliminando toda referencia al Grupo 415.
4. **Canal Oficial de Contacto y Solicitud de Pedidos:**
   - Formulario estructurado de solicitud de pedido/cotización con vista previa y envío directo al WhatsApp oficial de atención de Encardomy (`+52 55 7198 5641`), preparado para enlaces de pago vía **Clip** según cotización.

## 6. Elementos que deben eliminarse de inmediato

1. Eliminar por completo el archivo `/Users/shaminket/Desktop/Encardomy/js/recovered-data.js` que contiene la base de datos del Grupo 415.
2. Eliminar del HTML y de `js/app.js` todas las pestañas, funciones y referencias a:
   - Grupo 415, Sección A, Sección B y SIHO.
   - Horario escolar, monitor de clase en curso, simulador de hora y tolerancias de 10/20 minutos.
   - Directorio de los 15 profesores de la ENP 4.
   - Avisos, tareas y exámenes de octubre de 2026 del Grupo 415.
   - Agenda de Fotografía del salón B301 (2º Periodo ENP 4).
   - Registro de Clases Perdidas y Espacio Sección B.
3. Eliminar la estructura monolítica de un solo archivo HTML gigante para dar paso a una arquitectura multi-página limpia y mantenible.

## 7. Elementos que deben desarrollarse (y elementos pendientes de confirmación)

### Elementos a desarrollar en esta reconstrucción
1. **Arquitectura multi-página independiente** con archivos HTML dedicados para cada sección comercial y educativa de Encardomy:
   - `index.html` (Inicio: presentación de Encardomy, propuesta de valor, acceso rápido por institución UNAM/IPN y productos destacados).
   - `productos.html` (Catálogo detallado de productos y servicios confirmados con filtro por categoría/institución y solicitud directa).
   - `recursos.html` (Recursos educativos abiertos: guía interactiva de la Metodología `1 + 3 = 1` y suite de utilidades PDF para estudiantes).
   - `youtube.html` (Sección dedicada a impulsar el canal de YouTube de Encardomy, temáticas de contenido y suscripción).
   - `nosotros.html` (Identidad de Encardomy, propósito educativo y comercial, estándares de calidad y respaldo de ShaMinKet).
   - `contacto.html` (Canales de atención al cliente y generador interactivo de solicitudes de compra/cotización por WhatsApp).
   - `preguntas-frecuentes.html` (Resolución de dudas habituales de compradores sobre entregas, formatos, precios y proceso de pedido, sin inventar políticas no confirmadas).
   - `legal.html` (Términos de servicio y Aviso de Privacidad redactados específicamente para la plataforma comercial Encardomy).
2. **Sistema modular de hojas de estilo CSS** (`global.css`, `header.css`, `footer.css`, `home.css`, `products.css`, `responsive.css`).
3. **Sistema modular de scripts JavaScript** (`main.js`, `navigation.js`, `products.js`, `interactions.js`).

### Elementos pendientes de confirmación por parte del responsable (no inventados)
- **URL exacta del canal de YouTube de Encardomy y enlaces a videos publicados:** En Drive y archivos locales se menciona el identificador `@encardomy`, pero no consta aún la URL definitiva del canal de YouTube ni IDs de videos públicos específicos; `youtube.html` se deja estructurado y listo para enlazar los videos reales sin inventar títulos ni estadísticas falsas.
- **Tarifario fijo para Impresión de hojas y Boletería teatral:** Se respetan estrictamente como *"Precio: No definido (cotización según encargo)"* y *"Precio: Variable"*, manteniendo únicamente el precio confirmado de **$100 MXN** para las presentaciones 20 × 20.
- **Datos fiscales/domicilio legal definitivo en `legal.html`:** Se actualiza el marco legal para Encardomy como negocio educativo, dejando señalados únicamente los campos de domicilio y correo oficial si deseas personalizarlos antes del despliegue.

## 8. Arquitectura técnica propuesta e implementada para Encardomy

```text
Encardomy/
│
├── index.html                  # Inicio: propuesta de valor, accesos institucionales (UNAM/IPN) y servicios clave
├── productos.html              # Catálogo comercial de servicios y productos educativos confirmados
├── recursos.html               # Recursos educativos gratuitos: Metodología 1+3=1 y utilidades PDF
├── youtube.html                # Promoción del canal de YouTube de Encardomy (@encardomy)
├── nosotros.html               # Qué es Encardomy, filosofía "Cursor Inteligente" y respaldo ShaMinKet
├── contacto.html               # Atención al cliente y cotizador/solicitud directa de pedidos
├── preguntas-frecuentes.html   # Dudas frecuentes de compradores sobre los servicios confirmados
├── legal.html                  # Términos de uso y Aviso de Privacidad de Encardomy
│
├── assets/
│   ├── images/
│   │   ├── encardomy.png       # Logotipo oficial Encardomy
│   │   ├── unam.png            # Escudo oficial UNAM
│   │   └── ipn.png             # Escudo oficial IPN
│   ├── icons/
│   │   └── isotipo.svg         # Isotipo vectorial oficial "Cursor Inteligente"
│   └── fonts/                  # Referencia tipográfica (Sora & Inter vía Google Fonts)
│
├── css/
│   ├── global.css              # Variables de marca, reset, tipografía Sora/Inter, botones y utilidades
│   ├── header.css              # Barra de navegación superior consistente y menú activo
│   ├── footer.css              # Pie de página comercial e institucional de Encardomy
│   ├── home.css                # Estilos específicos de la página de Inicio y selector visual
│   ├── products.css            # Estilos del catálogo de productos, recursos, YouTube, FAQ y contacto
│   └── responsive.css          # Adaptación responsive para computadoras Mac, tabletas y móviles
│
├── js/
│   ├── main.js                 # Inicialización global, año dinámico y utilidades comunes
│   ├── navigation.js           # Control de menú móvil/responsive, estado activo de ruta y accesibilidad
│   ├── products.js             # Catálogo estructurado de productos confirmados, filtrado y modal/prellenado
│   └── interactions.js         # Acordeón de Preguntas Frecuentes, generador de pedidos WhatsApp y suite PDF
│
└── AUDITORIA_PROYECTOS.md      # Documento oficial de auditoría y separación de proyectos
```
