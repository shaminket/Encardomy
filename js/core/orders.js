/**
 * ENCARDOMY — INFRAESTRUCTURA COMPARTIDA DE PEDIDOS E HISTORIAL (js/core/orders.js)
 * Gestiona estados de reservación, confirmación de pedidos e historial separado por institución.
 */

import { StorageEngine } from './storage.js';
import { EncardomyAnalytics } from '../config/analytics.js';

const ORDERS_STORAGE_KEY = 'encardomy_orders_history_v1';

export const OrderManager = {
  getAllOrders() {
    return StorageEngine.get(ORDERS_STORAGE_KEY, []);
  },

  getOrdersByInstitution(institution) {
    if (!institution || institution === 'all') return this.getAllOrders();
    return this.getAllOrders().filter((order) => order.institution === institution);
  },

  createOrder({ institution, customer, items, fixedSubtotal, hasVariableOrQuote, notes }) {
    const orders = this.getAllOrders();
    const folioPrefix = institution === 'ipn' ? 'ENC-IPN' : 'ENC-UNAM';
    const randomCode = Math.floor(100000 + Math.random() * 900000);
    const folio = `${folioPrefix}-${randomCode}`;

    const initialStatus =
      institution === 'ipn'
        ? 'Reservación registrada · Pendiente de confirmación de pago'
        : hasVariableOrQuote
          ? 'Solicitud recibida · En revisión de cotización'
          : 'Pedido registrado · Pendiente de pago ($' + fixedSubtotal + ' MXN)';

    const newOrder = {
      folio,
      institution,
      customer: {
        name: customer.name,
        contact: customer.contact,
        schoolOrArea: customer.schoolOrArea || ''
      },
      items,
      fixedSubtotal,
      hasVariableOrQuote,
      notes: notes || '',
      status: initialStatus,
      createdAt: new Date().toISOString()
    };

    orders.unshift(newOrder);
    StorageEngine.set(ORDERS_STORAGE_KEY, orders);

    EncardomyAnalytics.track('purchase_completed', {
      folio,
      institution,
      fixedSubtotal,
      itemCount: items.length
    });

    return newOrder;
  },

  updateOrderStatus(folio, nextStatus) {
    const orders = this.getAllOrders();
    const target = orders.find((o) => o.folio === folio);
    if (target) {
      target.status = nextStatus;
      StorageEngine.set(ORDERS_STORAGE_KEY, orders);
    }
    return target;
  }
};
