<template>
  <transition name="slide-down">
    <div v-if="message" class="error-message" :class="type">
      <div class="error-content">
        <i :class="iconClass"></i>
        <span>{{ message }}</span>
      </div>
    </div>
  </transition>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  message: String,
  type: {
    type: String,
    default: 'error', // puede ser 'error', 'warning', 'success'
    validator: (value) => ['error', 'warning', 'success'].includes(value)
  }
})

const iconClass = computed(() => {
  return {
    'error': 'fas fa-exclamation-circle',
    'warning': 'fas fa-exclamation-triangle',
    'success': 'fas fa-check-circle'
  }[props.type]
})
</script>

<style scoped>
.error-message {
  position: fixed;
  top: 20px;
  left: 50%;
  transform: translateX(-50%);
  min-width: 300px;
  max-width: 90%;
  padding: 12px 16px;
  border-radius: 8px;
  margin-bottom: 20px;
  display: flex;
  justify-content: center;
  font-size: 14px;
  z-index: 1000;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.error-content {
  display: flex;
  align-items: center;
  gap: 8px;
}

.error-message.error {
  background-color: #ffebee;
  color: #c62828;
  border-left: 4px solid #c62828;
}

.error-message.warning {
  background-color: #fff8e1;
  color: #e65100;
  border-left: 4px solid #e65100;
}

.error-message.success {
  background-color: #e8f5e9;
  color: #2e7d32;
  border-left: 4px solid #2e7d32;
}

.slide-down-enter-active,
.slide-down-leave-active {
  transition: all 0.3s ease;
}

.slide-down-enter-from,
.slide-down-leave-to {
  opacity: 0;
  transform: translateX(-50%) translateY(-20px);
}
</style>