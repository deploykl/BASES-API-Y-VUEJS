<template>
  <div class="profile-container">
    <div class="card">
      <div class="card-header">
        <h3>Editar Perfil</h3>
      </div>
      <div class="card-body">
        <form @submit.prevent="updateProfile">
          <div class="text-center mb-4">
            <img :src="userImage" alt="Foto de perfil" class="profile-image">
            <input type="file" ref="fileInput" @change="handleImageChange" accept="image/*" class="d-none">
            <button type="button" @click="$refs.fileInput.click()" class="btn btn-sm btn-outline-primary mt-2">
              Cambiar Imagen
            </button>
          </div>

          <div class="row">
            <div class="col-md-6 mb-3">
              <label class="form-label">Nombre de usuario</label>
              <input type="text" class="form-control" v-model="user.username" required>
            </div>
            <div class="col-md-6 mb-3">
              <label class="form-label">Correo electrónico</label>
              <input type="email" class="form-control" v-model="user.email" required>
            </div>
          </div>

          <div class="row">
            <div class="col-md-6 mb-3">
              <label class="form-label">Nombres</label>
              <input type="text" class="form-control" v-model="user.first_name" required>
            </div>
            <div class="col-md-6 mb-3">
              <label class="form-label">Apellidos</label>
              <input type="text" class="form-control" v-model="user.last_name" required>
            </div>
          </div>

          <div class="d-flex justify-content-between mt-4">
            <router-link to="/cambiar-contrasena" class="btn btn-outline-secondary">
              Cambiar Contraseña
            </router-link>
            <button type="submit" class="btn btn-primary" :disabled="loading">
              <span v-if="loading" class="spinner-border spinner-border-sm"></span>
              Guardar Cambios
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { api } from '@/components/services/Axios'
import { useToast } from 'vue-toastification'

const toast = useToast()
const router = useRouter()

const user = ref({
  username: '',
  email: '',
  first_name: '',
  last_name: '',
  image: ''
})

const loading = ref(false)
const fileInput = ref(null)
const selectedImage = ref(null)
const imagePreview = ref(null)

// Computed property para manejar la imagen
const userImage = computed(() => {
  return imagePreview.value || user.value.image || '/img/empty.png'
})

onMounted(async () => {
  await fetchUserProfile()
})

const fetchUserProfile = async () => {
  try {
    const response = await api.get('user/profile/')
    user.value = response.data
  } catch (error) {
    console.error('Error al obtener perfil:', error)
    toast.error('Error al cargar el perfil')
  }
}

const handleImageChange = (event) => {
  const file = event.target.files[0]
  if (file) {
    // Validar tamaño y tipo de imagen
    if (!file.type.match('image.*')) {
      toast.error('Por favor selecciona un archivo de imagen válido')
      return
    }
    
    if (file.size > 2 * 1024 * 1024) { // 2MB
      toast.error('La imagen no debe exceder los 2MB')
      return
    }

    selectedImage.value = file
    
    // Mostrar vista previa
    const reader = new FileReader()
    reader.onload = (e) => {
      imagePreview.value = e.target.result
    }
    reader.readAsDataURL(file)
  }
}

const updateProfile = async () => {
  loading.value = true
  const formData = new FormData()
  
  // Agregar datos del usuario
  formData.append('username', user.value.username)
  formData.append('email', user.value.email)
  formData.append('first_name', user.value.first_name)
  formData.append('last_name', user.value.last_name)
  
  // Agregar imagen si se seleccionó una nueva
  if (selectedImage.value) {
    formData.append('image', selectedImage.value)
  }

  try {
    const response = await api.put('user/profile/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
    
    // Actualizar datos locales
    user.value = response.data
    imagePreview.value = null // Limpiar vista previa después de guardar
    selectedImage.value = null
    
    toast.success('Perfil actualizado correctamente')
    
  } catch (error) {
    console.error('Error al actualizar perfil:', error)
    
    let errorMessage = 'Error al actualizar el perfil'
    if (error.response?.data) {
      // Manejar errores específicos del backend
      if (error.response.data.username) {
        errorMessage = error.response.data.username[0]
      } else if (error.response.data.email) {
        errorMessage = error.response.data.email[0]
      }
    }
    
    toast.error(errorMessage)
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.profile-container {
  max-width: 800px;
  margin: 2rem auto;
  padding: 0 1rem;
}

.profile-image {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid #f0f0f0;
  background-color: #f8f9fa;
}

.card {
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(0, 0, 0, 0.125);
}

.card-header {
  background-color: #f8f9fa;
  border-bottom: 1px solid rgba(0, 0, 0, 0.125);
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

.btn-outline-primary {
  transition: all 0.3s ease;
}

.btn-outline-primary:hover {
  background-color: #0d6efd;
  color: white;
}

.spinner-border-sm {
  width: 1rem;
  height: 1rem;
  border-width: 0.2em;
}
</style>