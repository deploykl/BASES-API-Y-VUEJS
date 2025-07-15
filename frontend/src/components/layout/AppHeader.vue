<template>
  <header id="header" class="header fixed-top">
    <div class="container-fluid d-flex align-items-center justify-content-between">
      
      <button v-if="!isMobile" class="toggle-btn" @click="toggleSidebar">
        <i :class="[isCollapsed ? 'fas fa-angle-double-right' : 'fas fa-angle-double-left']"></i>
      </button>

      <!-- Botón de toggle para móvil -->
      <button v-if="isMobile" class="mobile-toggle-btn" @click="toggleSidebar">
        <i class="fas fa-bars"></i>
      </button>

      <!-- Navigation -->
      <nav class="header-nav ms-auto">
        <ul class="d-flex align-items-center gap-3">
          <!-- User Profile -->
          <li class="nav-item dropdown">
            <a class="nav-profile d-flex align-items-center" href="#" @click="toggleDropdown">
              <div class="avatar-container">
                <img :src="userImage" alt="Profile" class="avatar-img">
              </div>
              <span class="user-name">{{ userName }} {{ userLastName }}</span>
            </a>
          </li>

          <!-- Logout Button -->
          <li class="nav-item">
            <button class="logout-btn" @click="logout">
              <i class="fas fa-sign-out-alt"></i>
              <span class="logout-text">Salir</span>
            </button>
          </li>
        </ul>
      </nav>
    </div>
  </header>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { api } from '@/components/services/Axios';

const userName = ref('');
const userLastName = ref('');
const userImage = ref('');
const router = useRouter();
const imgServerURL = process.env.VUE_APP_IMG_SERVER;

const props = defineProps({
  isCollapsed: Boolean,
  isMobile: Boolean
});

const emit = defineEmits(['toggle-sidebar']);

const toggleSidebar = () => {
  emit('toggle-sidebar');
};

const fetchUserProfile = async () => {
  const accessToken = localStorage.getItem('auth_token');
  if (accessToken) {
    try {
      const response = await api.get('user/profile/', {
        headers: { Authorization: `Bearer ${accessToken}` }
      });
      userName.value = response.data.first_name || '';
      userLastName.value = response.data.last_name || '';

      if (response.data.image) {
        if (response.data.image.startsWith('http')) {
          userImage.value = response.data.image;
        } else {
          userImage.value = joinUrl(imgServerURL, response.data.image);
        }
      } else {
        userImage.value = joinUrl(imgServerURL, 'img/empty.png');
      }
    } catch (error) {
      console.error('Error al obtener el perfil:', error);
      userImage.value = joinUrl(imgServerURL, 'img/empty.png');
    }
  } else {
    userImage.value = joinUrl(imgServerURL, 'img/empty.png');
  }
};

function joinUrl(base, path) {
  const cleanBase = base.replace(/\/+$/, '');
  const cleanPath = path.replace(/^\/+/, '');
  
  if (cleanPath.startsWith('media/') || cleanPath.startsWith('/media/')) {
    return `${cleanBase}/${cleanPath}`;
  }
  
  return `${cleanBase}/media/${cleanPath}`;
}

onMounted(() => {
  fetchUserProfile();
});

const logout = async () => {
  const refreshToken = localStorage.getItem('refreshToken');

  if (!refreshToken) {
    console.error('No se encontró el token de refresco.');
    return;
  }

  try {
    const response = await api.post('user/logout/', {
      refresh: refreshToken,
    });

    if (response.status === 205) {
      localStorage.removeItem('refreshToken');
      localStorage.removeItem('auth_token');
      localStorage.removeItem('user_name');
      localStorage.removeItem('user_lastname');
      router.push('/');
    }
  } catch (error) {
    console.error('Error al cerrar sesión:', error);
  }
};
</script>

<style scoped>
/* Base Styles */
.header {
  background: #3F4D67;
  box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
  height: 70px;
  left: var(--sidebar-width, 250px);
  width: calc(100% - var(--sidebar-width, 250px));
  right: 0;
  padding: 0 1rem;
  transition: all 0.3s ease;
  z-index: 1000;
  border-bottom-right-radius: 15px;
}

.toggle-btn {
  background: rgba(255, 255, 255, 0.1);
  border: none;
  color: white;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
}

.toggle-btn:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: scale(1.05);
}

.mobile-toggle-btn {
  display: none;
  background: #4CAF50;
  border: none;
  color: white;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-right: 15px;
}

.container-fluid {
  height: 100%;
}

/* Reset list styles */
.header-nav ul {
  list-style: none;
  padding-left: 0;
  margin-bottom: 0;
}

.header-nav li {
  list-style: none;
  display: inline-block;
}

/* User Profile */
.nav-profile {
  text-decoration: none;
  color: white;
  transition: all 0.3s ease;
  padding: 0.5rem 1rem;
  border-radius: 50px;
}

.nav-profile:hover {
  background: rgba(255, 255, 255, 0.15);
}

.avatar-container {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  overflow: hidden;
  border: 2px solid rgba(255, 255, 255, 0.3);
}

.avatar-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.user-name {
  margin-left: 10px;
  font-weight: 500;
}

/* Logout Button */
.logout-btn {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.3);
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 50px;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
}

.logout-btn:hover {
  background: rgba(231, 76, 60, 0.8);
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

/* Ajustes para móvil */
@media (max-width: 768px) {
  .header {
    left: 0;
    padding: 0 0.5rem;
    width: 100% !important;
  }

  .mobile-toggle-btn {
    display: flex;
  }

  .toggle-btn {
    display: none;
  }

  .user-name {
    font-size: 0.8rem;
    margin-left: 5px;
    max-width: 100px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .logout-text {
    display: none;
  }

  .logout-btn i {
    font-size: 1.2rem;
  }

  .avatar-container {
    width: 32px;
    height: 32px;
  }
}
</style>