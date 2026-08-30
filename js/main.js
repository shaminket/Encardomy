/**
 * ENCARDOMY — CONTROLADOR PRINCIPAL Y SISTEMA DE COTIZACIÓN DINÁMICO
 * Adaptado a la Escuela Nacional Preparatoria 4 "Vidal Castañeda y Nájera" (UNAM)
 * Ecosistema Google Workspace + Compatibilidad Microsoft & Apple
 */

document.addEventListener('DOMContentLoaded', () => {
  initNavigation();
  initHeaderScroll();
  initFaqAccordions();
  initCatalogFilters();
  initOrderModal();
});

/* ==========================================================================
   PLAN DE ESTUDIOS Y GRUPOS OFICIALES DE LA ENP 4 (UNAM)
   ========================================================================== */
const ENP_MATERIAS = {
  "4": [
    "Matemáticas IV (Álgebra y Geometría Analítica)",
    "Física III",
    "Lengua Española",
    "Historia Universal I",
    "Lógica",
    "Geografía",
    "Dibujo II",
    "Educación Estética y Artística IV (Danza / Música / Pintura / Teatro)",
    "Educación Física IV",
    "Informática",
    "Lengua Extranjera IV (Inglés / Francés)",
    "Orientación Educativa IV",
    "otra"
  ],
  "5": [
    "Matemáticas V (Geometría Analítica y Funciones)",
    "Química III",
    "Biología IV",
    "Educación para la Salud",
    "Historia de México II",
    "Etimologías Grecolatinas del Español",
    "Ética",
    "Literatura Mexicana e Iberoamericana",
    "Lengua Extranjera V (Inglés / Francés)",
    "Educación Estética y Artística V",
    "Educación Física V",
    "Orientación Educativa V",
    "otra"
  ],
  "6": [
    "Derecho (Tronco Común)",
    "Literatura Universal (Tronco Común)",
    "Psicología (Tronco Común)",
    "Lengua Extranjera VI (Inglés / Francés)",
    "Matemáticas VI (Área 1 / 2 / 3)",
    "Física IV (Área 1)",
    "Química IV (Área 1 / 2)",
    "Dibujo Constructivo II (Área 1)",
    "Geología y Mineralogía (Área 1)",
    "Astronomía (Área 1)",
    "Biología V (Área 2)",
    "Fisiología e Higiene (Área 2)",
    "Geografía Económica (Área 3)",
    "Sociología (Área 3)",
    "Problemas Sociales, Económicos y Políticos de México (Área 3)",
    "Introducción al Estudio de las Ciencias Sociales (Área 3)",
    "Contabilidad y Gestión Administrativa (Área 3)",
    "Historia del Arte (Área 4)",
    "Historia de las Doctrinas Filosóficas (Área 4)",
    "Pensamiento Filosófico en México (Área 4)",
    "Estética (Área 4)",
    "Comunicación y Medios (Área 4)",
    "Latín (Área 4)",
    "Griego (Área 4)",
    "otra"
  ]
};

const ENP_GRUPOS = {
  "4": Array.from({ length: 70 }, (_, i) => 401 + i), // 401 a 470
  "5": Array.from({ length: 70 }, (_, i) => 501 + i), // 501 a 570
  "6": Array.from({ length: 63 }, (_, i) => 601 + i)  // 601 a 663
};

/* ==========================================================================
   NAVEGACIÓN MÓVIL Y DRAWER ACCESIBLE
   ========================================================================== */
function initNavigation() {
  const menuToggle = document.getElementById('menuToggleBtn');
  const drawer = document.getElementById('mobileNavDrawer');
  const overlay = document.getElementById('drawerOverlay');
  const closeBtn = document.getElementById('drawerCloseBtn');

  if (!drawer || !overlay) return;

  function openDrawer() {
    drawer.classList.add('open');
    overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
    if (menuToggle) menuToggle.setAttribute('aria-expanded', 'true');
  }

  function closeDrawer() {
    drawer.classList.remove('open');
    overlay.classList.remove('open');
    document.body.style.overflow = '';
    if (menuToggle) menuToggle.setAttribute('aria-expanded', 'false');
  }

  if (menuToggle) menuToggle.addEventListener('click', openDrawer);
  if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
  if (overlay) overlay.addEventListener('click', closeDrawer);

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && drawer.classList.contains('open')) {
      closeDrawer();
    }
  });
}

/* ==========================================================================
   HEADER SCROLL SHADOW
   ========================================================================== */
function initHeaderScroll() {
  const header = document.querySelector('.site-header');
  if (!header) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 20) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  }, { passive: true });
}

/* ==========================================================================
   ACORDEONES DE PREGUNTAS FRECUENTES (FAQ)
   ========================================================================== */
function initFaqAccordions() {
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const questionBtn = item.querySelector('.faq-question');
    if (!questionBtn) return;

    questionBtn.addEventListener('click', () => {
      const isActive = item.classList.contains('active');
      
      faqItems.forEach(other => {
        if (other !== item) {
          other.classList.remove('active');
          const otherBtn = other.querySelector('.faq-question');
          if (otherBtn) otherBtn.setAttribute('aria-expanded', 'false');
        }
      });

      if (isActive) {
        item.classList.remove('active');
        questionBtn.setAttribute('aria-expanded', 'false');
      } else {
        item.classList.add('active');
        questionBtn.setAttribute('aria-expanded', 'true');
      }
    });
  });
}

/* ==========================================================================
   FILTROS DE CATÁLOGO
   ========================================================================== */
function initCatalogFilters() {
  const filterButtons = document.querySelectorAll('.catalog-filter-btn');
  const serviceCards = document.querySelectorAll('.catalog-service-item');
  const searchInput = document.getElementById('catalogSearchInput');

  if (!filterButtons.length && !serviceCards.length) return;

  function filterServices() {
    const activeFilter = document.querySelector('.catalog-filter-btn.active')?.getAttribute('data-filter') || 'all';
    const query = searchInput ? searchInput.value.toLowerCase().trim() : '';

    serviceCards.forEach(card => {
      const category = card.getAttribute('data-category');
      const title = card.querySelector('.service-title')?.textContent.toLowerCase() || '';
      const desc = card.querySelector('.service-desc')?.textContent.toLowerCase() || '';

      const matchesFilter = (activeFilter === 'all' || category === activeFilter);
      const matchesSearch = (!query || title.includes(query) || desc.includes(query));

      if (matchesFilter && matchesSearch) {
        card.style.display = 'flex';
      } else {
        card.style.display = 'none';
      }
    });
  }

  filterButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      filterButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      filterServices();
    });
  });

  if (searchInput) {
    searchInput.addEventListener('input', filterServices);
  }
}

/* ==========================================================================
   MODAL DE COTIZACIÓN INTELIGENTE Y DINÁMICO (EXCLUSIVO PREPA 4)
   ========================================================================== */
function initOrderModal() {
  const modalBackdrop = document.getElementById('orderModal');
  if (!modalBackdrop) return;

  const closeBtn = document.getElementById('modalCloseBtn');
  const orderForm = document.getElementById('orderForm');
  const gradeSelect = document.getElementById('orderGradeSelect');
  const groupSelect = document.getElementById('orderGroupSelect');
  const sectionSelect = document.getElementById('orderSectionSelect');
  const subjectSelect = document.getElementById('orderSubjectSelect');
  const customSubjectWrapper = document.getElementById('customSubjectWrapper');
  const customSubjectInput = document.getElementById('orderCustomSubjectInput');
  const serviceSelect = document.getElementById('orderServiceSelect');
  const nameInput = document.getElementById('orderNameInput');
  const urgencySelect = document.getElementById('orderUrgencySelect');
  const detailsInput = document.getElementById('orderDetailsInput');

  // Flashcards Counter Elements
  const fcTotalInput = document.getElementById('fcTotal');
  const fcEasyInput = document.getElementById('fcEasy');
  const fcMedInput = document.getElementById('fcMed');
  const fcAdvInput = document.getElementById('fcAdv');
  const fcExpInput = document.getElementById('fcExp');
  const fcCounterBadge = document.getElementById('fcCounterBadge');

  // Delegación de eventos para botones de cotización / compra
  document.addEventListener('click', (e) => {
    const trigger = e.target.closest('[data-open-order]');
    if (trigger) {
      e.preventDefault();
      const serviceId = trigger.getAttribute('data-service-id') || 'resumen';
      openOrderModal(serviceId);
    }
  });

  function openOrderModal(serviceId) {
    if (serviceSelect && serviceId) {
      serviceSelect.value = serviceId;
      updateServicePanels(serviceId);
    }
    modalBackdrop.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeOrderModal() {
    modalBackdrop.classList.remove('open');
    document.body.style.overflow = '';
  }

  if (closeBtn) closeBtn.addEventListener('click', closeOrderModal);
  modalBackdrop.addEventListener('click', (e) => {
    if (e.target === modalBackdrop) closeOrderModal();
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modalBackdrop.classList.contains('open')) {
      closeOrderModal();
    }
  });

  // 1. Manejador dinámico de Grado -> Carga Grupos y Materias correspondientes
  if (gradeSelect) {
    gradeSelect.addEventListener('change', () => {
      const selectedGrade = gradeSelect.value;
      updateGradeDependents(selectedGrade);
    });
  }

  function updateGradeDependents(grade) {
    if (!grade) {
      if (groupSelect) {
        groupSelect.innerHTML = '<option value="" disabled selected>Primero elige tu grado</option>';
        groupSelect.disabled = true;
      }
      if (subjectSelect) {
        subjectSelect.innerHTML = '<option value="" disabled selected>Primero elige tu grado</option>';
        subjectSelect.disabled = true;
      }
      if (customSubjectWrapper) customSubjectWrapper.style.display = 'none';
      return;
    }

    // Actualizar Grupos
    if (groupSelect && ENP_GRUPOS[grade]) {
      groupSelect.disabled = false;
      const groups = ENP_GRUPOS[grade];
      let groupHtml = `<option value="" disabled selected>Elige tu grupo de ${grade}°</option>`;
      groups.forEach(g => {
        groupHtml += `<option value="${g}">Grupo ${g}</option>`;
      });
      groupSelect.innerHTML = groupHtml;
    }

    // Actualizar Materias
    if (subjectSelect && ENP_MATERIAS[grade]) {
      subjectSelect.disabled = false;
      const subjects = ENP_MATERIAS[grade];
      let subjectHtml = `<option value="" disabled selected>Selecciona la materia (${grade}° Año)</option>`;
      subjects.forEach(sub => {
        if (sub === 'otra') {
          subjectHtml += `<option value="otra">➕ Otra materia (especificar)...</option>`;
        } else {
          subjectHtml += `<option value="${sub}">${sub}</option>`;
        }
      });
      subjectSelect.innerHTML = subjectHtml;
    }

    if (customSubjectWrapper) customSubjectWrapper.style.display = 'none';
  }

  // 2. Manejador de Materia "Otra..."
  if (subjectSelect) {
    subjectSelect.addEventListener('change', () => {
      if (subjectSelect.value === 'otra') {
        if (customSubjectWrapper) {
          customSubjectWrapper.style.display = 'block';
          if (customSubjectInput) customSubjectInput.focus();
        }
      } else {
        if (customSubjectWrapper) {
          customSubjectWrapper.style.display = 'none';
        }
      }
    });
  }

  // 3. Manejador de Paneles Dinámicos por Servicio
  if (serviceSelect) {
    serviceSelect.addEventListener('change', () => {
      updateServicePanels(serviceSelect.value);
    });
  }

  function updateServicePanels(serviceId) {
    const panels = document.querySelectorAll('.service-dynamic-panel');
    panels.forEach(panel => {
      panel.style.display = 'none';
      panel.classList.remove('active');
    });

    const activePanel = document.getElementById(`servicePanel-${serviceId}`);
    if (activePanel) {
      activePanel.style.display = 'block';
      activePanel.classList.add('active');
    }

    if (serviceId === 'flashcards') {
      updateFlashcardsCounter();
    }
  }

  // 4. Validador en Tiempo Real de Flashcards por Dificultad
  function updateFlashcardsCounter() {
    if (!fcTotalInput || !fcCounterBadge) return;

    const total = parseInt(fcTotalInput.value, 10) || 0;
    const easy = parseInt(fcEasyInput?.value, 10) || 0;
    const med = parseInt(fcMedInput?.value, 10) || 0;
    const adv = parseInt(fcAdvInput?.value, 10) || 0;
    const exp = parseInt(fcExpInput?.value, 10) || 0;

    const sum = easy + med + adv + exp;

    if (total <= 0) {
      fcCounterBadge.className = 'fc-badge fc-badge-warn';
      fcCounterBadge.textContent = 'Indica el total de fichas';
      return;
    }

    if (sum === total) {
      fcCounterBadge.className = 'fc-badge fc-badge-ok';
      fcCounterBadge.innerHTML = `✓ Exacto: ${sum} de ${total} fichas asignadas`;
    } else if (sum < total) {
      const missing = total - sum;
      fcCounterBadge.className = 'fc-badge fc-badge-warn';
      fcCounterBadge.innerHTML = `⚠️ Faltan ${missing} ficha(s) por asignar (${sum}/${total})`;
    } else {
      const extra = sum - total;
      fcCounterBadge.className = 'fc-badge fc-badge-err';
      fcCounterBadge.innerHTML = `⚠️ Sobran ${extra} ficha(s) (${sum}/${total})`;
    }
  }

  [fcTotalInput, fcEasyInput, fcMedInput, fcAdvInput, fcExpInput].forEach(inp => {
    if (inp) inp.addEventListener('input', updateFlashcardsCounter);
  });

  // 5. Envío Inteligente y Formateo a WhatsApp (+52 55 7198 5641)
  if (orderForm) {
    orderForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const serviceId = serviceSelect ? serviceSelect.value : 'resumen';
      const serviceName = (window.ENCARDOMY_SERVICES && window.ENCARDOMY_SERVICES[serviceId])
        ? window.ENCARDOMY_SERVICES[serviceId].name 
        : serviceId;

      const userName = nameInput ? nameInput.value.trim() : 'Estudiante';
      const gradeVal = gradeSelect ? gradeSelect.value : 'No especificado';
      const groupVal = groupSelect ? groupSelect.value : 'No especificado';
      const sectionVal = sectionSelect ? sectionSelect.value : 'No especificada';
      
      let subjectVal = subjectSelect ? subjectSelect.value : 'No especificada';
      if (subjectVal === 'otra' && customSubjectInput && customSubjectInput.value.trim()) {
        subjectVal = customSubjectInput.value.trim() + " (Materia específica)";
      }

      const urgency = urgencySelect ? urgencySelect.value : 'Estándar';
      const generalNotes = detailsInput ? detailsInput.value.trim() : 'Sin notas generales';

      // Recopilar campos específicos del servicio
      let specificDetails = '';

      if (serviceId === 'resumen') {
        const pages = document.getElementById('resumenPages')?.value || 'No especificada';
        const src = document.getElementById('resumenSource')?.value || 'PDF / Digital';
        const depth = document.getElementById('resumenDepth')?.value || 'Estándar con conceptos y glosario';
        const goal = document.getElementById('resumenGoal')?.value || 'Estudio para examen';
        specificDetails = `• *Extensión original:* ${pages}\n` +
                          `• *Formato fuente:* ${src}\n` +
                          `• *Profundidad:* ${depth}\n` +
                          `• *Propósito:* ${goal}\n` +
                          `• *Entorno:* Google Docs editable + PDF (compatible con Word y Pages)`;
      } else if (serviceId === 'guia-de-estudio') {
        const examDate = document.getElementById('guiaDate')?.value || 'Por definir';
        const target = document.getElementById('guiaTarget')?.value || '10 / Máxima nota';
        const examType = document.getElementById('guiaType')?.value || 'Parcial';
        const itemType = document.getElementById('guiaItems')?.value || 'Teóricas y prácticas';
        const diffTopics = document.getElementById('guiaDifficultTopics')?.value.trim() || 'Temario general';
        specificDetails = `• *Fecha del Examen:* ${examDate}\n` +
                          `• *Meta / Calificación esperada:* ${target}\n` +
                          `• *Tipo de examen:* ${examType}\n` +
                          `• *Tipo de reactivos:* ${itemType}\n` +
                          `• *Temas prioritarios / difíciles:* ${diffTopics}\n` +
                          `• *Entorno:* Google Docs + PDF interactivo (compatible con Word y Pages)`;
      } else if (serviceId === 'flashcards') {
        const total = document.getElementById('fcTotal')?.value || '30';
        const easy = document.getElementById('fcEasy')?.value || '0';
        const med = document.getElementById('fcMed')?.value || '0';
        const adv = document.getElementById('fcAdv')?.value || '0';
        const exp = document.getElementById('fcExp')?.value || '0';
        const content = document.getElementById('fcContent')?.value || 'Conceptos clave';
        const app = document.getElementById('fcApp')?.value || 'Google Sheets + Anki (.apkg)';
        specificDetails = `• *Total de Flashcards:* ${total} tarjetas\n` +
                          `• *Distribución:* ${easy} Fáciles, ${med} Medias, ${adv} Avanzadas, ${exp} Expertas\n` +
                          `• *Tipo de contenido:* ${content}\n` +
                          `• *Formato de estudio:* ${app}`;
      } else if (serviceId === 'examen-de-practica') {
        const count = document.getElementById('simQuestionsCount')?.value || '30';
        const diff = document.getElementById('simDifficulty')?.value || 'Nivel Examen UNAM';
        const multi = document.getElementById('simMultiSubject')?.value.trim() || 'Materia única seleccionada';
        const teacher = document.getElementById('simTeacherName')?.value.trim() || 'No especificado';
        const teacherStyle = document.getElementById('simTeacherStyle')?.value || 'Preguntas conceptuales y problemas';
        const examDate = document.getElementById('simDate')?.value || 'Por definir';
        const targetGrade = document.getElementById('simTargetGrade')?.value || '10 / Exentar';
        specificDetails = `• *Reactivos solicitados:* ${count} preguntas\n` +
                          `• *Dificultad simulador:* ${diff}\n` +
                          `• *Desglose de materias:* ${multi}\n` +
                          `• *Profesor(a):* ${teacher}\n` +
                          `• *Estilo de evaluación:* ${teacherStyle}\n` +
                          `• *Fecha examen y Meta:* ${examDate} (${targetGrade})\n` +
                          `• *Solucionario:* Razonado paso a paso con Google Forms / Docs + PDF`;
      } else if (serviceId === 'correccion-academica') {
        const length = document.getElementById('corrLength')?.value || '5 a 15 cuartillas';
        const norm = document.getElementById('corrCitation')?.value || 'APA 7ma edición';
        const prio = document.getElementById('corrPriority')?.value || 'Ortografía, estilo y citas completas';
        const format = document.getElementById('corrFormat')?.value || 'Google Docs con sugerencias';
        specificDetails = `• *Extensión aproximada:* ${length}\n` +
                          `• *Norma de citación:* ${norm}\n` +
                          `• *Prioridad de corrección:* ${prio}\n` +
                          `• *Formato de entrega:* ${format} (exportable a Word .docx y Pages)`;
      } else if (serviceId === 'edicion-natural') {
        const length = document.getElementById('editLength')?.value || '1,500 a 3,500 palabras';
        const origin = document.getElementById('editOrigin')?.value || 'Borrador asistido con IA';
        const tone = document.getElementById('editTone')?.value || 'Estudiantil formal y fluido';
        const goal = document.getElementById('editGoal')?.value || 'Humanización y naturalidad total';
        specificDetails = `• *Volumen del borrador:* ${length}\n` +
                          `• *Origen del texto:* ${origin}\n` +
                          `• *Tono buscado:* ${tone}\n` +
                          `• *Enfoque:* ${goal}\n` +
                          `• *Entorno:* Google Docs editable + PDF (compatible con Word y Pages)`;
      } else if (serviceId === 'mejora-de-trabajo') {
        const goal = document.getElementById('mejoraGoal')?.value || 'Subir de 7 a 10';
        const weak = document.getElementById('mejoraWeak')?.value || 'Marco teórico y bibliografía';
        const rubric = document.getElementById('mejoraRubric')?.value.trim() || 'Rúbrica estándar de la materia';
        specificDetails = `• *Meta de calificación:* ${goal}\n` +
                          `• *Puntos débiles a reforzar:* ${weak}\n` +
                          `• *Detalles de rúbrica:* ${rubric}\n` +
                          `• *Entorno:* Google Docs enriquecido + Reporte de auditoría`;
      } else if (serviceId === 'documento-academico') {
        const type = document.getElementById('docType')?.value || 'Ensayo formal';
        const topic = document.getElementById('docTopic')?.value.trim() || 'Tema de la materia';
        const length = document.getElementById('docLength')?.value || '3 a 6 cuartillas';
        const sources = document.getElementById('docSources')?.value || 'Mínimo 5 fuentes Scielo/UNAM';
        specificDetails = `• *Tipo de documento:* ${type}\n` +
                          `• *Tema y Tesis:* ${topic}\n` +
                          `• *Extensión:* ${length}\n` +
                          `• *Requisitos de fuentes:* ${sources}\n` +
                          `• *Entorno:* Google Docs estructurado + PDF con citas APA 7 verificadas`;
      } else if (serviceId === 'investigacion') {
        const topic = document.getElementById('invTopic')?.value.trim() || 'Tema de investigación';
        const count = document.getElementById('invCount')?.value || '10 fuentes indexadas';
        const lang = document.getElementById('invLang')?.value || 'Español e Inglés';
        const deliv = document.getElementById('invDeliverable')?.value || 'Marco Teórico en Google Docs + Fichas en Sheets';
        specificDetails = `• *Tema y Palabras Clave:* ${topic}\n` +
                          `• *Cantidad de fuentes:* ${count}\n` +
                          `• *Idiomas requeridos:* ${lang}\n` +
                          `• *Entregables:* ${deliv} (compatible con Zotero / Mendeley)`;
      } else if (serviceId === 'presentacion') {
        const slides = document.getElementById('presSlides')?.value || '10 a 15 diapositivas';
        const topic = document.getElementById('presTopic')?.value.trim() || 'Tema segmentado para exposición';
        const bg = document.getElementById('presBgStyle')?.value || 'Fondo Oscuro (Recomendado)';
        const notes = document.getElementById('presNotes')?.value || 'Sí, notas del orador con guion completo';
        const app = document.getElementById('presApp')?.value || 'Google Slides editable + PDF';
        specificDetails = `• *Número de diapositivas:* ${slides}\n` +
                          `• *Tema delimitado:* ${topic}\n` +
                          `• *Estilo visual de fondo:* ${bg}\n` +
                          `• *Notas del orador:* ${notes}\n` +
                          `• *Herramienta:* ${app} (compatible con PowerPoint, Keynote y Canva)`;
      } else if (serviceId === 'infografia') {
        const palette = document.getElementById('infoPalette')?.value || 'Azul Eléctrico & Marino Encardomy';
        const orient = document.getElementById('infoOrient')?.value || 'Póster vertical (Carta / Tabloide)';
        const type = document.getElementById('infoType')?.value || 'Proceso paso a paso / Diagrama';
        specificDetails = `• *Paleta de colores:* ${palette}\n` +
                          `• *Orientación y formato:* ${orient}\n` +
                          `• *Tipo visual:* ${type}\n` +
                          `• *Entregable:* Google Drawings / Canva editable + PNG 4K + PDF 300 DPI`;
      } else if (serviceId === 'proyecto-encardomy') {
        const type = document.getElementById('projType')?.value || 'Trabajo Integrador Semestral';
        const stage = document.getElementById('projStage')?.value || 'Desde cero';
        const deadlines = document.getElementById('projDeadlines')?.value.trim() || 'Cronograma semestral';
        const rubric = document.getElementById('projRubric')?.value.trim() || 'Lineamientos oficiales ENP 4';
        specificDetails = `• *Tipo de proyecto:* ${type}\n` +
                          `• *Fase actual:* ${stage}\n` +
                          `• *Fechas clave:* ${deadlines}\n` +
                          `• *Lineamientos / Rúbrica:* ${rubric}\n` +
                          `• *Suite:* Google Workspace integral (Docs + Slides + Sheets + Drive)`;
      }

      const waNumber = "525571985641"; // WhatsApp oficial de Encardomy (+52 55 7198 5641)
      
      const message = `👋 ¡Hola Encardomy! Mi nombre es *${userName}*.\n\n` +
                      `🎓 *SOLICITUD DE COTIZACIÓN — PREPA 4 UNAM:*\n` +
                      `• *Plantel:* ENP 4 "Vidal Castañeda y Nájera"\n` +
                      `• *Grado:* ${gradeVal}° Año\n` +
                      `• *Grupo:* ${groupVal}\n` +
                      `• *Sección:* ${sectionVal}\n` +
                      `• *Materia:* ${subjectVal}\n` +
                      `• *Servicio:* ${serviceName}\n` +
                      `• *Urgencia requerida:* ${urgency}\n\n` +
                      `📋 *ESPECIFICACIONES DEL SERVICIO:*\n` +
                      `${specificDetails}\n\n` +
                      `📝 *Notas / Enlaces adicionales:* ${generalNotes}\n\n` +
                      `¿Me podrían compartir la cotización y los siguientes pasos? ¡Muchas gracias!`;

      const encodedUrl = `https://wa.me/${waNumber}?text=${encodeURIComponent(message)}`;
      window.open(encodedUrl, '_blank');
      closeOrderModal();
    });
  }
}
