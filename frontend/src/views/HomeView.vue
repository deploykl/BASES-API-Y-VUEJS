<template>
  <div class="page-wrapper">
    <main class="main-content py-4">
      <div class="container">
        <div class="row align-items-center justify-content-center">
          <!-- Columna de la imagen -->
          <div class="col-md-6 mb-4 mb-md-0 d-flex justify-content-center">
            <img src="@/assets/img/home/work.png" alt="Presentación"
              class="img-fluid rounded mx-auto d-block image-style me-5">
          </div>

          <!-- Columna del texto -->
          <div class="col-md-6 text-center">
            <h1 class="mb-3 text-center text-primary fw-bold">Dirección de Monitoreo y Evaluación de la Gestión en Salud</h1>
            <p class="mb-3 lead">
              Dirección de Monitoreo y Evaluación de la Gestión en Salud.
            </p>

            <div class="alert alert-info d-flex align-items-center mb-4">
              <i class="bi bi-exclamation-circle-fill me-2 fs-4"></i>
              <div>
                <strong>Novedad:</strong> Lanzamiento de la Versión Demo (v1.0) con módulos esenciales
              </div>
            </div>

            <div class="mb-4">
              <h5 class="mb-3 text-center"><i class="bi bi-grid-fill me-2"></i>Módulos Principales</h5>
              <div class="row justify-content-center g-3">
                <div class="col-8 col-sm-3 col-md-5 col-lg-3">
                  <div class="p-3 border rounded bg-light text-center h-100 module-card">
                    <i class="bi bi-clipboard-check fs-3 text-success mb-2"></i>
                    <h6 class="fw-bold">Fichas de Verificación</h6>
                    <p class="small text-muted mb-0">Gestión completa de fichas técnicas</p>
                  </div>
                </div>

                <div class="col-8 col-sm-3 col-md-5 col-lg-3">
                  <div class="p-3 border rounded bg-light text-center h-100 module-card">
                    <i class="bi bi-microsoft-teams fs-3 text-primary mb-2"></i>
                    <h6 class="fw-bold">Compromisos</h6>
                    <p class="small text-muted mb-0">Seguimiento de acuerdos</p>
                  </div>
                </div>

                <div class="col-8 col-sm-3 col-md-5 col-lg-3">
                  <div class="p-3 border rounded bg-light text-center h-100 module-card">
                    <i class="bi bi-exclamation-triangle fs-3 text-warning mb-2"></i>
                    <h6 class="fw-bold">Alertas</h6>
                    <p class="small text-muted mb-0">Notificaciones importantes</p>
                  </div>
                </div>

                <div class="col-8 col-sm-3 col-md-5 col-lg-3">
                  <div class="p-3 border rounded bg-light text-center h-100 module-card">
                    <i class="bi bi-link-45deg fs-3 text-info mb-2"></i>
                    <h6 class="fw-bold">Enlaces Rápidos</h6>
                    <p class="small text-muted mb-0">Acceso directo a recursos</p>
                  </div>
                </div>
              </div>
            </div>

            <div class="access-buttons">
              <button v-if="isAuthenticated" @click="goToDashboard" class="btn btn-primary btn-lg">
                <i class="bi bi-box-arrow-in-right me-2"></i>Ingresar al Sistema
              </button>
              <router-link v-else to="/login" class="btn btn-primary px-4">
                <i class="bi bi-box-arrow-in-right me-2"></i>Ingresar al Sistema
              </router-link>
            </div>
          </div>
        </div>
      </div>

      <!-- Sección del Roadmap -->
      <section class="roadmap-section py-5 bg-light mt-5">
        <div class="container">
          <h2 class="text-center mb-5 fw-bold text-primary">Nuestro Roadmap</h2>
          <p class="text-center mb-5 lead">Descubre nuestro plan de desarrollo y las próximas funcionalidades</p>
          
          <div class="roadmap-timeline">
            <!-- Fase 1 -->
            <div class="roadmap-phase">
              <div class="phase-date left">Q1 2024</div>
              <div class="phase-marker">
                <div class="marker-dot completed"></div>
                <div class="marker-line"></div>
              </div>
              <div class="phase-card right">
                <div class="card-header bg-primary text-white">
                  <h3 class="mb-0">Versión Inicial</h3>
                  <span class="badge bg-white text-primary">Completado</span>
                </div>
                <div class="card-body">
                  <ul class="phase-features">
                    <li><i class="bi bi-check-circle-fill text-success me-2"></i>Módulo de Fichas Técnicas</li>
                    <li><i class="bi bi-check-circle-fill text-success me-2"></i>Gestión Básica de Compromisos</li>
                    <li><i class="bi bi-check-circle-fill text-success me-2"></i>Sistema de Alertas</li>
                  </ul>
                </div>
              </div>
            </div>
            
            <!-- Fase 2 -->
            <div class="roadmap-phase">
              <div class="phase-date right">Q3 2024</div>
              <div class="phase-marker">
                <div class="marker-dot current"></div>
                <div class="marker-line"></div>
              </div>
              <div class="phase-card left">
                <div class="card-header bg-warning text-dark">
                  <h3 class="mb-0">Versión 2.0</h3>
                  <span class="badge bg-white text-warning">En Desarrollo</span>
                </div>
                <div class="card-body">
                  <ul class="phase-features">
                    <li><i class="bi bi-gear-fill text-info me-2"></i>Dashboard Analítico</li>
                    <li><i class="bi bi-gear-fill text-info me-2"></i>Notificaciones Automáticas</li>
                    <li><i class="bi bi-gear-fill text-info me-2"></i>Exportación de Reportes</li>
                  </ul>
                </div>
              </div>
            </div>
            
            <!-- Fase 3 -->
            <div class="roadmap-phase">
              <div class="phase-date left">Q1 2025</div>
              <div class="phase-marker">
                <div class="marker-dot future"></div>
                <div class="marker-line"></div>
              </div>
              <div class="phase-card right">
                <div class="card-header bg-secondary text-white">
                  <h3 class="mb-0">Versión 3.0</h3>
                  <span class="badge bg-white text-secondary">Planificado</span>
                </div>
                <div class="card-body">
                  <ul class="phase-features">
                    <li><i class="bi bi-lightbulb text-muted me-2"></i>Inteligencia de Negocios</li>
                    <li><i class="bi bi-lightbulb text-muted me-2"></i>API Pública</li>
                    <li><i class="bi bi-lightbulb text-muted me-2"></i>App Móvil</li>
                  </ul>
                </div>
              </div>
            </div>
            
            <!-- Fase 4 -->
            <div class="roadmap-phase">
              <div class="phase-date right">Q3 2025</div>
              <div class="phase-marker">
                <div class="marker-dot future"></div>
                <div class="marker-line last"></div>
              </div>
              <div class="phase-card left">
                <div class="card-header bg-info text-white">
                  <h3 class="mb-0">Versión 4.0</h3>
                  <span class="badge bg-white text-info">En Planeación</span>
                </div>
                <div class="card-body">
                  <ul class="phase-features">
                    <li><i class="bi bi-lightbulb text-muted me-2"></i>Machine Learning</li>
                    <li><i class="bi bi-lightbulb text-muted me-2"></i>Integración Avanzada</li>
                    <li><i class="bi bi-lightbulb text-muted me-2"></i>Asistente Virtual</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
          
          <div class="text-center mt-5">
            <button class="btn btn-primary btn-lg" @click="showRoadmapDetails">
              <i class="bi bi-calendar2-week me-2"></i>Explorar Roadmap Completo
            </button>
          </div>
        </div>
      </section>
    </main>

    <footer class="footer">
      <div class="quotes-container">
        <div id="quoteCarousel" class="quotes-slider">
          <div class="quote active">
            <div class="quote-content">
              <div class="quote-icon">“</div>
              <p class="quote-text">Si lo puedes imaginar, lo puedes programar</p>
              <div class="quote-author">
                <div class="author-line"></div>
                <span>Alan Kay</span>
              </div>
            </div>
          </div>
          <div class="quote">
            <div class="quote-content">
              <div class="quote-icon">“</div>
              <p class="quote-text">Camina hacia el futuro, abriendo nuevas puertas y probando cosas nuevas...</p>
              <div class="quote-author">
                <div class="author-line"></div>
                <span>Walt Disney</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="footer-info">
        <div class="copyright">
          &copy; {{ currentYear }} - Desarrollado por el área de TI de la DGOS
        </div>
        <div class="technologies">
          Tecnologías:
          <span class="tech-tag"><i class="fab fa-python"></i> Python</span>
          <span class="tech-tag"><i class="fab fa-python"></i> Django</span>
          <span class="tech-tag"><i class="fas fa-layer-group"></i> REST API</span>
          <span class="tech-tag"><i class="fab fa-js"></i> Vue.js</span>
          <span class="tech-tag"><i class="fas fa-database"></i> SQL Server</span>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const isAuthenticated = computed(() => localStorage.getItem('auth_token'));

const goToDashboard = () => {
  router.push('/dashboard');
};

const currentYear = ref(new Date().getFullYear());

const showRoadmapDetails = () => {
  // Lógica para mostrar detalles completos del roadmap
  alert("Próximamente: Página detallada del roadmap con fechas exactas y progreso.");
};

onMounted(() => {
  const quotes = document.querySelectorAll('.quote');
  let currentIndex = 0;

  setInterval(() => {
    quotes[currentIndex].classList.remove('active');
    currentIndex = (currentIndex + 1) % quotes.length;
    quotes[currentIndex].classList.add('active');
  }, 5000);
});
</script>

<style>
/* Reset básico */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Segoe UI', 'Roboto', sans-serif;
  line-height: 1.6;
  color: #333;
  background-color: #f8f9fa;
}

.access-buttons {
  margin-top: 2rem;
}

.btn-primary {
  background-color: #0b4a7a;
  border-color: #0b4a7a;
  padding: 0.75rem 2rem;
  font-size: 1.1rem;
  font-weight: 600;
  border-radius: 8px;
  transition: all 0.3s ease;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.btn-primary:hover {
  background-color: #083758;
  border-color: #083758;
  transform: translateY(-2px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
}

.btn-primary:active {
  transform: translateY(0);
}

/* Estructura principal */
.page-wrapper {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

/* Header */
.header {
  background: linear-gradient(to right, #0b4a7a, #083758);
  padding: 1rem 0;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 90%;
  max-width: 1200px;
  margin: 0 auto;
}

.logo {
  height: 50px;
  width: auto;
}

/* Contenido principal */
.main-content {
  flex: 1;
  display: flex;
  align-items: center;
  padding: 3rem 0;
  text-align: center;
}

.container {
  width: 100%;
  padding-right: 15px;
  padding-left: 15px;
  margin-right: auto;
  margin-left: auto;
  text-align: center;
}

/* Footer */
.footer {
  background-color: #0f172a;
  color: white;
  padding: 1rem 0;
}

/* Contenedor de frases */
.quotes-container {
  width: 90%;
  max-width: 700px;
  margin: 0 auto 1rem;
  padding: 1rem;
  background: linear-gradient(145deg, #1e293b, #0f172a);
  border-radius: 12px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  position: relative;
  overflow: hidden;
}

.quotes-container::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 4px;
  height: 100%;
  background: linear-gradient(to bottom, #3b82f6, #8b5cf6);
}

.quotes-slider {
  position: relative;
  min-height: 80px;
}

.quote {
  position: absolute;
  width: 100%;
  opacity: 0;
  transition: all 0.5s ease;
}

.quote.active {
  opacity: 1;
}

.quote-content {
  padding: 0 1rem;
}

.quote-icon {
  font-size: 3rem;
  color: #3b82f6;
  opacity: 0.2;
  position: absolute;
  top: -1rem;
  left: 0;
  line-height: 1;
  font-family: Georgia, serif;
}

.quote-text {
  font-size: 1.1rem;
  line-height: 1.5;
  color: #f8fafc;
  margin-bottom: 1rem;
  position: relative;
  font-style: italic;
  padding-left: 1rem;
}

.quote-author {
  display: flex;
  align-items: center;
  gap: 0.8rem;
}

.author-line {
  flex-grow: 1;
  height: 1px;
  background: linear-gradient(to right, rgba(59, 130, 246, 0.5), transparent);
}

.quote-author span {
  color: #94a3b8;
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-weight: 600;
}

/* Información del footer */
.footer-info {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  width: 90%;
  max-width: 1200px;
  margin: 0 auto;
  padding-top: 1.5rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.copyright {
  color: #94a3b8;
  font-size: 0.9rem;
}

.technologies {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  align-items: center;
}

.tech-tag {
  background-color: rgba(255, 255, 255, 0.1);
  padding: 0.3rem 0.8rem;
  border-radius: 20px;
  font-size: 0.85rem;
  display: flex;
  align-items: center;
  gap: 0.3rem;
}

/* Estilos para la imagen */
.image-style {
  border: none !important;
  box-shadow: none !important;
  filter: drop-shadow(0 12px 20px rgba(0, 0, 0, 0.25));
  transition: all 0.3s ease;
  max-width: 90%;
  margin: 0 auto;
  transform: translateY(-3px);
}

.image-style:hover {
  filter: drop-shadow(0 12px 20px rgba(0, 0, 0, 0.25));
  transform: translateY(-3px);
}

/* Estilos para el nuevo roadmap */
.roadmap-section {
  background: linear-gradient(135deg, #f8f9fa 0%, #e9f5ff 100%);
  position: relative;
  overflow: hidden;
}

.roadmap-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100" fill="none" stroke="%23e1e9f2" stroke-width="0.5"><rect x="0.5" y="0.5" width="99" height="99"/></svg>');
  opacity: 0.3;
}

.roadmap-timeline {
  position: relative;
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 0;
}

.roadmap-timeline::before {
  content: '';
  position: absolute;
  top: 0;
  left: 50%;
  width: 4px;
  height: 100%;
  background: linear-gradient(to bottom, #0b4a7a, #3b82f6);
  transform: translateX(-50%);
  border-radius: 10px;
}

.roadmap-phase {
  position: relative;
  width: 100%;
  margin-bottom: 40px;
  display: flex;
  justify-content: center;
  align-items: flex-start;
}

.phase-date {
  width: 150px;
  padding: 10px;
  font-weight: 600;
  color: #0b4a7a;
  text-align: center;
  position: relative;
  z-index: 2;
}

.phase-date.left {
  text-align: right;
  padding-right: 30px;
}

.phase-date.right {
  text-align: left;
  padding-left: 30px;
}

.phase-marker {
  position: relative;
  width: 40px;
  height: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-shrink: 0;
  z-index: 2;
}

.marker-dot {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: #0b4a7a;
  border: 4px solid white;
  box-shadow: 0 0 0 2px #0b4a7a;
  position: relative;
}

.marker-dot.completed {
  background: #0b4a7a;
  box-shadow: 0 0 0 2px #0b4a7a;
}

.marker-dot.current {
  background: #ffc107;
  box-shadow: 0 0 0 2px #ffc107;
  animation: pulse 2s infinite;
}

.marker-dot.future {
  background: #6c757d;
  box-shadow: 0 0 0 2px #6c757d;
}

.marker-line {
  position: absolute;
  width: 2px;
  height: 100%;
  background: #dee2e6;
  top: 40px;
}

.marker-line.last {
  display: none;
}

.phase-card {
  width: calc(50% - 100px);
  min-width: 300px;
  background: white;
  border-radius: 10px;
  box-shadow: 0 5px 25px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  transition: all 0.3s ease;
}

.phase-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
}

.card-header {
  padding: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.card-header h3 {
  font-size: 1.3rem;
  margin: 0;
}

.card-body {
  padding: 20px;
}

.phase-features {
  list-style: none;
  padding: 0;
  margin: 0;
}

.phase-features li {
  padding: 8px 0;
  display: flex;
  align-items: center;
}

/* Animación para la fase actual */
@keyframes pulse {
  0% {
    box-shadow: 0 0 0 0 rgba(255, 193, 7, 0.7);
  }
  70% {
    box-shadow: 0 0 0 10px rgba(255, 193, 7, 0);
  }
  100% {
    box-shadow: 0 0 0 0 rgba(255, 193, 7, 0);
  }
}

/* Responsive */
@media (max-width: 992px) {
  .roadmap-timeline::before {
    left: 40px;
  }
  
  .roadmap-phase {
    justify-content: flex-start;
    padding-left: 40px;
  }
  
  .phase-date {
    width: 100px;
    text-align: left !important;
    padding: 0 20px 0 0 !important;
    order: 1;
  }
  
  .phase-marker {
    order: 2;
    margin-left: -40px;
  }
  
  .phase-card {
    width: calc(100% - 100px);
    order: 3;
    margin-left: 20px;
  }
  
  .phase-card.left, .phase-card.right {
    margin-left: 20px;
    margin-right: 0;
  }
}

@media (max-width: 576px) {
  .main-content {
    padding: 1rem 0;
  }

  .min-vh-75 {
    min-height: auto;
    padding: 2rem 0;
  }

  .quotes-container {
    padding: 1.2rem;
    min-height: 100px;
  }

  .quote-text {
    font-size: 1rem;
  }

  .quote-icon {
    font-size: 2.5rem;
    top: -0.8rem;
  }

  .footer-info {
    flex-direction: column;
    gap: 1rem;
    text-align: center;
  }

  .technologies {
    justify-content: center;
  }

  .col-md-6 {
    text-align: center !important;
  }

  .d-flex.justify-content-center.justify-content-md-start {
    justify-content: center !important;
  }

  .roadmap-timeline::before {
    left: 20px;
  }
  
  .roadmap-phase {
    padding-left: 20px;
  }
  
  .phase-card {
    min-width: 250px;
    width: calc(100% - 60px);
  }
  
  .card-header {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .card-header .badge {
    margin-top: 10px;
  }
}
</style>