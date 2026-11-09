/**
 * ENCARDOMY — MÓDULO DE EXPERIENCIA UNAM (js/unam/unam-app.js)
 * Gestiona el catálogo exclusivo de la ruta /unam/:
 * - Servicios confirmados (Presentaciones 20×20 por $100 MXN e Impresión de hojas)
 * - Líneas académicas UNAM (Guías de estudio, Resúmenes, Infografías, Materiales, Asesorías, Revisión de trabajos)
 * - Integración con el carrito exclusivo UNAM y solicitud directa.
 */

import { CartManager } from '../core/cart.js';
import { EncardomyAnalytics } from '../config/analytics.js';

export const UNAM_CATALOG = [
  {
    id: 'unam-presentaciones-20x20',
    title: 'Realización de presentaciones 20 × 20',
    category: 'presentaciones',
    categoryLabel: 'Presentaciones y Diseño Visual',
    status: 'active',
    priceType: 'fixed',
    unitPrice: 100,
    priceLabel: '$100 MXN',
    summary: 'Diseño y estructuración profesional de presentaciones bajo el formato 20 × 20 listas para exponer.',
    specs: [
      '20 diapositivas diseñadas con jerarquía visual limpia',
      'Aplicación de la metodología de exposición 1 + 3 = 1 de Encardomy',
      'Tarifa oficial fija establecida: $100 MXN'
    ]
  },
  {
    id: 'unam-impresion-hojas',
    title: 'Impresión de hojas y documentos',
    category: 'impresion',
    categoryLabel: 'Servicios Documentales',
    status: 'active',
    priceType: 'quote',
    unitPrice: null,
    priceLabel: 'Precio no definido (Bajo cotización)',
    summary: 'Servicio de impresión de hojas, trabajos, reportes y documentos académicos.',
    specs: [
      'Recepción de archivos en formato PDF o documento listo para impresión',
      'Cotización personalizada según número de páginas y especificaciones',
      'Entrega acordada tras confirmar tu solicitud'
    ]
  },
  {
    id: 'unam-guias-resumenes',
    title: 'Guías de estudio y resúmenes estructurados',
    category: 'materiales',
    categoryLabel: 'Guías y Resúmenes',
    status: 'custom_request',
    priceType: 'quote',
    unitPrice: null,
    priceLabel: 'Solicitud personalizada',
    summary: 'Elaboración de síntesis académicas, guías de estudio por temario y resúmenes claros para preparación de asignaturas.',
    specs: [
      'Adaptados al temario o bibliografía proporcionada por el estudiante',
      'Organización jerárquica de conceptos clave',
      'Cotización según extensión y nivel de profundidad'
    ]
  },
  {
    id: 'unam-infografias-digitales',
    title: 'Infografías y materiales de aprendizaje',
    category: 'materiales',
    categoryLabel: 'Infografías y Productos Digitales',
    status: 'custom_request',
    priceType: 'quote',
    unitPrice: null,
    priceLabel: 'Solicitud personalizada',
    summary: 'Síntesis visual de procesos, líneas del tiempo, esquemas comparativos y láminas de exposición.',
    specs: [
      'Diseño limpio sin saturación de texto',
      'Formato optimizado para entrega digital o proyección en aula',
      'Cotización previa según requerimientos del tema'
    ]
  },
  {
    id: 'unam-revision-asesorias',
    title: 'Revisión, mejora de trabajos y asesorías',
    category: 'asesorias',
    categoryLabel: 'Asesorías y Revisión Académica',
    status: 'custom_request',
    priceType: 'quote',
    unitPrice: null,
    priceLabel: 'Solicitud personalizada',
    summary: 'Acompañamiento para estructurar proyectos, mejorar redacción, dar formato a entregas y preparar exposiciones.',
    specs: [
      'Revisión de estructura lógica, claridad y presentación documental',
      'Orientación metodológica para exposiciones orales',
      'Sujeto a disponibilidad y alcance del documento'
    ]
  }
];

export function initUnamExperience() {
  CartManager.updateCartBadges('unam');

  const catalogContainer = document.querySelector('[data-unam-catalog]');
  const filterButtons = document.querySelectorAll('[data-unam-filter]');
  const requestForm = document.querySelector('[data-unam-request-form]');
  const feedbackBox = document.querySelector('[data-unam-feedback]');

  function renderCatalog(category = 'all') {
    if (!catalogContainer) return;
    const filtered =
      category === 'all'
        ? UNAM_CATALOG
        : UNAM_CATALOG.filter((item) => item.category === category);

    catalogContainer.innerHTML = filtered
      .map(
        (item) => `
      <article class="unam-service-card" id="${item.id}">
        <div>
          <div class="unam-service-meta">
            <span class="badge badge-unam">${item.categoryLabel}</span>
            <span class="unam-price-tag">${item.priceLabel}</span>
          </div>
          <h3>${item.title}</h3>
          <p style="margin-top:8px;font-size:0.94rem;">${item.summary}</p>
          <ul class="unam-spec-list">
            ${item.specs.map((s) => `<li>${s}</li>`).join('')}
          </ul>
        </div>
        <div style="display:flex;gap:10px;flex-wrap:wrap;padding-top:14px;border-top:1px solid var(--border-subtle);">
          <button type="button" class="btn btn-unam btn-sm" data-add-unam-item="${item.id}">
            Agregar a mi solicitud UNAM
          </button>
          <a href="solicitud.html?item=${encodeURIComponent(item.id)}" class="btn btn-secondary btn-sm">
            Configurar detalles
          </a>
        </div>
      </article>
    `
      )
      .join('');

    catalogContainer.querySelectorAll('[data-add-unam-item]').forEach((btn) => {
      btn.addEventListener('click', () => {
        const itemId = btn.getAttribute('data-add-unam-item');
        const found = UNAM_CATALOG.find((x) => x.id === itemId);
        if (!found) return;

        CartManager.addItem('unam', found);
        EncardomyAnalytics.track('service_interest', {
          institution: 'unam',
          serviceId: found.id
        });
        btn.textContent = 'Agregado a solicitud UNAM ✓';
        setTimeout(() => {
          btn.textContent = 'Agregar a mi solicitud UNAM';
        }, 1600);
      });
    });
  }

  if (filterButtons.length && catalogContainer) {
    filterButtons.forEach((btn) => {
      btn.addEventListener('click', () => {
        filterButtons.forEach((b) => b.classList.remove('active'));
        btn.classList.add('active');
        renderCatalog(btn.getAttribute('data-unam-filter'));
      });
    });
    renderCatalog('all');
  }

  if (requestForm) {
    const select = requestForm.querySelector('[name="serviceId"]');
    const params = new URLSearchParams(window.location.search);
    const preselected = params.get('item');
    if (select && preselected) {
      select.value = preselected;
    }

    requestForm.addEventListener('submit', (event) => {
      event.preventDefault();
      const data = new FormData(requestForm);
      const serviceId = (data.get('serviceId') || '').toString();
      const quantity = Math.max(1, parseInt((data.get('quantity') || '1').toString(), 10));
      const notes = (data.get('notes') || '').toString().trim();

      const item = UNAM_CATALOG.find((x) => x.id === serviceId) || UNAM_CATALOG[0];
      CartManager.addItem('unam', {
        ...item,
        quantity,
        notes
      });

      if (feedbackBox) {
        feedbackBox.hidden = false;
      }
    });
  }
}

document.addEventListener('DOMContentLoaded', initUnamExperience);
