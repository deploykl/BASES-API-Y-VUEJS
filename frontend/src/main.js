import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import { createPinia } from 'pinia'
import ErrorMessage from '@/components/ErrorMessage.vue' // Asegúrate de importar tu componente

// LIBRERÍAS
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-icons/font/bootstrap-icons.css'
import 'sweetalert2'
import 'sweetalert2/dist/sweetalert2.min.css'

import '@/assets/lib/fontawesome-v6.5.2/css/all.css'
import '@/assets/lib/fontawesome-v6.5.2/css/sharp-light.css'
import '@/assets/lib/fontawesome-v6.5.2/css/sharp-regular.css'
import '@/assets/lib/fontawesome-v6.5.2/css/sharp-solid.css'
import '@/assets/lib/fontawesome-v6.5.2/css/sharp-thin.css'

// PERSONALIZADO
import '@/assets/css/font.css'
import '@/assets/css/main.css'

const app = createApp(App)
const pinia = createPinia()

// Usa los plugins
app.use(store)
app.use(router)
app.use(pinia)

// Registra componentes globales
app.component('ErrorMessage', ErrorMessage)

// Monta la aplicación
app.mount('#app')