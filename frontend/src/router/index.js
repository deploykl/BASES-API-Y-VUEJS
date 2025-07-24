import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import DashBoardView from "../views/DashBoardView.vue";
import NotFoundView from "../components/layout/NotFoundView.vue"; // Componente para 404
import AdminPoi from "./AdminPoi";
import AdminAuth from "./AdminAuth";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
    meta: {
      title: "HOME",
      public: true,
    },
  },
  {
    path: "/dashboard",
    name: "dashboard",
    component: DashBoardView,
    meta: {
      title: "DASHBOARD",
      requiresAuth: true,
    },
  },
  {
    path: "/:catchAll(.*)",
    name: "not-found",
    component: NotFoundView,
    meta: {
      title: "Página no encontrada",
      public: true,  // Marca como pública
      hideLayout: true  // Nueva propiedad para ocultar layout
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

// En router.js
router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem('auth_token');
  
  // Si la ruta requiere autenticación y no está logueado
  if (to.meta.requiresAuth && !isAuthenticated) {
    return next('/login');
  }
  
  // Solo redirigir desde login si está autenticado
  if (to.name === 'login' && isAuthenticated) {
    return next('/dashboard');
  }
  
  next();
});
export default router;
