<template>
  <header id="header" class="header fixed-top">
    <div class="container-fluid d-flex align-items-center justify-content-between">
    <button v-if="!isMobile" class="toggle-btn" @click="toggleSidebar">
        <i :class="isCollapsed ? 'fas fa-bars' : 'fas fa-bars'"></i>
      </button>

      <!-- Botón de toggle para móvil -->
      <button v-if="isMobile" class="mobile-toggle-btn" @click="toggleSidebar">
        <i class="fas fa-bars"></i>
      </button>

      <nav class="header-nav ms-auto">
        <ul class="d-flex align-items-center gap-3">
          <li class="nav-item dropdown">
            <a class="nav-profile d-flex align-items-center" href="#" @click.prevent="toggleDropdown">
              <div class="avatar-container">
                <img :src="userImage" alt="Profile" class="avatar-img">
              </div>
              <span class="user-name">{{ userName }} {{ userLastName }}</span>
              <i class="fas fa-chevron-down ms-2 dropdown-arrow"></i>
            </a>

            <!-- Menú desplegable -->
            <div v-if="showDropdown" class="dropdown-menu">
              <div class="dropdown-header">
                <div class="avatar-container-lg">
                  <img :src="userImage" alt="Profile" class="avatar-img">
                </div>
                <div class="user-info">
                  <div class="user-fullname">{{ userName }} {{ userLastName }}</div>
                  <div class="user-email">{{ userEmail }}</div>
                </div>
              </div>
              <div class="dropdown-divider"></div>
              <a href="#" class="dropdown-item">
                <i class="fas fa-cog"></i> Settings
              </a>
              <a href="#" class="dropdown-item">
                <i class="fas fa-share-alt"></i> Share
              </a>
              <a href="#" class="dropdown-item">
                <i class="fas fa-key"></i> Change Password
              </a>
              <div class="dropdown-divider"></div>
              <a href="#" class="dropdown-item logout-item" @click.prevent="logout">
                <i class="fas fa-sign-out-alt"></i> Logout
              </a>
            </div>
          </li>
        </ul>
      </nav>
    </div>
  </header>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { useRouter } from 'vue-router';
import { api } from '@/components/services/Axios';

const userName = ref('');
const userLastName = ref('');
const userImage = ref('');
const router = useRouter();
const imgServerURL = process.env.VUE_APP_IMG_SERVER;
const showDropdown = ref(false);

const props = defineProps({
  isCollapsed: Boolean,
  isMobile: Boolean
})

const emit = defineEmits(['toggle-sidebar'])

const toggleSidebar = () => {
  emit('toggle-sidebar')
}
// Cerrar el dropdown al hacer clic fuera
const handleClickOutside = (event) => {
  const dropdown = document.querySelector('.dropdown-menu');
  const profileBtn = document.querySelector('.nav-profile');

  if (dropdown && profileBtn &&
    !dropdown.contains(event.target) &&
    !profileBtn.contains(event.target)) {
    showDropdown.value = false;
  }
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
  document.addEventListener('click', handleClickOutside);

});
onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside);
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
  box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
  height: 70px;
  left: var(--sidebar-width, 250px);
  width: calc(100% - var(--sidebar-width, 250px));
  right: 0;
  padding: 0 1rem;
  transition: all 0.3s ease;
  z-index: 1000;
  border-bottom-right-radius: 15px;
  position: relative;
  /* Asegurar que sea fixed */
}

.toggle-btn {
  background: rgba(255, 255, 255, 0.1);
  border: none;
  color: #364257;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-right: 10px;
}

.toggle-btn:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: scale(1.05);
}

.mobile-toggle-btn {
  background: rgba(255, 255, 255, 0.1);
  border: none;
  color: #364257;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
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

/* Dropdown styles */
.dropdown-menu {
  position: absolute;
  right: 15px;
  top: 60px;
  width: 280px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.15);
  z-index: 1001;
  padding: 0;
  overflow: hidden;
  display: block;
}

.dropdown-header {
  display: flex;
  align-items: center;
  padding: 15px;
  background: #f8f9fa;
}

.avatar-container-lg {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  overflow: hidden;
  border: 2px solid rgba(0, 0, 0, 0.1);
  margin-right: 12px;
}

.user-info {
  flex: 1;
}

.user-fullname {
  font-weight: 600;
  color: #333;
  margin-bottom: 3px;
}

.user-email {
  font-size: 0.85rem;
  color: #6c757d;
}

.dropdown-divider {
  height: 1px;
  background: #e9ecef;
  margin: 0;
}

.dropdown-item {
  display: flex;
  align-items: center;
  padding: 10px 15px;
  color: #495057;
  text-decoration: none;
  transition: all 0.2s;
}

.dropdown-item i {
  margin-right: 10px;
  width: 20px;
  text-align: center;
  color: #6c757d;
}

.dropdown-item:hover {
  background: #f8f9fa;
  color: #3F4D67;
}

.dropdown-item:hover i {
  color: #3F4D67;
}

.logout-item {
  color: #dc3545;
}

.logout-item:hover {
  background: rgba(220, 53, 69, 0.1);
}

.dropdown-arrow {
  transition: transform 0.3s;
  font-size: 0.8rem;
}

.nav-profile:hover .dropdown-arrow {
  transform: rotate(180deg);
}

/* Mobile adjustments */
@media (max-width: 768px) {
  .dropdown-menu {
    right: 10px;
    width: 260px;
  }

  .user-name {
    display: none;
  }

  .dropdown-arrow {
    display: none;
  }
}
</style>