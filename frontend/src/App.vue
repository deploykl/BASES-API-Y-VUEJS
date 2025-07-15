<template>
  <div class="app-layout">
    <template v-if="shouldShowComponents">
      <AppHeader 
        :isCollapsed="isCollapsed" 
        :isMobile="isMobile"
        @toggle-sidebar="toggleSidebar"
      />
      <div class="main-container">
        <AppSidebar 
          :isCollapsed="isCollapsed"
          :isMobile="isMobile"
          @toggle-collapse="toggleSidebar"
        />
        <main class="content-area" :class="{ 'sidebar-collapsed': isCollapsed }">
          <div class="content-wrapper">
            <router-view />
          </div>
          <AppFooter/>
        </main>
      </div>
    </template>
    
    <template v-else>
      <router-view />
    </template>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { ref, computed, onMounted } from 'vue'
import AppHeader from './components/layout/AppHeader.vue'
import AppFooter from './components/layout/AppFooter.vue'
import AppSidebar from './components/layout/AppSidebar.vue'

const route = useRoute()
const isCollapsed = ref(false)
const isMobile = ref(false)

const shouldShowComponents = computed(() => {
  const hiddenRoutes = [
    'HOME', 
    'login', 
    'password-reset', 
    'reset-password', 
    'reuniones'
  ]
  return !hiddenRoutes.includes(route.name)
})

const toggleSidebar = () => {
  isCollapsed.value = !isCollapsed.value
  updateSidebarWidth()
}

const updateSidebarWidth = () => {
  document.documentElement.style.setProperty(
    '--sidebar-width', 
    isCollapsed.value ? '70px' : '250px'
  )
}

const checkScreenSize = () => {
  isMobile.value = window.innerWidth < 768
  if (isMobile.value) {
    isCollapsed.value = true
  }
  updateSidebarWidth()
}

onMounted(() => {
  checkScreenSize()
  window.addEventListener('resize', checkScreenSize)
})
</script>

<style>
:root {
  --header-height: 70px;
  --sidebar-width: 250px;
  --sidebar-collapsed-width: 70px;
  --transition-speed: 0.3s;
  --footer-height: 60px;
}

html, body, #app, .app-layout {
  height: 100%;
  margin: 0;
  padding: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  display: flex;
  flex-direction: column;
}

.main-container {
  display: flex;
  flex: 1;
  margin-top: var(--header-height);
  position: relative;
  min-height: calc(100vh - var(--header-height));
}

.home {
  background-color: #ffffff;
  padding: 20px;
  border-radius: 20px;
}

.content-area {
  flex: 1;
  padding: 15px;
  transition: margin-left var(--transition-speed) ease;
  width: 100%;
  background-color: #F4F7FA;
  display: flex;
  flex-direction: column;
  min-height: calc(100vh - var(--header-height));
}

.content-wrapper {
  flex: 1;
  padding-bottom: 20px;
}

/* Estilos responsivos solo para layout con sidebar */
@media (min-width: 769px) {
  .content-area {
    margin-left: var(--sidebar-width);
  }
  
  .content-area.sidebar-collapsed {
    margin-left: var(--sidebar-collapsed-width);
  }
}

/* Ajustes para el footer */
footer {
  background: linear-gradient(to right bottom, #011a27, #023047, #03496e);
  color: white;
  padding: 20px 0;
  margin-top: auto;
}
</style>