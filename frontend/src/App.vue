<template>
  <div class="app-layout">
    <template v-if="shouldShowLayout">
      <AppHeader :is-collapsed="isCollapsed" :is-mobile="isMobile" @toggle-sidebar="toggleSidebar" />
      <div class="main-container">
        <AppSidebar :is-collapsed="isCollapsed" :is-mobile="isMobile" @toggle-collapse="toggleSidebar" />
        <div class="content-wrapper">
          <main class="content-area">
            <router-view />
          </main>
          <AppFooter />
        </div>
      </div>
    </template>
    <template v-else>
      <router-view />
    </template>
  </div>
</template>

<script setup>
import { computed, onMounted, onUnmounted, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import AppHeader from './components/layout/AppHeader.vue'
import AppFooter from './components/layout/AppFooter.vue'
import AppSidebar from './components/layout/AppSidebar.vue'

const route = useRoute()
const isCollapsed = ref(false)
const isMobile = ref(false)

const shouldShowLayout = computed(() => {
  const hiddenRoutes = ['not-found', 'login'];
  const isAuthenticated = localStorage.getItem('auth_token');
  
  // No mostrar layout para rutas ocultas o si no está autenticado (excepto login)
  return !hiddenRoutes.includes(route.name) && (isAuthenticated || route.name === 'login');
});

const updateCssVariables = () => {
  const width = isCollapsed.value ? '0px' : '250px'
  document.documentElement.style.setProperty('--sidebar-width', width)
}

const checkScreenSize = () => {
  isMobile.value = window.innerWidth < 768
  // Solo establecer el estado inicial si no ha sido modificado por el usuario
  if (isMobile.value && !localStorage.getItem('sidebar-state-changed')) {
    isCollapsed.value = true
  }
  updateCssVariables()
}

const toggleSidebar = () => {
  isCollapsed.value = !isCollapsed.value
  // Marcar que el usuario ha modificado el estado
  localStorage.setItem('sidebar-state-changed', 'true')
}

watch(isCollapsed, updateCssVariables)

onMounted(() => {
  checkScreenSize()
  window.addEventListener('resize', checkScreenSize)
})

onUnmounted(() => {
  window.removeEventListener('resize', checkScreenSize)
})
</script>

<style>
:root {
  --sidebar-width: 250px;
  --transition-speed: 0.3s;
}

html,
body,
#app,
.app-layout {
  height: 100%;
  margin: 0;
  padding: 0;
  background-color: #F4F7FA;
}

.app-layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  /* Usar viewport height */
}

.main-container {
  display: flex;
  flex: 1;
  padding: 15px;
}

.content-wrapper {
  flex: 1;
  display: flex;
  flex-direction: column;
  width: 100%;
  margin-left: var(--sidebar-width);
}

.content-area {
  flex: 1;
  padding: 15px;
  transition: margin-left var(--transition-speed) ease;
}

@media (max-width: 768px) {
  .content-wrapper {
    margin-left: 0;
  }
}

.home {
  background-color: #ffffff;
  border-radius: 20px;
  padding: 20px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  border: 1px solid rgba(0, 0, 0, 0.05);
  margin-bottom: 20px;
}
</style>