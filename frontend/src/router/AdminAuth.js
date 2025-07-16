import LoginView from "../views/account/LoginView.vue";

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
];

export default AdminAuth;