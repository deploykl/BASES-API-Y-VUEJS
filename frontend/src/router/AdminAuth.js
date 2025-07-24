import LoginView from "../views/account/LoginView.vue";
import ProfileView from "../views/account/ProfileView.vue";
import ChangePasswordView from "../views/account/ChangePasswordView.vue";

const AdminAuth = [
  {
    path: "/login",
    name: "login",
    component: LoginView,
    meta: {
      title: "Login",
      requiresUnauth: true,
    },
  },
  {
    path: "/perfil",
    name: "perfil",
    component: ProfileView,
    meta: {
      title: "Perfil",
      requiresAuth: true,
    },
  },
   {
    path: "/change-password",
    name: "change-password",
    component: ChangePasswordView,
    meta: {
      title: "Cambiar Contraseña",
      requiresAuth: true,
    },
  },
];

export default AdminAuth;
