import { ref, onMounted, onUnmounted } from 'vue'
import { api } from '@/components/services/Axios'
import { useToast } from 'vue-toastification'

export function useConnection() {
  const toast = useToast()
  // Estados
  const isOnline = ref(navigator.onLine)
  const isApiConnected = ref(null)
  const isCheckingApi = ref(false)
  const lastApiCheck = ref(null)
  const lastNetworkChange = ref(null)
  
  // Configuración
  const checkIntervals = {
    online: 60000,  // 60 segundos cuando está conectado
    offline: 10000,  // 10 segundos cuando está desconectado
    retry: 1000     // 1 segundo para reintentos
  }
  
  let apiCheckInterval = null
  let retryTimeout = null
  let networkCheckTimeout = null

  // Mostrar notificación
  const showNotification = (message, type = 'info') => {
    toast[type](message, {
      timeout: 3000,
      closeOnClick: true,
      pauseOnFocusLoss: true,
      pauseOnHover: true
    })
  }
// Add multiple endpoints for network verification
const NETWORK_TEST_ENDPOINTS = [
  'https://www.gstatic.com/generate_204',  // Endpoint de Google
  'https://connectivitycheck.gstatic.com/generate_204',  // Alternativo de Google
  'https://api.ipify.org?format=json'  // Para obtener IP pública
]

const checkRealNetworkStatus = async () => {
  clearTimeout(networkCheckTimeout)
  
  let conexionOK = false
  
  for (const endpoint of NETWORK_TEST_ENDPOINTS) {
    try {
      // Construir URL correctamente según el endpoint
      const url = endpoint.includes('?') 
        ? `${endpoint}&ts=${Date.now()}`
        : `${endpoint}?ts=${Date.now()}`
      
      const response = await fetch(url, {
        method: endpoint.includes('generate_204') ? 'HEAD' : 'GET',
        cache: 'no-cache',
        mode: 'no-cors'
      })
      
      // Para generate_204, el status 204 indica éxito
      if (endpoint.includes('generate_204')) {
        conexionOK = true
      } 
      // Para otros endpoints, consideramos éxito si no hubo error
      else {
        conexionOK = true
      }
      
      if (conexionOK) break
    } catch (error) {
      console.debug(`Fallo en endpoint ${endpoint}:`, error)
      continue
    }
  }
  
  if (conexionOK && !isOnline.value) {
    isOnline.value = true
    showNotification('Conexión a Internet restablecida', 'success')
    checkApiConnection()
  } else if (!conexionOK && isOnline.value) {
    isOnline.value = false
    showNotification('Se perdió la conexión a Internet', 'error')
    isApiConnected.value = false
  }
  
  networkCheckTimeout = setTimeout(checkRealNetworkStatus, 5000)
}

  // Verificación de conexión a Internet
  const updateNetworkStatus = () => {
    const now = new Date()
    
    // Evitar cambios demasiado rápidos (debouncing)
    if (lastNetworkChange.value && (now - lastNetworkChange.value < 2000)) {
      return
    }
    
    lastNetworkChange.value = now
    const newStatus = navigator.onLine
    
    if (newStatus !== isOnline.value) {
      isOnline.value = newStatus
      
      if (newStatus) {
        showNotification('Conexión a Internet restablecida', 'success')
        checkApiConnection()
      } else {
        showNotification('Se perdió la conexión a Internet', 'error')
        isApiConnected.value = false
      }
    }
    
    // Verificación adicional para casos donde navigator.onLine no es confiable
    checkRealNetworkStatus()
  }

  // Verificación de conexión a la API
  const checkApiConnection = async () => {
    if (isCheckingApi.value || !isOnline.value) return
    
    isCheckingApi.value = true
    const controller = new AbortController()
    const timeoutId = setTimeout(() => controller.abort(), 3000)
    
    try {
      const response = await api.options('', { signal: controller.signal })
      const newStatus = response.status >= 200 && response.status < 500
      
      if (isApiConnected.value !== newStatus) {
        if (newStatus) {
          showNotification('Conexión con el servidor restablecida', 'success')
        } else {
          showNotification('Problemas de conexión con el servidor', 'error')
        }
      }
      
      isApiConnected.value = newStatus
      lastApiCheck.value = new Date()
      resetCheckInterval()
    } catch (error) {
      if (isApiConnected.value !== false) {
        showNotification('Error al conectar con el servidor', 'error')
      }
      isApiConnected.value = false
      scheduleRetry()
    } finally {
      clearTimeout(timeoutId)
      isCheckingApi.value = false
    }
  }

  // Programar reintento
  const scheduleRetry = () => {
    clearTimeout(retryTimeout)
    retryTimeout = setTimeout(checkApiConnection, checkIntervals.retry)
  }

  // Ajustar intervalo de verificación
  const resetCheckInterval = () => {
    clearInterval(apiCheckInterval)
    const interval = isApiConnected.value ? 
      checkIntervals.online : 
      checkIntervals.offline
    apiCheckInterval = setInterval(checkApiConnection, interval)
  }

  // Inicialización
  onMounted(() => {
    window.addEventListener('online', updateNetworkStatus)
    window.addEventListener('offline', updateNetworkStatus)
    checkApiConnection()
    resetCheckInterval()
    checkRealNetworkStatus()
  })

  // Limpieza
  onUnmounted(() => {
    window.removeEventListener('online', updateNetworkStatus)
    window.removeEventListener('offline', updateNetworkStatus)
    clearInterval(apiCheckInterval)
    clearTimeout(retryTimeout)
    clearTimeout(networkCheckTimeout)
  })

return {
  isOnline,
  isApiConnected,
  isCheckingApi,
  lastApiCheck,
  lastNetworkChange,  // Add this
  checkApiConnection
}
}