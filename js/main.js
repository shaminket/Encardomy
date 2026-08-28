/**
 * ENCARDOMY — CONTROLADOR PRINCIPAL Y SISTEMA DE COTIZACIÓN / PEDIDOS
 */

document.addEventListener('DOMContentLoaded', () => {
  initNavigation();
  initHeaderScroll();
  initFaqAccordions();
  initOrderModal();
  initCatalogFilters();
});

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
      
      // Cerrar otros si se desea acordeón estricto
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
   MODAL DE COTIZACIÓN Y CONFIGURACIÓN DE PEDIDO
   ========================================================================== */
function initOrderModal() {
  const modalBackdrop = document.getElementById('orderModal');
  if (!modalBackdrop) return;

  const closeBtn = document.getElementById('modalCloseBtn');
  const serviceSelect = document.getElementById('orderServiceSelect');
  const orderForm = document.getElementById('orderForm');
  const sendWhatsAppBtn = document.getElementById('sendWhatsAppBtn');
  const urgencySelect = document.getElementById('orderUrgencySelect');
  const detailsInput = document.getElementById('orderDetailsInput');
  const nameInput = document.getElementById('orderNameInput');
  const educationLevel = document.getElementById('orderLevelSelect');

  // Delegación de eventos para botones de cotización / compra
  document.addEventListener('click', (e) => {
    const trigger = e.target.closest('[data-open-order]');
    if (trigger) {
      e.preventDefault();
      const serviceId = trigger.getAttribute('data-service-id');
      openOrderModal(serviceId);
    }
  });

  function openOrderModal(serviceId) {
    if (serviceSelect && serviceId) {
      serviceSelect.value = serviceId;
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

  // Generador de mensaje estructurado a WhatsApp
  if (orderForm) {
    orderForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const serviceValue = serviceSelect ? serviceSelect.value : 'General';
      const serviceName = (window.ENCARDOMY_SERVICES && window.ENCARDOMY_SERVICES[serviceValue])
        ? window.ENCARDOMY_SERVICES[serviceValue].name 
        : serviceValue;
      
      const userName = nameInput ? nameInput.value.trim() : 'Estudiante';
      const level = educationLevel ? educationLevel.value : 'No especificado';
      const urgency = urgencySelect ? urgencySelect.value : 'Estándar';
      const details = detailsInput ? detailsInput.value.trim() : 'Sin notas adicionales';

      const waNumber = "5215512345678"; // Número de WhatsApp oficial de Encardomy
      const message = `👋 ¡Hola Encardomy! Mi nombre es ${userName}.

` +
                      `📚 *Me gustaría cotizar un servicio:*
` +
                      `• *Servicio:* ${serviceName}
` +
                      `• *Nivel escolar:* ${level}
` +
                      `• *Urgencia requerida:* ${urgency}
` +
                      `• *Detalles / Materia:* ${details}

` +
                      `¿Me podrían indicar los siguientes pasos y propuesta? ¡Gracias!`;

      const encodedUrl = `https://wa.me/${waNumber}?text=${encodeURIComponent(message)}`;
      window.open(encodedUrl, '_blank');
      closeOrderModal();
    });
  }
}

/* ==========================================================================
   FILTROS DE CATÁLOGO (SI EXISTEN EN LA PÁGINA)
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
