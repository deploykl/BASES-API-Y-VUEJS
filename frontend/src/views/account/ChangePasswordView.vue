<template>
  <div class="change-password-container">
    <div class="card">
      <div class="card-header">
        <h3>Cambiar Contraseña</h3>
      </div>
      <div class="card-body">
        <form @submit.prevent="changePassword">
          <div class="mb-3">
            <label class="form-label">Contraseña Actual</label>
            <input type="password" class="form-control" v-model="passwords.current_password" required>
          </div>
          
          <div class="mb-3">
            <label class="form-label">Nueva Contraseña</label>
            <input type="password" class="form-control" v-model="passwords.new_password" required>
            <small class="form-text text-muted">Mínimo 8 caracteres</small>
          </div>
          
          <div class="mb-3">
            <label class="form-label">Confirmar Nueva Contraseña</label>
            <input type="password" class="form-control" v-model="passwords.confirm_password" required>
          </div>
          
          <div class="d-flex justify-content-between mt-4">
            <router-link to="/perfil" class="btn btn-outline-secondary">
              Volver al Perfil
            </router-link>
            <button type="submit" class="btn btn-primary" :disabled="loading">
              <span v-if="loading" class="spinner-border spinner-border-sm"></span>
              Cambiar Contraseña
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import { api } from '@/components/services/Axios';

const store = useStore()
const router = useRouter()

const passwords = ref({
  current_password: '',
  new_password: '',
  confirm_password: ''
})

const loading = ref(false)
const error = ref(null)

const changePassword = async () => {
  if (passwords.value.new_password !== passwords.value.confirm_password) {
    error.value = 'Las contraseñas no coinciden'
    store.dispatch('showToast', {
      message: 'Las contraseñas no coinciden',
      type: 'error'
    })
    return
  }

  if (passwords.value.new_password.length < 8) {
    error.value = 'La contraseña debe tener al menos 8 caracteres'
    store.dispatch('showToast', {
      message: 'La contraseña debe tener al menos 8 caracteres',
      type: 'error'
    })
    return
  }

  loading.value = true
  error.value = null

  try {
    await api.post('user/change-password/', {
      current_password: passwords.value.current_password,
      new_password: passwords.value.new_password,
      confirm_password: passwords.value.confirm_password
    })

    store.dispatch('showToast', {
      message: 'Contraseña cambiada exitosamente',
      type: 'success'
    })
    
    // Limpiar formulario
    passwords.value = {
      current_password: '',
      new_password: '',
      confirm_password: ''
    }
    
    // Redirigir al perfil
    router.push('/perfil')
    
  } catch (err) {
    console.error('Error al cambiar contraseña:', err)
    error.value = err.response?.data?.detail || 'Error al cambiar la contraseña'
    store.dispatch('showToast', {
      message: error.value,
      type: 'error'
    })
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.change-password-container {
  max-width: 600px;
  margin: 2rem auto;
  padding: 0 1rem;
}

.card {
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.card-header {
  background-color: #f8f9fa;
  border-bottom: 1px solid #eee;
  padding: 1.5rem;
  border-radius: 10px 10px 0 0 !important;
}

.card-body {
  padding: 2rem;
}

.form-label {
  font-weight: 500;
  margin-bottom: 0.5rem;
}

.error-message {
  color: #dc3545;
  font-size: 0.875rem;
  margin-top: 0.25rem;
}
</style>