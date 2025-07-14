<template>
  <div class="app-layout">
    <template v-if="shouldShowComponents">
      <AppHeader/>
      <div class="main-container">
        <AppSidebar 
          @toggle-collapse="handleSidebarToggle"
          :is-collapsed="isSidebarCollapsed"
        />
        <main class="content-area" :class="{ 'sidebar-collapsed': isSidebarCollapsed }">
          <router-view />
          
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
import { ref, computed } from 'vue'
import AppHeader from './components/layout/AppHeader.vue'
import AppFooter from './components/layout/AppFooter.vue'
import AppSidebar from './components/layout/AppSidebar.vue'

const route = useRoute()
const isSidebarCollapsed = ref(false)

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

const handleSidebarToggle = (collapsed) => {
  isSidebarCollapsed.value = collapsed
}
</script>
<style>
:root {
  --header-height: 70px;
  --sidebar-width: 250px;
  --sidebar-collapsed-width: 70px;
  --transition-speed: 0.3s;
}

html, body, #app {
  height: 100%;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

/* Solo aplica estos estilos cuando shouldShowComponents es true */
.main-container {
  display: flex;
  flex: 1;
  margin-top: var(--header-height);
  position: relative;
}

.content-area {
  flex: 1;
  padding: 20px;
  transition: margin-left var(--transition-speed) ease;
  width: 100%;
  min-height: calc(100vh - var(--header-height));
  background-color: #f8f9fa;
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
</style>
