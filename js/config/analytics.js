/**
 * ENCARDOMY — CAPA DE MEDICIÓN Y EVENTOS FUTUROS (js/config/analytics.js)
 * Preparada para medir conversiones por ruta sin ejecutar campañas publicitarias
 * no autorizadas ni agregar elementos visibles en la portada.
 *
 * Eventos soportados:
 * - view_experience_unam
 * - view_experience_ipn
 * - view_brand_encardomy
 * - view_product
 * - service_interest
 * - ticket_interest
 * - add_to_cart
 * - begin_checkout
 * - purchase_completed
 */

const ANALYTICS_STORAGE_KEY = 'encardomy_analytics_log_v1';
const CONSENT_STORAGE_KEY = 'encardomy_analytics_consent_v1';

export const EncardomyAnalytics = {
  hasConsent() {
    try {
      return localStorage.getItem(CONSENT_STORAGE_KEY) !== 'denied';
    } catch {
      return true;
    }
  },

  setConsent(status) {
    try {
      localStorage.setItem(CONSENT_STORAGE_KEY, status ? 'granted' : 'denied');
    } catch {
      // Sin bloqueo en navegación privada
    }
  },

  track(eventName, payload = {}) {
    if (!this.hasConsent()) return;

    const entry = {
      event: eventName,
      path: window.location.pathname,
      timestamp: new Date().toISOString(),
      ...payload
    };

    try {
      const current = JSON.parse(localStorage.getItem(ANALYTICS_STORAGE_KEY) || '[]');
      current.push(entry);
      // Conservar los últimos 100 eventos para diagnóstico y futura conexión de píxel
      while (current.length > 100) current.shift();
      localStorage.setItem(ANALYTICS_STORAGE_KEY, JSON.stringify(current));
    } catch {
      // Fallback silencioso
    }

    if (typeof window.dataLayer !== 'undefined' && Array.isArray(window.dataLayer)) {
      window.dataLayer.push(entry);
    }
  },

  getRecentEvents() {
    try {
      return JSON.parse(localStorage.getItem(ANALYTICS_STORAGE_KEY) || '[]');
    } catch {
      return [];
    }
  }
};

// Detección automática de ruta e interacción en portada
document.addEventListener('DOMContentLoaded', () => {
  const path = window.location.pathname;

  if (path.includes('/unam/')) {
    EncardomyAnalytics.track('view_experience_unam', { experience: 'unam' });
  } else if (path.includes('/ipn/')) {
    EncardomyAnalytics.track('view_experience_ipn', { experience: 'ipn' });
  } else if (path.includes('/encardomy/')) {
    EncardomyAnalytics.track('view_brand_encardomy', { experience: 'encardomy' });
  }

  // Enlaces interactivos de la portada (con animación circular de salida suave al hacer clic)
  const portalLinks = document.querySelectorAll('[data-portal-link]');
  const viewport = document.querySelector('[data-portal-viewport]');

  portalLinks.forEach((link) => {
    link.addEventListener('click', (event) => {
      const targetExperience = link.getAttribute('data-portal-link');
      const href = link.getAttribute('href');
      EncardomyAnalytics.track(`portal_select_${targetExperience}`, {
        destination: href
      });

      if (viewport && !event.metaKey && !event.ctrlKey && !event.shiftKey) {
        event.preventDefault();
        viewport.style.transition = 'clip-path 320ms cubic-bezier(0.4, 0, 0.2, 1), opacity 280ms ease';
        viewport.style.clipPath = 'circle(0% at 50% 50%)';
        viewport.style.opacity = '0';
        setTimeout(() => {
          window.location.href = href;
        }, 280);
      }
    });
  });
});
