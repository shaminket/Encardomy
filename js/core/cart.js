/**
 * ENCARDOMY — INFRAESTRUCTURA DE CARRITO SEPARADO POR EXPERIENCIA (js/core/cart.js)
 * Regla 5: UNAM e IPN no mezclan catálogos, precios, inventarios ni procesos de compra.
 * Cada experiencia opera su propio contenedor de carrito ('encardomy_cart_unam' y 'encardomy_cart_ipn').
 */

import { StorageEngine } from './storage.js';
import { EncardomyAnalytics } from '../config/analytics.js';

function getCartKey(institution) {
  const safeInst = institution === 'ipn' ? 'ipn' : 'unam';
  return `encardomy_cart_${safeInst}_v1`;
}

export const CartManager = {
  getItems(institution) {
    return StorageEngine.get(getCartKey(institution), []);
  },

  addItem(institution, item) {
    const items = this.getItems(institution);
    const existingIndex = items.findIndex((i) => i.id === item.id);

    if (existingIndex > -1) {
      const maxAllowed = item.maxUnits || 99;
      const nextQty = Math.min(items[existingIndex].quantity + (item.quantity || 1), maxAllowed);
      items[existingIndex].quantity = nextQty;
      items[existingIndex].notes = item.notes || items[existingIndex].notes;
    } else {
      items.push({
        id: item.id,
        institution,
        title: item.title,
        category: item.category || 'general',
        priceType: item.priceType || 'fixed', // 'fixed' | 'quote' | 'variable'
        unitPrice: typeof item.unitPrice === 'number' ? item.unitPrice : null,
        priceLabel: item.priceLabel || '',
        quantity: item.quantity || 1,
        maxUnits: item.maxUnits || 99,
        notes: item.notes || '',
        addedAt: new Date().toISOString()
      });
    }

    StorageEngine.set(getCartKey(institution), items);
    EncardomyAnalytics.track('add_to_cart', {
      institution,
      itemId: item.id,
      title: item.title,
      quantity: item.quantity || 1
    });

    this.updateCartBadges(institution);
    return items;
  },

  removeItem(institution, itemId) {
    const items = this.getItems(institution).filter((i) => i.id !== itemId);
    StorageEngine.set(getCartKey(institution), items);
    this.updateCartBadges(institution);
    return items;
  },

  clear(institution) {
    StorageEngine.remove(getCartKey(institution));
    this.updateCartBadges(institution);
  },

  getSummary(institution) {
    const items = this.getItems(institution);
    let fixedSubtotal = 0;
    let hasVariableOrQuote = false;
    let totalUnits = 0;

    items.forEach((item) => {
      totalUnits += item.quantity;
      if (item.priceType === 'fixed' && typeof item.unitPrice === 'number') {
        fixedSubtotal += item.unitPrice * item.quantity;
      } else {
        hasVariableOrQuote = true;
      }
    });

    return {
      institution,
      items,
      totalUnits,
      fixedSubtotal,
      hasVariableOrQuote
    };
  },

  updateCartBadges(institution) {
    const summary = this.getSummary(institution);
    const badges = document.querySelectorAll(`[data-cart-count="${institution}"]`);
    badges.forEach((el) => {
      el.textContent = String(summary.totalUnits);
    });
  }
};
