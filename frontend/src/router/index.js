import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import NotFoundView from '../components/layout/NotFoundView.vue'; // Componente para 404
import AdminPoi from './AdminPoi';
import AdminAuth from './AdminAuth';

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
    meta: {
      title: "HOME",
    },
  },
  {
    path: '/:catchAll(.*)',
    name: 'not-found',
    component: NotFoundView,
    meta: {
      title: 'Página no encontrada',
    },
  },
  // INTEGRANDO POI ADMIN ROUTES
  ...AdminPoi,
  ...AdminAuth,
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
