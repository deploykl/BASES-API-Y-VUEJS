<template>
  <div class="container-fluid mt-4">
    <!-- Modal para crear/editar usuario -->
    <div class="modal fade" id="userModal" tabindex="-1" aria-hidden="true">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">{{ modalTitle }}</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="handleSubmit">
              <div class="row">
                <div class="col-md-6">
                  <div class="mb-3">
                    <label class="form-label">Nombre de usuario</label>
                    <input v-model="form.username" type="text" class="form-control" required>
                  </div>
                  <div class="mb-3">
                    <label class="form-label">Email</label>
                    <input v-model="form.email" type="email" class="form-control" required>
                  </div>
                  <!-- Sección de contraseña -->
                  <div v-if="!editing" class="mb-3">
                    <div class="mb-3">
                      <label class="form-label">Contraseña</label>
                      <input v-model="form.password" type="password" class="form-control" required>
                    </div>
                    <div class="mb-3">
                      <label class="form-label">Confirmar Contraseña</label>
                      <input v-model="form.password2" type="password" class="form-control" required>
                    </div>
                  </div>
                  <div v-if="editing" class="mb-3">
                    <div class="alert alert-info">
                      <div class="form-check form-switch">
                        <input v-model="resetPassword" class="form-check-input" type="checkbox" id="resetPasswordCheck">
                        <label class="form-check-label" for="resetPasswordCheck">
                          <strong>Resetear contraseña</strong>
                        </label>
                      </div>
                      <small class="text-muted">Marque esta opción si desea establecer una nueva contraseña para este
                        usuario</small>
                    </div>
                    <div v-if="resetPassword" class="mt-3">
                      <div class="mb-3">
                        <label class="form-label">Nueva Contraseña</label>
                        <input v-model="form.password" type="password" class="form-control" required>
                      </div>
                      <div class="mb-3">
                        <label class="form-label">Confirmar Nueva Contraseña</label>
                        <input v-model="form.password2" type="password" class="form-control" required>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="mb-3">
                    <label class="form-label">Nombres</label>
                    <input v-model="form.first_name" type="text" class="form-control">
                  </div>
                  <div class="mb-3">
                    <label class="form-label">Apellidos</label>
                    <input v-model="form.last_name" type="text" class="form-control">
                  </div>
                  <div class="mb-3">
                    <label class="form-label">DNI</label>
                    <input v-model="form.dni" type="text" class="form-control">
                  </div>
                  <div class="mb-3">
                    <label class="form-label">Celular</label>
                    <input v-model="form.celular" type="text" class="form-control">
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-md-4">
                  <div class="form-check form-switch mb-3">
                    <input v-model="form.is_active" class="form-check-input" type="checkbox" id="isActiveCheck">
                    <label class="form-check-label" for="isActiveCheck">Activo</label>
                  </div>
                </div>
                <div class="col-md-4">
                  <div class="form-check form-switch mb-3">
                    <input v-model="form.is_staff" class="form-check-input" type="checkbox" id="isStaffCheck">
                    <label class="form-check-label" for="isStaffCheck">Staff</label>
                  </div>
                </div>
                <div class="col-md-4">
                  <div class="form-check form-switch mb-3">
                    <input v-model="form.is_superuser" class="form-check-input" type="checkbox" id="isSuperuserCheck">
                    <label class="form-check-label" for="isSuperuserCheck">Superusuario</label>
                  </div>
                </div>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                <button type="submit" class="btn btn-primary" :disabled="isSubmitting">
                  {{ isSubmitting ? 'Guardando...' : 'Guardar' }}
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <!-- Modal de confirmación para eliminar -->
    <div class="modal fade" id="deleteConfirmModal" tabindex="-1" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header bg-danger text-white">
            <h5 class="modal-title">Confirmar Eliminación</h5>
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            ¿Estás seguro de eliminar permanentemente al usuario <strong>{{ userToDelete?.username }}</strong>?
            <div class="alert alert-warning mt-3">
              <i class="fas fa-exclamation-triangle me-2"></i>
              Esta acción no se puede deshacer y eliminará todos los datos asociados al usuario.
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
            <button type="button" class="btn btn-danger" @click="proceedDelete" :disabled="isDeleting">
              {{ isDeleting ? 'Eliminando...' : 'Eliminar Permanentemente' }}
            </button>
          </div>
        </div>
      </div>
    </div>
    <!-- Listado de usuarios -->
    <div class="card">
      <div class="card-header d-flex justify-content-between align-items-center">
        <h2 class="mb-0">Gestión de Usuarios</h2>
        <button class="btn btn-primary" @click="openCreateModal">
          <i class="fas fa-plus me-2"></i>Nuevo Usuario
        </button>
      </div>
      <div class="card-body">
        <div class="table-responsive">
          <table class="table table-striped table-hover">
            <thead>
              <tr>
                <th>N°</th>
                <th>Usuario</th>
                <th>Nombre</th>
                <th>Email</th>
                <th>Estado</th>
                <th>Roles</th>
                <th>Creado por</th>
                <th>Acciones</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(user, index) in users" :key="user.id"> <!-- Añadido index -->
                <td>{{ index + 1 }}</td> <!-- Mostrar posición en la lista -->
                <td>{{ user.username }}</td>
                <td>{{ fullName(user) }}</td>
                <td>{{ user.email }}</td>
                <td>
                  <span class="badge" :class="user.is_active ? 'bg-success' : 'bg-danger'">
                    {{ user.is_active ? 'Activo' : 'Inactivo' }}
                  </span>
                </td>
                <td>
                  <span v-if="user.is_superuser" class="badge bg-dark me-1">Admin</span>
                  <span v-if="user.is_staff" class="badge bg-info">Staff</span>
                </td>
                <td>{{ user.created_by ? user.created_by.username : 'Sistema' }}</td>
                <td>
                  <button @click="openEditModal(user)" class="btn btn-sm btn-warning me-2">
                    <i class="fas fa-edit"></i>
                  </button>
                  <button v-if="user.is_active" @click="deactivateUser(user.id)" class="btn btn-sm btn-danger me-2">
                    <i class="fas fa-times"></i>
                  </button>
                  <button v-else @click="activateUser(user.id)" class="btn btn-sm btn-success me-2">
                    <i class="fas fa-check"></i>
                  </button>
                  <!-- Nuevo botón para eliminar -->
                  <button @click="confirmDelete(user)" class="btn btn-sm btn-danger">
                    <i class="fas fa-trash"></i>
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { Modal } from 'bootstrap'
import { api } from '@/components/services/Axios'
import { toast } from 'vue-sonner'

// Estado reactivo
const users = ref([])
const userModal = ref(null)
const modalTitle = ref('')
const editing = ref(false)
const currentUserId = ref(null)
const isSubmitting = ref(false)
const resetPassword = ref(false)
const deleteConfirmModal = ref(null)
const userToDelete = ref(null)
const isDeleting = ref(false)

const form = ref({
  username: '',
  email: '',
  password: '',
  password2: '',
  first_name: '',
  last_name: '',
  dni: '',
  celular: '',
  is_active: true,
  is_staff: false,
  is_superuser: false
})

// Métodos
const fetchUsers = async () => {
  try {
    const response = await api.get('user/users/')
    users.value = response.data
  } catch (error) {
    toast.error('Error al cargar usuarios')
    console.error('Error fetching users:', error)
  }
}

const openCreateModal = () => {
  resetForm()
  modalTitle.value = 'Crear Nuevo Usuario'
  editing.value = false
  resetPassword.value = false
  userModal.value.show()
}
const confirmDelete = (user) => {
  userToDelete.value = user
  deleteConfirmModal.value.show()
}

const proceedDelete = async () => {
  isDeleting.value = true
  try {
    await api.delete(`user/users/${userToDelete.value.id}/`)
    toast.success('Usuario eliminado correctamente')
    deleteConfirmModal.value.hide()
    fetchUsers()
  } catch (error) {
    console.error('Error deleting user:', error)
    if (error.response?.data?.detail) {
      toast.error(error.response.data.detail)
    } else {
      toast.error('Error al eliminar el usuario')
    }
  } finally {
    isDeleting.value = false
  }
}

const openEditModal = (user) => {
  form.value = {
    username: user.username,
    email: user.email,
    password: '',
    password2: '',
    first_name: user.first_name || '',
    last_name: user.last_name || '',
    dni: user.dni || '',
    celular: user.celular || '',
    is_active: user.is_active,
    is_staff: user.is_staff,
    is_superuser: user.is_superuser
  }
  currentUserId.value = user.id
  modalTitle.value = 'Editar Usuario'
  editing.value = true
  resetPassword.value = false
  userModal.value.show()
}

const resetForm = () => {
  form.value = {
    username: '',
    email: '',
    password: '',
    password2: '',
    first_name: '',
    last_name: '',
    dni: '',
    celular: '',
    is_active: true,
    is_staff: false,
    is_superuser: false
  }
  currentUserId.value = null
  resetPassword.value = false
}

const handleSubmit = async () => {
  if ((!editing.value || resetPassword.value) && form.value.password !== form.value.password2) {
    toast.error('Las contraseñas no coinciden')
    return
  }

  isSubmitting.value = true

  try {
    const dataToSend = { ...form.value }

    if (editing.value) {
      if (!resetPassword.value) {
        delete dataToSend.password
        delete dataToSend.password2
      } else {
        delete dataToSend.password2
      }

      await api.patch(`user/users/${currentUserId.value}/`, dataToSend)
      toast.success('Usuario actualizado correctamente')
    } else {
      delete dataToSend.password2
      await api.post('user/users/', dataToSend)
      toast.success('Usuario creado correctamente')
    }

    userModal.value.hide()
    fetchUsers()
  } catch (error) {
    console.error('Error saving user:', error)
    if (error.response?.data) {
      for (const key in error.response.data) {
        if (Array.isArray(error.response.data[key])) {
          toast.error(`${key}: ${error.response.data[key].join(', ')}`)
        } else {
          toast.error(`${key}: ${error.response.data[key]}`)
        }
      }
    } else {
      toast.error('Error al guardar el usuario')
    }
  } finally {
    isSubmitting.value = false
  }
}

const activateUser = async (userId) => {
  try {
    await api.post(`user/users/${userId}/activate/`)
    toast.success('Usuario activado correctamente')
    fetchUsers()
  } catch (error) {
    toast.error('Error al activar usuario')
    console.error('Error activating user:', error)
  }
}

const deactivateUser = async (userId) => {
  try {
    await api.post(`user/users/${userId}/deactivate/`)
    toast.success('Usuario desactivado correctamente')
    fetchUsers()
  } catch (error) {
    toast.error('Error al desactivar usuario')
    console.error('Error deactivating user:', error)
  }
}

const fullName = (user) => {
  return [user.first_name, user.last_name].filter(Boolean).join(' ') || '-'
}

// Inicialización
onMounted(() => {
  userModal.value = new Modal(document.getElementById('userModal'))
  deleteConfirmModal.value = new Modal(document.getElementById('deleteConfirmModal'))
  fetchUsers()
})
</script>

<style scoped>
.table-responsive {
  max-height: 70vh;
  overflow-y: auto;
}

.badge {
  font-size: 0.875em;
}

.btn-sm {
  padding: 0.25rem 0.5rem;
  font-size: 0.875rem;
}

.alert-info {
  background-color: #e7f5ff;
  border-color: #d0ebff;
  color: #0a58ca;
}

.btn-danger {
  background-color: #dc3545;
  border-color: #dc3545;
}

.btn-danger:hover {
  background-color: #bb2d3b;
  border-color: #b02a37;
}

.modal-header.bg-danger {
  background-color: #dc3545 !important;
}
</style>