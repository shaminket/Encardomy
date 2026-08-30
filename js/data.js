/**
 * ENCARDOMY — CATÁLOGO OFICIAL DE SERVICIOS Y CATEGORÍAS
 * 5 Categorías | 12 Servicios Académicos | Metodología 3P de 15 Secciones
 */

const ENCARDOMY_CATEGORIES = {
  crear: {
    id: "crear",
    name: "Crear",
    tagline: "Estructuras sólidas, ensayos y marcos teóricos desde cero",
    color: "#7C3AED",
    badgeClass: "badge-cat-crear",
    services: ["documento-academico", "investigacion"]
  },
  mejorar: {
    id: "mejorar",
    name: "Mejorar",
    tagline: "Revisión ortotipográfica, tono natural y enriquecimiento de fuentes",
    color: "#2D7FF9",
    badgeClass: "badge-cat-mejorar",
    services: ["correccion-academica", "edicion-natural", "mejora-de-trabajo"]
  },
  disenar: {
    id: "disenar",
    name: "Diseñar",
    tagline: "Diapositivas e infografías modernas de alto impacto visual",
    color: "#EC4899",
    badgeClass: "badge-cat-disenar",
    services: ["presentacion", "infografia"]
  },
  estudiar: {
    id: "estudiar",
    name: "Estudiar",
    tagline: "Resúmenes, flashcards y simuladores para dominar cualquier examen",
    color: "#31C98D",
    badgeClass: "badge-cat-estudiar",
    services: ["resumen", "guia-de-estudio", "flashcards", "examen-de-practica"]
  },
  proyectos: {
    id: "proyectos",
    name: "Proyectos",
    tagline: "Acompañamiento integral para entregas finales, tesis y prototipos",
    color: "#F59E0B",
    badgeClass: "badge-cat-proyectos",
    services: ["proyecto-encardomy"]
  }
};

const ENCARDOMY_SERVICES = {
  "resumen": {
    id: "resumen",
    name: "Resumen Académico Estructurado",
    slug: "resumen",
    category: "estudiar",
    categoryName: "Estudiar",
    badgeClass: "badge-cat-estudiar",
    shortDesc: "Síntesis conceptual profunda con ideas clave, mapas de conceptos y glosario para asimilar lecturas extensas en minutos.",
    heroTitle: "Domina lecturas de 50 páginas en 10 minutos con rigor y claridad",
    heroSubtitle: "Transformamos PDFs extensos, capítulos de libros y artículos densos en resúmenes organizados, con ideas centrales y verificación humana experta.",
    turnaround: "12 a 24 horas",
    format: "Google Docs editable + PDF maquetado (100% compatible y exportable a Word .docx y Pages)",
    pricePlaceholder: "Cotización inmediata según extensión",
    icon: "book-open",
    offerList: [
      "Extracción jerárquica de tesis central y argumentos clave",
      "Glosario contextualizado de terminología compleja",
      "Diagrama conceptual o mapa mental sintetizado",
      "Resumen ejecutivo de 1 página para repaso ultra rápido",
      "Revisión humana contra el texto original para evitar omisiones críticas"
    ],
    differentiator: "Mientras que una IA genérica suele inventar datos ('alucinar') o cortar párrafos al azar, en Encardomy la IA procesa la estructura masiva y un revisor humano verifica que cada concepto sea fiel a tu fuente original.",
    benefits: [
      { title: "Ahorro de hasta 85% de tiempo", desc: "No te desgastes leyendo 80 páginas de relleno la noche previa a clase." },
      { title: "Comprensión conceptual real", desc: "Estructura lógica diseñada para retención mental rápida, no un copy-paste." },
      { title: "Listo para tus apuntes", desc: "Archivos editables en Word y PDF diseñados con tipografía legible y márgenes limpios." },
      { title: "Sin distorsiones de contenido", desc: "Control de calidad humano que verifica fórmulas, fechas, autores y teorías." }
    ],
    unboxing: [
      { item: "Resumen Maestro", desc: "Documento estructurado en PDF y Word con índice temático." },
      { item: "Executive Flash Summary", desc: "Síntesis visual en 1 página para la hora antes de clase." },
      { item: "Glosario Clave", desc: "Términos técnicos definidos con ejemplos sencillos." },
      { item: "Reporte de Revisión Humana", desc: "Checklist de verificación de fuentes y fidelidad." }
    ],
    targetAudience: "Estudiantes de preparatoria y universidad con alto volumen de lecturas teóricas (Derecho, Medicina, Filosofía, Ciencias Sociales, Ingeniería, Administración).",
    faq: [
      { q: "¿Puedo enviar fotos de copias o libros físicos?", a: "Sí. Aceptamos PDFs, capturas legibles, enlaces web y fotos de apuntes. Nuestro equipo los procesa y transcribe con precisión." },
      { q: "¿El resumen omite detalles importantes?", a: "No. Nuestro estándar garantiza que las ideas primarias, secundarias y las citas indispensables queden perfectamente documentadas." },
      { q: "¿En qué formato recibo mi entrega?", a: "Recibes un archivo PDF optimizado para leer en celular o tablet, más el archivo DOCX editable por si quieres añadir notas." }
    ]
  },
  "guia-de-estudio": {
    id: "guia-de-estudio",
    name: "Guía de Estudio Integral",
    slug: "guia-de-estudio",
    category: "estudiar",
    categoryName: "Estudiar",
    badgeClass: "badge-cat-estudiar",
    shortDesc: "Cuaderno temático con objetivos de aprendizaje, preguntas tipo examen resueltas, explicaciones paso a paso y mapas mentales.",
    heroTitle: "Tu temario de examen transformado en una ruta de estudio infalible",
    heroSubtitle: "Concentramos todo el contenido que tu profesor evaluará en una guía didáctica con preguntas modelo, explicaciones claras y ejemplos.",
    turnaround: "24 a 48 horas",
    format: "Google Docs Cuaderno de Estudio + PDF de alta resolución (compatible con Word, Pages y Google Drive)",
    pricePlaceholder: "Cotización personalizada por número de temas",
    icon: "compass",
    offerList: [
      "Desglose temático alineado a tu programa de estudios",
      "Preguntas clave con justificación pedagógica de respuestas",
      "Ejercicios resueltos paso a paso con advertencia de errores comunes",
      "Sección de autoevaluación rápida con clave de respuestas",
      "Revisión por un asesor humano para asegurar que cubra el nivel académico exigido"
    ],
    differentiator: "No es un simple compilado de texto. Es una herramienta pedagógica diseñada para que estudies en orden progresivo de dificultad, supervisada por personas con experiencia académica.",
    benefits: [
      { title: "Claridad total en el examen", desc: "Sabrás con exactitud qué temas estudiar y cómo te los pueden preguntar." },
      { title: "Reduce la ansiedad", desc: "Elimina la incertidumbre de no saber por dónde empezar con un plan claro." },
      { title: "Aprende el 'por qué'", desc: "No memorices a ciegas; entiende los conceptos con explicaciones sencillas." },
      { title: "100% personalizada", desc: "Hecha a la medida de tu profesor, temario escolar o rúbrica institucional." }
    ],
    unboxing: [
      { item: "Cuaderno de Estudio PDF", desc: "Diseño visual con espacios para anotaciones y resolución." },
      { item: "Simulador de Preguntas", desc: "Banco de reactivos modelo con respuestas explicadas." },
      { item: "Mapa de Rutas Temáticas", desc: "Checklist de avance para marcar temas dominados." },
      { item: "Versión Editable DOCX", desc: "Para que integres tus propios apuntes de clase." }
    ],
    targetAudience: "Estudiantes que preparan exámenes parciales, finales, extraordinarios o exámenes de ingreso universitario.",
    faq: [
      { q: "¿Puedo adjuntar el temario oficial de mi escuela?", a: "¡Por supuesto! De hecho es lo ideal: compártenos el temario o foto del pizarrón y estructuramos la guía exactamente sobre esos puntos." },
      { q: "¿Incluye materias prácticas como Matemáticas o Química?", a: "Sí, desarrollamos guías con problemas modelo resueltos paso a paso indicando la fórmula y el procedimiento." }
    ]
  },
  "flashcards": {
    id: "flashcards",
    name: "Flashcards de Repetición Espaciada",
    slug: "flashcards",
    category: "estudiar",
    categoryName: "Estudiar",
    badgeClass: "badge-cat-estudiar",
    shortDesc: "Tarjetas de estudio activas listas para importar en Anki, Quizlet o imprimir, estructuradas para memorización a largo plazo.",
    heroTitle: "Memoriza fórmulas, fechas, vocabulario y conceptos para siempre",
    heroSubtitle: "Mazo de tarjetas inteligentes con preguntas directas y respuestas concisas basadas en la ciencia del Active Recall y Repetición Espaciada.",
    turnaround: "12 a 24 horas",
    format: "Google Sheets / CSV para Anki (.apkg) + Enlace interactivo Quizlet + PDF imprimible",
    pricePlaceholder: "Por paquete de 50 / 100 / 200 tarjetas",
    icon: "layers",
    offerList: [
      "Formulación de preguntas atómicas (1 concepto por tarjeta)",
      "Respuestas con nemotecnias y ayudas visuales",
      "Archivos listos para sincronizar en Anki y Quizlet en 1 clic",
      "Versión en PDF lista para imprimir y recortar si prefieres papel",
      "Validación humana de conceptos y precisión ortográfica"
    ],
    differentiator: "Aplicamos las reglas de formulación del conocimiento (SuperMemo/Anki) para evitar tarjetas con párrafos largos imposibles de memorizar.",
    benefits: [
      { title: "Retención permanente", desc: "Estudia menos horas al día con mayor retención para exámenes acumulativos." },
      { title: "Estudia donde sea", desc: "Lleva tus mazos en el transporte público o momentos libres en tu celular." },
      { title: "Cero fricción técnica", desc: "Te entregamos los archivos listos para abrir en tu app favorita sin configurar nada." },
      { title: "Precisión conceptual", desc: "Revisadas para que no memorices definiciones erróneas o ambiguas." }
    ],
    unboxing: [
      { item: "Mazo Anki (.apkg)", desc: "Listo para doble tap y sincronización en iOS/Android/PC." },
      { item: "Link a Mazo Quizlet", desc: "Para estudiar con juegos interactivos en el navegador." },
      { item: "Plantilla PDF para Imprimir", desc: "Frente y vuelta alineados para impresión estándar." }
    ],
    targetAudience: "Estudiantes de Medicina, Idiomas, Historia, Derecho, Biología o cualquier materia con alta carga de memoria técnica.",
    faq: [
      { q: "¿Cómo las abro en mi teléfono?", a: "Te enviamos un video tutorial de 30 segundos; solo descargas AnkiDroid o AnkiMobile y abres el archivo que te enviamos." }
    ]
  },
  "examen-de-practica": {
    id: "examen-de-practica",
    name: "Examen de Práctica y Simulador",
    slug: "examen-de-practica",
    category: "estudiar",
    categoryName: "Estudiar",
    badgeClass: "badge-cat-estudiar",
    shortDesc: "Simulacros de prueba con reactivos de opción múltiple, problemas abiertos, rúbricas y retroalimentación de respuestas.",
    heroTitle: "Llega al examen real sabiendo exactamente qué esperar",
    heroSubtitle: "Diseñamos un simulacro con el mismo nivel de exigencia, formato de reactivos y tiempo estimado que tu evaluación real.",
    turnaround: "24 a 36 horas",
    format: "Google Forms interactivo + PDF de Examen y Solucionario + Google Docs editable (compatible con Word y Pages)",
    pricePlaceholder: "Por número de reactivos (20, 40, 60+ preguntas)",
    icon: "check-square",
    offerList: [
      "Reactivos de opción múltiple con distractores realistas",
      "Preguntas abiertas con rúbrica de calificación paso a paso",
      "Hoja de respuestas razonadas (por qué la A es correcta y por qué la B no)",
      "Temporizador recomendado y baremo de autoevaluación",
      "Control de calidad humano para calibrar la dificultad al nivel de tu grado"
    ],
    differentiator: "No creamos preguntas obvias de internet. Desarrollamos casos prácticos y trampas conceptuales típicas que los profesores suelen usar.",
    benefits: [
      { title: "Elimina el factor sorpresa", desc: "Practica con la misma estructura y presión que vivirás en el aula." },
      { title: "Detecta tus puntos ciegos", desc: "Descubre antes del examen qué temas dominas y cuáles debes reforzar." },
      { title: "Aprende de tus errores", desc: "La hoja de respuestas te explica el fundamento de cada reactivo." }
    ],
    unboxing: [
      { item: "Cuadernillo de Preguntas", desc: "Diseñado en formato de examen formal para autoevaluación." },
      { item: "Solucionario Razonado", desc: "Explicación detallada de cada reactivo con citas teóricas." },
      { item: "Matriz de Diagnóstico", desc: "Semáforo para identificar qué unidades repasar." }
    ],
    targetAudience: "Estudiantes que quieren validar si están listos antes de presentar un examen decisivo.",
    faq: [
      { q: "¿Puedo pedir que simule el formato de mi profesor?", a: "Sí, descríbenos si tu profesor suele hacer preguntas de opción múltiple, desarrollo, falso/verdadero o problemas prácticos." }
    ]
  },
  "correccion-academica": {
    id: "correccion-academica",
    name: "Corrección Académica y Estilo",
    slug: "correccion-academica",
    category: "mejorar",
    categoryName: "Mejorar",
    badgeClass: "badge-cat-mejorar",
    shortDesc: "Revisión ortotipográfica exhaustiva, coherencia sintáctica, tono formal y ajuste riguroso a normas APA 7, Vancouver o MLA.",
    heroTitle: "Eleva la calidad de tu trabajo al estándar de publicación académica",
    heroSubtitle: "Corregimos ortografía, sintaxis, puntuación, fluidez de párrafos y formateamos tus citas bibliográficas para que entregues con total seguridad.",
    turnaround: "12 a 24 horas",
    format: "Google Docs con sugerencias marcadas + Google Docs limpio + PDF (exportable a Word .docx y Pages)",
    pricePlaceholder: "Cotización por cuartilla o número de palabras",
    icon: "edit-3",
    offerList: [
      "Corrección ortográfica, gramatical y tipográfica completa",
      "Eliminación de redundancias, muletillas y frases ambiguas",
      "Verificación de coherencia argumental y estructura de párrafos",
      "Formateo estricto de citas y bibliografía (APA 7, Vancouver, Chicago, MLA)",
      "Revisión línea por línea por un corrector de estilo humano"
    ],
    differentiator: "Un corrector automático no entiende el contexto académico ni la intención de tu tesis. Nosotros preservamos tus ideas mientras pulimos la redacción.",
    benefits: [
      { title: "Cero penalizaciones de ortografía", desc: "Asegura la máxima puntuación en los criterios de forma y estilo de tu rúbrica." },
      { title: "Transparencia absoluta", desc: "Te entregamos la versión con Control de Cambios para que veas cada ajuste realizado." },
      { title: "Citas bibliográficas impecables", desc: "Se acabaron los dolores de cabeza con sangrías francesas y formatos de autor-año." }
    ],
    unboxing: [
      { item: "Documento con Control de Cambios", desc: "Muestra cada corrección y sugerencia en los márgenes." },
      { item: "Versión Limpia Lista para Entregar", desc: "Formato final en Word y PDF con diseño editorial sobrio." },
      { item: "Checklist de Estilo Aplicado", desc: "Resumen de normas y reglas de citación verificadas." }
    ],
    targetAudience: "Estudiantes que ya redactaron su ensayo, tesis, reporte o tesina y quieren asegurar una entrega impecable.",
    faq: [
      { q: "¿Cambiarán el sentido de lo que escribí?", a: "Jamás. La corrección de estilo respeta tu voz, tu argumento y tus ideas originales; solo potencia su claridad y elegancia formal." }
    ]
  },
  "edicion-natural": {
    id: "edicion-natural",
    name: "Edición Natural y Humanización",
    slug: "edicion-natural",
    category: "mejorar",
    categoryName: "Mejorar",
    badgeClass: "badge-cat-mejorar",
    shortDesc: "Reescritura de textos rígidos o generados con IA para devolverles fluidez orgánica, voz propia y coherencia académica real.",
    heroTitle: "Devuélvele a tu texto un ritmo orgánico, personal y genuino",
    heroSubtitle: "Transformamos borradores robóticos o artificiales en prosa fluida, convincente y bien estructurada, mediante revisión y reescritura humana.",
    turnaround: "12 a 24 horas",
    format: "Google Docs editable humanizado + PDF + Informe de fluidez (compatible con Word y Pages)",
    pricePlaceholder: "Cotización por volumen de texto",
    icon: "feather",
    offerList: [
      "Eliminación de patrones repetitivos y frases cliché típicas de IA genérica",
      "Variación de longitud de oraciones y cadencia natural de lectura",
      "Sustitución de vocabulario artificial por léxico académico preciso",
      "Incorporación de conectores lógicos naturales y coherencia interna",
      "Reescritura activa y supervisión 100% humana"
    ],
    differentiator: "No usamos trucos de 'bypassing' ni sustitución de caracteres extraños que dañan tu texto. Revertimos la rigidez mediante auténtica edición lingüística y criterio humano.",
    benefits: [
      { title: "Lectura agradable y convincente", desc: "Tu texto se sentirá natural, maduro y fácil de defender ante tu profesor." },
      { title: "Sin palabras huecas", desc: "Reemplazamos la paja y los adjetivos vacíos por argumentos concretos." },
      { title: "Comprensible al 100%", desc: "Estructuras gramaticales claras que comunican exactamente lo que necesitas." }
    ],
    unboxing: [
      { item: "Texto Editado Humanizado", desc: "Documento final en Word con estructura de párrafo enriquecida." },
      { item: "Reporte de Mejoras Aplicadas", desc: "Comparativa de antes y después con notas del editor." }
    ],
    targetAudience: "Estudiantes que redactaron con apoyo de IA y sienten que el resultado quedó tieso, impersonal o lleno de fórmulas repetitivas.",
    faq: [
      { q: "¿Garantizan que sea 'indetectable'?", a: "En Encardomy somos transparentes: no hacemos promesas falsas de 'indetectabilidad' porque los detectores automáticos son inconsistentes. Nuestro compromiso es que tu texto tenga calidad humana real, profundidad y coherencia legítima." }
    ]
  },
  "mejora-de-trabajo": {
    id: "mejora-de-trabajo",
    name: "Diagnóstico y Mejora de Trabajo",
    slug: "mejora-de-trabajo",
    category: "mejorar",
    categoryName: "Mejorar",
    badgeClass: "badge-cat-mejorar",
    shortDesc: "Auditoría integral de proyectos existentes para reforzar argumentos débiles, incorporar fuentes de impacto y robustecer conclusiones.",
    heroTitle: "Convierte un trabajo de 7 en una entrega de 10",
    heroSubtitle: "Analizamos tu borrador frente a tu rúbrica escolar, detectamos vacíos argumentales y lo enriquecemos con mejor bibliografía y estructura.",
    turnaround: "24 a 48 horas",
    format: "Google Docs enriquecido + Reporte de diagnóstico en Google Docs/PDF (compatible con Word y Pages)",
    pricePlaceholder: "Cotización según nivel de profundidad",
    icon: "trending-up",
    offerList: [
      "Diagnóstico exhaustivo de fortalezas y debilidades del borrador",
      "Enriquecimiento del marco teórico con fuentes de mayor rigor",
      "Reestructuración de introducción y conclusiones para mayor impacto",
      "Alineación estricta con la rúbrica de evaluación de tu profesor",
      "Acompañamiento y retroalimentación de un revisor especializado"
    ],
    differentiator: "No solo corregimos lo que ya está escrito; agregamos valor conceptual y fuentes de mayor nivel académico para elevar la nota final.",
    benefits: [
      { title: "Asegura la máxima nota", desc: "Cubrimos todos los puntos exigidos por tu rúbrica antes de que califique tu profesor." },
      { title: "Argumentos blindados", desc: "Reforzamos los puntos débiles de tu trabajo para que resistan preguntas difíciles." },
      { title: "Bibliografía de primer nivel", desc: "Sustituimos fuentes dudosas de blogs por artículos de revistas científicas y libros clave." }
    ],
    unboxing: [
      { item: "Versión Mejorada y Ampliada", desc: "Documento con contenido enriquecido y referencias integradas." },
      { item: "Informe de Auditoría Académica", desc: "Diagnóstico detallado con consejos para tu defensa oral." }
    ],
    targetAudience: "Estudiantes que tienen un primer borrador y quieren asegurar la mejor calificación posible en proyectos decisivos.",
    faq: [
      { q: "¿Puedo enviar la rúbrica de mi profesor?", a: "Sí, es lo ideal. Evaluamos tu trabajo punto por punto conforme a los criterios de evaluación exactos de tu docente." }
    ]
  },
  "documento-academico": {
    id: "documento-academico",
    name: "Redacción Base de Documento Académico",
    slug: "documento-academico",
    category: "crear",
    categoryName: "Crear",
    badgeClass: "badge-cat-crear",
    shortDesc: "Estructuración y redacción inicial de ensayos, monografías y reportes con metodología rigurosa, citas reales y bibliografía comprobable.",
    heroTitle: "Vence la hoja en blanco con una estructura académica sólida",
    heroSubtitle: "Desarrollamos borradores base rigurosos con introducción, desarrollo argumental sustentado, conclusiones y citas en formato estándar.",
    turnaround: "24 a 72 horas",
    format: "Google Docs editable + PDF con citas verificadas (100% compatible con Word .docx y Pages)",
    pricePlaceholder: "Cotización por cuartilla o extensión requerida",
    icon: "file-text",
    offerList: [
      "Planteamiento de hipótesis o tesis central clara",
      "Estructura por capítulos o apartados con lógica deductiva",
      "Citas bibliográficas reales obtenidas de repositorios académicos",
      "Conclusiones fundamentadas en el desarrollo del texto",
      "Verificación humana de fuentes y coherencia de datos"
    ],
    differentiator: "No inventamos referencias ni dejamos cabos sueltos. Cada afirmación relevante cuenta con su respectiva cita bibliográfica real y verificable.",
    benefits: [
      { title: "Avanza a paso firme", desc: "Olvídate del bloqueo de la página en blanco y cuenta con una base de trabajo profesional." },
      { title: "Fuentes 100% comprobables", desc: "Garantizamos que todas las citas provienen de libros, papers y fuentes autorizadas." },
      { title: "Adaptado a tu nivel", desc: "Lenguaje y profundidad ajustados a preparatoria o licenciatura según solicites." }
    ],
    unboxing: [
      { item: "Documento Académico Base", desc: "Archivo DOCX estructurado con carátula formal, índice y cuerpo del texto." },
      { item: "Anexo de Fuentes y Citas", desc: "Listado de referencias en APA/Vancouver con enlaces de consulta directa." },
      { item: "Guía de Lectura y Defensa", desc: "Puntos clave resumidos para que comprendas y expongas el trabajo." }
    ],
    targetAudience: "Estudiantes que necesitan estructurar un ensayo, monografía o reporte técnico con alto estándar metodológico.",
    faq: [
      { q: "¿Cómo garantizan que las fuentes sean reales?", a: "La IA sugiere marcos de búsqueda y nuestro equipo humano consulta directamente Google Scholar, Redalyc, Scielo y repositorios universitarios para verificar los autores y páginas." }
    ]
  },
  "investigacion": {
    id: "investigacion",
    name: "Búsqueda Bibliográfica y Marco Teórico",
    slug: "investigacion",
    category: "crear",
    categoryName: "Crear",
    badgeClass: "badge-cat-crear",
    shortDesc: "Compilación bibliográfica especializada, estado del arte, fichas de lectura analíticas y síntesis de papers indexados.",
    heroTitle: "El respaldo teórico que tu investigación o tesis necesita",
    heroSubtitle: "Localizamos, filtramos y sintetizamos la literatura científica más actualizada sobre tu tema de estudio en un marco conceptual impecable.",
    turnaround: "48 a 72 horas",
    format: "Google Docs con marco teórico + Google Sheets con fichas bibliográficas + Referencias verificadas (compatible con Word y Zotero)",
    pricePlaceholder: "Cotización por número de fuentes y extensión",
    icon: "search",
    offerList: [
      "Búsqueda en bases de datos indexadas (Scopus, Scielo, Redalyc, PubMed)",
      "Fichas de lectura con resumen metodológico de cada artículo",
      "Redacción integrada del estado del arte o marco conceptual",
      "Archivo de gestión bibliográfica (.bib / .ris para Mendeley o Zotero)",
      "Validación de relevancia por un revisor académico"
    ],
    differentiator: "Te ahorramos decenas de horas de lectura dispersa entregándote exactamente los autores seminales y las investigaciones más recientes de tu campo.",
    benefits: [
      { title: "Sustento científico intachable", desc: "Presenta tu trabajo respaldado por las autoridades académicas más reconocidas." },
      { title: "Ahorro masivo de tiempo", desc: "No pierdas semanas navegando en bases de datos sin saber qué artículos elegir." },
      { title: "Listo para citar", desc: "Referencias perfectamente formateadas listas para importar en tu gestor bibliográfico." }
    ],
    unboxing: [
      { item: "Documento de Marco Teórico", desc: "Texto articulado con análisis comparativo de autores." },
      { item: "Fichero Bibliográfico Resumido", desc: "Cuadro sinóptico de metodologías, muestras y hallazgos." },
      { item: "Base de Datos de Referencias", desc: "Archivos compatibles con Zotero, Mendeley o Word." }
    ],
    targetAudience: "Estudiantes en proyectos de titulación, tesis, protocolos de investigación o seminarios avanzados.",
    faq: [
      { q: "¿Pueden buscar fuentes en inglés?", a: "Sí, podemos rastrear literatura tanto en español como en inglés u otros idiomas y sintetizarla en tu idioma de entrega." }
    ]
  },
  "presentacion": {
    id: "presentacion",
    name: "Diseño de Presentación Visual",
    slug: "presentacion",
    category: "disenar",
    categoryName: "Diseñar",
    badgeClass: "badge-cat-disenar",
    shortDesc: "Diapositivas modernas, limpias y profesionales en PowerPoint, Canva o Google Slides enfocadas en retener la atención de tu audiencia.",
    heroTitle: "Diapositivas que atrapan miradas y aseguran tu 10",
    heroSubtitle: "Transformamos textos densos y aburridos en presentaciones dinámicas con diseño minimalista, gráficos claros y notas para el expositor.",
    turnaround: "12 a 24 horas",
    format: "Google Slides editable + PDF de proyección (100% compatible con PowerPoint .pptx, Canva y Keynote)",
    pricePlaceholder: "Por número de diapositivas (10, 20, 30+ slides)",
    icon: "layout",
    offerList: [
      "Diseño visual moderno con la jerarquía visual de Encardomy",
      "Reducción de texto a ideas fuerza e infografías de diapositiva",
      "Notas del orador debajo de cada lámina con el guion sugerido",
      "Iconografía vectorial y paleta de colores armónica",
      "Revisión humana de diagramación y legibilidad proyectable"
    ],
    differentiator: "Adiós a las diapositivas saturadas de párrafos que nadie lee. Aplicamos diseño visual contemporáneo con notas de apoyo para que expongas con total confianza.",
    benefits: [
      { title: "Seguridad al hablar en público", desc: "Las notas del orador te dicen exactamente qué decir en cada lámina." },
      { title: "Impacto visual profesional", desc: "Diferénciate al instante de las plantillas genéricas de tus compañeros." },
      { title: "100% editable", desc: "Modifica textos, fuentes o colores fácilmente en tu plataforma preferida." }
    ],
    unboxing: [
      { item: "Archivo PPTX / Enlace Canva", desc: "Totalmente editable con fuentes estándar o enlace en la nube." },
      { item: "PDF de Respaldo para Proyector", desc: "Optimizado para abrir en cualquier computadora de aula." },
      { item: "Guion / Notas del Expositor", desc: "Texto sugerido para cada minuto de tu presentación." }
    ],
    targetAudience: "Estudiantes que deben exponer temas complejos o defender proyectos finales ante sinodales y profesores exigentes.",
    faq: [
      { q: "¿Puedo pedir que usen Canva?", a: "Sí, podemos diseñar directamente en Canva y compartirte el enlace de edición con permisos completos, o entregarte en PowerPoint (.pptx)." }
    ]
  },
  "infografia": {
    id: "infografia",
    name: "Infografía y Esquemas Visuales",
    slug: "infografia",
    category: "disenar",
    categoryName: "Diseñar",
    badgeClass: "badge-cat-disenar",
    shortDesc: "Láminas gráficas de alto impacto que traducen procesos, líneas de tiempo o datos estadísticos en un formato visual atractivo y pedagógico.",
    heroTitle: "Traduce cualquier concepto complejo en una sola imagen memorable",
    heroSubtitle: "Diseñamos infografías académicas y pósters científicos con diagramas explicativos, estadísticas visuales y tipografía de máxima legibilidad.",
    turnaround: "12 a 24 horas",
    format: "Google Drawings / Canva editable + PNG 4K + PDF vectorial de 300 DPI listo para impresión",
    pricePlaceholder: "Por infografía o serie temática",
    icon: "pie-chart",
    offerList: [
      "Conceptualización y jerarquización visual de datos",
      "Ilustraciones vectoriales, íconos y diagramas de flujo",
      "Formato listo para impresión en alta resolución y publicación web",
      "Estructura narrativa que guía la vista del lector paso a paso",
      "Revisión técnica de datos y proporciones por un diseñador humano"
    ],
    differentiator: "Combinamos rigor en los datos con estética editorial moderna. No es un gráfico automático, es una pieza gráfica curada.",
    benefits: [
      { title: "Explicación instantánea", desc: "Cualquier persona comprende tu tema en menos de 60 segundos." },
      { title: "Ideal para pósters y proyectos", desc: "Resolución lista para imprimir en gran formato sin pixelarse." },
      { title: "Súper compartible", desc: "Formato perfecto para WhatsApp, redes sociales o adjuntar en tareas." }
    ],
    unboxing: [
      { item: "Infografía en PNG 4K", desc: "Para visualización digital en pantallas y dispositivos." },
      { item: "PDF para Impresión Alta Resolución", desc: "Con marcas de corte si requieres llevar a imprenta." },
      { item: "Resumen de Fuentes de Datos", desc: "Pie de página y ficha técnica de procedencia de la información." }
    ],
    targetAudience: "Estudiantes de ciencias, medicina, historia, ecología y diseño que necesitan entregar carteles o síntesis gráficas.",
    faq: [
      { q: "¿Puedo definir las medidas de la infografía?", a: "Sí, podemos trabajar en tamaño carta, tabloide, póster para congreso o formato vertical para celular." }
    ]
  },
  "proyecto-encardomy": {
    id: "proyecto-encardomy",
    name: "Proyecto Encardomy Integral",
    slug: "proyecto-encardomy",
    category: "proyectos",
    categoryName: "Proyectos",
    badgeClass: "badge-cat-proyectos",
    shortDesc: "Acompañamiento integral end-to-end para proyectos semestrales, prototipos, entregas de grado y tesinas.",
    heroTitle: "Tu proyecto semestral completo resuelto con asesoría continua",
    heroSubtitle: "Coordinamos todas las etapas: desde la definición del tema y marco teórico, hasta el informe final, las diapositivas y la preparación de tu defensa.",
    turnaround: "3 a 7 días hábiles (según alcance)",
    format: "Suite Google Workspace (Google Docs + Google Slides + Google Sheets + Carpeta compartida en Google Drive, compatible con Office y Apple)",
    pricePlaceholder: "Cotización por fases o paquete integral",
    icon: "briefcase",
    offerList: [
      "Diagnóstico inicial de objetivos y cronograma de entregas parciales",
      "Redacción estructurada del informe técnico o memoria de proyecto",
      "Diseño de presentación visual ejecutiva para la exposición",
      "Guía de posibles preguntas y respuestas de profesores/sinodales",
      "Acompañamiento y seguimiento personalizado por un asesor humano"
    ],
    differentiator: "No te dejamos solo con un archivo. Te entregamos un ecosistema completo para que entiendas, defiendas y apruebes tu proyecto con excelencia.",
    benefits: [
      { title: "Tranquilidad total en fin de semestre", desc: "Cumple con entregas complejas sin colapsar en semanas de alta presión." },
      { title: "Coherencia de inicio a fin", desc: "El informe escrito, la presentación y las notas comparten el mismo hilo conductor." },
      { title: "Preparación para preguntas difíciles", desc: "Te anticipamos qué cuestionamientos te harán tus evaluadores." }
    ],
    unboxing: [
      { item: "Informe Completo del Proyecto", desc: "Documento maestro en Word y PDF con todos los capítulos." },
      { item: "Presentación Ejecutiva (PPTX)", desc: "Diapositivas diseñadas listas para tu exposición oral." },
      { item: "Resumen Ejecutivo de 2 Páginas", desc: "Para entrega rápida al jurado calificador." },
      { item: "Simulador de Preguntas de Defensa", desc: "Banco de preguntas con respuestas sugeridas." }
    ],
    targetAudience: "Estudiantes en semestres avanzados o finalistas con proyectos de titulación, integradores o ferias de ciencias.",
    faq: [
      { q: "¿Cómo se coordina un proyecto de esta magnitud?", a: "Asignamos un canal directo de seguimiento (vía WhatsApp o correo) con hitos de entrega para que vayas validando cada fase." }
    ]
  }
};

// Exportar globalmente para scripts del navegador
if (typeof window !== 'undefined') {
  window.ENCARDOMY_CATEGORIES = ENCARDOMY_CATEGORIES;
  window.ENCARDOMY_SERVICES = ENCARDOMY_SERVICES;
}
