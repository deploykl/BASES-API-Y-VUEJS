<template>
  <div class="home container text-center py-5">
    <img alt="Vue logo" src="../assets/logo.png" class="mb-4" style="max-width: 150px;">
    <p class="mb-5">
      For a guide and recipes on how to configure / customize this project,<br>
      check out the
      <a href="https://cli.vuejs.org" target="_blank" rel="noopener" class="text-decoration-none">vue-cli
        documentation</a>.
    </p>

    <div class="row justify-content-center mb-5">
      <div class="col-md-8 col-lg-6">
        <h3 class="mb-4">Installed CLI Plugins</h3>
        <ul class="list-inline">
          <li class="list-inline-item mx-2 mb-2">
            <a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel" target="_blank"
              rel="noopener" class="btn btn-outline-primary">
              babel
            </a>
          </li>
          <li class="list-inline-item mx-2 mb-2">
            <a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-pwa" target="_blank"
              rel="noopener" class="btn btn-outline-primary">
              pwa
            </a>
          </li>
          <li class="list-inline-item mx-2 mb-2">
            <a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-router" target="_blank"
              rel="noopener" class="btn btn-outline-primary">
              router
            </a>
          </li>
          <li class="list-inline-item mx-2 mb-2">
            <a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-vuex" target="_blank"
              rel="noopener" class="btn btn-outline-primary">
              vuex
            </a>
          </li>
          <li>
            <!-- Óptimo (navegación SPA) -->
            <router-link to="/login" class="btn btn-primary px-4">
              <i class="bi bi-box-arrow-in-right me-2"></i> Ingresar al sistema
            </router-link>
          </li>
        </ul>
      </div>
    </div>

  </div>
</template>

<script setup>
// Tu código script aquí
</script>

<style scoped>
.home {
  padding-top: 2rem;
  padding-bottom: 2rem;
}

/* Opcional: personalización adicional */
.btn-outline-primary {
  --bs-btn-color: #42b983;
  --bs-btn-border-color: #42b983;
  --bs-btn-hover-bg: #42b983;
}

.btn-outline-success {
  --bs-btn-color: #2c3e50;
  --bs-btn-border-color: #2c3e50;
  --bs-btn-hover-bg: #2c3e50;
}

.btn-outline-info {
  --bs-btn-color: #34495e;
  --bs-btn-border-color: #34495e;
  --bs-btn-hover-bg: #34495e;
}
</style>