import os
import json

services_data = [
    {
        "id": "resumen",
        "slug": "resumen",
        "name": "Resumen Académico Estructurado",
        "category": "estudiar",
        "category_name": "Estudiar",
        "badge_class": "badge-cat-estudiar",
        "hero_title": "Domina lecturas de 50 páginas en 10 minutos con rigor y claridad",
        "hero_subtitle": "Transformamos PDFs extensos, capítulos de libros y artículos densos en resúmenes organizados, con ideas centrales y verificación humana experta.",
        "short_desc": "Síntesis conceptual profunda con ideas clave, mapas de conceptos y glosario para asimilar lecturas extensas en minutos.",
        "turnaround": "12 a 24 horas",
        "format": "Google Docs editable + PDF maquetado (100% compatible y exportable a Microsoft Word .docx y Apple Pages)",
        "price_note": "Estructura preparada para precios por número de páginas o cuartillas",
        "offer_items": [
            "Extracción jerárquica de la tesis central y argumentos secundarios",
            "Glosario contextualizado de terminología técnica y conceptos clave",
            "Esquema o mapa conceptual sintetizado de relaciones lógicas",
            "Resumen ejecutivo de 1 página ('Flash Summary') para repaso de última hora",
            "Revisión humana contra el texto original para evitar omisiones de autores, fechas y teorías"
        ],
        "visual_samples": [
            {"title": "Estructura Jerárquica", "desc": "Tesis principal, subtemas numerados y viñetas de alta legibilidad."},
            {"title": "Glosario Rápido", "desc": "Definiciones claras con ejemplos cotidianos para facilitar la asimilación."},
            {"title": "Executive Summary", "desc": "Una sola carilla con los 5 puntos clave indispensables para el examen."}
        ],
        "differentiator_text": "A diferencia de pedirle a ChatGPT un resumen genérico que 'alucina' datos o ignora el contexto de tu clase, en Encardomy la IA procesa la densidad del texto y un especialista humano valida cada concepto, fecha y fórmula frente a tu documento fuente.",
        "benefits": [
            {"title": "Ahorro de hasta 85% de tiempo", "desc": "No te desgastes leyendo 80 páginas de relleno la noche previa a tu clase o examen."},
            {"title": "Comprensión conceptual real", "desc": "Estructura lógica diseñada para la retención mental rápida, no un simple copy-paste."},
            {"title": "Archivos 100% editables", "desc": "Recibes Word y PDF limpios con tipografía legible para que agregues tus propios apuntes."},
            {"title": "Cero distorsiones teóricas", "desc": "Control de calidad humano que verifica que no se omitan postulados esenciales."}
        ],
        "features": [
            {"label": "Tiempo de Entrega", "value": "12 a 24 horas (opción express disponible)"},
            {"label": "Formatos Entregables", "value": "Google Docs editable + PDF maquetado (exportable a Word y Pages)"},
            {"label": "Fuentes Aceptadas", "value": "PDF, fotos de libros/copias, diapositivas, enlaces web"},
            {"label": "Revisiones Incluidas", "value": "1 ronda de ajustes y aclaraciones sin costo adicional"},
            {"label": "Revisión Humana", "value": "100% verificada línea por línea por un revisor académico"}
        ],
        "about_company": "Encardomy nació de la necesidad real de estudiantes de preparatoria y universidad que enfrentan cargas académicas abrumadoras. Creemos en una educación más eficiente donde la tecnología acelera el trabajo tedioso y el criterio humano asegura la calidad.",
        "authority_text": "Rigor metodológico basado en técnicas de lectura analítica y síntesis deductiva. Cada resumen pasa por un protocolo estandarizado de validación cruzada.",
        "objections": [
            {"q": "¿Es ético usar este resumen para estudiar?", "a": "Totalmente. El resumen es una herramienta de estudio y comprensión de lectura acelerada, equivalente a estudiar con una guía sintetizada de alta calidad."},
            {"q": "¿Y si el profesor pregunta detalles muy específicos?", "a": "Nuestros resúmenes jerarquizan tanto la idea general como los datos específicos (fechas, experimentos, autores clave) para que tengas respuesta a preguntas capciosas."},
            {"q": "¿Qué pasa si mis archivos son fotos de copias borrosas?", "a": "Nuestro equipo procesa las imágenes y transcribe las partes difíciles para asegurar que nada quede fuera."}
        ],
        "unboxing": [
            {"item": "Resumen Maestro (PDF + Word)", "desc": "Documento completo con índice temático y jerarquía visual."},
            {"item": "Executive Flash Sheet", "desc": "Hoja de 1 página con lo indispensable para repasar 15 min antes."},
            {"item": "Glosario Conceptual", "desc": "Lista de definiciones técnicas desglosadas."},
            {"item": "Reporte de Revisión Humana", "desc": "Sello de verificación de fidelidad contra tu texto original."}
        ],
        "for_who": [
            {"type": "Ideal para ti si...", "text": "Tienes lecturas de 30 a 100 páginas en materias teóricas (Derecho, Medicina, Historia, Sociología, Psicología, Ingeniería) y poco tiempo para procesarlas."},
            {"type": "NO es para ti si...", "text": "Buscas que alguien haga un examen en tiempo real por ti (no realizamos actividades no éticas)."}
        ],
        "faq": [
            {"q": "¿Cuántas páginas puede tener mi texto original?", "a": "Trabajamos desde artículos cortos de 5 páginas hasta libros enteros de 300+ páginas. Adaptamos la profundidad según tus necesidades de examen o clase."},
            {"q": "¿Puedo pedir que enfaticen ciertos temas en particular?", "a": "¡Claro que sí! Al enviarnos tu solicitud por WhatsApp puedes indicarnos qué temas evaluará tu profesor para darles máxima prioridad."},
            {"q": "¿Cómo se realiza el pago y entrega?", "a": "Te enviamos la cotización y datos por WhatsApp; una vez confirmado, iniciamos la producción y te entregamos los archivos descargables en tu chat y correo."}
        ]
    },
    {
        "id": "guia-de-estudio",
        "slug": "guia-de-estudio",
        "name": "Guía de Estudio Integral",
        "category": "estudiar",
        "category_name": "Estudiar",
        "badge_class": "badge-cat-estudiar",
        "hero_title": "Tu temario de examen transformado en una ruta de estudio infalible",
        "hero_subtitle": "Concentramos todo el contenido que tu profesor evaluará en una guía didáctica con preguntas modelo, explicaciones paso a paso y mapas mentales.",
        "short_desc": "Cuaderno temático estructurado con objetivos de aprendizaje, preguntas tipo examen resueltas y explicaciones didácticas.",
        "turnaround": "24 a 48 horas",
        "format": "Google Docs Cuaderno de Estudio + PDF de alta resolución (compatible con Word, Pages y Google Drive)",
        "price_note": "Estructura preparada para precios por número de temas o unidades",
        "offer_items": [
            "Desglose temático alineado exactamente a tu programa escolar o temario",
            "Banco de preguntas clave con justificación pedagógica de respuestas",
            "Ejercicios resueltos paso a paso con advertencia de trampas comunes",
            "Sección de autoevaluación rápida con clave de respuestas comentada",
            "Revisión humana para garantizar que cubra el nivel exigido por tu grado"
        ],
        "visual_samples": [
            {"title": "Ruta de Aprendizaje", "desc": "Temario secuenciado de menor a mayor dificultad para un estudio ordenado."},
            {"title": "Preguntas Razonadas", "desc": "Reactivos con explicación de por qué cada respuesta es correcta o incorrecta."},
            {"title": "Cajas de Advertencia", "desc": "Destacados con los errores más comunes que suelen cometer los estudiantes."}
        ],
        "differentiator_text": "No es un simple compilado de información de Wikipedia. Es una guía didáctica diseñada por especialistas pedagógicos que estructuran los temas como los pregunta un profesor real.",
        "benefits": [
            {"title": "Claridad total para el examen", "desc": "Sabrás con exactitud qué temas estudiar y cómo te los pueden formular."},
            {"title": "Reduce la ansiedad", "desc": "Elimina la incertidumbre de no saber por dónde empezar con un plan paso a paso."},
            {"title": "Aprende el fundamento", "desc": "No memorices a ciegas; entiende el origen y aplicación de cada concepto."},
            {"title": "100% personalizada", "desc": "Ajustada a tu profesor, escuela (Prepa UNAM, CCH, Bachilleres, Universidad) o rúbrica."}
        ],
        "features": [
            {"label": "Tiempo de Entrega", "value": "24 a 48 horas"},
            {"label": "Formatos", "value": "Google Docs Cuaderno Didáctico + PDF de alta resolución"},
            {"label": "Alcance", "value": "Temarios parciales, semestrales o extraordinarios"},
            {"label": "Revisiones", "value": "1 ronda de calibración temática incluida"},
            {"label": "Supervisión", "value": "Verificación pedagógica humana"}
        ],
        "about_company": "Encardomy fue creada para democratizar el acceso a materiales de estudio de primer nivel. Queremos que cada estudiante tenga herramientas claras y accesibles para aprobar con tranquilidad.",
        "authority_text": "Diseño instruccional basado en taxonomía de Bloom y principios de aprendizaje cognitivo.",
        "objections": [
            {"q": "¿Sirve para materias prácticas como Matemáticas o Física?", "a": "Sí, incluimos ejercicios resueltos paso a paso señalando la fórmula, el despeje y la sustitución."},
            {"q": "¿Qué pasa si mi profesor tiene un temario muy raro?", "a": "Nos compartes una foto del temario o tus apuntes y construimos la guía apegada a sus requerimientos particulares."}
        ],
        "unboxing": [
            {"item": "Cuaderno Didáctico de Estudio", "desc": "PDF formateado con diseño editorial limpio y espacios de notas."},
            {"item": "Simulador de Preguntas y Respuestas", "desc": "Cuestionario modelo resuelto con justificaciones."},
            {"item": "Mapa de Ruta Temática", "desc": "Checklist para marcar tu avance de estudio tema por tema."},
            {"item": "Versión Editable DOCX", "desc": "Para que agregues anotaciones o ejemplos de tus clases."}
        ],
        "for_who": [
            {"type": "Ideal para ti si...", "text": "Tienes un examen parcial, final o extraordinario y necesitas una guía estructurada que cubra todo el temario en orden."},
            {"type": "NO es para ti si...", "text": "Esperas que alguien resuelva el examen en vivo durante la clase."}
        ],
        "faq": [
            {"q": "¿Puedo enviar apuntes de clase para que los incluyan?", "a": "Sí, integrar tus apuntes hace que la guía sea todavía más fiel al estilo de tu profesor."}
        ]
    },
    {
        "id": "flashcards",
        "slug": "flashcards",
        "name": "Flashcards de Repetición Espaciada",
        "category": "estudiar",
        "category_name": "Estudiar",
        "badge_class": "badge-cat-estudiar",
        "hero_title": "Memoriza fórmulas, fechas y conceptos para siempre",
        "hero_subtitle": "Mazo de tarjetas inteligentes con preguntas atómicas y nemotecnias basadas en la ciencia del Active Recall y Repetición Espaciada.",
        "short_desc": "Tarjetas de estudio activas listas para importar en Anki, Quizlet o imprimir, estructuradas para memorización a largo plazo.",
        "turnaround": "12 a 24 horas",
        "format": "Google Sheets / CSV para Anki (.apkg) + Enlace interactivo Quizlet + PDF imprimible",
        "price_note": "Estructura preparada para paquetes de 50, 100 o 200 tarjetas",
        "offer_items": [
            "Formulación de preguntas atómicas (1 concepto clave por tarjeta)",
            "Respuestas claras con nemotecnias y ayudas conceptuales",
            "Archivos listos para sincronizar en Anki y Quizlet en un solo clic",
            "Versión PDF alineada lista para imprimir y recortar en papel",
            "Supervisión humana de precisión conceptual y ortografía"
        ],
        "visual_samples": [
            {"title": "Mazo Digital Anki", "desc": "Configurado con etiquetas temáticas y algoritmos de repetición espaciada."},
            {"title": "Quizlet Interactivo", "desc": "Enlace directo para repasar en modo juego y prueba rápida."},
            {"title": "PDF Imprimible", "desc": "Formato de frente y vuelta para estudiar sin pantallas."}
        ],
        "differentiator_text": "La mayoría de las tarjetas generadas por IA contienen párrafos larguísimos imposibles de memorizar. Nosotros aplicamos las 20 reglas del conocimiento de SuperMemo para garantizar preguntas atómicas y efectivas.",
        "benefits": [
            {"title": "Retención a largo plazo", "desc": "Estudia 20 minutos al día y recuerda conceptos semanas después para el examen final."},
            {"title": "Estudia en el transporte", "desc": "Repasa desde tu celular en cualquier lugar sin necesidad de cargar libros pesados."},
            {"title": "Cero configuración técnica", "desc": "Te entregamos los archivos listos para abrir y usar en Anki o Quizlet."}
        ],
        "features": [
            {"label": "Tiempo de Entrega", "value": "12 a 24 horas"},
            {"label": "Compatibilidad", "value": "Anki (iOS/Android/PC), Quizlet, PDF estándar"},
            {"label": "Número de Tarjetas", "value": "Desde 30 hasta 300+ tarjetas personalizadas"},
            {"label": "Control de Calidad", "value": "Revisión conceptual humana"}
        ],
        "about_company": "En Encardomy creemos en métodos de estudio con base científica como el Active Recall y la Repetición Espaciada para que estudies menos tiempo con mejores resultados.",
        "authority_text": "Metodología basada en la curva del olvido de Ebbinghaus y los estándares de formulación de SuperMemo.",
        "objections": [
            {"q": "¿No sé usar Anki, podré usarlas?", "a": "¡Sí! Te enviamos un video tutorial de 30 segundos y también te damos el link a Quizlet y la versión imprimible en PDF."}
        ],
        "unboxing": [
            {"item": "Mazo Anki (.apkg)", "desc": "Archivo listo para importar en AnkiDroid / AnkiMobile."},
            {"item": "Acceso a Mazo Quizlet", "desc": "Enlace interactivo para practicar en web o app."},
            {"item": "Plantilla Imprimible PDF", "desc": "Diseño listo para cortar con tijeras si te gusta el papel."}
        ],
        "for_who": [
            {"type": "Ideal para ti si...", "text": "Estudias Medicina, Derecho, Idiomas, Historia, Biología o cualquier materia con alto volumen de memoria técnica."},
            {"type": "NO es para ti si...", "text": "Buscas un documento largo de lectura continua (para eso solicita nuestro servicio de Resumen)."}
        ],
        "faq": [
            {"q": "¿Puedo pedir tarjetas con imágenes o fórmulas?", "a": "Sí, podemos incluir fórmulas matemáticas o diagramas en el anverso o reverso de las tarjetas."}
        ]
    },
    {
        "id": "examen-de-practica",
        "slug": "examen-de-practica",
        "name": "Examen de Práctica y Simulador",
        "category": "estudiar",
        "category_name": "Estudiar",
        "badge_class": "badge-cat-estudiar",
        "hero_title": "Llega al examen real sabiendo exactamente qué esperar",
        "hero_subtitle": "Diseñamos un simulacro con el mismo nivel de exigencia, formato de reactivos y tiempo estimado que tu evaluación escolar real.",
        "short_desc": "Simulacros de prueba con reactivos de opción múltiple, problemas abiertos, rúbricas y retroalimentación de respuestas.",
        "turnaround": "24 a 36 horas",
        "format": "Google Forms interactivo + PDF de Examen y Solucionario + Google Docs editable (compatible con Word y Pages)",
        "price_note": "Estructura preparada por número de reactivos (20, 40, 60+ preguntas)",
        "offer_items": [
            "Reactivos de opción múltiple con distractores realistas y trampas conceptuales",
            "Preguntas abiertas y problemas con desglose de rúbrica",
            "Solucionario razonado que explica por qué la opción correcta es válida",
            "Temporizador sugerido y baremo de autoevaluación",
            "Control de calidad humano para calibrar la dificultad a tu grado exacto"
        ],
        "visual_samples": [
            {"title": "Cuadernillo de Examen", "desc": "Formato formal idéntico a una prueba de preparatoria o facultad."},
            {"title": "Hoja de Respuestas", "desc": "Explicación argumentada de cada reactivo con fundamentos teóricos."},
            {"title": "Matriz de Diagnóstico", "desc": "Semáforo para identificar qué unidades debes repasar antes del examen."}
        ],
        "differentiator_text": "No son preguntas triviales de opción múltiple copiadas de Google. Diseñamos casos prácticos y distractores verosímiles que ponen a prueba tu comprensión real.",
        "benefits": [
            {"title": "Elimina el factor sorpresa", "desc": "Practica con la misma presión y formato que vivirás en el aula escolar."},
            {"title": "Detecta tus puntos ciegos", "desc": "Descubre exactamente en qué temas estás fallando antes de que califique tu maestro."},
            {"title": "Aprende de los errores", "desc": "El solucionario te enseña el porqué de cada fallo para no repetirlo."}
        ],
        "features": [
            {"label": "Tiempo de Entrega", "value": "24 a 36 horas"},
            {"label": "Formatos", "value": "Google Forms interactivo + Google Docs + PDF de Examen y Solucionario"},
            {"label": "Tipos de Reactivos", "value": "Opción múltiple, desarrollo, falso/verdadero, casos prácticos"},
            {"label": "Calibración", "value": "Supervisada por revisor humano"}
        ],
        "about_company": "Encardomy crea herramientas de simulación para que ningún estudiante vuelva a reprobar por culpa de los nervios o del desconocimiento del formato del examen.",
        "authority_text": "Metodología de diseño de reactivos basada en estándares de evaluación formativa y pruebas estandarizadas.",
        "objections": [
            {"q": "¿Las preguntas serán exactamente las de mi profesor?", "a": "Diseñamos un simulacro apegado a tu temario y estilo de evaluación; no vendemos exámenes robados ni realizamos fraudes."}
        ],
        "unboxing": [
            {"item": "Cuadernillo de Evaluación", "desc": "Prueba lista para contestar con tiempo límite."},
            {"item": "Solucionario Razonado", "desc": "Respuestas detalladas con explicaciones paso a paso."},
            {"item": "Tabla de Ponderación", "desc": "Escala para calcular tu calificación estimada."}
        ],
        "for_who": [
            {"type": "Ideal para ti si...", "text": "Quieres ponerte a prueba 2 o 3 días antes del examen para medir tu nivel real y llegar seguro al aula."},
            {"type": "NO es para ti si...", "text": "Buscas que alguien conteste el examen en vivo por ti."}
        ],
        "faq": [
            {"q": "¿Pueden incluir casos clínicos o problemas numéricos?", "a": "Sí, adaptamos los reactivos al área de conocimiento: Medicina, Derecho, Ingenierías o Humanidades."}
        ]
    },
    {
        "id": "correccion-academica",
        "slug": "correccion-academica",
        "name": "Corrección Académica y Estilo",
        "category": "mejorar",
        "category_name": "Mejorar",
        "badge_class": "badge-cat-mejorar",
        "hero_title": "Eleva la calidad de tu trabajo al estándar de publicación académica",
        "hero_subtitle": "Corregimos ortografía, sintaxis, puntuación, fluidez de párrafos y formateamos tus citas bibliográficas para que entregues con total seguridad.",
        "short_desc": "Revisión ortotipográfica exhaustiva, coherencia formal y formateo estricto de citas APA 7, Vancouver o MLA.",
        "turnaround": "12 a 24 horas",
        "format": "Google Docs con sugerencias marcadas + Google Docs limpio + PDF (exportable a Word .docx y Pages)",
        "price_note": "Estructura preparada por cuartilla o número de palabras",
        "offer_items": [
            "Corrección ortográfica, gramatical y tipográfica exhaustiva",
            "Eliminación de redundancias, muletillas y frases ambiguas",
            "Verificación de coherencia argumental y estructura lógica de párrafos",
            "Formateo estricto de citas y bibliografía (APA 7, Vancouver, Chicago, MLA)",
            "Revisión línea por línea realizada por un corrector de estilo humano"
        ],
        "visual_samples": [
            {"title": "Control de Cambios", "desc": "Muestra cada ajuste, sugerencia y corrección en los márgenes de Word."},
            {"title": "Versión Limpia Editorial", "desc": "Documento formateado con sangrías, márgenes y tipografía formal."},
            {"title": "Formato de Citas APA 7", "desc": "Referencias bibliográficas completas con sangría francesa y orden alfabético."}
        ],
        "differentiator_text": "Un corrector automático ignora la coherencia de tu argumento y las normas específicas de tu institución. Nosotros preservamos tu voz original mientras pulimos la redacción con rigor profesional.",
        "benefits": [
            {"title": "Cero penalizaciones de ortografía", "desc": "Asegura la puntuación máxima en los criterios de forma y redacción de tu rúbrica."},
            {"title": "Transparencia absoluta", "desc": "Con la versión en Control de Cambios sabes exactamente qué se corrigió y por qué."},
            {"title": "Citas bibliográficas impecables", "desc": "Se acabaron las dudas con sangrías francesas, cursivas y formato autor-año."}
        ],
        "features": [
            {"label": "Tiempo de Entrega", "value": "12 a 24 horas"},
            {"label": "Normas Soportadas", "value": "APA 7ma edición, Vancouver, Chicago, MLA, IEEE"},
            {"label": "Entregables", "value": "Google Docs con sugerencias + Google Docs limpio (exportable a Word y Pages)"},
            {"label": "Revisor", "value": "Corrector humano con experiencia editorial"}
        ],
        "about_company": "Encardomy ayuda a los estudiantes a comunicar sus ideas con elegancia, precisión y rigor académico, evitando que una mala redacción opaque una gran investigación.",
        "authority_text": "Estándares basados en el Manual de Publicaciones de la APA (7ª ed.) y las normas de la Real Academia Española (RAE).",
        "objections": [
            {"q": "¿Cambiarán mis ideas o mi conclusión?", "a": "Jamás. La corrección de estilo respeta tu hipótesis y argumentos; únicamente potencia su claridad formal."}
        ],
        "unboxing": [
            {"item": "DOCX con Control de Cambios", "desc": "Para que revises y aceptes cada modificación."},
            {"item": "DOCX Limpio Listo para Entrega", "desc": "Documento final formateado según la norma solicitada."},
            {"item": "PDF de Respaldo", "desc": "Diseño editorial listo para imprimir o subir a plataforma."}
        ],
        "for_who": [
            {"type": "Ideal para ti si...", "text": "Ya redactaste tu ensayo, tesis, tesina o reporte y quieres asegurar que no tenga faltas de ortografía ni citas mal puestas."},
            {"type": "NO es para ti si...", "text": "No tienes nada escrito y necesitas que se investigue desde cero (solicita 'Documento Académico')."}
        ],
        "faq": [
            {"q": "¿Qué pasa si mi profesor pide una norma institucional especial?", "a": "Solo adjúntanos los lineamientos de tu facultad o escuela y los aplicamos al pie de la letra."}
        ]
    },
    {
        "id": "edicion-natural",
        "slug": "edicion-natural",
        "name": "Edición Natural y Humanización",
        "category": "mejorar",
        "category_name": "Mejorar",
        "badge_class": "badge-cat-mejorar",
        "hero_title": "Devuélvele a tu texto un ritmo orgánico, personal y genuino",
        "hero_subtitle": "Transformamos borradores robóticos o artificiales en prosa fluida, convincente y bien estructurada, mediante revisión y reescritura humana.",
        "short_desc": "Reescritura de textos rígidos o generados con IA para devolverles fluidez orgánica, voz propia y coherencia académica.",
        "turnaround": "12 a 24 horas",
        "format": "Google Docs editable humanizado + PDF + Informe de fluidez (compatible con Word y Pages)",
        "price_note": "Estructura preparada por extensión de palabras",
        "offer_items": [
            "Eliminación de fórmulas repetitivas, clichés y estructuras tiesas de IA genérica",
            "Variación orgánica de longitud de oraciones y cadencia natural de lectura",
            "Sustitución de vocabulario artificial por léxico académico auténtico",
            "Incorporación de conectores lógicos naturales y coherencia temática profunda",
            "Reescritura y supervisión 100% humana"
        ],
        "visual_samples": [
            {"title": "Antes y Después", "desc": "Comparativa de párrafos acartonados transformados en prosa convincente."},
            {"title": "Variación Sintáctica", "desc": "Ritmo dinámico entre oraciones cortas e ideas complejas desarrolladas."},
            {"title": "Léxico Contextual", "desc": "Uso de terminología propia de tu materia en vez de palabras rimbombantes vacías."}
        ],
        "differentiator_text": "No usamos trucos engañosos como meter caracteres invisibles o sinónimos raros que arruinan tu trabajo. Revertimos la artificialidad mediante auténtica edición lingüística y criterio humano.",
        "benefits": [
            {"title": "Lectura convincente y natural", "desc": "Tu texto se leerá como el trabajo de un estudiante preparado y maduro."},
            {"title": "Sin palabras huecas", "desc": "Reemplazamos la paja y los adjetivos vacíos por argumentos concretos."},
            {"title": "Tranquilidad al exponer", "desc": "Podrás defender tu trabajo oralmente porque sonará como algo que tú mismo dirías."}
        ],
        "features": [
            {"label": "Tiempo de Entrega", "value": "12 a 24 horas"},
            {"label": "Formato", "value": "Google Docs editable con sugerencias de fluidez"},
            {"label": "Enfoque", "value": "Humanización, fluidez, naturalidad, coherencia"},
            {"label": "Transparencia", "value": "Cero promesas de 'indetectabilidad' falsa; 100% calidad real"}
        ],
        "about_company": "Encardomy defiende la voz auténtica del estudiante. Creemos que la IA es un acelerador, pero el toque humano es lo que hace que un trabajo sea valioso y respetable.",
        "authority_text": "Técnicas de redacción estilística, lingüística aplicada y análisis de discurso.",
        "objections": [
            {"q": "¿Prometen que el texto será 'indetectable'?", "a": "No hacemos promesas de 'indetectable' porque los detectores automáticos arrojan falsos positivos incluso con textos históricos. Nuestro compromiso es que tu texto tenga calidad humana real, profundidad y coherencia auténtica."}
        ],
        "unboxing": [
            {"item": "Texto Editado Humanizado (DOCX)", "desc": "Documento final con prosa enriquecida."},
            {"item": "Informe de Ajustes Estilísticos", "desc": "Resumen de los cambios de cadencia y léxico aplicados."}
        ],
        "for_who": [
            {"type": "Ideal para ti si...", "text": "Usaste IA para un borrador y el resultado quedó frío, repetitivo o parece traducido del inglés con fórmulas raras."},
            {"type": "NO es para ti si...", "text": "Buscas un truco mágico de 'bypassing' (nosotros hacemos edición lingüística real)."}
        ],
        "faq": [
            {"q": "¿Puedo conservar mis citas originales?", "a": "Sí, mantenemos todas tus citas y referencias intactas, puliendo únicamente la redacción circundante."}
        ]
    },
    {
        "id": "mejora-de-trabajo",
        "slug": "mejora-de-trabajo",
        "name": "Diagnóstico y Mejora de Trabajo",
        "category": "mejorar",
        "category_name": "Mejorar",
        "badge_class": "badge-cat-mejorar",
        "hero_title": "Convierte un trabajo de 7 en una entrega de 10",
        "hero_subtitle": "Analizamos tu borrador frente a tu rúbrica escolar, detectamos vacíos argumentales y lo enriquecemos con mejor bibliografía y estructura.",
        "short_desc": "Auditoría integral de proyectos existentes para reforzar argumentos débiles, sumar fuentes de peso y alinear con rúbrica.",
        "turnaround": "24 a 48 horas",
        "format": "Google Docs enriquecido + Reporte de diagnóstico en Google Docs/PDF (compatible con Word y Pages)",
        "price_note": "Estructura preparada según el alcance y extensión del borrador",
        "offer_items": [
            "Diagnóstico exhaustivo de fortalezas, debilidades y vacíos del borrador",
            "Enriquecimiento del marco teórico con fuentes académicas de mayor rigor",
            "Reestructuración de introducción y conclusiones para causar alto impacto",
            "Alineación estricta con la rúbrica de evaluación de tu profesor",
            "Acompañamiento y retroalimentación de un revisor especializado"
        ],
        "visual_samples": [
            {"title": "Auditoría de Rúbrica", "desc": "Evaluación preliminar criterio por criterio para prever la calificación."},
            {"title": "Inserción de Fuentes Top", "desc": "Sustitución de blogs por papers indexados y libros seminales."},
            {"title": "Conclusión Contundente", "desc": "Cierre argumental sólido que demuestra dominio del tema."}
        ],
        "differentiator_text": "No solo corregimos errores de dedo; aportamos sustancia intelectual, autores reconocidos y solidez metodológica para elevar tu calificación.",
        "benefits": [
            {"title": "Asegura la máxima nota", "desc": "Cubrimos todos los criterios exigidos por tu rúbrica antes de que califique tu maestro."},
            {"title": "Argumentos blindados", "desc": "Reforzamos los puntos débiles de tu trabajo para que resistas preguntas difíciles."},
            {"title": "Bibliografía de primer nivel", "desc": "Cambia fuentes dudosas por artículos de revistas científicas de impacto."}
        ],
        "features": [
            {"label": "Tiempo de Entrega", "value": "24 a 48 horas"},
            {"label": "Entregables", "value": "Documento enriquecido + Informe de diagnóstico"},
            {"label": "Compatibilidad", "value": "Word DOCX, PDF, Google Docs"},
            {"label": "Revisión", "value": "Especialista académico en el área"}
        ],
        "about_company": "Encardomy funciona como tu asesor de cabecera: identificamos qué le falta a tu entrega para que alcances el 10 sin tener que rehacer todo desde cero.",
        "authority_text": "Evaluación conforme a rúbricas estandarizadas de educación media superior y superior.",
        "objections": [
            {"q": "¿Tengo que enviar la rúbrica del profesor?", "a": "Es lo ideal. Si no tienes rúbrica formal, aplicamos los estándares generales de excelencia para tu grado."}
        ],
        "unboxing": [
            {"item": "Versión Mejorada y Ampliada (DOCX)", "desc": "Tu trabajo con párrafos robustecidos y nuevas citas."},
            {"item": "Informe de Auditoría Académica", "desc": "Checklist con consejos para tu defensa oral."}
        ],
        "for_who": [
            {"type": "Ideal para ti si...", "text": "Tienes un borrador hecho a las carreras y sabes que le faltan fuentes o profundidad para obtener una buena nota."},
            {"type": "NO es para ti si...", "text": "Aún no tienes ninguna idea escrita (revisa 'Documento Académico')."}
        ],
        "faq": [
            {"q": "¿Cuánto contenido nuevo pueden agregar?", "a": "Podemos ampliar desde 1 página hasta capítulos enteros según lo que requiera tu rúbrica."}
        ]
    },
    {
        "id": "documento-academico",
        "slug": "documento-academico",
        "name": "Documento Académico Base",
        "category": "crear",
        "category_name": "Crear",
        "badge_class": "badge-cat-crear",
        "hero_title": "Vence la hoja en blanco con una estructura académica sólida",
        "hero_subtitle": "Desarrollamos borradores base rigurosos con introducción, desarrollo argumental sustentado, conclusiones y citas en formato estándar.",
        "short_desc": "Estructuración y redacción base de ensayos, monografías y reportes con metodología formal y citas reales verificadas.",
        "turnaround": "24 a 72 horas",
        "format": "Google Docs editable + PDF con citas verificadas (100% compatible con Word .docx y Pages)",
        "price_note": "Estructura preparada por cuartilla o extensión requerida",
        "offer_items": [
            "Planteamiento de hipótesis o tesis central clara y bien delimitada",
            "Estructura organizada por apartados con lógica deductiva formal",
            "Citas bibliográficas reales obtenidas de repositorios indexados (Scielo, Redalyc)",
            "Conclusiones fundamentadas en el desarrollo del texto",
            "Verificación humana de fuentes, datos históricos y coherencia"
        ],
        "visual_samples": [
            {"title": "Estructura Capitular", "desc": "Índice claro con carátula formal y desglose de apartados."},
            {"title": "Citas Verificables", "desc": "Cada afirmación central respaldada por un autor y año real."},
            {"title": "Aparato Crítico", "desc": "Referencias bibliográficas completas en formato APA 7 o Vancouver."}
        ],
        "differentiator_text": "No inventamos referencias ni dejamos cabos sueltos. Cada afirmación relevante cuenta con su respectiva cita bibliográfica real que puedes buscar y comprobar en Google Scholar.",
        "benefits": [
            {"title": "Avanza a paso firme", "desc": "Olvídate del bloqueo de la hoja en blanco y cuenta con una base de trabajo impecable."},
            {"title": "Fuentes 100% comprobables", "desc": "Garantizamos que todas las referencias existen y corresponden al tema."},
            {"title": "Adaptado a tu nivel", "desc": "Lenguaje y profundidad calibrados a preparatoria o universidad según solicites."}
        ],
        "features": [
            {"label": "Tiempo de Entrega", "value": "24 a 72 horas (según extensión)"},
            {"label": "Formatos", "value": "DOCX editable + PDF final"},
            {"label": "Citas", "value": "APA 7, Vancouver, MLA o Chicago"},
            {"label": "Revisión", "value": "Verificación humana de fuentes y coherencia"}
        ],
        "about_company": "Encardomy proporciona cimientos académicos sólidos para que los estudiantes desarrollen su pensamiento crítico sin perderse en el bloqueo creativo inicial.",
        "authority_text": "Metodología de redacción basada en el método IMRyD y pautas de publicación científica.",
        "objections": [
            {"q": "¿Las citas son inventadas por la IA?", "a": "No. Nuestro equipo humano busca y valida cada referencia en repositorios académicos reales antes de integrarla."}
        ],
        "unboxing": [
            {"item": "Documento Académico Base (DOCX)", "desc": "Archivo editable con carátula, índice y cuerpo del texto."},
            {"item": "Anexo de Fuentes y Citas", "desc": "Listado de referencias con enlaces de consulta directa."},
            {"item": "Guía de Lectura y Exposición", "desc": "Puntos clave resumidos para que comprendas y expongas el trabajo."}
        ],
        "for_who": [
            {"type": "Ideal para ti si...", "text": "Necesitas redactar un ensayo, monografía o reporte técnico y buscas una estructura sólida con fuentes confiables."},
            {"type": "NO es para ti si...", "text": "Buscas comprar un título o tesis completa para plagiar."}
        ],
        "faq": [
            {"q": "¿Puedo pedir un número específico de cuartillas y fuentes?", "a": "Sí, indícanos cuántas cuartillas y cuántas fuentes bibliográficas mínimas te solicitó tu profesor."}
        ]
    },
    {
        "id": "investigacion",
        "slug": "investigacion",
        "name": "Búsqueda Bibliográfica y Marco Teórico",
        "category": "crear",
        "category_name": "Crear",
        "badge_class": "badge-cat-crear",
        "hero_title": "El respaldo teórico que tu investigación o tesis necesita",
        "hero_subtitle": "Localizamos, filtramos y sintetizamos la literatura científica más actualizada sobre tu tema de estudio en un marco conceptual impecable.",
        "short_desc": "Compilación de literatura científica actualizada, estado del arte, fichas de lectura y base de datos para gestores (Zotero).",
        "turnaround": "48 a 72 horas",
        "format": "Google Docs con marco teórico + Google Sheets con fichas bibliográficas + Referencias verificadas (compatible con Word y Zotero)",
        "price_note": "Estructura preparada por número de fuentes o extensión",
        "offer_items": [
            "Rastreo en bases de datos científicas indexadas (Scopus, Scielo, Redalyc, PubMed)",
            "Fichas de lectura con resumen metodológico de cada artículo",
            "Redacción integrada del estado del arte o marco conceptual",
            "Archivo de gestión bibliográfica (.bib / .ris para Zotero o Mendeley)",
            "Validación de relevancia por un revisor académico"
        ],
        "visual_samples": [
            {"title": "Matriz de Autores", "desc": "Comparativa conceptual de corrientes teóricas y hallazgos recientes."},
            {"title": "Fichas RAE/RPA", "desc": "Resúmenes analíticos de educación y fichas bibliográficas detalladas."},
            {"title": "Colección Zotero/Mendeley", "desc": "Archivo listo para importar en tu gestor con metadatos limpios."}
        ],
        "differentiator_text": "Te ahorramos semanas de búsqueda infructuosa en internet, entregándote una selección curada de papers actuales y autores seminales sobre tu tema.",
        "benefits": [
            {"title": "Sustento científico sólido", "desc": "Presenta tu investigación respaldada por literatura de impacto."},
            {"title": "Ahorro masivo de tiempo", "desc": "No pierdas días descargando PDFs que al final no te sirven."},
            {"title": "Listo para citar", "desc": "Metadatos listos para importar a tu gestor bibliográfico preferido."}
        ],
        "features": [
            {"label": "Tiempo de Entrega", "value": "48 a 72 horas"},
            {"label": "Bases de Datos", "value": "Scielo, Redalyc, Dialnet, Scopus, Google Scholar, PubMed"},
            {"label": "Entregables", "value": "Documento de Marco Teórico + Fichas + Archivo .ris/.bib"},
            {"label": "Supervisión", "value": "Investigador / revisor académico"}
        ],
        "about_company": "En Encardomy facilitamos el acceso al conocimiento científico para que los estudiantes universitarios fundamenten sus proyectos con el más alto rigor.",
        "authority_text": "Protocolo de búsqueda bibliográfica basado en pautas PRISMA y cribado sistemático.",
        "objections": [
            {"q": "¿Pueden incluir artículos en inglés?", "a": "Sí, podemos rastrear y sintetizar literatura en español e inglés según lo requieras."}
        ],
        "unboxing": [
            {"item": "Documento de Marco Teórico (DOCX)", "desc": "Texto articulado con análisis comparativo de autores."},
            {"item": "Fichero Bibliográfico Resumido", "desc": "Cuadro sinóptico de metodologías y hallazgos clave."},
            {"item": "Base de Datos de Referencias (.ris)", "desc": "Para importar en 1 clic en Zotero, Mendeley o Word."}
        ],
        "for_who": [
            {"type": "Ideal para ti si...", "text": "Estás haciendo tu protocolo de tesis, seminario de investigación o tesina y te cuesta encontrar papers relevantes."},
            {"type": "NO es para ti si...", "text": "Solo requieres un resumen breve de 1 página de un texto que ya tienes."}
        ],
        "faq": [
            {"q": "¿Cuántos artículos incluyen?", "a": "Configuramos paquetes desde 10 hasta 50+ artículos científicos según el nivel de tu posgrado o licenciatura."}
        ]
    },
    {
        "id": "presentacion",
        "slug": "presentacion",
        "name": "Diseño de Presentación Visual",
        "category": "disenar",
        "category_name": "Diseñar",
        "badge_class": "badge-cat-disenar",
        "hero_title": "Diapositivas que atrapan miradas y aseguran tu 10",
        "hero_subtitle": "Transformamos textos densos y aburridos en presentaciones dinámicas con diseño minimalista, gráficos claros y notas para el orador.",
        "short_desc": "Diapositivas modernas y visuales con diseño minimalista, gráficos claros y notas para el orador listas para tu exposición.",
        "turnaround": "12 a 24 horas",
        "format": "Google Slides editable + PDF de proyección (100% compatible con PowerPoint .pptx, Canva y Keynote)",
        "price_note": "Estructura preparada por número de diapositivas (10, 20, 30+ slides)",
        "offer_items": [
            "Diseño visual moderno con la jerarquía limpia de Encardomy",
            "Reducción de texto a ideas fuerza y esquemas gráficos",
            "Notas del orador debajo de cada diapositiva con el guion sugerido",
            "Iconografía vectorial y paleta de colores armónica de alto contraste",
            "Revisión humana de diagramación y legibilidad en proyector"
        ],
        "visual_samples": [
            {"title": "Diapositivas de Impacto", "desc": "1 idea principal por lámina para mantener al público atento."},
            {"title": "Notas de Orador", "desc": "Guion redactado debajo de cada slide para que sepas qué decir."},
            {"title": "Iconos y Diagramas", "desc": "Gráficos vectoriales limpios en vez de fotos pixeladas de internet."}
        ],
        "differentiator_text": "Adiós a las diapositivas saturadas de párrafos que nadie lee. Aplicamos diseño visual contemporáneo con notas de apoyo para que expongas con total soltura.",
        "benefits": [
            {"title": "Seguridad al hablar en público", "desc": "Las notas del orador te indican qué decir en cada lámina sin titubear."},
            {"title": "Impacto visual profesional", "desc": "Diferénciate al instante de las plantillas predeterminadas de tus compañeros."},
            {"title": "100% editable", "desc": "Modifica textos o colores fácilmente en PowerPoint o Canva."}
        ],
        "features": [
            {"label": "Tiempo de Entrega", "value": "12 a 24 horas"},
            {"label": "Formatos", "value": "PowerPoint (.pptx) + Canva Link + PDF para proyector"},
            {"label": "Diapositivas", "value": "Paquetes de 10, 15, 20 o 30+ láminas"},
            {"label": "Extras", "value": "Guion para exposición incluido en notas"}
        ],
        "about_company": "En Encardomy creemos que una buena exposición no depende de leer diapositivas, sino de contar con un apoyo visual claro que respalde tus palabras.",
        "authority_text": "Principios de diseño visual, carga cognitiva reducida y comunicación persuasiva.",
        "objections": [
            {"q": "¿Puedo pedir que se haga directamente en mi cuenta de Canva?", "a": "Sí, te compartimos un enlace con permisos de edición completos para que lo copies a tu cuenta de Canva en 1 clic."}
        ],
        "unboxing": [
            {"item": "Archivo PPTX / Enlace Canva", "desc": "Totalmente editable con elementos desbloqueados."},
            {"item": "PDF de Respaldo para Proyector", "desc": "Optimizado para abrir en cualquier computadora sin desfasarse."},
            {"item": "Guion / Notas del Expositor", "desc": "Texto de apoyo para cada minuto de tu presentación."}
        ],
        "for_who": [
            {"type": "Ideal para ti si...", "text": "Tienes que exponer un tema difícil ante tu grupo o defender un proyecto final ante sinodales."},
            {"type": "NO es para ti si...", "text": "Quieres diapositivas atascadas de texto para leerlas en voz alta."}
        ],
        "faq": [
            {"q": "¿Pueden basarse en un Word que ya tengo?", "a": "¡Claro! Nos envías tu documento de Word o PDF y nosotros extraemos las ideas clave y diseñamos las diapositivas."}
        ]
    },
    {
        "id": "infografia",
        "slug": "infografia",
        "name": "Infografía y Esquemas Visuales",
        "category": "disenar",
        "category_name": "Diseñar",
        "badge_class": "badge-cat-disenar",
        "hero_title": "Traduce cualquier concepto complejo en una sola imagen memorable",
        "hero_subtitle": "Diseñamos infografías académicas y pósters científicos con diagramas explicativos, estadísticas visuales y tipografía de máxima legibilidad.",
        "short_desc": "Láminas gráficas y pósters que traducen datos o procesos complejos en un formato visual atractivo y de fácil lectura.",
        "turnaround": "12 a 24 horas",
        "format": "Google Drawings / Canva editable + PNG 4K + PDF vectorial de 300 DPI listo para impresión",
        "price_note": "Estructura preparada por infografía o serie gráfica",
        "offer_items": [
            "Conceptualización y jerarquización visual de datos o procesos",
            "Ilustraciones vectoriales, íconos y diagramas de flujo integrados",
            "Formato listo para impresión en alta resolución (A4, Tabloide, Póster)",
            "Estructura narrativa que guía la vista del lector paso a paso",
            "Revisión técnica de datos y proporciones por un diseñador humano"
        ],
        "visual_samples": [
            {"title": "Póster Científico / Académico", "desc": "Diseño en columnas con gráficos, metodología y conclusiones."},
            {"title": "Infografía de Proceso", "desc": "Línea de tiempo o diagrama de pasos con iconografía moderna."},
            {"title": "Formato para Celular", "desc": "Versión vertical optimizada para compartir en redes o WhatsApp."}
        ],
        "differentiator_text": "Combinamos rigor en los datos con estética editorial moderna. No es un gráfico automático; es una pieza visual curada para comunicar con impacto.",
        "benefits": [
            {"title": "Explicación instantánea", "desc": "Cualquier persona comprende tu tema en menos de 60 segundos."},
            {"title": "Lista para imprimir", "desc": "Resolución vectorial para imprimir en gran formato sin pixelarse."},
            {"title": "Fácil de compartir", "desc": "Formato perfecto para adjuntar en tareas digitales o plataformas escolares."}
        ],
        "features": [
            {"label": "Tiempo de Entrega", "value": "12 a 24 horas"},
            {"label": "Resolución", "value": "PDF Vectorial 300 DPI + PNG 4K"},
            {"label": "Tamaños", "value": "Carta, Oficio, Tabloide, Póster de Congreso o Formato Móvil"},
            {"label": "Revisión", "value": "Supervisada por diseñador humano"}
        ],
        "about_company": "En Encardomy hacemos que la ciencia y los datos complejos se vuelvan intuitivos, atractivos y memorables a través del diseño visual.",
        "authority_text": "Pautas de visualización de datos de Edward Tufte y principios de diseño informativo.",
        "objections": [
            {"q": "¿Puedo pedir correcciones si no me gusta un color?", "a": "Sí, incluimos una ronda de ajustes de color, tipografía o acomodo de elementos sin costo."}
        ],
        "unboxing": [
            {"item": "Infografía en PNG 4K", "desc": "Para visualización en computadoras y celulares."},
            {"item": "PDF de Impresión Alta Resolución", "desc": "Con marcas de corte para llevar a imprenta."},
            {"item": "Ficha Técnica de Fuentes", "desc": "Pie de página con procedencia de los datos utilizados."}
        ],
        "for_who": [
            {"type": "Ideal para ti si...", "text": "Tienes que entregar un cartel escolar, póster para feria de ciencias o infografía de resumen."},
            {"type": "NO es para ti si...", "text": "Requieres un documento de texto corrido de 20 páginas."}
        ],
        "faq": [
            {"q": "¿Hacen pósters para congresos médicos o de ingeniería?", "a": "Sí, tenemos experiencia en diagramación de carteles científicos con rigor en gráficas y metodologías."}
        ]
    },
    {
        "id": "proyecto-encardomy",
        "slug": "proyecto-encardomy",
        "name": "Proyecto Encardomy Integral",
        "category": "proyectos",
        "category_name": "Proyectos",
        "badge_class": "badge-cat-proyectos",
        "hero_title": "Tu proyecto semestral completo resuelto con asesoría continua",
        "hero_subtitle": "Coordinamos todas las etapas: desde la definición del tema y marco teórico, hasta el informe final, las diapositivas y la preparación de tu defensa.",
        "short_desc": "Acompañamiento integral end-to-end para proyectos de titulación, integradores, prototipos y tesinas de grado.",
        "turnaround": "3 a 7 días hábiles (según alcance)",
        "format": "Suite Google Workspace (Google Docs + Google Slides + Google Sheets + Carpeta compartida en Google Drive, compatible con Office y Apple)",
        "price_note": "Estructura preparada por fases o paquete integral",
        "offer_items": [
            "Diagnóstico inicial de objetivos y cronograma de entregas parciales",
            "Redacción estructurada del informe técnico o memoria de proyecto",
            "Diseño de presentación visual ejecutiva para la exposición ante jurado",
            "Guía de posibles preguntas y respuestas de profesores/sinodales",
            "Acompañamiento y seguimiento personalizado por un asesor humano"
        ],
        "visual_samples": [
            {"title": "Memoria de Proyecto", "desc": "Documento maestro con todos los capítulos, justificación y anexos."},
            {"title": "Presentación Ejecutiva", "desc": "Diapositivas diseñadas listas para tu exposición oral."},
            {"title": "Simulador de Jurado", "desc": "Preguntas clave anticipadas con argumentos para tu defensa."}
        ],
        "differentiator_text": "No te dejamos solo con un archivo suelto. Te entregamos un ecosistema completo para que entiendas, defiendas y apruebes tu proyecto con excelencia.",
        "benefits": [
            {"title": "Tranquilidad en fin de semestre", "desc": "Cumple con entregas complejas sin colapsar en semanas de alta presión."},
            {"title": "Coherencia de inicio a fin", "desc": "El informe escrito, la presentación y las notas comparten el mismo hilo conductor."},
            {"title": "Preparación para preguntas difíciles", "desc": "Te anticipamos qué cuestionamientos te harán tus evaluadores."}
        ],
        "features": [
            {"label": "Tiempo de Entrega", "value": "3 a 7 días hábiles (entregas por fases)"},
            {"label": "Entregables", "value": "Informe DOCX/PDF + Presentación PPTX + Guía de Defensa"},
            {"label": "Canal de Atención", "value": "WhatsApp directo con tu asesor asignado"},
            {"label": "Ajustes", "value": "Revisiones continuas durante el desarrollo"}
        ],
        "about_company": "Encardomy acompaña a los estudiantes en los momentos más decisivos de su carrera, asegurando que sus proyectos finales reflejen su máximo potencial.",
        "authority_text": "Gestión de proyectos académicos bajo metodologías ágiles y estándares de titulación universitaria.",
        "objections": [
            {"q": "¿Cómo sé si el proyecto avanza a tiempo?", "a": "Establecemos un cronograma de entregas parciales para que revises y apruebes cada etapa antes de pasar a la siguiente."}
        ],
        "unboxing": [
            {"item": "Informe Completo del Proyecto", "desc": "Documento maestro en Word y PDF con todos los capítulos."},
            {"item": "Presentación Ejecutiva (PPTX)", "desc": "Diapositivas diseñadas listas para tu exposición."},
            {"item": "Resumen Ejecutivo de 2 Páginas", "desc": "Para entrega rápida al jurado calificador."},
            {"item": "Simulador de Preguntas de Defensa", "desc": "Banco de preguntas con respuestas sugeridas."}
        ],
        "for_who": [
            {"type": "Ideal para ti si...", "text": "Estás en semestres avanzados o finalistas con proyectos de titulación, integradores o ferias de ciencias."},
            {"type": "NO es para ti si...", "text": "Buscas solo una tarea pequeña de 1 día (revisa nuestros otros servicios individuales)."}
        ],
        "faq": [
            {"q": "¿Puedo pagar en parcialidades por avance de proyecto?", "a": "Sí, estructuramos el pago en etapas conforme vamos cumpliendo con cada entrega del cronograma."}
        ]
    }
]

template = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{name} — Encardomy | Metodología 3P de 15 Secciones</title>
  <meta name="description" content="{short_desc} Producción rápida con IA y revisión humana experta en Encardomy.">
  
  <!-- Google Fonts: Sora (Headings) & Inter (Body) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Sora:wght@400;600;700;800&display=swap" rel="stylesheet">
  
  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>
  
  <!-- Hoja de estilos oficial de Encardomy -->
  <link rel="stylesheet" href="../css/styles.css">
</head>
<body>

  <!-- ==========================================================================
       SITE HEADER / NAVEGACIÓN GLOBAL
       ========================================================================== -->
  <header class="site-header">
    <div class="container header-inner">
      <a href="../index.html" class="brand-logo" aria-label="Ir al inicio de Encardomy">
        <span class="logo-symbol">E</span>
        <span>Encardomy</span>
        <span class="logo-tagline">&bull; {category_name}</span>
      </a>

      <nav class="nav-desktop" aria-label="Navegación principal">
        <a href="../index.html" class="nav-link">Inicio</a>
        <a href="../categorias.html" class="nav-link">Catálogo</a>
        <a href="#oferta" class="nav-link">Qué Incluye</a>
        <a href="#diferenciador" class="nav-link">IA + Humano</a>
        <a href="#faq" class="nav-link">Preguntas</a>
      </nav>

      <div class="header-actions">
        <button class="btn btn-primary btn-sm" data-open-order data-service-id="{id}">
          <i data-lucide="sparkles" style="width: 16px; height: 16px;"></i>
          <span>Cotizar Servicio</span>
        </button>
        <button class="menu-toggle-btn" id="menuToggleBtn" aria-label="Abrir menú de navegación" aria-expanded="false">
          <i data-lucide="menu" style="width: 24px; height: 24px;"></i>
        </button>
      </div>
    </div>
  </header>

  <!-- Menú Drawer para Móviles -->
  <div class="drawer-overlay" id="drawerOverlay"></div>
  <aside class="mobile-nav-drawer" id="mobileNavDrawer" aria-label="Menú móvil">
    <div class="drawer-header">
      <div class="brand-logo">
        <span class="logo-symbol">E</span>
        <span>Encardomy</span>
      </div>
      <button class="modal-close-btn" id="drawerCloseBtn" aria-label="Cerrar menú">
        <i data-lucide="x" style="width: 20px; height: 20px;"></i>
      </button>
    </div>
    <ul class="drawer-links">
      <li><a href="../index.html" class="drawer-link"><span>🏠 Inicio</span> <i data-lucide="chevron-right"></i></a></li>
      <li><a href="../categorias.html" class="drawer-link"><span>📚 Catálogo Completo</span> <i data-lucide="chevron-right"></i></a></li>
      <li><a href="../categorias.html?cat={category}" class="drawer-link active"><span>🏷️ Categoría: {category_name}</span> <i data-lucide="chevron-right"></i></a></li>
    </ul>
    <div class="mt-32">
      <button class="btn btn-primary btn-block btn-lg" data-open-order data-service-id="{id}">
        <i data-lucide="message-circle"></i>
        <span>Cotizar este Servicio</span>
      </button>
    </div>
  </aside>

  <!-- ==========================================================================
       BREADCRUMB / RUTA DE NAVEGACIÓN
       ========================================================================== -->
  <div style="background: var(--color-bg-light); border-bottom: 1px solid var(--color-border); padding: 10px 0; font-size: 0.86rem;">
    <div class="container" style="display: flex; align-items: center; gap: 8px; color: var(--color-text-muted);">
      <a href="../index.html" style="color: var(--color-text-muted);">Inicio</a>
      <span>&rsaquo;</span>
      <a href="../categorias.html" style="color: var(--color-text-muted);">Catálogo</a>
      <span>&rsaquo;</span>
      <a href="../categorias.html?cat={category}" style="color: var(--color-text-muted);">{category_name}</a>
      <span>&rsaquo;</span>
      <span style="color: var(--color-navy); font-weight: 600;">{name}</span>
    </div>
  </div>

  <!-- ==========================================================================
       1. PORTADA / HERO (METODOLOGÍA SECCIÓN 1)
       ========================================================================== -->
  <main>
    <section class="product-hero" id="portada">
      <div class="container">
        <div class="product-hero-grid">
          <div>
            <div class="mb-16">
              <span class="badge {badge_class}">{category_name}</span>
              <span class="badge badge-success" style="margin-left: 8px;">
                <i data-lucide="shield-check" style="width: 13px; height: 13px;"></i> IA + Revisión Humana
              </span>
            </div>
            
            <h1 class="mb-16" style="color: var(--color-navy);">{hero_title}</h1>
            <p class="text-muted mb-24" style="font-size: 1.12rem;">{hero_subtitle}</p>

                    <div style="display: flex; gap: var(--space-16); align-items: center; flex-wrap: wrap;">
          <a href="../legal.html" style="color: #b0c6e0; text-decoration: underline;">Centro Legal</a>
          <span>&bull;</span>
          <a href="../privacidad.html" style="color: #b0c6e0; text-decoration: underline;">Aviso de Privacidad</a>
          <span>&bull;</span>
          <a href="../propiedad-intelectual.html" style="color: #b0c6e0; text-decoration: underline;">Propiedad Intelectual</a>
          <span>&bull;</span>
          <span>Accesibilidad WCAG AA</span>
          <span>&bull;</span>
          <span>Diseño Mobile-First</span>
        </div>
      </div>
    </div>
  </footer>

  <!-- ==========================================================================
       BARRA FLOTANTE MÓVIL (MOBILE QUICK-BAR)
       ========================================================================== -->
  <div class="mobile-bottom-bar">
    <div>
      <div style="font-family: var(--font-heading); font-weight: 700; font-size: 0.86rem; color: var(--color-navy); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 200px;">
        {name}
      </div>
      <div style="font-size: 0.74rem; color: var(--color-text-muted);">
        Entrega: {turnaround}
      </div>
    </div>
    <button class="btn btn-primary btn-sm" data-open-order data-service-id="{id}">
      <i data-lucide="message-circle"></i>
      <span>Cotizar</span>
    </button>
  </div>

  <!-- ==========================================================================
       MODAL DE COTIZACIÓN INTELIGENTE Y PERSONALIZADA (EXCLUSIVO PREPA 4)
       ========================================================================== -->
  <div class="modal-backdrop" id="orderModal" role="dialog" aria-modal="true" aria-labelledby="modalTitle">
    <div class="modal-card">
      <button class="modal-close-btn" id="modalCloseBtn" aria-label="Cerrar ventana">
        <i data-lucide="x" style="width: 20px; height: 20px;"></i>
      </button>

      <!-- Encabezado del Modal -->
      <div class="mb-20">
        <div style="display: flex; gap: 8px; align-items: center; margin-bottom: 6px; flex-wrap: wrap;">
          <span class="badge badge-primary">Cotización Inteligente</span>
          <span class="badge badge-success" style="font-size: 0.72rem;">Prepa 4 UNAM</span>
          <span class="ecosystem-pill"><i data-lucide="folder-check" style="width: 13px; height: 13px;"></i> Google Workspace + MS & Apple</span>
        </div>
        <h3 id="modalTitle" style="color: var(--color-navy); font-size: 1.35rem;">Configura tu Solicitud Académica</h3>
        <p class="text-muted" style="font-size: 0.88rem; line-height: 1.45;">
          Selecciona tu grado, materia y servicio. El formulario se adaptará para solicitarte exactamente lo necesario sin hacerte perder tiempo.
        </p>
      </div>

      <form id="orderForm">
        <!-- 1. Nombre y Plantel -->
        <div class="grid-2 mb-16">
          <div class="form-group mb-0">
            <label class="form-label" for="orderNameInput">Tu Nombre / Apodo *</label>
            <input type="text" id="orderNameInput" class="form-input" placeholder="Ej. Carlos Mendoza" required>
          </div>
          <div class="form-group mb-0">
            <label class="form-label">Plantel Escolar</label>
            <input type="text" class="form-input" value="Prepa 4 UNAM (Vidal Castañeda y Nájera)" readonly style="background-color: var(--color-blue-tint); font-weight: 600; color: var(--color-navy); cursor: not-allowed;">
          </div>
        </div>

        <!-- 2. Grado, Grupo y Sección (Lógica Dependiente) -->
        <div class="grid-3 mb-16" style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: var(--space-12, 12px);">
          <div class="form-group mb-0">
            <label class="form-label" for="orderGradeSelect">Grado Escolar *</label>
            <select id="orderGradeSelect" class="form-select" required>
              <option value="" disabled selected>Elige tu grado</option>
              <option value="4">4° Cuarto Año</option>
              <option value="5">5° Quinto Año</option>
              <option value="6">6° Sexto Año</option>
            </select>
          </div>
          <div class="form-group mb-0">
            <label class="form-label" for="orderGroupSelect">Grupo *</label>
            <select id="orderGroupSelect" class="form-select" required disabled>
              <option value="" disabled selected>Primero elige grado</option>
            </select>
          </div>
          <div class="form-group mb-0">
            <label class="form-label" for="orderSectionSelect">Sección *</label>
            <select id="orderSectionSelect" class="form-select" required>
              <option value="" disabled selected>Sección</option>
              <option value="Sección A">Sección A</option>
              <option value="Sección B">Sección B</option>
            </select>
          </div>
        </div>

        <!-- 3. Materia Oficial de la ENP 4 -->
        <div class="form-group mb-16">
          <label class="form-label" for="orderSubjectSelect">Materia Oficial de la ENP 4 *</label>
          <select id="orderSubjectSelect" class="form-select" required disabled>
            <option value="" disabled selected>Primero elige tu grado escolar (4°, 5° o 6°)</option>
          </select>
          <div id="customSubjectWrapper" style="display: none; margin-top: 8px;">
            <label class="form-label" for="orderCustomSubjectInput" style="font-size: 0.82rem; color: var(--color-primary);">Especifica el nombre de tu materia:</label>
            <input type="text" id="orderCustomSubjectInput" class="form-input" placeholder="Ej. Taller de Expresión Gráfica o Materia Optativa...">
          </div>
        </div>

        <!-- 4. Servicio Principal -->
        <div class="form-group mb-16">
          <label class="form-label" for="orderServiceSelect">Servicio que necesitas *</label>
          <select id="orderServiceSelect" class="form-select" required>
            <optgroup label="Estudiar">
              <option value="resumen">Resumen Académico Estructurado</option>
              <option value="guia-de-estudio">Guía de Estudio Integral</option>
              <option value="flashcards">Flashcards de Repetición Espaciada</option>
              <option value="examen-de-practica">Examen de Práctica y Simulador</option>
            </optgroup>
            <optgroup label="Mejorar">
              <option value="correccion-academica">Corrección Académica y Normas APA</option>
              <option value="edicion-natural">Edición Natural y Humanización</option>
              <option value="mejora-de-trabajo">Diagnóstico y Mejora de Borrador</option>
            </optgroup>
            <optgroup label="Crear">
              <option value="documento-academico">Documento Académico Base</option>
              <option value="investigacion">Búsqueda Bibliográfica y Marco Teórico</option>
            </optgroup>
            <optgroup label="Diseñar">
              <option value="presentacion">Diseño de Presentación Visual (Google Slides)</option>
              <option value="infografia">Infografía y Esquemas Visuales</option>
            </optgroup>
            <optgroup label="Proyectos">
              <option value="proyecto-encardomy">Proyecto Encardomy Semestral</option>
            </optgroup>
          </select>
        </div>

        <!-- ==================================================================
             PANELES DINÁMICOS Y PERSONALIZADOS POR CADA SERVICIO
             ================================================================== -->

        <!-- Panel 1: Resumen -->
        <div class="service-dynamic-panel" id="servicePanel-resumen" style="display: block;">
          <div class="service-panel-header">
            <div class="service-panel-title">
              <i data-lucide="book-open" style="width: 18px; height: 18px; color: var(--color-primary);"></i>
              <span>Personalización de Resumen Académico</span>
            </div>
            <span class="ecosystem-pill">Google Docs + PDF</span>
          </div>
          <div class="grid-2 mb-12">
            <div class="form-group mb-0">
              <label class="form-label" for="resumenPages">Extensión del texto original</label>
              <select id="resumenPages" class="form-select">
                <option value="1 a 15 páginas">1 a 15 páginas</option>
                <option value="16 a 35 páginas" selected>16 a 35 páginas</option>
                <option value="36 a 70 páginas">36 a 70 páginas</option>
                <option value="71 a 120 páginas">71 a 120 páginas</option>
                <option value="Libro completo (120+ págs)">Libro completo (120+ págs)</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="resumenSource">Formato de tu material fuente</label>
              <select id="resumenSource" class="form-select">
                <option value="PDF digital / Enlace" selected>PDF digital / Enlace</option>
                <option value="Fotos de libro / Fotocopias">Fotos de libro / Fotocopias</option>
                <option value="Diapositivas de clase">Diapositivas de clase</option>
                <option value="Apuntes de libreta">Apuntes de libreta</option>
              </select>
            </div>
          </div>
          <div class="grid-2">
            <div class="form-group mb-0">
              <label class="form-label" for="resumenDepth">Nivel de profundidad</label>
              <select id="resumenDepth" class="form-select">
                <option value="Síntesis ejecutiva (repaso rápido en 10 min)">Síntesis ejecutiva (repaso en 10 min)</option>
                <option value="Estándar (conceptos + glosario + mapa mental)" selected>Estándar (conceptos + glosario + mapa)</option>
                <option value="Exhaustivo (autores, fechas, fórmulas y citas)">Exhaustivo (autores, fechas, fórmulas)</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="resumenGoal">Propósito del resumen</label>
              <select id="resumenGoal" class="form-select">
                <option value="Estudiar para examen" selected>Estudiar para examen</option>
                <option value="Tarea formal para entregar con carátula">Tarea formal para entregar</option>
                <option value="Apoyo para exposición">Apoyo para exposición</option>
              </select>
            </div>
          </div>
        </div>

        <!-- Panel 2: Guía de Estudio -->
        <div class="service-dynamic-panel" id="servicePanel-guia-de-estudio" style="display: none;">
          <div class="service-panel-header">
            <div class="service-panel-title">
              <i data-lucide="compass" style="width: 18px; height: 18px; color: var(--color-primary);"></i>
              <span>Personalización de Guía de Estudio</span>
            </div>
            <span class="ecosystem-pill">Google Docs + PDF</span>
          </div>
          <div class="grid-3 mb-12" style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: var(--space-12, 12px);">
            <div class="form-group mb-0">
              <label class="form-label" for="guiaDate">¿Cuándo es tu examen? *</label>
              <input type="date" id="guiaDate" class="form-input">
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="guiaTarget">Calificación objetivo</label>
              <select id="guiaTarget" class="form-select">
                <option value="10 Perfecto / Máxima nota" selected>10 Perfecto / Máxima nota</option>
                <option value="9 para asegurar promedio">9 para asegurar promedio</option>
                <option value="8+ para exentar">8+ para exentar</option>
                <option value="6+ para salvar extraordinario">6+ para salvar extraordinario</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="guiaType">Tipo de evaluación</label>
              <select id="guiaType" class="form-select">
                <option value="Examen Parcial" selected>Examen Parcial</option>
                <option value="Examen Final / Semestral">Examen Final / Semestral</option>
                <option value="Examen Extraordinario">Examen Extraordinario</option>
                <option value="Examen Departamental UNAM">Examen Departamental UNAM</option>
              </select>
            </div>
          </div>
          <div class="form-group mb-12">
            <label class="form-label" for="guiaItems">Tipo de reactivos a incluir</label>
            <select id="guiaItems" class="form-select">
              <option value="Teóricos conceptuales y explicaciones paso a paso" selected>Teóricos conceptuales y explicaciones paso a paso</option>
              <option value="Problemas prácticos resueltos con fórmulas y despejes">Problemas prácticos con fórmulas y despejes</option>
              <option value="Mixto: Teoría + Problemas + Preguntas trampa del profesor">Mixto: Teoría + Problemas + Preguntas trampa</option>
            </select>
          </div>
          <div class="form-group mb-0">
            <label class="form-label" for="guiaDifficultTopics">Temas o unidades más difíciles a enfatizar</label>
            <textarea id="guiaDifficultTopics" class="form-textarea" style="min-height: 65px;" placeholder="Ej. Unidades 2 y 3: Leyes de Newton, Termodinámica y despejes difíciles..."></textarea>
          </div>
        </div>

        <!-- Panel 3: Flashcards -->
        <div class="service-dynamic-panel" id="servicePanel-flashcards" style="display: none;">
          <div class="service-panel-header">
            <div class="service-panel-title">
              <i data-lucide="layers" style="width: 18px; height: 18px; color: var(--color-primary);"></i>
              <span>Personalización de Flashcards Activas</span>
            </div>
            <span class="ecosystem-pill">Google Sheets + Anki/Quizlet</span>
          </div>
          <div class="grid-2 mb-12">
            <div class="form-group mb-0">
              <label class="form-label" for="fcTotal">Cantidad total de flashcards</label>
              <input type="number" id="fcTotal" class="form-input" value="30" min="10" max="300" placeholder="Ej. 30">
              <span class="form-tip">Elige el total para desbloquear la distribución por nivel.</span>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="fcApp">Plataforma de estudio</label>
              <select id="fcApp" class="form-select">
                <option value="Google Sheets + Archivo Anki (.apkg)" selected>Google Sheets + Archivo Anki (.apkg)</option>
                <option value="Enlace interactivo Quizlet">Enlace interactivo Quizlet</option>
                <option value="PDF imprimible para recortar">PDF imprimible para recortar</option>
              </select>
            </div>
          </div>
          
          <label class="form-label mb-8">Distribución por Nivel de Dificultad (Suma en vivo):</label>
          <div class="grid-4-form">
            <div class="form-group mb-0">
              <label class="form-label" style="font-size: 0.78rem;" for="fcEasy">🟢 Fácil</label>
              <input type="number" id="fcEasy" class="form-input" value="10" min="0">
            </div>
            <div class="form-group mb-0">
              <label class="form-label" style="font-size: 0.78rem;" for="fcMed">🟡 Medio</label>
              <input type="number" id="fcMed" class="form-input" value="10" min="0">
            </div>
            <div class="form-group mb-0">
              <label class="form-label" style="font-size: 0.78rem;" for="fcAdv">🟠 Avanzado</label>
              <input type="number" id="fcAdv" class="form-input" value="5" min="0">
            </div>
            <div class="form-group mb-0">
              <label class="form-label" style="font-size: 0.78rem;" for="fcExp">🔴 Experto</label>
              <input type="number" id="fcExp" class="form-input" value="5" min="0">
            </div>
          </div>

          <div class="fc-counter-container">
            <span>Comprobación automática:</span>
            <div id="fcCounterBadge" class="fc-badge fc-badge-ok">✓ Exacto: 30 de 30 fichas asignadas</div>
          </div>

          <div class="form-group mt-12 mb-0">
            <label class="form-label" for="fcContent">¿Incluyen fórmulas o esquemas visuales?</label>
            <select id="fcContent" class="form-select">
              <option value="Solo conceptos y definiciones clave" selected>Solo conceptos y definiciones clave</option>
              <option value="Incluye fórmulas matemáticas / químicas">Incluye fórmulas matemáticas / químicas</option>
              <option value="Incluye diagramas y esquemas visuales">Incluye diagramas y esquemas visuales</option>
            </select>
          </div>
        </div>

        <!-- Panel 4: Examen de Práctica y Simulador -->
        <div class="service-dynamic-panel" id="servicePanel-examen-de-practica" style="display: none;">
          <div class="service-panel-header">
            <div class="service-panel-title">
              <i data-lucide="check-square" style="width: 18px; height: 18px; color: var(--color-primary);"></i>
              <span>Personalización de Examen y Simulador</span>
            </div>
            <span class="ecosystem-pill">Google Forms + Docs + PDF</span>
          </div>
          <div class="grid-3 mb-12" style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: var(--space-12, 12px);">
            <div class="form-group mb-0">
              <label class="form-label" for="simQuestionsCount">Número de reactivos</label>
              <select id="simQuestionsCount" class="form-select">
                <option value="20 reactivos">20 reactivos</option>
                <option value="30 reactivos" selected>30 reactivos</option>
                <option value="40 reactivos">40 reactivos</option>
                <option value="50+ reactivos">50+ reactivos</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="simDifficulty">Dificultad de prueba</label>
              <select id="simDifficulty" class="form-select">
                <option value="Nivel Parcial Estándar">Nivel Parcial Estándar</option>
                <option value="Nivel Exigente / Con Trampas" selected>Nivel Exigente / Con Trampas</option>
                <option value="Nivel Extraordinario / Departamental">Nivel Extraordinario / Departamental</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="simTargetGrade">Calificación meta</label>
              <select id="simTargetGrade" class="form-select">
                <option value="10 / 9 para promedio" selected>10 / 9 para promedio</option>
                <option value="8 para exentar">8 para exentar</option>
                <option value="6 para salvar materia">6 para salvar materia</option>
              </select>
            </div>
          </div>

          <div class="form-group mb-12">
            <label class="form-label" for="simMultiSubject">¿Quieres incluir más de una materia? (Opcional)</label>
            <input type="text" id="simMultiSubject" class="form-input" placeholder="Ej. 15 preguntas de Física III y 15 de Matemáticas IV (o déjalo en blanco si es solo una)">
          </div>

          <!-- Sección Sobre el Profesor -->
          <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: 12px; margin-bottom: 12px;">
            <div style="font-weight: 700; font-size: 0.86rem; color: var(--color-navy); margin-bottom: 8px; display: flex; align-items: center; gap: 6px;">
              <i data-lucide="user" style="width: 15px; height: 15px; color: var(--color-primary);"></i> Sobre tu Profesor(a) de la Prepa 4
            </div>
            <div class="grid-2">
              <div class="form-group mb-0">
                <label class="form-label" style="font-size: 0.78rem;" for="simTeacherName">Nombre del Profesor(a) (completo de preferencia)</label>
                <input type="text" id="simTeacherName" class="form-input" placeholder="Ej. Prof. Roberto García">
              </div>
              <div class="form-group mb-0">
                <label class="form-label" style="font-size: 0.78rem;" for="simTeacherStyle">Estilo o mañas de evaluación</label>
                <select id="simTeacherStyle" class="form-select">
                  <option value="Preguntas conceptuales con opciones trampa" selected>Opciones con trampas conceptuales</option>
                  <option value="Preguntas abiertas de desarrollo largo">Preguntas abiertas de desarrollo largo</option>
                  <option value="Problemas numéricos con despejes difíciles">Problemas numéricos y despejes</option>
                  <option value="Pregunta lo que dice en clase pero no está en libros">Pregunta detalles dichos en clase</option>
                  <option value="Preguntas textuales de sus diapositivas">Textual de sus diapositivas</option>
                </select>
              </div>
            </div>
          </div>

          <div class="form-group mb-0">
            <label class="form-label" for="simDate">Fecha estimada de tu examen</label>
            <input type="date" id="simDate" class="form-input">
          </div>
        </div>

        <!-- Panel 5: Corrección Académica -->
        <div class="service-dynamic-panel" id="servicePanel-correccion-academica" style="display: none;">
          <div class="service-panel-header">
            <div class="service-panel-title">
              <i data-lucide="edit-3" style="width: 18px; height: 18px; color: var(--color-primary);"></i>
              <span>Personalización de Corrección y Estilo APA</span>
            </div>
            <span class="ecosystem-pill">Google Docs + Word/Pages</span>
          </div>
          <div class="grid-2 mb-12">
            <div class="form-group mb-0">
              <label class="form-label" for="corrLength">Extensión del trabajo</label>
              <select id="corrLength" class="form-select">
                <option value="1 a 5 cuartillas">1 a 5 cuartillas</option>
                <option value="6 a 15 cuartillas" selected>6 a 15 cuartillas</option>
                <option value="16 a 30 cuartillas">16 a 30 cuartillas</option>
                <option value="31 a 60 cuartillas">31 a 60 cuartillas</option>
                <option value="Tesis / 60+ cuartillas">Tesis / 60+ cuartillas</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="corrCitation">Norma de citación requerida</label>
              <select id="corrCitation" class="form-select">
                <option value="APA 7ma edición" selected>APA 7ma edición</option>
                <option value="Vancouver">Vancouver</option>
                <option value="Chicago / Turabian">Chicago / Turabian</option>
                <option value="MLA 9na edición">MLA 9na edición</option>
                <option value="Rúbrica libre del profesor">Rúbrica libre del profesor</option>
              </select>
            </div>
          </div>
          <div class="grid-2">
            <div class="form-group mb-0">
              <label class="form-label" for="corrPriority">Prioridad de revisión</label>
              <select id="corrPriority" class="form-select">
                <option value="Ortografía, sintaxis y formato de citas APA" selected>Ortografía, sintaxis y citas APA</option>
                <option value="Coherencia argumental y estructura de párrafos">Coherencia y estructura de párrafos</option>
                <option value="Revisión integral completa">Revisión integral completa</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="corrFormat">Formato de tu borrador</label>
              <select id="corrFormat" class="form-select">
                <option value="Enlace a Google Docs" selected>Enlace a Google Docs</option>
                <option value="Archivo Microsoft Word (.docx)">Archivo Microsoft Word (.docx)</option>
                <option value="Archivo Apple Pages o PDF">Archivo Apple Pages o PDF</option>
              </select>
            </div>
          </div>
        </div>

        <!-- Panel 6: Edición Natural y Humanización -->
        <div class="service-dynamic-panel" id="servicePanel-edicion-natural" style="display: none;">
          <div class="service-panel-header">
            <div class="service-panel-title">
              <i data-lucide="feather" style="width: 18px; height: 18px; color: var(--color-primary);"></i>
              <span>Personalización de Edición Natural</span>
            </div>
            <span class="ecosystem-pill">Google Docs + Word/Pages</span>
          </div>
          <div class="grid-2 mb-12">
            <div class="form-group mb-0">
              <label class="form-label" for="editLength">Extensión del borrador</label>
              <select id="editLength" class="form-select">
                <option value="Hasta 1,500 palabras">Hasta 1,500 palabras</option>
                <option value="1,500 a 3,500 palabras" selected>1,500 a 3,500 palabras</option>
                <option value="3,500 a 7,000 palabras">3,500 a 7,000 palabras</option>
                <option value="7,000+ palabras">7,000+ palabras</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="editOrigin">Origen del texto</label>
              <select id="editOrigin" class="form-select">
                <option value="Redactado con IA y suena robótico o repetitivo" selected>Redactado con IA (suena tieso)</option>
                <option value="Borrador propio pero acartonado">Borrador propio (le falta fluidez)</option>
                <option value="Traducción literal de artículos en inglés">Traducción de inglés</option>
              </select>
            </div>
          </div>
          <div class="grid-2">
            <div class="form-group mb-0">
              <label class="form-label" for="editTone">Tono deseado</label>
              <select id="editTone" class="form-select">
                <option value="Estudiantil formal y fluido" selected>Estudiantil formal y fluido</option>
                <option value="Ensayo reflexivo / crítico">Ensayo reflexivo / crítico</option>
                <option value="Reporte científico / técnico">Reporte científico / técnico</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="editGoal">Objetivo principal</label>
              <select id="editGoal" class="form-select">
                <option value="Humanización total y eliminar fórmulas repetitivas" selected>Humanización y fluidez total</option>
                <option value="Enriquecer vocabulario sin palabras raras">Vocabulario natural y preciso</option>
              </select>
            </div>
          </div>
        </div>

        <!-- Panel 7: Diagnóstico y Mejora de Trabajo -->
        <div class="service-dynamic-panel" id="servicePanel-mejora-de-trabajo" style="display: none;">
          <div class="service-panel-header">
            <div class="service-panel-title">
              <i data-lucide="trending-up" style="width: 18px; height: 18px; color: var(--color-primary);"></i>
              <span>Personalización de Diagnóstico y Mejora</span>
            </div>
            <span class="ecosystem-pill">Google Docs + Reporte</span>
          </div>
          <div class="grid-2 mb-12">
            <div class="form-group mb-0">
              <label class="form-label" for="mejoraGoal">Meta de calificación</label>
              <select id="mejoraGoal" class="form-select">
                <option value="Subir de 7 preliminar a 9 o 10 definitivo" selected>Subir de 7 a 9 o 10 definitivo</option>
                <option value="Alinear con rúbrica exigente antes de entregar">Alinear con rúbrica exigente</option>
                <option value="Reestructuración y enriquecimiento general">Reestructuración general</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="mejoraWeak">Puntos débiles a reforzar</label>
              <select id="mejoraWeak" class="form-select">
                <option value="Marco teórico débil y fuentes dudosas (Wikipedia/blogs)" selected>Marco teórico y fuentes dudosas</option>
                <option value="Introducción y justificación flojas">Introducción y justificación</option>
                <option value="Conclusiones sin fuerza argumental">Conclusiones sin fuerza</option>
                <option value="Falta de hilo conductor entre apartados">Falta de coherencia/hilo conductor</option>
              </select>
            </div>
          </div>
          <div class="form-group mb-0">
            <label class="form-label" for="mejoraRubric">Lineamientos específicos o rúbrica de tu profesor</label>
            <textarea id="mejoraRubric" class="form-textarea" style="min-height: 65px;" placeholder="Puntos exactos que calificará el docente o comentarios que te hizo..."></textarea>
          </div>
        </div>

        <!-- Panel 8: Documento Académico Base -->
        <div class="service-dynamic-panel" id="servicePanel-documento-academico" style="display: none;">
          <div class="service-panel-header">
            <div class="service-panel-title">
              <i data-lucide="file-text" style="width: 18px; height: 18px; color: var(--color-primary);"></i>
              <span>Personalización de Documento Académico</span>
            </div>
            <span class="ecosystem-pill">Google Docs + PDF APA 7</span>
          </div>
          <div class="grid-2 mb-12">
            <div class="form-group mb-0">
              <label class="form-label" for="docType">Tipo de documento</label>
              <select id="docType" class="form-select">
                <option value="Ensayo académico formal" selected>Ensayo académico formal</option>
                <option value="Reporte de investigación / práctica">Reporte de investigación / práctica</option>
                <option value="Monografía temática">Monografía temática</option>
                <option value="Estado del arte / Marco teórico">Estado del arte / Marco teórico</option>
                <option value="Artículo de opinión fundamentado">Artículo de opinión fundamentado</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="docLength">Extensión requerida</label>
              <select id="docLength" class="form-select">
                <option value="2 a 4 cuartillas">2 a 4 cuartillas</option>
                <option value="5 a 8 cuartillas" selected>5 a 8 cuartillas</option>
                <option value="9 a 15 cuartillas">9 a 15 cuartillas</option>
                <option value="16 a 25 cuartillas">16 a 25 cuartillas</option>
              </select>
            </div>
          </div>
          <div class="form-group mb-12">
            <label class="form-label" for="docTopic">Tema delimitado y Tesis / Postura central *</label>
            <textarea id="docTopic" class="form-textarea" style="min-height: 65px;" placeholder="Ej. Título del ensayo, hipótesis a defender o preguntas guía de tu profesor..."></textarea>
          </div>
          <div class="form-group mb-0">
            <label class="form-label" for="docSources">Requisitos de fuentes bibliográficas</label>
            <select id="docSources" class="form-select">
              <option value="Mínimo 5 fuentes académicas indexadas (Scielo/Redalyc)" selected>Mínimo 5 fuentes académicas (Scielo/Redalyc)</option>
              <option value="Mínimo 10 fuentes con citas APA 7 verificables">Mínimo 10 fuentes con citas APA 7</option>
              <option value="Libros de texto UNAM y artículos seminales">Libros de texto UNAM y artículos</option>
            </select>
          </div>
        </div>

        <!-- Panel 9: Búsqueda Bibliográfica -->
        <div class="service-dynamic-panel" id="servicePanel-investigacion" style="display: none;">
          <div class="service-panel-header">
            <div class="service-panel-title">
              <i data-lucide="search" style="width: 18px; height: 18px; color: var(--color-primary);"></i>
              <span>Personalización de Búsqueda Bibliográfica</span>
            </div>
            <span class="ecosystem-pill">Google Docs + Google Sheets</span>
          </div>
          <div class="form-group mb-12">
            <label class="form-label" for="invTopic">Tema de investigación y Palabras clave *</label>
            <textarea id="invTopic" class="form-textarea" style="min-height: 65px;" placeholder="Ej. Tesis: La gentrificación en la CDMX; Palabras clave: vivienda, desplazamiento, políticas públicas..."></textarea>
          </div>
          <div class="grid-3" style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: var(--space-12, 12px);">
            <div class="form-group mb-0">
              <label class="form-label" for="invCount">Cantidad de fuentes</label>
              <select id="invCount" class="form-select">
                <option value="5 artículos / libros seminales">5 artículos/libros</option>
                <option value="10 artículos científicos indexados" selected>10 artículos indexados</option>
                <option value="15 a 20 fuentes especializadas">15 a 20 fuentes</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="invLang">Idiomas de fuentes</label>
              <select id="invLang" class="form-select">
                <option value="Solo español">Solo español</option>
                <option value="Español e Inglés" selected>Español e Inglés</option>
                <option value="Multilingüe internacional">Multilingüe</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="invDeliverable">Entregable</label>
              <select id="invDeliverable" class="form-select">
                <option value="Marco Teórico Docs + Fichas Sheets" selected>Docs + Sheets</option>
                <option value="Solo fichero bibliográfico">Solo fichero</option>
                <option value="Base Zotero / Mendeley">Base Zotero / Word</option>
              </select>
            </div>
          </div>
        </div>

        <!-- Panel 10: Presentación Visual -->
        <div class="service-dynamic-panel" id="servicePanel-presentacion" style="display: none;">
          <div class="service-panel-header">
            <div class="service-panel-title">
              <i data-lucide="layout" style="width: 18px; height: 18px; color: var(--color-primary);"></i>
              <span>Personalización de Presentación Visual</span>
            </div>
            <span class="ecosystem-pill">Google Slides + PPTX/Canva</span>
          </div>
          <div class="grid-2 mb-12">
            <div class="form-group mb-0">
              <label class="form-label" for="presSlides">Número de diapositivas</label>
              <select id="presSlides" class="form-select">
                <option value="8 a 10 diapositivas">8 a 10 láminas</option>
                <option value="12 a 15 diapositivas" selected>12 a 15 láminas</option>
                <option value="16 a 20 diapositivas">16 a 20 láminas</option>
                <option value="25+ diapositivas">25+ láminas</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="presBgStyle">Estilo de fondo y contraste *</label>
              <select id="presBgStyle" class="form-select" style="font-weight: 600; color: var(--color-navy);">
                <option value="Fondo Oscuro (Recomendado por impacto visual y modernidad)" selected>🌙 Fondo Oscuro (Recomendado)</option>
                <option value="Fondo Claro (Minimalista editorial clásico)">☀️ Fondo Claro (Editorial clásico)</option>
              </select>
            </div>
          </div>
          <div class="form-group mb-12">
            <label class="form-label" for="presTopic">Tema bien segmentado y delimitado *</label>
            <input type="text" id="presTopic" class="form-input" placeholder="Ej. Factores de mortalidad acelerada en las tortugas marinas del Pacífico">
            <span class="form-tip">💡 <strong>Consejo Encardomy:</strong> Evita temas genéricos como <em>'Las tortugas'</em>; segmenta el enfoque para causar mayor impacto en tu exposición.</span>
          </div>
          <div class="grid-2">
            <div class="form-group mb-0">
              <label class="form-label" for="presNotes">¿Notas del orador (guion de qué decir)?</label>
              <select id="presNotes" class="form-select">
                <option value="Sí, incluir guion detallado de exposición debajo de cada lámina" selected>Sí, guion de qué decir (Recomendado)</option>
                <option value="Solo diapositivas limpias con puntos clave">Solo diapositivas limpias</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="presApp">Herramienta de entrega</label>
              <select id="presApp" class="form-select">
                <option value="Google Slides editable + PDF de proyección" selected>Google Slides editable + PDF</option>
                <option value="Plantilla en Canva con enlace editable">Plantilla Canva editable</option>
                <option value="Microsoft PowerPoint (.pptx)">Microsoft PowerPoint (.pptx)</option>
              </select>
            </div>
          </div>
        </div>

        <!-- Panel 11: Infografía -->
        <div class="service-dynamic-panel" id="servicePanel-infografia" style="display: none;">
          <div class="service-panel-header">
            <div class="service-panel-title">
              <i data-lucide="pie-chart" style="width: 18px; height: 18px; color: var(--color-primary);"></i>
              <span>Personalización de Infografía y Esquemas</span>
            </div>
            <span class="ecosystem-pill">Google Drawings/Canva + PNG 4K</span>
          </div>
          <div class="grid-2 mb-12">
            <div class="form-group mb-0">
              <label class="form-label" for="infoPalette">Paleta de colores principal *</label>
              <select id="infoPalette" class="form-select" style="font-weight: 600;">
                <option value="Azul Eléctrico & Marino Encardomy (#2D7FF9, #123B6A)" selected>🎨 Azul Eléctrico & Marino Encardomy (Recomendada)</option>
                <option value="Formal Académico (Azul pizarra, grafito y menta)">Formal Académico (Pizarra y Menta)</option>
                <option value="Tonos Cálidos Dinámicos (Ámbar, terracota y blanco)">Tonos Cálidos (Ámbar y Terracota)</option>
                <option value="Minimalista Monocromático de Alto Contraste">Minimalista Monocromático</option>
                <option value="Personalizada según materia escolar">Personalizada según materia</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="infoOrient">Orientación y formato</label>
              <select id="infoOrient" class="form-select">
                <option value="Póster vertical (Carta / Tabloide para imprimir)" selected>Póster vertical (Carta / Tabloide)</option>
                <option value="Lámina horizontal 16:9 para diapositiva">Horizontal 16:9 (Presentación)</option>
                <option value="Formato vertical / cuadrado para celular">Vertical para celular</option>
              </select>
            </div>
          </div>
          <div class="form-group mb-0">
            <label class="form-label" for="infoType">Tipo de representación visual</label>
            <select id="infoType" class="form-select">
              <option value="Proceso paso a paso / Diagrama de flujo" selected>Proceso paso a paso / Diagrama de flujo</option>
              <option value="Línea de tiempo histórica y cronología">Línea de tiempo histórica</option>
              <option value="Cuadro comparativo visual de conceptos">Cuadro comparativo de conceptos</option>
              <option value="Gráficos estadísticos y síntesis de datos">Gráficos estadísticos y datos</option>
            </select>
          </div>
        </div>

        <!-- Panel 12: Proyecto Encardomy -->
        <div class="service-dynamic-panel" id="servicePanel-proyecto-encardomy" style="display: none;">
          <div class="service-panel-header">
            <div class="service-panel-title">
              <i data-lucide="briefcase" style="width: 18px; height: 18px; color: var(--color-primary);"></i>
              <span>Personalización de Proyecto Semestral</span>
            </div>
            <span class="ecosystem-pill">Suite Google Workspace Completa</span>
          </div>
          <div class="grid-2 mb-12">
            <div class="form-group mb-0">
              <label class="form-label" for="projType">Tipo de proyecto</label>
              <select id="projType" class="form-select">
                <option value="Trabajo Integrador Semestral" selected>Trabajo Integrador Semestral</option>
                <option value="Proyecto de Titulación / Práctica Técnica">Proyecto de Titulación / Práctica</option>
                <option value="Proyecto de Feria de las Ciencias UNAM">Proyecto de Feria de las Ciencias</option>
                <option value="Tesina / Monografía extensa">Tesina / Monografía extensa</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="projStage">Fase o avance actual</label>
              <select id="projStage" class="form-select">
                <option value="Desde cero (definición de tema y objetivos)" selected>Desde cero (tema y objetivos)</option>
                <option value="Esquema y marco teórico en proceso">Esquema y marco en proceso</option>
                <option value="Borrador avanzado que requiere pulido">Borrador avanzado a pulir</option>
              </select>
            </div>
          </div>
          <div class="form-group mb-12">
            <label class="form-label" for="projDeadlines">Fechas de entregas parciales y entrega final</label>
            <input type="text" id="projDeadlines" class="form-input" placeholder="Ej. Primer avance 15 Octubre, Segundo 30 Octubre, Entrega final 15 Noviembre">
          </div>
          <div class="form-group mb-0">
            <label class="form-label" for="projRubric">Rúbrica oficial o lineamientos de los profesores de la Prepa 4</label>
            <textarea id="projRubric" class="form-textarea" style="min-height: 65px;" placeholder="Puntos específicos que exigen los profesores del colegio/academia..."></textarea>
          </div>
        </div>

        <!-- 5. Tiempo de entrega -->
        <div class="form-group mb-16">
          <label class="form-label" for="orderUrgencySelect">Tiempo de entrega deseado</label>
          <select id="orderUrgencySelect" class="form-select">
            <option value="Estándar (24 a 48 horas)" selected>Estándar (24 a 48 horas)</option>
            <option value="Express urgente (Menos de 12 a 24 horas)">Express urgente (Menos de 12 a 24 horas)</option>
            <option value="Con calma (3 a 5 días hábiles)">Con calma (3 a 5 días hábiles)</option>
          </select>
        </div>

        <!-- 6. Notas generales y enlaces -->
        <div class="form-group mb-20">
          <label class="form-label" for="orderDetailsInput">Notas adicionales o enlace a tu carpeta de Google Drive (Opcional)</label>
          <textarea id="orderDetailsInput" class="form-textarea" style="min-height: 65px;" placeholder="Ej. Ya subí los archivos a Google Drive, o indicación especial de tu profesor..."></textarea>
        </div>

        <!-- 7. Botón de Envío -->
        <button type="submit" id="sendWhatsAppBtn" class="btn btn-primary btn-block btn-lg">
          <i data-lucide="message-circle"></i>
          <span>Enviar Cotización a WhatsApp (+52 55 7198 5641)</span>
        </button>

                        <div style="text-align: center; margin-top: 10px; font-size: 0.78rem; color: var(--color-text-muted);">
          🔒 Tus datos están protegidos. Al solicitar tu cotización aceptas nuestro <a href="../privacidad.html" target="_blank" style="text-decoration: underline; color: var(--color-primary); font-weight: 600;">Aviso de Privacidad</a> y la <a href="../propiedad-intelectual.html" target="_blank" style="text-decoration: underline; color: var(--color-primary); font-weight: 600;">Política de Propiedad Intelectual</a>.
        </div>
      </form>
    </div>
  </div>

        <!-- 2. Grado, Grupo y Sección (Lógica Dependiente) -->
        <div class="grid-3 mb-16" style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: var(--space-12, 12px);">
          <div class="form-group mb-0">
            <label class="form-label" for="orderGradeSelect">Grado Escolar *</label>
            <select id="orderGradeSelect" class="form-select" required>
              <option value="" disabled selected>Elige tu grado</option>
              <option value="4">4° Cuarto Año</option>
              <option value="5">5° Quinto Año</option>
              <option value="6">6° Sexto Año</option>
            </select>
          </div>
          <div class="form-group mb-0">
            <label class="form-label" for="orderGroupSelect">Grupo *</label>
            <select id="orderGroupSelect" class="form-select" required disabled>
              <option value="" disabled selected>Primero elige grado</option>
            </select>
          </div>
          <div class="form-group mb-0">
            <label class="form-label" for="orderSectionSelect">Sección *</label>
            <select id="orderSectionSelect" class="form-select" required>
              <option value="" disabled selected>Sección</option>
              <option value="Sección A">Sección A</option>
              <option value="Sección B">Sección B</option>
            </select>
          </div>
        </div>

        <!-- 3. Materia Oficial de la ENP 4 -->
        <div class="form-group mb-16">
          <label class="form-label" for="orderSubjectSelect">Materia Oficial de la ENP 4 *</label>
          <select id="orderSubjectSelect" class="form-select" required disabled>
            <option value="" disabled selected>Primero elige tu grado escolar (4°, 5° o 6°)</option>
          </select>
          <div id="customSubjectWrapper" style="display: none; margin-top: 8px;">
            <label class="form-label" for="orderCustomSubjectInput" style="font-size: 0.82rem; color: var(--color-primary);">Especifica el nombre de tu materia:</label>
            <input type="text" id="orderCustomSubjectInput" class="form-input" placeholder="Ej. Taller de Expresión Gráfica o Materia Optativa...">
          </div>
        </div>

        <!-- 4. Servicio Principal -->
        <div class="form-group mb-16">
          <label class="form-label" for="orderServiceSelect">Servicio que necesitas *</label>
          <select id="orderServiceSelect" class="form-select" required>
            <optgroup label="Estudiar">
              <option value="resumen">Resumen Académico Estructurado</option>
              <option value="guia-de-estudio">Guía de Estudio Integral</option>
              <option value="flashcards">Flashcards de Repetición Espaciada</option>
              <option value="examen-de-practica">Examen de Práctica y Simulador</option>
            </optgroup>
            <optgroup label="Mejorar">
              <option value="correccion-academica">Corrección Académica y Normas APA</option>
              <option value="edicion-natural">Edición Natural y Humanización</option>
              <option value="mejora-de-trabajo">Diagnóstico y Mejora de Borrador</option>
            </optgroup>
            <optgroup label="Crear">
              <option value="documento-academico">Documento Académico Base</option>
              <option value="investigacion">Búsqueda Bibliográfica y Marco Teórico</option>
            </optgroup>
            <optgroup label="Diseñar">
              <option value="presentacion">Diseño de Presentación Visual (Google Slides)</option>
              <option value="infografia">Infografía y Esquemas Visuales</option>
            </optgroup>
            <optgroup label="Proyectos">
              <option value="proyecto-encardomy">Proyecto Encardomy Semestral</option>
            </optgroup>
          </select>
        </div>

        <!-- ==================================================================
             PANELES DINÁMICOS Y PERSONALIZADOS POR CADA SERVICIO
             ================================================================== -->

        <!-- Panel 1: Resumen -->
        <div class="service-dynamic-panel" id="servicePanel-resumen" style="display: block;">
          <div class="service-panel-header">
            <div class="service-panel-title">
              <i data-lucide="book-open" style="width: 18px; height: 18px; color: var(--color-primary);"></i>
              <span>Personalización de Resumen Académico</span>
            </div>
            <span class="ecosystem-pill">Google Docs + PDF</span>
          </div>
          <div class="grid-2 mb-12">
            <div class="form-group mb-0">
              <label class="form-label" for="resumenPages">Extensión del texto original</label>
              <select id="resumenPages" class="form-select">
                <option value="1 a 15 páginas">1 a 15 páginas</option>
                <option value="16 a 35 páginas" selected>16 a 35 páginas</option>
                <option value="36 a 70 páginas">36 a 70 páginas</option>
                <option value="71 a 120 páginas">71 a 120 páginas</option>
                <option value="Libro completo (120+ págs)">Libro completo (120+ págs)</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="resumenSource">Formato de tu material fuente</label>
              <select id="resumenSource" class="form-select">
                <option value="PDF digital / Enlace" selected>PDF digital / Enlace</option>
                <option value="Fotos de libro / Fotocopias">Fotos de libro / Fotocopias</option>
                <option value="Diapositivas de clase">Diapositivas de clase</option>
                <option value="Apuntes de libreta">Apuntes de libreta</option>
              </select>
            </div>
          </div>
          <div class="grid-2">
            <div class="form-group mb-0">
              <label class="form-label" for="resumenDepth">Nivel de profundidad</label>
              <select id="resumenDepth" class="form-select">
                <option value="Síntesis ejecutiva (repaso rápido en 10 min)">Síntesis ejecutiva (repaso en 10 min)</option>
                <option value="Estándar (conceptos + glosario + mapa mental)" selected>Estándar (conceptos + glosario + mapa)</option>
                <option value="Exhaustivo (autores, fechas, fórmulas y citas)">Exhaustivo (autores, fechas, fórmulas)</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="resumenGoal">Propósito del resumen</label>
              <select id="resumenGoal" class="form-select">
                <option value="Estudiar para examen" selected>Estudiar para examen</option>
                <option value="Tarea formal para entregar con carátula">Tarea formal para entregar</option>
                <option value="Apoyo para exposición">Apoyo para exposición</option>
              </select>
            </div>
          </div>
        </div>

        <!-- Panel 2: Guía de Estudio -->
        <div class="service-dynamic-panel" id="servicePanel-guia-de-estudio" style="display: none;">
          <div class="service-panel-header">
            <div class="service-panel-title">
              <i data-lucide="compass" style="width: 18px; height: 18px; color: var(--color-primary);"></i>
              <span>Personalización de Guía de Estudio</span>
            </div>
            <span class="ecosystem-pill">Google Docs + PDF</span>
          </div>
          <div class="grid-3 mb-12" style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: var(--space-12, 12px);">
            <div class="form-group mb-0">
              <label class="form-label" for="guiaDate">¿Cuándo es tu examen? *</label>
              <input type="date" id="guiaDate" class="form-input">
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="guiaTarget">Calificación objetivo</label>
              <select id="guiaTarget" class="form-select">
                <option value="10 Perfecto / Máxima nota" selected>10 Perfecto / Máxima nota</option>
                <option value="9 para asegurar promedio">9 para asegurar promedio</option>
                <option value="8+ para exentar">8+ para exentar</option>
                <option value="6+ para salvar extraordinario">6+ para salvar extraordinario</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="guiaType">Tipo de evaluación</label>
              <select id="guiaType" class="form-select">
                <option value="Examen Parcial" selected>Examen Parcial</option>
                <option value="Examen Final / Semestral">Examen Final / Semestral</option>
                <option value="Examen Extraordinario">Examen Extraordinario</option>
                <option value="Examen Departamental UNAM">Examen Departamental UNAM</option>
              </select>
            </div>
          </div>
          <div class="form-group mb-12">
            <label class="form-label" for="guiaItems">Tipo de reactivos a incluir</label>
            <select id="guiaItems" class="form-select">
              <option value="Teóricos conceptuales y explicaciones paso a paso" selected>Teóricos conceptuales y explicaciones paso a paso</option>
              <option value="Problemas prácticos resueltos con fórmulas y despejes">Problemas prácticos con fórmulas y despejes</option>
              <option value="Mixto: Teoría + Problemas + Preguntas trampa del profesor">Mixto: Teoría + Problemas + Preguntas trampa</option>
            </select>
          </div>
          <div class="form-group mb-0">
            <label class="form-label" for="guiaDifficultTopics">Temas o unidades más difíciles a enfatizar</label>
            <textarea id="guiaDifficultTopics" class="form-textarea" style="min-height: 65px;" placeholder="Ej. Unidades 2 y 3: Leyes de Newton, Termodinámica y despejes difíciles..."></textarea>
          </div>
        </div>

        <!-- Panel 3: Flashcards -->
        <div class="service-dynamic-panel" id="servicePanel-flashcards" style="display: none;">
          <div class="service-panel-header">
            <div class="service-panel-title">
              <i data-lucide="layers" style="width: 18px; height: 18px; color: var(--color-primary);"></i>
              <span>Personalización de Flashcards Activas</span>
            </div>
            <span class="ecosystem-pill">Google Sheets + Anki/Quizlet</span>
          </div>
          <div class="grid-2 mb-12">
            <div class="form-group mb-0">
              <label class="form-label" for="fcTotal">Cantidad total de flashcards</label>
              <input type="number" id="fcTotal" class="form-input" value="30" min="10" max="300" placeholder="Ej. 30">
              <span class="form-tip">Elige el total para desbloquear la distribución por nivel.</span>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="fcApp">Plataforma de estudio</label>
              <select id="fcApp" class="form-select">
                <option value="Google Sheets + Archivo Anki (.apkg)" selected>Google Sheets + Archivo Anki (.apkg)</option>
                <option value="Enlace interactivo Quizlet">Enlace interactivo Quizlet</option>
                <option value="PDF imprimible para recortar">PDF imprimible para recortar</option>
              </select>
            </div>
          </div>
          
          <label class="form-label mb-8">Distribución por Nivel de Dificultad (Suma en vivo):</label>
          <div class="grid-4-form">
            <div class="form-group mb-0">
              <label class="form-label" style="font-size: 0.78rem;" for="fcEasy">🟢 Fácil</label>
              <input type="number" id="fcEasy" class="form-input" value="10" min="0">
            </div>
            <div class="form-group mb-0">
              <label class="form-label" style="font-size: 0.78rem;" for="fcMed">🟡 Medio</label>
              <input type="number" id="fcMed" class="form-input" value="10" min="0">
            </div>
            <div class="form-group mb-0">
              <label class="form-label" style="font-size: 0.78rem;" for="fcAdv">🟠 Avanzado</label>
              <input type="number" id="fcAdv" class="form-input" value="5" min="0">
            </div>
            <div class="form-group mb-0">
              <label class="form-label" style="font-size: 0.78rem;" for="fcExp">🔴 Experto</label>
              <input type="number" id="fcExp" class="form-input" value="5" min="0">
            </div>
          </div>

          <div class="fc-counter-container">
            <span>Comprobación automática:</span>
            <div id="fcCounterBadge" class="fc-badge fc-badge-ok">✓ Exacto: 30 de 30 fichas asignadas</div>
          </div>

          <div class="form-group mt-12 mb-0">
            <label class="form-label" for="fcContent">¿Incluyen fórmulas o esquemas visuales?</label>
            <select id="fcContent" class="form-select">
              <option value="Solo conceptos y definiciones clave" selected>Solo conceptos y definiciones clave</option>
              <option value="Incluye fórmulas matemáticas / químicas">Incluye fórmulas matemáticas / químicas</option>
              <option value="Incluye diagramas y esquemas visuales">Incluye diagramas y esquemas visuales</option>
            </select>
          </div>
        </div>

        <!-- Panel 4: Examen de Práctica y Simulador -->
        <div class="service-dynamic-panel" id="servicePanel-examen-de-practica" style="display: none;">
          <div class="service-panel-header">
            <div class="service-panel-title">
              <i data-lucide="check-square" style="width: 18px; height: 18px; color: var(--color-primary);"></i>
              <span>Personalización de Examen y Simulador</span>
            </div>
            <span class="ecosystem-pill">Google Forms + Docs + PDF</span>
          </div>
          <div class="grid-3 mb-12" style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: var(--space-12, 12px);">
            <div class="form-group mb-0">
              <label class="form-label" for="simQuestionsCount">Número de reactivos</label>
              <select id="simQuestionsCount" class="form-select">
                <option value="20 reactivos">20 reactivos</option>
                <option value="30 reactivos" selected>30 reactivos</option>
                <option value="40 reactivos">40 reactivos</option>
                <option value="50+ reactivos">50+ reactivos</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="simDifficulty">Dificultad de prueba</label>
              <select id="simDifficulty" class="form-select">
                <option value="Nivel Parcial Estándar">Nivel Parcial Estándar</option>
                <option value="Nivel Exigente / Con Trampas" selected>Nivel Exigente / Con Trampas</option>
                <option value="Nivel Extraordinario / Departamental">Nivel Extraordinario / Departamental</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="simTargetGrade">Calificación meta</label>
              <select id="simTargetGrade" class="form-select">
                <option value="10 / 9 para promedio" selected>10 / 9 para promedio</option>
                <option value="8 para exentar">8 para exentar</option>
                <option value="6 para salvar materia">6 para salvar materia</option>
              </select>
            </div>
          </div>

          <div class="form-group mb-12">
            <label class="form-label" for="simMultiSubject">¿Quieres incluir más de una materia? (Opcional)</label>
            <input type="text" id="simMultiSubject" class="form-input" placeholder="Ej. 15 preguntas de Física III y 15 de Matemáticas IV (o déjalo en blanco si es solo una)">
          </div>

          <!-- Sección Sobre el Profesor -->
          <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: 12px; margin-bottom: 12px;">
            <div style="font-weight: 700; font-size: 0.86rem; color: var(--color-navy); margin-bottom: 8px; display: flex; align-items: center; gap: 6px;">
              <i data-lucide="user" style="width: 15px; height: 15px; color: var(--color-primary);"></i> Sobre tu Profesor(a) de la Prepa 4
            </div>
            <div class="grid-2">
              <div class="form-group mb-0">
                <label class="form-label" style="font-size: 0.78rem;" for="simTeacherName">Nombre del Profesor(a) (completo de preferencia)</label>
                <input type="text" id="simTeacherName" class="form-input" placeholder="Ej. Prof. Roberto García">
              </div>
              <div class="form-group mb-0">
                <label class="form-label" style="font-size: 0.78rem;" for="simTeacherStyle">Estilo o mañas de evaluación</label>
                <select id="simTeacherStyle" class="form-select">
                  <option value="Preguntas conceptuales con opciones trampa" selected>Opciones con trampas conceptuales</option>
                  <option value="Preguntas abiertas de desarrollo largo">Preguntas abiertas de desarrollo largo</option>
                  <option value="Problemas numéricos con despejes difíciles">Problemas numéricos y despejes</option>
                  <option value="Pregunta lo que dice en clase pero no está en libros">Pregunta detalles dichos en clase</option>
                  <option value="Preguntas textuales de sus diapositivas">Textual de sus diapositivas</option>
                </select>
              </div>
            </div>
          </div>

          <div class="form-group mb-0">
            <label class="form-label" for="simDate">Fecha estimada de tu examen</label>
            <input type="date" id="simDate" class="form-input">
          </div>
        </div>

        <!-- Panel 5: Corrección Académica -->
        <div class="service-dynamic-panel" id="servicePanel-correccion-academica" style="display: none;">
          <div class="service-panel-header">
            <div class="service-panel-title">
              <i data-lucide="edit-3" style="width: 18px; height: 18px; color: var(--color-primary);"></i>
              <span>Personalización de Corrección y Estilo APA</span>
            </div>
            <span class="ecosystem-pill">Google Docs + Word/Pages</span>
          </div>
          <div class="grid-2 mb-12">
            <div class="form-group mb-0">
              <label class="form-label" for="corrLength">Extensión del trabajo</label>
              <select id="corrLength" class="form-select">
                <option value="1 a 5 cuartillas">1 a 5 cuartillas</option>
                <option value="6 a 15 cuartillas" selected>6 a 15 cuartillas</option>
                <option value="16 a 30 cuartillas">16 a 30 cuartillas</option>
                <option value="31 a 60 cuartillas">31 a 60 cuartillas</option>
                <option value="Tesis / 60+ cuartillas">Tesis / 60+ cuartillas</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="corrCitation">Norma de citación requerida</label>
              <select id="corrCitation" class="form-select">
                <option value="APA 7ma edición" selected>APA 7ma edición</option>
                <option value="Vancouver">Vancouver</option>
                <option value="Chicago / Turabian">Chicago / Turabian</option>
                <option value="MLA 9na edición">MLA 9na edición</option>
                <option value="Rúbrica libre del profesor">Rúbrica libre del profesor</option>
              </select>
            </div>
          </div>
          <div class="grid-2">
            <div class="form-group mb-0">
              <label class="form-label" for="corrPriority">Prioridad de revisión</label>
              <select id="corrPriority" class="form-select">
                <option value="Ortografía, sintaxis y formato de citas APA" selected>Ortografía, sintaxis y citas APA</option>
                <option value="Coherencia argumental y estructura de párrafos">Coherencia y estructura de párrafos</option>
                <option value="Revisión integral completa">Revisión integral completa</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="corrFormat">Formato de tu borrador</label>
              <select id="corrFormat" class="form-select">
                <option value="Enlace a Google Docs" selected>Enlace a Google Docs</option>
                <option value="Archivo Microsoft Word (.docx)">Archivo Microsoft Word (.docx)</option>
                <option value="Archivo Apple Pages o PDF">Archivo Apple Pages o PDF</option>
              </select>
            </div>
          </div>
        </div>

        <!-- Panel 6: Edición Natural y Humanización -->
        <div class="service-dynamic-panel" id="servicePanel-edicion-natural" style="display: none;">
          <div class="service-panel-header">
            <div class="service-panel-title">
              <i data-lucide="feather" style="width: 18px; height: 18px; color: var(--color-primary);"></i>
              <span>Personalización de Edición Natural</span>
            </div>
            <span class="ecosystem-pill">Google Docs + Word/Pages</span>
          </div>
          <div class="grid-2 mb-12">
            <div class="form-group mb-0">
              <label class="form-label" for="editLength">Extensión del borrador</label>
              <select id="editLength" class="form-select">
                <option value="Hasta 1,500 palabras">Hasta 1,500 palabras</option>
                <option value="1,500 a 3,500 palabras" selected>1,500 a 3,500 palabras</option>
                <option value="3,500 a 7,000 palabras">3,500 a 7,000 palabras</option>
                <option value="7,000+ palabras">7,000+ palabras</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="editOrigin">Origen del texto</label>
              <select id="editOrigin" class="form-select">
                <option value="Redactado con IA y suena robótico o repetitivo" selected>Redactado con IA (suena tieso)</option>
                <option value="Borrador propio pero acartonado">Borrador propio (le falta fluidez)</option>
                <option value="Traducción literal de artículos en inglés">Traducción de inglés</option>
              </select>
            </div>
          </div>
          <div class="grid-2">
            <div class="form-group mb-0">
              <label class="form-label" for="editTone">Tono deseado</label>
              <select id="editTone" class="form-select">
                <option value="Estudiantil formal y fluido" selected>Estudiantil formal y fluido</option>
                <option value="Ensayo reflexivo / crítico">Ensayo reflexivo / crítico</option>
                <option value="Reporte científico / técnico">Reporte científico / técnico</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="editGoal">Objetivo principal</label>
              <select id="editGoal" class="form-select">
                <option value="Humanización total y eliminar fórmulas repetitivas" selected>Humanización y fluidez total</option>
                <option value="Enriquecer vocabulario sin palabras raras">Vocabulario natural y preciso</option>
              </select>
            </div>
          </div>
        </div>

        <!-- Panel 7: Diagnóstico y Mejora de Trabajo -->
        <div class="service-dynamic-panel" id="servicePanel-mejora-de-trabajo" style="display: none;">
          <div class="service-panel-header">
            <div class="service-panel-title">
              <i data-lucide="trending-up" style="width: 18px; height: 18px; color: var(--color-primary);"></i>
              <span>Personalización de Diagnóstico y Mejora</span>
            </div>
            <span class="ecosystem-pill">Google Docs + Reporte</span>
          </div>
          <div class="grid-2 mb-12">
            <div class="form-group mb-0">
              <label class="form-label" for="mejoraGoal">Meta de calificación</label>
              <select id="mejoraGoal" class="form-select">
                <option value="Subir de 7 preliminar a 9 o 10 definitivo" selected>Subir de 7 a 9 o 10 definitivo</option>
                <option value="Alinear con rúbrica exigente antes de entregar">Alinear con rúbrica exigente</option>
                <option value="Reestructuración y enriquecimiento general">Reestructuración general</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="mejoraWeak">Puntos débiles a reforzar</label>
              <select id="mejoraWeak" class="form-select">
                <option value="Marco teórico débil y fuentes dudosas (Wikipedia/blogs)" selected>Marco teórico y fuentes dudosas</option>
                <option value="Introducción y justificación flojas">Introducción y justificación</option>
                <option value="Conclusiones sin fuerza argumental">Conclusiones sin fuerza</option>
                <option value="Falta de hilo conductor entre apartados">Falta de coherencia/hilo conductor</option>
              </select>
            </div>
          </div>
          <div class="form-group mb-0">
            <label class="form-label" for="mejoraRubric">Lineamientos específicos o rúbrica de tu profesor</label>
            <textarea id="mejoraRubric" class="form-textarea" style="min-height: 65px;" placeholder="Puntos exactos que calificará el docente o comentarios que te hizo..."></textarea>
          </div>
        </div>

        <!-- Panel 8: Documento Académico Base -->
        <div class="service-dynamic-panel" id="servicePanel-documento-academico" style="display: none;">
          <div class="service-panel-header">
            <div class="service-panel-title">
              <i data-lucide="file-text" style="width: 18px; height: 18px; color: var(--color-primary);"></i>
              <span>Personalización de Documento Académico</span>
            </div>
            <span class="ecosystem-pill">Google Docs + PDF APA 7</span>
          </div>
          <div class="grid-2 mb-12">
            <div class="form-group mb-0">
              <label class="form-label" for="docType">Tipo de documento</label>
              <select id="docType" class="form-select">
                <option value="Ensayo académico formal" selected>Ensayo académico formal</option>
                <option value="Reporte de investigación / práctica">Reporte de investigación / práctica</option>
                <option value="Monografía temática">Monografía temática</option>
                <option value="Estado del arte / Marco teórico">Estado del arte / Marco teórico</option>
                <option value="Artículo de opinión fundamentado">Artículo de opinión fundamentado</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="docLength">Extensión requerida</label>
              <select id="docLength" class="form-select">
                <option value="2 a 4 cuartillas">2 a 4 cuartillas</option>
                <option value="5 a 8 cuartillas" selected>5 a 8 cuartillas</option>
                <option value="9 a 15 cuartillas">9 a 15 cuartillas</option>
                <option value="16 a 25 cuartillas">16 a 25 cuartillas</option>
              </select>
            </div>
          </div>
          <div class="form-group mb-12">
            <label class="form-label" for="docTopic">Tema delimitado y Tesis / Postura central *</label>
            <textarea id="docTopic" class="form-textarea" style="min-height: 65px;" placeholder="Ej. Título del ensayo, hipótesis a defender o preguntas guía de tu profesor..."></textarea>
          </div>
          <div class="form-group mb-0">
            <label class="form-label" for="docSources">Requisitos de fuentes bibliográficas</label>
            <select id="docSources" class="form-select">
              <option value="Mínimo 5 fuentes académicas indexadas (Scielo/Redalyc)" selected>Mínimo 5 fuentes académicas (Scielo/Redalyc)</option>
              <option value="Mínimo 10 fuentes con citas APA 7 verificables">Mínimo 10 fuentes con citas APA 7</option>
              <option value="Libros de texto UNAM y artículos seminales">Libros de texto UNAM y artículos</option>
            </select>
          </div>
        </div>

        <!-- Panel 9: Búsqueda Bibliográfica -->
        <div class="service-dynamic-panel" id="servicePanel-investigacion" style="display: none;">
          <div class="service-panel-header">
            <div class="service-panel-title">
              <i data-lucide="search" style="width: 18px; height: 18px; color: var(--color-primary);"></i>
              <span>Personalización de Búsqueda Bibliográfica</span>
            </div>
            <span class="ecosystem-pill">Google Docs + Google Sheets</span>
          </div>
          <div class="form-group mb-12">
            <label class="form-label" for="invTopic">Tema de investigación y Palabras clave *</label>
            <textarea id="invTopic" class="form-textarea" style="min-height: 65px;" placeholder="Ej. Tesis: La gentrificación en la CDMX; Palabras clave: vivienda, desplazamiento, políticas públicas..."></textarea>
          </div>
          <div class="grid-3" style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: var(--space-12, 12px);">
            <div class="form-group mb-0">
              <label class="form-label" for="invCount">Cantidad de fuentes</label>
              <select id="invCount" class="form-select">
                <option value="5 artículos / libros seminales">5 artículos/libros</option>
                <option value="10 artículos científicos indexados" selected>10 artículos indexados</option>
                <option value="15 a 20 fuentes especializadas">15 a 20 fuentes</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="invLang">Idiomas de fuentes</label>
              <select id="invLang" class="form-select">
                <option value="Solo español">Solo español</option>
                <option value="Español e Inglés" selected>Español e Inglés</option>
                <option value="Multilingüe internacional">Multilingüe</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="invDeliverable">Entregable</label>
              <select id="invDeliverable" class="form-select">
                <option value="Marco Teórico Docs + Fichas Sheets" selected>Docs + Sheets</option>
                <option value="Solo fichero bibliográfico">Solo fichero</option>
                <option value="Base Zotero / Mendeley">Base Zotero / Word</option>
              </select>
            </div>
          </div>
        </div>

        <!-- Panel 10: Presentación Visual -->
        <div class="service-dynamic-panel" id="servicePanel-presentacion" style="display: none;">
          <div class="service-panel-header">
            <div class="service-panel-title">
              <i data-lucide="layout" style="width: 18px; height: 18px; color: var(--color-primary);"></i>
              <span>Personalización de Presentación Visual</span>
            </div>
            <span class="ecosystem-pill">Google Slides + PPTX/Canva</span>
          </div>
          <div class="grid-2 mb-12">
            <div class="form-group mb-0">
              <label class="form-label" for="presSlides">Número de diapositivas</label>
              <select id="presSlides" class="form-select">
                <option value="8 a 10 diapositivas">8 a 10 láminas</option>
                <option value="12 a 15 diapositivas" selected>12 a 15 láminas</option>
                <option value="16 a 20 diapositivas">16 a 20 láminas</option>
                <option value="25+ diapositivas">25+ láminas</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="presBgStyle">Estilo de fondo y contraste *</label>
              <select id="presBgStyle" class="form-select" style="font-weight: 600; color: var(--color-navy);">
                <option value="Fondo Oscuro (Recomendado por impacto visual y modernidad)" selected>🌙 Fondo Oscuro (Recomendado)</option>
                <option value="Fondo Claro (Minimalista editorial clásico)">☀️ Fondo Claro (Editorial clásico)</option>
              </select>
            </div>
          </div>
          <div class="form-group mb-12">
            <label class="form-label" for="presTopic">Tema bien segmentado y delimitado *</label>
            <input type="text" id="presTopic" class="form-input" placeholder="Ej. Factores de mortalidad acelerada en las tortugas marinas del Pacífico">
            <span class="form-tip">💡 <strong>Consejo Encardomy:</strong> Evita temas genéricos como <em>'Las tortugas'</em>; segmenta el enfoque para causar mayor impacto en tu exposición.</span>
          </div>
          <div class="grid-2">
            <div class="form-group mb-0">
              <label class="form-label" for="presNotes">¿Notas del orador (guion de qué decir)?</label>
              <select id="presNotes" class="form-select">
                <option value="Sí, incluir guion detallado de exposición debajo de cada lámina" selected>Sí, guion de qué decir (Recomendado)</option>
                <option value="Solo diapositivas limpias con puntos clave">Solo diapositivas limpias</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="presApp">Herramienta de entrega</label>
              <select id="presApp" class="form-select">
                <option value="Google Slides editable + PDF de proyección" selected>Google Slides editable + PDF</option>
                <option value="Plantilla en Canva con enlace editable">Plantilla Canva editable</option>
                <option value="Microsoft PowerPoint (.pptx)">Microsoft PowerPoint (.pptx)</option>
              </select>
            </div>
          </div>
        </div>

        <!-- Panel 11: Infografía -->
        <div class="service-dynamic-panel" id="servicePanel-infografia" style="display: none;">
          <div class="service-panel-header">
            <div class="service-panel-title">
              <i data-lucide="pie-chart" style="width: 18px; height: 18px; color: var(--color-primary);"></i>
              <span>Personalización de Infografía y Esquemas</span>
            </div>
            <span class="ecosystem-pill">Google Drawings/Canva + PNG 4K</span>
          </div>
          <div class="grid-2 mb-12">
            <div class="form-group mb-0">
              <label class="form-label" for="infoPalette">Paleta de colores principal *</label>
              <select id="infoPalette" class="form-select" style="font-weight: 600;">
                <option value="Azul Eléctrico & Marino Encardomy (#2D7FF9, #123B6A)" selected>🎨 Azul Eléctrico & Marino Encardomy (Recomendada)</option>
                <option value="Formal Académico (Azul pizarra, grafito y menta)">Formal Académico (Pizarra y Menta)</option>
                <option value="Tonos Cálidos Dinámicos (Ámbar, terracota y blanco)">Tonos Cálidos (Ámbar y Terracota)</option>
                <option value="Minimalista Monocromático de Alto Contraste">Minimalista Monocromático</option>
                <option value="Personalizada según materia escolar">Personalizada según materia</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="infoOrient">Orientación y formato</label>
              <select id="infoOrient" class="form-select">
                <option value="Póster vertical (Carta / Tabloide para imprimir)" selected>Póster vertical (Carta / Tabloide)</option>
                <option value="Lámina horizontal 16:9 para diapositiva">Horizontal 16:9 (Presentación)</option>
                <option value="Formato vertical / cuadrado para celular">Vertical para celular</option>
              </select>
            </div>
          </div>
          <div class="form-group mb-0">
            <label class="form-label" for="infoType">Tipo de representación visual</label>
            <select id="infoType" class="form-select">
              <option value="Proceso paso a paso / Diagrama de flujo" selected>Proceso paso a paso / Diagrama de flujo</option>
              <option value="Línea de tiempo histórica y cronología">Línea de tiempo histórica</option>
              <option value="Cuadro comparativo visual de conceptos">Cuadro comparativo de conceptos</option>
              <option value="Gráficos estadísticos y síntesis de datos">Gráficos estadísticos y datos</option>
            </select>
          </div>
        </div>

        <!-- Panel 12: Proyecto Encardomy -->
        <div class="service-dynamic-panel" id="servicePanel-proyecto-encardomy" style="display: none;">
          <div class="service-panel-header">
            <div class="service-panel-title">
              <i data-lucide="briefcase" style="width: 18px; height: 18px; color: var(--color-primary);"></i>
              <span>Personalización de Proyecto Semestral</span>
            </div>
            <span class="ecosystem-pill">Suite Google Workspace Completa</span>
          </div>
          <div class="grid-2 mb-12">
            <div class="form-group mb-0">
              <label class="form-label" for="projType">Tipo de proyecto</label>
              <select id="projType" class="form-select">
                <option value="Trabajo Integrador Semestral" selected>Trabajo Integrador Semestral</option>
                <option value="Proyecto de Titulación / Práctica Técnica">Proyecto de Titulación / Práctica</option>
                <option value="Proyecto de Feria de las Ciencias UNAM">Proyecto de Feria de las Ciencias</option>
                <option value="Tesina / Monografía extensa">Tesina / Monografía extensa</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <label class="form-label" for="projStage">Fase o avance actual</label>
              <select id="projStage" class="form-select">
                <option value="Desde cero (definición de tema y objetivos)" selected>Desde cero (tema y objetivos)</option>
                <option value="Esquema y marco teórico en proceso">Esquema y marco en proceso</option>
                <option value="Borrador avanzado que requiere pulido">Borrador avanzado a pulir</option>
              </select>
            </div>
          </div>
          <div class="form-group mb-12">
            <label class="form-label" for="projDeadlines">Fechas de entregas parciales y entrega final</label>
            <input type="text" id="projDeadlines" class="form-input" placeholder="Ej. Primer avance 15 Octubre, Segundo 30 Octubre, Entrega final 15 Noviembre">
          </div>
          <div class="form-group mb-0">
            <label class="form-label" for="projRubric">Rúbrica oficial o lineamientos de los profesores de la Prepa 4</label>
            <textarea id="projRubric" class="form-textarea" style="min-height: 65px;" placeholder="Puntos específicos que exigen los profesores del colegio/academia..."></textarea>
          </div>
        </div>

        <!-- 5. Tiempo de entrega -->
        <div class="form-group mb-16">
          <label class="form-label" for="orderUrgencySelect">Tiempo de entrega deseado</label>
          <select id="orderUrgencySelect" class="form-select">
            <option value="Estándar (24 a 48 horas)" selected>Estándar (24 a 48 horas)</option>
            <option value="Express urgente (Menos de 12 a 24 horas)">Express urgente (Menos de 12 a 24 horas)</option>
            <option value="Con calma (3 a 5 días hábiles)">Con calma (3 a 5 días hábiles)</option>
          </select>
        </div>

        <!-- 6. Notas generales y enlaces -->
        <div class="form-group mb-20">
          <label class="form-label" for="orderDetailsInput">Notas adicionales o enlace a tu carpeta de Google Drive (Opcional)</label>
          <textarea id="orderDetailsInput" class="form-textarea" style="min-height: 65px;" placeholder="Ej. Ya subí los archivos a Google Drive, o indicación especial de tu profesor..."></textarea>
        </div>

        <!-- 7. Botón de Envío -->
        <button type="submit" id="sendWhatsAppBtn" class="btn btn-primary btn-block btn-lg">
          <i data-lucide="message-circle"></i>
          <span>Enviar Cotización a WhatsApp (+52 55 7198 5641)</span>
        </button>

                <div style="text-align: center; margin-top: 10px; font-size: 0.78rem; color: var(--color-text-muted);">
          🔒 Tus datos están protegidos. Al solicitar tu cotización aceptas nuestro <a href="../privacidad.html" target="_blank" style="text-decoration: underline; color: var(--color-primary); font-weight: 600;">Aviso de Privacidad</a> y la <a href="../propiedad-intelectual.html" target="_blank" style="text-decoration: underline; color: var(--color-primary); font-weight: 600;">Política de Propiedad Intelectual</a>.
        </div>
      </form>
    </div>
  </div>

        <div class="grid-2-form">
          <div class="form-group">
            <label class="form-label" for="orderGroupSelect">Grupo (401 - 663)</label>
            <select id="orderGroupSelect" class="form-select" required>
              <option value="" disabled selected>Elige tu grupo</option>
              <optgroup label="Cuarto Año (4to)">
                <option value="401">Grupo 401</option>
                <option value="402">Grupo 402</option>
                <option value="403">Grupo 403</option>
                <option value="404">Grupo 404</option>
                <option value="405">Grupo 405</option>
                <option value="406">Grupo 406</option>
                <option value="407">Grupo 407</option>
                <option value="408">Grupo 408</option>
                <option value="409">Grupo 409</option>
                <option value="410">Grupo 410</option>
                <option value="411">Grupo 411</option>
                <option value="412">Grupo 412</option>
                <option value="413">Grupo 413</option>
                <option value="414">Grupo 414</option>
                <option value="415">Grupo 415</option>
                <option value="416">Grupo 416</option>
                <option value="417">Grupo 417</option>
                <option value="418">Grupo 418</option>
                <option value="419">Grupo 419</option>
                <option value="420">Grupo 420</option>
                <option value="421">Grupo 421</option>
                <option value="422">Grupo 422</option>
                <option value="423">Grupo 423</option>
                <option value="424">Grupo 424</option>
                <option value="425">Grupo 425</option>
                <option value="426">Grupo 426</option>
                <option value="427">Grupo 427</option>
                <option value="428">Grupo 428</option>
                <option value="429">Grupo 429</option>
                <option value="430">Grupo 430</option>
                <option value="431">Grupo 431</option>
                <option value="432">Grupo 432</option>
                <option value="433">Grupo 433</option>
                <option value="434">Grupo 434</option>
                <option value="435">Grupo 435</option>
                <option value="436">Grupo 436</option>
                <option value="437">Grupo 437</option>
                <option value="438">Grupo 438</option>
                <option value="439">Grupo 439</option>
                <option value="440">Grupo 440</option>
                <option value="441">Grupo 441</option>
                <option value="442">Grupo 442</option>
                <option value="443">Grupo 443</option>
                <option value="444">Grupo 444</option>
                <option value="445">Grupo 445</option>
                <option value="446">Grupo 446</option>
                <option value="447">Grupo 447</option>
                <option value="448">Grupo 448</option>
                <option value="449">Grupo 449</option>
                <option value="450">Grupo 450</option>
                <option value="451">Grupo 451</option>
                <option value="452">Grupo 452</option>
                <option value="453">Grupo 453</option>
                <option value="454">Grupo 454</option>
                <option value="455">Grupo 455</option>
                <option value="456">Grupo 456</option>
                <option value="457">Grupo 457</option>
                <option value="458">Grupo 458</option>
                <option value="459">Grupo 459</option>
                <option value="460">Grupo 460</option>
                <option value="461">Grupo 461</option>
                <option value="462">Grupo 462</option>
                <option value="463">Grupo 463</option>
                <option value="464">Grupo 464</option>
                <option value="465">Grupo 465</option>
                <option value="466">Grupo 466</option>
                <option value="467">Grupo 467</option>
                <option value="468">Grupo 468</option>
                <option value="469">Grupo 469</option>
                <option value="470">Grupo 470</option>
                <option value="471">Grupo 471</option>
                <option value="472">Grupo 472</option>
                <option value="473">Grupo 473</option>
                <option value="474">Grupo 474</option>
                <option value="475">Grupo 475</option>
                <option value="476">Grupo 476</option>
                <option value="477">Grupo 477</option>
                <option value="478">Grupo 478</option>
                <option value="479">Grupo 479</option>
                <option value="480">Grupo 480</option>
                <option value="481">Grupo 481</option>
                <option value="482">Grupo 482</option>
                <option value="483">Grupo 483</option>
                <option value="484">Grupo 484</option>
                <option value="485">Grupo 485</option>
                <option value="486">Grupo 486</option>
                <option value="487">Grupo 487</option>
                <option value="488">Grupo 488</option>
                <option value="489">Grupo 489</option>
                <option value="490">Grupo 490</option>
                <option value="491">Grupo 491</option>
                <option value="492">Grupo 492</option>
                <option value="493">Grupo 493</option>
                <option value="494">Grupo 494</option>
                <option value="495">Grupo 495</option>
                <option value="496">Grupo 496</option>
                <option value="497">Grupo 497</option>
                <option value="498">Grupo 498</option>
                <option value="499">Grupo 499</option>
              </optgroup>
              <optgroup label="Quinto Año (5to)">
                <option value="501">Grupo 501</option>
                <option value="502">Grupo 502</option>
                <option value="503">Grupo 503</option>
                <option value="504">Grupo 504</option>
                <option value="505">Grupo 505</option>
                <option value="506">Grupo 506</option>
                <option value="507">Grupo 507</option>
                <option value="508">Grupo 508</option>
                <option value="509">Grupo 509</option>
                <option value="510">Grupo 510</option>
                <option value="511">Grupo 511</option>
                <option value="512">Grupo 512</option>
                <option value="513">Grupo 513</option>
                <option value="514">Grupo 514</option>
                <option value="515">Grupo 515</option>
                <option value="516">Grupo 516</option>
                <option value="517">Grupo 517</option>
                <option value="518">Grupo 518</option>
                <option value="519">Grupo 519</option>
                <option value="520">Grupo 520</option>
                <option value="521">Grupo 521</option>
                <option value="522">Grupo 522</option>
                <option value="523">Grupo 523</option>
                <option value="524">Grupo 524</option>
                <option value="525">Grupo 525</option>
                <option value="526">Grupo 526</option>
                <option value="527">Grupo 527</option>
                <option value="528">Grupo 528</option>
                <option value="529">Grupo 529</option>
                <option value="530">Grupo 530</option>
                <option value="531">Grupo 531</option>
                <option value="532">Grupo 532</option>
                <option value="533">Grupo 533</option>
                <option value="534">Grupo 534</option>
                <option value="535">Grupo 535</option>
                <option value="536">Grupo 536</option>
                <option value="537">Grupo 537</option>
                <option value="538">Grupo 538</option>
                <option value="539">Grupo 539</option>
                <option value="540">Grupo 540</option>
                <option value="541">Grupo 541</option>
                <option value="542">Grupo 542</option>
                <option value="543">Grupo 543</option>
                <option value="544">Grupo 544</option>
                <option value="545">Grupo 545</option>
                <option value="546">Grupo 546</option>
                <option value="547">Grupo 547</option>
                <option value="548">Grupo 548</option>
                <option value="549">Grupo 549</option>
                <option value="550">Grupo 550</option>
                <option value="551">Grupo 551</option>
                <option value="552">Grupo 552</option>
                <option value="553">Grupo 553</option>
                <option value="554">Grupo 554</option>
                <option value="555">Grupo 555</option>
                <option value="556">Grupo 556</option>
                <option value="557">Grupo 557</option>
                <option value="558">Grupo 558</option>
                <option value="559">Grupo 559</option>
                <option value="560">Grupo 560</option>
                <option value="561">Grupo 561</option>
                <option value="562">Grupo 562</option>
                <option value="563">Grupo 563</option>
                <option value="564">Grupo 564</option>
                <option value="565">Grupo 565</option>
                <option value="566">Grupo 566</option>
                <option value="567">Grupo 567</option>
                <option value="568">Grupo 568</option>
                <option value="569">Grupo 569</option>
                <option value="570">Grupo 570</option>
                <option value="571">Grupo 571</option>
                <option value="572">Grupo 572</option>
                <option value="573">Grupo 573</option>
                <option value="574">Grupo 574</option>
                <option value="575">Grupo 575</option>
                <option value="576">Grupo 576</option>
                <option value="577">Grupo 577</option>
                <option value="578">Grupo 578</option>
                <option value="579">Grupo 579</option>
                <option value="580">Grupo 580</option>
                <option value="581">Grupo 581</option>
                <option value="582">Grupo 582</option>
                <option value="583">Grupo 583</option>
                <option value="584">Grupo 584</option>
                <option value="585">Grupo 585</option>
                <option value="586">Grupo 586</option>
                <option value="587">Grupo 587</option>
                <option value="588">Grupo 588</option>
                <option value="589">Grupo 589</option>
                <option value="590">Grupo 590</option>
                <option value="591">Grupo 591</option>
                <option value="592">Grupo 592</option>
                <option value="593">Grupo 593</option>
                <option value="594">Grupo 594</option>
                <option value="595">Grupo 595</option>
                <option value="596">Grupo 596</option>
                <option value="597">Grupo 597</option>
                <option value="598">Grupo 598</option>
                <option value="599">Grupo 599</option>
              </optgroup>
              <optgroup label="Sexto Año (6to)">
                <option value="601">Grupo 601</option>
                <option value="602">Grupo 602</option>
                <option value="603">Grupo 603</option>
                <option value="604">Grupo 604</option>
                <option value="605">Grupo 605</option>
                <option value="606">Grupo 606</option>
                <option value="607">Grupo 607</option>
                <option value="608">Grupo 608</option>
                <option value="609">Grupo 609</option>
                <option value="610">Grupo 610</option>
                <option value="611">Grupo 611</option>
                <option value="612">Grupo 612</option>
                <option value="613">Grupo 613</option>
                <option value="614">Grupo 614</option>
                <option value="615">Grupo 615</option>
                <option value="616">Grupo 616</option>
                <option value="617">Grupo 617</option>
                <option value="618">Grupo 618</option>
                <option value="619">Grupo 619</option>
                <option value="620">Grupo 620</option>
                <option value="621">Grupo 621</option>
                <option value="622">Grupo 622</option>
                <option value="623">Grupo 623</option>
                <option value="624">Grupo 624</option>
                <option value="625">Grupo 625</option>
                <option value="626">Grupo 626</option>
                <option value="627">Grupo 627</option>
                <option value="628">Grupo 628</option>
                <option value="629">Grupo 629</option>
                <option value="630">Grupo 630</option>
                <option value="631">Grupo 631</option>
                <option value="632">Grupo 632</option>
                <option value="633">Grupo 633</option>
                <option value="634">Grupo 634</option>
                <option value="635">Grupo 635</option>
                <option value="636">Grupo 636</option>
                <option value="637">Grupo 637</option>
                <option value="638">Grupo 638</option>
                <option value="639">Grupo 639</option>
                <option value="640">Grupo 640</option>
                <option value="641">Grupo 641</option>
                <option value="642">Grupo 642</option>
                <option value="643">Grupo 643</option>
                <option value="644">Grupo 644</option>
                <option value="645">Grupo 645</option>
                <option value="646">Grupo 646</option>
                <option value="647">Grupo 647</option>
                <option value="648">Grupo 648</option>
                <option value="649">Grupo 649</option>
                <option value="650">Grupo 650</option>
                <option value="651">Grupo 651</option>
                <option value="652">Grupo 652</option>
                <option value="653">Grupo 653</option>
                <option value="654">Grupo 654</option>
                <option value="655">Grupo 655</option>
                <option value="656">Grupo 656</option>
                <option value="657">Grupo 657</option>
                <option value="658">Grupo 658</option>
                <option value="659">Grupo 659</option>
                <option value="660">Grupo 660</option>
                <option value="661">Grupo 661</option>
                <option value="662">Grupo 662</option>
                <option value="663">Grupo 663</option>
              </optgroup>
            </select>
          </div>
          <div class="form-group">
            <label class="form-label" for="orderSectionSelect">Sección</label>
            <select id="orderSectionSelect" class="form-select" required>
              <option value="" disabled selected>Elige sección</option>
              <option value="Sección A">Sección A</option>
              <option value="Sección B">Sección B</option>
            </select>
          </div>
        </div>

        <div class="form-group">
          <label class="form-label" for="orderUrgencySelect">Tiempo de entrega deseado</label>
          <select id="orderUrgencySelect" class="form-select">
            <option value="Estándar ({turnaround})" selected>Estándar ({turnaround})</option>
            <option value="Express urgente (Menos de 12 horas)">Express urgente (Menos de 12 horas)</option>
            <option value="Con calma (3 a 5 días)">Con calma (3 a 5 días)</option>
          </select>
        </div>

        <div class="form-group">
          <label class="form-label" for="orderDetailsInput">Materia, tema o detalles de tu trabajo</label>
          <textarea id="orderDetailsInput" class="form-textarea" placeholder="Ej. Necesito apoyo para mi entrega de este viernes con 20 páginas de tema..."></textarea>
        </div>

        <button type="submit" id="sendWhatsAppBtn" class="btn btn-primary btn-block btn-lg">
          <i data-lucide="message-circle"></i>
          <span>Enviar Cotización a WhatsApp (+52 55 7198 5641)</span>
        </button>
      </form>
    </div>
  </div>

        <div class="form-group">
          <label class="form-label" for="orderUrgencySelect">Tiempo de entrega deseado</label>
          <select id="orderUrgencySelect" class="form-select">
            <option value="Estándar ({turnaround})" selected>Estándar ({turnaround})</option>
            <option value="Express urgente (Menos de 12 horas)">Express urgente (Menos de 12 horas)</option>
            <option value="Con calma (3 a 5 días)">Con calma (3 a 5 días)</option>
          </select>
        </div>

        <div class="form-group">
          <label class="form-label" for="orderDetailsInput">Materia, tema o detalles de tu trabajo</label>
          <textarea id="orderDetailsInput" class="form-textarea" placeholder="Ej. Necesito apoyo para mi entrega de este viernes con 20 páginas de tema..."></textarea>
        </div>

        <button type="submit" class="btn btn-primary btn-block btn-lg">
          <i data-lucide="send"></i>
          <span>Enviar Cotización a WhatsApp</span>
        </button>
      </form>
    </div>
  </div>

  <!-- Scripts -->
  <script src="../js/data.js"></script>
  <script src="../js/main.js"></script>
  <script>
    lucide.createIcons();
  </script>
</body>
</html>
"""

output_dir = "/Users/shaminket/.gemini/users/user1/encardomy-web/servicios"
os.makedirs(output_dir, exist_ok=True)

for s in services_data:
    # Build offer items HTML
    offer_items_html = "".join([f'<li style="display: flex; gap: 8px; align-items: flex-start;"><span style="color: var(--color-primary); font-weight: 700;">✓</span><span>{item}</span></li>' for item in s["offer_items"]])
    
    # Build visual samples HTML
    visual_samples_html = "".join([
        f'''<div class="card">
              <div style="height: 120px; background: var(--color-blue-tint); border-radius: var(--radius-md); display: flex; align-items: center; justify-content: center; margin-bottom: var(--space-16); color: var(--color-primary); font-weight: 700; font-family: var(--font-heading);">
                <i data-lucide="file-text" style="width: 36px; height: 36px;"></i>
              </div>
              <h4>{v["title"]}</h4>
              <p class="text-muted" style="font-size: 0.88rem; margin-top: 6px;">{v["desc"]}</p>
            </div>'''
        for v in s["visual_samples"]
    ])
    
    # Build benefits HTML
    benefits_html = "".join([
        f'''<div class="card" style="border-top: 3px solid var(--color-success);">
              <div style="width: 36px; height: 36px; border-radius: 8px; background: var(--color-success-light); color: var(--color-success); display: flex; align-items: center; justify-content: center; margin-bottom: 12px;">
                <i data-lucide="check" style="width: 20px; height: 20px;"></i>
              </div>
              <h4 style="font-size: 1.05rem; margin-bottom: 6px;">{b["title"]}</h4>
              <p class="text-muted" style="font-size: 0.88rem;">{b["desc"]}</p>
            </div>'''
        for b in s["benefits"]
    ])
    
    # Build features HTML
    features_html = "".join([
        f'''<tr>
              <td style="font-weight: 700; color: var(--color-navy); width: 35%;">{f["label"]}</td>
              <td>{f["value"]}</td>
            </tr>'''
        for f in s["features"]
    ])
    
    # Build objections HTML
    objections_html = "".join([
        f'''<div class="card" style="border-left: 4px solid var(--color-primary);">
              <h4 style="font-size: 1rem; color: var(--color-navy); margin-bottom: 8px;">{obj["q"]}</h4>
              <p class="text-muted" style="font-size: 0.92rem;">{obj["a"]}</p>
            </div>'''
        for obj in s["objections"]
    ])
    
    # Build unboxing HTML
    unboxing_html = "".join([
        f'''<div class="unboxing-item">
              <div style="font-family: var(--font-heading); font-weight: 700; color: var(--color-navy); font-size: 0.95rem;">
                📦 {u["item"]}
              </div>
              <p class="text-muted" style="font-size: 0.84rem;">{u["desc"]}</p>
            </div>'''
        for u in s["unboxing"]
    ])
    
    # Build for_who HTML
    for_who_html = "".join([
        f'''<div class="card" style="border-top: 4px solid {'var(--color-success)' if 'Ideal' in fw['type'] else '#991b1b'};">
              <h3 style="font-size: 1.15rem; color: {'var(--color-navy)' if 'Ideal' in fw['type'] else '#991b1b'}; margin-bottom: 12px;">{fw['type']}</h3>
              <p class="text-muted" style="font-size: 0.95rem;">{fw['text']}</p>
            </div>'''
        for fw in s["for_who"]
    ])
    
    # Build FAQ HTML
    faq_html = "".join([
        f'''<div class="faq-item">
              <button class="faq-question" aria-expanded="false">
                <span>{item["q"]}</span>
                <span class="faq-icon"><i data-lucide="chevron-down"></i></span>
              </button>
              <div class="faq-answer">
                <p class="text-muted">{item["a"]}</p>
              </div>
            </div>'''
        for item in s["faq"]
    ])
    
    page_content = template.format(
        id=s["id"],
        slug=s["slug"],
        name=s["name"],
        category=s["category"],
        category_name=s["category_name"],
        badge_class=s["badge_class"],
        hero_title=s["hero_title"],
        hero_subtitle=s["hero_subtitle"],
        short_desc=s["short_desc"],
        turnaround=s["turnaround"],
        format=s["format"],
        price_note=s["price_note"],
        offer_items_html=offer_items_html,
        visual_samples_html=visual_samples_html,
        differentiator_text=s["differentiator_text"],
        benefits_html=benefits_html,
        features_html=features_html,
        about_company=s["about_company"],
        authority_text=s["authority_text"],
        objections_html=objections_html,
        unboxing_html=unboxing_html,
        for_who_html=for_who_html,
        faq_html=faq_html
    )
    
    file_path = os.path.join(output_dir, f"{s['slug']}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(page_content)
    print(f"Generated: {file_path}")

print("All 12 service pages generated successfully!")
