/**
 * ENCARDOMY — MOTOR DE INVENTARIO Y RESERVACIONES IPN (js/ipn/ipn-inventory.js)
 * Gestiona la lógica comercial propia de /ipn/:
 * - Existencias reales por unidades.
 * - Prevención estricta de sobreventas (no permite agregar más unidades que el stock disponible).
 * - Estados de reservación ('Disponible', 'Últimas unidades', 'Agotado').
 * - Condiciones de acceso visibles antes de confirmar pedido.
 * - Cero promesas académicas o puntos extra no autorizados.
 */

import { StorageEngine } from '../core/storage.js';
import { CartManager } from '../core/cart.js';
import { EncardomyAnalytics } from '../config/analytics.js';

const IPN_INVENTORY_STORAGE_KEY = 'encardomy_ipn_inventory_v1';

export const DEFAULT_IPN_INVENTORY = [
  {
    id: 'ipn-boletos-obras-teatrales',
    title: 'Venta de boletos para obras teatrales',
    category: 'Actividades Culturales y Escénicas',
    priceType: 'variable',
    unitPrice: null,
    priceLabel: 'Precio: Variable (según obra y función)',
    availableUnits: 12,
    maxPerOrder: 4,
    includes: [
      'Venta de boletos para la función seleccionada',
      'Entrega de fotografías',
      'Entrega de videos',
      'Un resumen de la obra'
    ],
    accessConditions: [
      'Sujeto a existencias reales por función para evitar sobreventas.',
      'La reservación se confirma una vez validado el pago correspondiente.',
      'El paquete incluye únicamente los entregables culturales descritos (boleto, fotografías, videos y resumen). No otorga ni promete puntos extra ni acreditaciones escolares.'
    ]
  }
];

export const IpnInventoryManager = {
  getInventory() {
    return StorageEngine.get(IPN_INVENTORY_STORAGE_KEY, DEFAULT_IPN_INVENTORY);
  },

  saveInventory(items) {
    StorageEngine.set(IPN_INVENTORY_STORAGE_KEY, items);
  },

  getItem(itemId) {
    return this.getInventory().find((i) => i.id === itemId) || null;
  },

  getAvailabilityBadge(availableUnits) {
    if (availableUnits <= 0) {
      return { label: 'Agotado · 0 unidades', css: 'badge-soldout', canReserve: false };
    }
    if (availableUnits <= 4) {
      return {
        label: `Últimas unidades · ${availableUnits} disponibles`,
        css: 'badge-low',
        canReserve: true
      };
    }
    return {
      label: `Disponible · ${availableUnits} lugares en inventario`,
      css: 'badge-available',
      canReserve: true
    };
  },

  reserveUnits(itemId, requestedUnits, notes = '') {
    const inventory = this.getInventory();
    const target = inventory.find((i) => i.id === itemId);
    if (!target) {
      return { ok: false, message: 'El producto solicitado no existe en el inventario IPN.' };
    }

    const qty = parseInt(String(requestedUnits), 10);
    if (isNaN(qty) || qty < 1) {
      return { ok: false, message: 'Selecciona al menos 1 unidad válida.' };
    }

    if (qty > target.availableUnits) {
      return {
        ok: false,
        message: `Prevención de sobreventa: solo quedan ${target.availableUnits} unidades disponibles.`
      };
    }

    if (qty > target.maxPerOrder) {
      return {
        ok: false,
        message: `El límite máximo por reservación es de ${target.maxPerOrder} unidades.`
      };
    }

    // Descontar unidades reservadas temporalmente para evitar sobreventa
    target.availableUnits -= qty;
    this.saveInventory(inventory);

    CartManager.addItem('ipn', {
      id: target.id,
      title: target.title,
      category: target.category,
      priceType: target.priceType,
      unitPrice: target.unitPrice,
      priceLabel: target.priceLabel,
      quantity: qty,
      maxUnits: target.maxPerOrder,
      notes
    });

    EncardomyAnalytics.track('ticket_interest', {
      institution: 'ipn',
      itemId: target.id,
      reservedUnits: qty,
      remainingUnits: target.availableUnits
    });

    return {
      ok: true,
      remainingUnits: target.availableUnits,
      message: `Se apartaron ${qty} unidad(es) en tu carrito IPN. Quedan ${target.availableUnits} disponibles.`
    };
  },

  updateStockFromAdmin(itemId, newUnits) {
    const inventory = this.getInventory();
    const target = inventory.find((i) => i.id === itemId);
    if (target) {
      target.availableUnits = Math.max(0, parseInt(String(newUnits), 10) || 0);
      this.saveInventory(inventory);
    }
    return target;
  }
};

export function initIpnExperience() {
  CartManager.updateCartBadges('ipn');

  const listContainer = document.querySelector('[data-ipn-inventory-list]');
  if (!listContainer) return;

  function renderInventory() {
    const items = IpnInventoryManager.getInventory();

    listContainer.innerHTML = items
      .map((item) => {
        const status = IpnInventoryManager.getAvailabilityBadge(item.availableUnits);
        const maxSelectable = Math.min(item.availableUnits, item.maxPerOrder);

        return `
        <article class="ipn-event-card" id="${item.id}">
          <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;margin-bottom:14px;">
            <span class="badge badge-ipn">${item.category}</span>
            <span class="badge ${status.css}">${status.label}</span>
          </div>

          <h2>${item.title}</h2>
          <p style="margin-top:6px;font-weight:700;color:var(--color-ipn-guinda);">${item.priceLabel}</p>

          <div style="margin-top:18px;">
            <h3 style="font-size:1rem;margin-bottom:8px;">El servicio incluye:</h3>
            <ul class="unam-spec-list">
              ${item.includes.map((inc) => `<li>${inc}</li>`).join('')}
            </ul>
          </div>

          <div class="ipn-conditions-box">
            <strong style="display:block;color:var(--color-navy-blue);margin-bottom:6px;">Condiciones comerciales y de acceso:</strong>
            <ul class="unam-spec-list" style="margin:0;">
              ${item.accessConditions.map((cond) => `<li>${cond}</li>`).join('')}
            </ul>
          </div>

          <form class="ipn-stock-bar-wrap" data-ipn-reserve-form="${item.id}">
            <div>
              <label class="form-label" for="qty-${item.id}">Unidades a reservar (máx. ${item.maxPerOrder} por pedido)</label>
              <input
                type="number"
                id="qty-${item.id}"
                name="units"
                class="form-control"
                style="max-width:140px;"
                min="1"
                max="${maxSelectable || 1}"
                value="${status.canReserve ? 1 : 0}"
                ${status.canReserve ? '' : 'disabled'}
              >
            </div>
            <div style="flex:1;min-width:220px;">
              <label class="form-label" for="notes-${item.id}">Obra o función requerida</label>
              <input
                type="text"
                id="notes-${item.id}"
                name="notes"
                class="form-control"
                placeholder="Indica el nombre de la obra o fecha de función"
                ${status.canReserve ? 'required' : 'disabled'}
              >
            </div>
            <div style="align-self:flex-end;">
              <button type="submit" class="btn btn-ipn" ${status.canReserve ? '' : 'disabled'}>
                ${status.canReserve ? 'Apartar unidades' : 'Sin existencias'}
              </button>
            </div>
          </form>
          <div data-ipn-msg="${item.id}" style="font-size:0.9rem;font-weight:600;margin-top:8px;"></div>
        </article>
      `;
      })
      .join('');

    listContainer.querySelectorAll('[data-ipn-reserve-form]').forEach((form) => {
      form.addEventListener('submit', (event) => {
        event.preventDefault();
        const itemId = form.getAttribute('data-ipn-reserve-form');
        const data = new FormData(form);
        const units = data.get('units');
        const notes = (data.get('notes') || '').toString().trim();
        const msgBox = listContainer.querySelector(`[data-ipn-msg="${itemId}"]`);

        const result = IpnInventoryManager.reserveUnits(itemId, units, notes);
        renderInventory();

        const updatedMsgBox = listContainer.querySelector(`[data-ipn-msg="${itemId}"]`);
        if (updatedMsgBox) {
          updatedMsgBox.style.color = result.ok
            ? 'var(--status-available-text)'
            : 'var(--status-soldout-text)';
          updatedMsgBox.textContent = result.message;
        }
      });
    });
  }

  renderInventory();
}

document.addEventListener('DOMContentLoaded', initIpnExperience);
