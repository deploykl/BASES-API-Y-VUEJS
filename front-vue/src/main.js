import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'

import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-icons/font/bootstrap-icons.css';  // Asegúrate de esta línea
import '@/assets/lib/fontawesome-v6.5.2/css/all.css'
import '@/assets/lib/fontawesome-v6.5.2/css/sharp-light.css'
import '@/assets/lib/fontawesome-v6.5.2/css/sharp-regular.css'
import '@/assets/lib/fontawesome-v6.5.2/css/sharp-solid.css'
import '@/assets/lib/fontawesome-v6.5.2/css/sharp-thin.css'

createApp(App).use(store).use(router).mount('#app')
