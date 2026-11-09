/**
 * ENCARDOMY — INFRAESTRUCTURA COMPARTIDA DE PERSISTENCIA (js/core/storage.js)
 * Aísla los estados por experiencia institucional para que nunca se mezclen
 * catálogos, carritos ni inventarios entre UNAM e IPN.
 */

export const StorageEngine = {
  get(key, fallback = null) {
    try {
      const raw = localStorage.getItem(key);
      return raw ? JSON.parse(raw) : fallback;
    } catch {
      return fallback;
    }
  },

  set(key, value) {
    try {
      localStorage.setItem(key, JSON.stringify(value));
      return true;
    } catch {
      return false;
    }
  },

  remove(key) {
    try {
      localStorage.removeItem(key);
    } catch {
      // Ignorar errores de almacenamiento restringido
    }
  }
};
