<template>
  <!-- Contenedor para los botones -->
  <div class="btn-container">
    <!-- Botón de retroceso -->
    <button 
      class="btn btn-warning btn-float btn-back" 
      @click="goBack"
      :disabled="isOnActividades">
      <i class="fas fa-arrow-left"></i>
    </button>

    <!-- Botón de inicio -->
    <router-link :to="{ name: 'actividades' }" class="btn-link">
      <button class="btn btn-success btn-float">
        <i class="fas fa-home"></i>
      </button>
    </router-link>
    
    <!-- Botón de avance -->
    <button class="btn btn-info btn-float btn-forward" @click="goForward">
      <i class="fas fa-arrow-right"></i>
    </button>

    <!-- Botón Dashboard rectangular -->
    <router-link :to="{ name: 'dashboard' }" class="btn-dashboard">
      <button class="btn btn-primary">
        <i class="fas fa-tachometer-alt me-2"></i>
        Dashboard
      </button>
    </router-link>
  </div>
</template>

<script setup>
import { useRouter, useRoute } from 'vue-router';
import { computed } from 'vue';

const router = useRouter();
const route = useRoute();

const goBack = () => {
  if (!isOnActividades.value) {
    router.go(-1);
  }
};

const goForward = () => {
  router.go(1);
};

const isOnActividades = computed(() => {
  return route.name === 'actividades';
});
</script>

<style scoped>
.btn-container {
  position: relative;
  display: flex;
  flex-direction: row;
  gap: 8px;
  align-items: center;
}

.btn-link {
  display: flex;
  text-decoration: none;
}

.btn-dashboard {
  margin-left: auto; /* Empuja el botón a la derecha */
  text-decoration: none;
}

/* Estilo para botones circulares */
.btn-float {
  border-radius: 50%;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 25px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  cursor: pointer;
  transition: all 0.3s ease;
  border: 2px solid #fff;
}

/* Estilo para botón Dashboard rectangular */
.btn-dashboard .btn {
  border-radius: 20px; /* Bordes ligeramente redondeados */
  padding: 8px 16px;
  display: flex;
  align-items: center;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  transition: all 0.3s ease;
  border: 2px solid #fff;
}

.btn-float:disabled {
  cursor: not-allowed;
  opacity: 0.5;
}

.btn-float:hover,
.btn-dashboard .btn:hover {
  background-color: #fff;
  color: #333;
  border: 2px solid #333;
}

.btn-back {
  background-color: #9c3e32;
  color: #fff;
}

.btn-forward {
  background-color: #14517a;
  color: #fff;
}

.btn-primary {
  background-color: #3b82f6;
  color: #fff;
}

.btn-back:hover {
  background-color: #fff;
  color: #9c3e32;
}

.btn-forward:hover {
  background-color: #fff;
  color: #3498db;
}

.btn-primary:hover {
  background-color: #fff;
  color: #3b82f6;
}

/* Ajuste para ícono dentro del botón Dashboard */
.btn-dashboard .btn i {
  margin-right: 8px;
}
</style>