import LoginView from "../views/account/LoginView.vue";
import ProfileView from "../views/account/ProfileView.vue";

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
      requiresUnauth: true,
    },
  },
];

export default AdminAuth;