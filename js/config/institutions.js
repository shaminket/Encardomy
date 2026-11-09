/**
 * ENCARDOMY — REGISTRO ESCALABLE DE EXPERIENCIAS INSTITUCIONALES (js/config/institutions.js)
 * Permite agregar nuevas instituciones en el futuro sin reconstruir la infraestructura.
 * UNAM e IPN son las dos experiencias iniciales.
 */

export const INSTITUTIONS_REGISTRY = {
  encardomy: {
    id: 'encardomy',
    name: 'Encardomy',
    route: '/encardomy/index.html',
    type: 'brand_editorial',
    emblem: '../assets/images/encardomy.png'
  },
  unam: {
    id: 'unam',
    name: 'Comunidad UNAM',
    fullName: 'Universidad Nacional Autónoma de México',
    route: '/unam/index.html',
    type: 'academic_services_and_materials',
    emblem: '../assets/images/unam.png',
    currency: 'MXN'
  },
  ipn: {
    id: 'ipn',
    name: 'Comunidad IPN',
    fullName: 'Instituto Politécnico Nacional',
    route: '/ipn/index.html',
    type: 'inventory_events_and_tickets',
    emblem: '../assets/images/ipn.png',
    currency: 'MXN'
  }
};

export function getInstitutionConfig(institutionId) {
  return INSTITUTIONS_REGISTRY[institutionId] || null;
}
