<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const isOnline = ref(navigator.onLine)

// Función optimizada para actualizar estado
const updateStatus = () => {
  const newStatus = navigator.onLine
  if (isOnline.value !== newStatus) {
    isOnline.value = newStatus
    console.log(`Estado de conexión cambiado: ${newStatus ? 'Online' : 'Offline'}`)
  }
}

onMounted(() => {
  // Verificación inicial más robusta
  updateStatus()
  
  // Agregar listeners
  window.addEventListener('online', updateStatus)
  window.addEventListener('offline', updateStatus)
  
  // Opcional: Verificación pasiva ocasional
  // Solo si realmente se necesita
  const slowCheck = () => {
    if (Math.random() < 0.1) { // 10% de probabilidad
      updateStatus()
    }
  }
  const idleCheck = setInterval(slowCheck, 15000)

  onUnmounted(() => {
    window.removeEventListener('online', updateStatus)
    window.removeEventListener('offline', updateStatus)
    clearInterval(idleCheck)
  })
})
</script>

<template>
  <div>
    <p v-if="isOnline">🟢 Estás conectado a Internet</p>
    <p v-else>🔴 Estás sin conexión</p>
  </div>
</template>
