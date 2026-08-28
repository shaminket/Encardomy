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
        "format": "PDF interactivo + DOCX editable + Formato Móvil",
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
            {"label": "Formatos Entregables", "value": "PDF Maquetado + Microsoft Word (.docx) editable"},
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
        "format": "PDF Cuaderno de Estudio + DOCX + Enlaces Interactivos",
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
            {"label": "Formatos", "value": "PDF Cuaderno Editorial + Word DOCX editable"},
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
        "format": "Archivo Anki (.apkg) + Formato Quizlet + PDF Imprimible",
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
        "format": "PDF Interactivo de Examen + Hoja de Respuestas Explicadas",
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
            {"label": "Formatos", "value": "PDF de Examen + PDF de Solucionario + Formato DOCX"},
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
        "format": "DOCX con Control de Cambios + DOCX Limpio + PDF Final",
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
            {"label": "Entregables", "value": "Versión con cambios marcados + Versión limpia lista"},
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
        "format": "DOCX Editable + Reporte de Fluidez y Calidad Lingüística",
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
            {"label": "Formato", "value": "DOCX editable con notas al margen"},
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
        "format": "Documento Enriquecido + Reporte de Diagnóstico con Rúbrica",
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
        "format": "DOCX Editable + PDF con Citas Verificadas",
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
        "format": "Marco Teórico DOCX + Fichas de Lectura + Biblioteca de Referencias",
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
        "format": "PowerPoint (.pptx) + Enlace Editable Canva + PDF de Alta Resolución",
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
        "format": "PDF Vectorial Imprimible (A4/Tabloide) + PNG 4K + Editable",
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
        "format": "Suite Completa (Documento + Diapositivas + Resumen Ejecutivo + Asesoría)",
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

            <div style="display: flex; gap: var(--space-16); flex-wrap: wrap; margin-bottom: var(--space-24);">
              <button class="btn btn-primary btn-lg" data-open-order data-service-id="{id}">
                <i data-lucide="message-circle"></i>
                <span>Solicitar Cotización Rápida</span>
              </button>
              <a href="#oferta" class="btn btn-secondary btn-lg">
                <span>Ver qué incluye</span>
                <i data-lucide="arrow-down"></i>
              </a>
            </div>

            <!-- Ficha técnica rápida -->
            <div style="display: flex; gap: var(--space-16); flex-wrap: wrap; font-size: 0.85rem; color: var(--color-text-muted);">
              <span style="display: flex; align-items: center; gap: 4px;">
                <i data-lucide="clock" style="color: var(--color-primary); width: 16px; height: 16px;"></i> Entrega: <strong>{turnaround}</strong>
              </span>
              <span style="display: flex; align-items: center; gap: 4px;">
                <i data-lucide="file" style="color: var(--color-primary); width: 16px; height: 16px;"></i> Formato: <strong>{format}</strong>
              </span>
              <span style="display: flex; align-items: center; gap: 4px;">
                <i data-lucide="refresh-cw" style="color: var(--color-success); width: 16px; height: 16px;"></i> Ajustes incluidos
              </span>
            </div>
          </div>

          <!-- Tarjeta Lateral de Configuración Rápida -->
          <div class="hero-quick-card">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: var(--space-16);">
              <span style="font-family: var(--font-heading); font-weight: 700; color: var(--color-navy); font-size: 1.1rem;">
                Resumen del Servicio
              </span>
              <span class="badge badge-primary">Oficial</span>
            </div>
            
            <p class="text-muted mb-16" style="font-size: 0.9rem;">
              {short_desc}
            </p>

            <div style="background: var(--color-bg-light); padding: var(--space-16); border-radius: var(--radius-md); margin-bottom: var(--space-20, 20px);">
              <div style="font-size: 0.82rem; font-weight: 700; color: var(--color-navy); margin-bottom: 6px;">
                ESTRUCTURA DE PRECIOS
              </div>
              <div style="font-size: 0.92rem; color: var(--color-text-dark);">
                {price_note}
              </div>
            </div>

            <button class="btn btn-primary btn-block btn-lg" data-open-order data-service-id="{id}">
              <i data-lucide="send"></i>
              <span>Cotizar por WhatsApp</span>
            </button>
            <div style="text-align: center; margin-top: 10px; font-size: 0.78rem; color: var(--color-text-muted);">
              Respuesta en menos de 15 minutos en horario escolar
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ==========================================================================
         2. OFERTA (METODOLOGÍA SECCIÓN 2)
         ========================================================================== -->
    <section class="section-padding" id="oferta">
      <div class="container">
        <div class="product-section-title">
          <span class="section-num">2</span>
          <h2>¿Qué incluye exactamente este servicio?</h2>
        </div>
        <p class="text-muted mb-32" style="max-width: 680px;">
          Desglose completo de cada elemento y entregable que recibirás al contratar {name}.
        </p>

        <div class="grid-2">
          <div class="card card-highlight">
            <h3 class="mb-16" style="font-size: 1.25rem;">Entregables y Componentes Incluidos</h3>
            <ul style="list-style: none; display: flex; flex-direction: column; gap: var(--space-12, 12px);">
              {offer_items_html}
            </ul>
          </div>

          <div class="card" style="background: var(--color-bg-subtle);">
            <h3 class="mb-16" style="font-size: 1.25rem;">Garantía de Entrega Encardomy</h3>
            <div style="display: flex; flex-direction: column; gap: var(--space-16);">
              <div style="display: flex; gap: 12px; align-items: flex-start;">
                <div style="width: 32px; height: 32px; border-radius: 8px; background: var(--color-success-light); color: var(--color-success); display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                  <i data-lucide="check" style="width: 18px; height: 18px;"></i>
                </div>
                <div>
                  <strong style="color: var(--color-navy); font-size: 0.95rem;">Verificación Humana Línea por Línea</strong>
                  <p class="text-muted" style="font-size: 0.88rem;">Un revisor comprueba la exactitud de fechas, citas, conceptos y redacción antes del envío.</p>
                </div>
              </div>

              <div style="display: flex; gap: 12px; align-items: flex-start;">
                <div style="width: 32px; height: 32px; border-radius: 8px; background: var(--color-blue-tint); color: var(--color-primary); display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                  <i data-lucide="edit" style="width: 18px; height: 18px;"></i>
                </div>
                <div>
                  <strong style="color: var(--color-navy); font-size: 0.95rem;">Archivos 100% Editables</strong>
                  <p class="text-muted" style="font-size: 0.88rem;">Siempre recibes el archivo fuente (DOCX, PPTX, Anki, Canva) para tus propios ajustes.</p>
                </div>
              </div>

              <div style="display: flex; gap: 12px; align-items: flex-start;">
                <div style="width: 32px; height: 32px; border-radius: 8px; background: #fef3c7; color: #b45309; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                  <i data-lucide="shield" style="width: 18px; height: 18px;"></i>
                </div>
                <div>
                  <strong style="color: var(--color-navy); font-size: 0.95rem;">Ronda de Ajustes Incluida</strong>
                  <p class="text-muted" style="font-size: 0.88rem;">Si tu profesor solicita alguna precisión o cambio de formato, lo realizamos sin costo.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ==========================================================================
         3. IMÁGENES Y VIDEOS / MUESTRAS VISUALES (METODOLOGÍA SECCIÓN 3)
         ========================================================================== -->
    <section class="section-padding bg-surface" id="muestras">
      <div class="container">
        <div class="product-section-title">
          <span class="section-num">3</span>
          <h2>Muestras de Formato y Estructura Visual</h2>
        </div>
        <p class="text-muted mb-32">
          Cómo se organiza visualmente el material para maximizar la legibilidad y facilitar el estudio.
        </p>

        <div class="grid-3">
          {visual_samples_html}
        </div>
      </div>
    </section>

    <!-- ==========================================================================
         4. DIFERENCIADOR (METODOLOGÍA SECCIÓN 4)
         ========================================================================== -->
    <section class="section-padding" id="diferenciador">
      <div class="container">
        <div class="product-section-title">
          <span class="section-num">4</span>
          <h2>El Diferenciador Encardomy</h2>
        </div>
        <div class="card card-highlight" style="padding: var(--space-32); background: linear-gradient(135deg, #ffffff 0%, #f4f8ff 100%);">
          <div class="grid-2" style="align-items: center;">
            <div>
              <span class="badge badge-success mb-16">Producción Híbrida Inteligente</span>
              <h3 class="mb-16">¿Por qué no conformarte con una IA genérica sin supervisión?</h3>
              <p class="text-muted mb-16" style="font-size: 1.02rem;">
                {differentiator_text}
              </p>
              <div style="display: flex; align-items: center; gap: 8px; color: var(--color-navy); font-weight: 600; font-size: 0.9rem;">
                <i data-lucide="check-circle" style="color: var(--color-success);"></i> Cero falsas promesas &bull; Rigor real y honestidad académica
              </div>
            </div>

            <div style="background: var(--color-white); padding: var(--space-24); border-radius: var(--radius-lg); border: 1px solid var(--color-border); box-shadow: var(--shadow-sm);">
              <div style="font-size: 0.85rem; font-weight: 700; color: var(--color-navy); margin-bottom: 12px;">
                ESTÁNDAR DE CONTROL DE CALIDAD
              </div>
              <div style="display: flex; flex-direction: column; gap: 10px; font-size: 0.88rem; color: var(--color-text-dark);">
                <div style="display: flex; gap: 8px;"><span style="color: var(--color-success);">✓</span> Verificación de fuentes bibliográficas reales</div>
                <div style="display: flex; gap: 8px;"><span style="color: var(--color-success);">✓</span> Corrección de sintaxis y tono formal escolar</div>
                <div style="display: flex; gap: 8px;"><span style="color: var(--color-success);">✓</span> Adecuación estricta a rúbricas institucionales</div>
                <div style="display: flex; gap: 8px;"><span style="color: var(--color-success);">✓</span> Maquetación editorial lista para entrega</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ==========================================================================
         5. BENEFICIOS (METODOLOGÍA SECCIÓN 5)
         ========================================================================== -->
    <section class="section-padding bg-subtle" id="beneficios">
      <div class="container">
        <div class="product-section-title">
          <span class="section-num">5</span>
          <h2>Beneficios Clave para tu Rutina Escolar</h2>
        </div>
        <p class="text-muted mb-32">Ventajas tangibles en tus tiempos de estudio, calificaciones y bienestar.</p>

        <div class="grid-4">
          {benefits_html}
        </div>
      </div>
    </section>

    <!-- ==========================================================================
         6. VIDEO REVIEW DE INFLUENCER / CREADOR (METODOLOGÍA SECCIÓN 6)
         ========================================================================== -->
    <section class="section-padding" id="video-review">
      <div class="container">
        <div class="product-section-title">
          <span class="section-num">6</span>
          <h2>Video Review de la Experiencia</h2>
        </div>
        <div class="placeholder-box">
          <span class="badge badge-placeholder mb-12">[Placeholder: Video Review de Creador / Estudiante de Prepa & Universidad]</span>
          <div class="placeholder-icon mb-12">
            <i data-lucide="play" style="width: 28px; height: 28px; color: var(--color-primary);"></i>
          </div>
          <h4 style="color: var(--color-navy);">Espacio reservado para video reseña demostrativa</h4>
          <p class="text-muted" style="max-width: 480px; font-size: 0.88rem;">
            En este espacio se reproducirá el video de un estudiante explicando cómo solicitó {name} y cómo le ayudó en sus calificaciones.
          </p>
        </div>
      </div>
    </section>

    <!-- ==========================================================================
         7. CARACTERÍSTICAS Y ESPECIFICACIONES (METODOLOGÍA SECCIÓN 7)
         ========================================================================== -->
    <section class="section-padding bg-surface" id="caracteristicas">
      <div class="container container-narrow">
        <div class="product-section-title">
          <span class="section-num">7</span>
          <h2>Ficha Técnica y Especificaciones</h2>
        </div>
        <p class="text-muted mb-24">Parámetros operativos y estándares técnicos del servicio.</p>

        <div class="card" style="padding: 0; overflow: hidden;">
          <table class="diff-table" style="margin: 0; border: none;">
            <tbody>
              {features_html}
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- ==========================================================================
         8. SOBRE EMPRESA / CREADOR (METODOLOGÍA SECCIÓN 8)
         ========================================================================== -->
    <section class="section-padding" id="empresa">
      <div class="container">
        <div class="product-section-title">
          <span class="section-num">8</span>
          <h2>Sobre Encardomy</h2>
        </div>
        <div class="card" style="padding: var(--space-32); background: var(--color-white); border-left: 4px solid var(--color-navy);">
          <div style="display: flex; gap: 16px; align-items: center;" class="mb-16">
            <div class="logo-symbol">E</div>
            <div>
              <h3 style="font-size: 1.25rem;">Nuestra Filosofía Académica</h3>
              <span class="text-muted" style="font-size: 0.86rem;">Diseñado por y para estudiantes de 15 a 25 años</span>
            </div>
          </div>
          <p class="text-muted mb-16" style="font-size: 1rem; line-height: 1.7;">
            {about_company}
          </p>
          <div style="display: flex; gap: var(--space-24); flex-wrap: wrap; font-size: 0.88rem; color: var(--color-navy); font-weight: 600;">
            <span>✓ Cero intermediarios lentos</span>
            <span>✓ Atención directa por WhatsApp</span>
            <span>✓ Precios accesibles para estudiantes</span>
          </div>
        </div>
      </div>
    </section>

    <!-- ==========================================================================
         9. AUTORIDAD Y RIGOR (METODOLOGÍA SECCIÓN 9)
         ========================================================================== -->
    <section class="section-padding bg-subtle" id="autoridad">
      <div class="container">
        <div class="product-section-title">
          <span class="section-num">9</span>
          <h2>Estándares de Autoridad y Rigor Académico</h2>
        </div>
        <div class="placeholder-box" style="text-align: left; align-items: flex-start;">
          <span class="badge badge-placeholder mb-12">[Placeholder: Rigor Metodológico y Alianzas Académicas en Desarrollo]</span>
          <h4 style="color: var(--color-navy); margin-bottom: 8px;">Marco Metodológico de Validación</h4>
          <p class="text-muted mb-16" style="font-size: 0.92rem;">
            {authority_text}
          </p>
          <div style="font-size: 0.82rem; color: var(--color-text-muted);">
            <em>* Los sellos institucionales y certificaciones formales se publicarán conforme se completen los convenios correspondientes.</em>
          </div>
        </div>
      </div>
    </section>

    <!-- ==========================================================================
         10. OBJECIONES Y TRANSPARENCIA (METODOLOGÍA SECCIÓN 10)
         ========================================================================== -->
    <section class="section-padding" id="objeciones">
      <div class="container container-narrow">
        <div class="product-section-title">
          <span class="section-num">10</span>
          <h2>Manejo Transparente de Objeciones</h2>
        </div>
        <p class="text-muted mb-24">Respuestas directas a las dudas más comunes sobre la ética y calidad de nuestro servicio.</p>

        <div style="display: flex; flex-direction: column; gap: var(--space-16);">
          {objections_html}
        </div>
      </div>
    </section>

    <!-- ==========================================================================
         11. UNBOXING / QUÉ RECIBES (METODOLOGÍA SECCIÓN 11)
         ========================================================================== -->
    <section class="section-padding bg-surface" id="unboxing">
      <div class="container">
        <div class="product-section-title">
          <span class="section-num">11</span>
          <h2>Unboxing Digital: ¿Qué recibes en tu bandeja?</h2>
        </div>
        <p class="text-muted mb-32">El desglose de los archivos y complementos listos para usar tras tu pedido.</p>

        <div class="unboxing-grid">
          {unboxing_html}
        </div>
      </div>
    </section>

    <!-- ==========================================================================
         12. ¿PARA QUIÉN ES? (METODOLOGÍA SECCIÓN 12)
         ========================================================================== -->
    <section class="section-padding" id="para-quien">
      <div class="container">
        <div class="product-section-title">
          <span class="section-num">12</span>
          <h2>¿Para quién es este servicio?</h2>
        </div>
        <div class="grid-2">
          {for_who_html}
        </div>
      </div>
    </section>

    <!-- ==========================================================================
         13. PRUEBA SOCIAL / SOCIAL PROOF (METODOLOGÍA SECCIÓN 13)
         ========================================================================== -->
    <section class="section-padding bg-subtle" id="prueba-social">
      <div class="container">
        <div class="product-section-title">
          <span class="section-num">13</span>
          <h2>Prueba Social y Testimonios</h2>
        </div>
        <div class="placeholder-box">
          <span class="badge badge-placeholder mb-12">[Placeholder: Testimonios de Alumnos Verificados en Recolección Activa]</span>
          <h4 style="color: var(--color-navy); margin-bottom: 8px;">Compromiso de Honestidad con Nuestra Comunidad</h4>
          <p class="text-muted" style="max-width: 540px; font-size: 0.9rem;">
            Encardomy no publica testimonios ficticios. Este módulo mostrará opiniones reales y verificadas de estudiantes de preparatoria y facultades conforme completen sus ciclos de evaluación.
          </p>
        </div>
      </div>
    </section>

    <!-- ==========================================================================
         14. ¿CÓMO COMPRAR? / PASO A PASO (METODOLOGÍA SECCIÓN 14)
         ========================================================================== -->
    <section class="section-padding" id="como-comprar">
      <div class="container">
        <div class="product-section-title">
          <span class="section-num">14</span>
          <h2>Cómo Solicitar este Servicio (Paso a Paso)</h2>
        </div>
        <p class="text-muted mb-32">Un proceso sin fricción pensado para resolver tus urgencias escolares en minutos.</p>

        <div class="process-grid">
          <div class="process-step">
            <div class="process-icon process-icon-ai">1</div>
            <h4>1. Cuéntanos tu Necesidad</h4>
            <p class="text-muted" style="font-size: 0.92rem;">
              Haz clic en cotizar y dinos qué materia, tema, extensión o archivos tienes listos.
            </p>
          </div>

          <div class="process-step">
            <div class="process-icon process-icon-deliver">2</div>
            <h4>2. Cotización y Tiempo</h4>
            <p class="text-muted" style="font-size: 0.92rem;">
              Te enviamos una propuesta clara con el plazo exacto de entrega (desde 12 horas) y métodos de pago.
            </p>
          </div>

          <div class="process-step" style="border-color: var(--color-success);">
            <div class="process-icon process-icon-human">3</div>
            <h4 style="color: #167a50;">3. Producción y Entrega</h4>
            <p class="text-muted" style="font-size: 0.92rem;">
              La IA acelera la estructura y nuestro equipo humano revisa y pule cada detalle antes de entregarte tus archivos editables.
            </p>
          </div>
        </div>

        <div class="text-center mt-32">
          <button class="btn btn-primary btn-lg" data-open-order data-service-id="{id}">
            <i data-lucide="message-circle"></i>
            <span>Iniciar Solicitud de {name}</span>
          </button>
        </div>
      </div>
    </section>

    <!-- ==========================================================================
         15. FAQ ESPECÍFICO (METODOLOGÍA SECCIÓN 15)
         ========================================================================== -->
    <section class="section-padding bg-surface" id="faq">
      <div class="container container-narrow">
        <div class="product-section-title">
          <span class="section-num">15</span>
          <h2>Preguntas Frecuentes sobre {name}</h2>
        </div>
        <p class="text-muted mb-24">Resolvemos tus dudas antes de iniciar.</p>

        <div class="faq-list">
          {faq_html}
        </div>
      </div>
    </section>
  </main>

  <!-- ==========================================================================
       FOOTER GLOBAL
       ========================================================================== -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <div class="brand-logo mb-16" style="color: #FFFFFF;">
            <span class="logo-symbol">E</span>
            <span>Encardomy</span>
          </div>
          <p style="color: #9cb5d3; font-size: 0.92rem; max-width: 320px;">
            Plataforma de servicios académicos inteligentes para estudiantes. Combinamos la aceleración de la IA con la revisión y verificación de personas expertas.
          </p>
        </div>

        <div>
          <h4 class="footer-col-title">Categorías</h4>
          <ul class="footer-links">
            <li><a href="../categorias.html?cat=estudiar">Estudiar</a></li>
            <li><a href="../categorias.html?cat=mejorar">Mejorar</a></li>
            <li><a href="../categorias.html?cat=crear">Crear</a></li>
            <li><a href="../categorias.html?cat=disenar">Diseñar</a></li>
            <li><a href="../categorias.html?cat=proyectos">Proyectos</a></li>
          </ul>
        </div>

        <div>
          <h4 class="footer-col-title">Servicios Relacionados</h4>
          <ul class="footer-links">
            <li><a href="resumen.html">Resumen Académico</a></li>
            <li><a href="guia-de-estudio.html">Guía de Estudio</a></li>
            <li><a href="correccion-academica.html">Corrección APA</a></li>
            <li><a href="presentacion.html">Presentaciones</a></li>
            <li><a href="flashcards.html">Flashcards Anki</a></li>
          </ul>
        </div>

        <div>
          <h4 class="footer-col-title">Transparencia</h4>
          <p style="color: #9cb5d3; font-size: 0.86rem;" class="mb-16">
            Encardomy promueve el estudio ético, el aprendizaje activo y el rigor académico. Cero promesas falsas de "indetectabilidad".
          </p>
          <button class="btn btn-primary btn-sm btn-block" data-open-order data-service-id="{id}">
            <i data-lucide="message-circle"></i> Cotizar {name}
          </button>
        </div>
      </div>

      <div class="footer-bottom">
        <div>
          &copy; 2026 Encardomy &bull; Identidad visual oficial (#2D7FF9, #123B6A, Sora & Inter).
        </div>
        <div style="display: flex; gap: var(--space-16);">
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
       MODAL DE COTIZACIÓN Y PEDIDO RÁPIDO
       ========================================================================== -->
  <div class="modal-backdrop" id="orderModal" role="dialog" aria-modal="true" aria-labelledby="modalTitle">
    <div class="modal-card">
      <button class="modal-close-btn" id="modalCloseBtn" aria-label="Cerrar ventana">
        <i data-lucide="x" style="width: 20px; height: 20px;"></i>
      </button>

      <div class="mb-24">
        <span class="badge badge-primary mb-8">Cotización Inmediata</span>
        <h3 id="modalTitle" style="color: var(--color-navy);">Configura tu Solicitud</h3>
        <p class="text-muted" style="font-size: 0.9rem;">
          Completa los datos y te generaremos el mensaje listo para enviar a nuestro WhatsApp oficial.
        </p>
      </div>

      <form id="orderForm">
        <div class="form-group">
          <label class="form-label" for="orderServiceSelect">Servicio que necesitas</label>
          <select id="orderServiceSelect" class="form-select" required>
            <option value="{id}" selected>{name}</option>
            <optgroup label="Todos los Servicios">
              <option value="resumen">Resumen Académico Estructurado</option>
              <option value="guia-de-estudio">Guía de Estudio Integral</option>
              <option value="flashcards">Flashcards (Anki / Quizlet / PDF)</option>
              <option value="examen-de-practica">Examen de Práctica y Simulador</option>
              <option value="correccion-academica">Corrección Académica y Normas APA</option>
              <option value="edicion-natural">Edición Natural y Humanización</option>
              <option value="mejora-de-trabajo">Diagnóstico y Mejora de Borrador</option>
              <option value="documento-academico">Documento Académico Base</option>
              <option value="investigacion">Búsqueda Bibliográfica y Marco Teórico</option>
              <option value="presentacion">Presentación Visual (PowerPoint/Canva)</option>
              <option value="infografia">Infografía y Esquemas Visuales</option>
              <option value="proyecto-encardomy">Proyecto Encardomy Semestral</option>
            </optgroup>
          </select>
        </div>

        <div class="grid-2">
          <div class="form-group">
            <label class="form-label" for="orderNameInput">Tu Nombre / Apodo</label>
            <input type="text" id="orderNameInput" class="form-input" placeholder="Ej. Carlos" required>
          </div>
          <div class="form-group">
            <label class="form-label" for="orderLevelSelect">Nivel Académico</label>
            <select id="orderLevelSelect" class="form-select">
              <option value="Preparatoria / Bachillerato">Preparatoria / Bachillerato</option>
              <option value="Universidad / Licenciatura" selected>Universidad / Licenciatura</option>
              <option value="Posgrado / Maestría">Posgrado / Maestría</option>
              <option value="Examen de Admisión">Examen de Admisión</option>
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
