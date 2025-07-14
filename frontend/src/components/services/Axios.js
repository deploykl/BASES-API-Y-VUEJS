import axios from 'axios';
import router from '@/router';

// Función para obtener el token de autenticación (versión mejorada)
export const getAuthToken = () => {
  return localStorage.getItem('auth_token'); // Simplemente retorna el token sin validar
};

const api = axios.create({
  baseURL: process.env.VUE_APP_API_BASE_URL,
});

// Interceptor de solicitudes mejorado
api.interceptors.request.use(
  config => {
    // Excluir rutas que no requieren autenticación
    const publicRoutes = ['user/login/', 'user/register/']; // Agrega otras rutas públicas si es necesario
    
    const isPublicRoute = publicRoutes.some(route => config.url.includes(route));
    
    if (!isPublicRoute) {
      const token = getAuthToken();
      if (token) {
        config.headers.Authorization = `Bearer ${token}`;
      } else {
        // Redirigir solo si no es una ruta pública
        router.push('/login');
        return Promise.reject(new Error('Token de autenticación no encontrado'));
      }
    }
    
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

// Interceptor de respuestas (se mantiene igual)
api.interceptors.response.use(
  response => response,
  error => {
    if (error.response && error.response.status === 401) {
      localStorage.removeItem('auth_token');
      localStorage.removeItem('refreshToken');
      localStorage.removeItem('is_superuser');
      localStorage.removeItem('is_staff');
      router.push('/login');
    } else if (error.response && error.response.status === 500) {
      console.error('Server error:', error.response.data);
    }
    return Promise.reject(error);
  }
);

export { api };