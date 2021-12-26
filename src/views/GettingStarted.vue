<template>
  <b-container fluid="md">
    <div id="home">
      <h1 class="header"> Bienvenido a network.ly </h1>
      <h4> Herramienta de visualización de grafos y de detección de comunidades. </h4>
      <router-link to="/about" id="about-link">Aprende más sobre la detección de comunidades</router-link>
      
      <div class="tools">
        <b-card-group deck>
          <b-card
          title="Detección de comunidades: método de Louvain"
          tag="community-detection-louvain"
          style="max-width: 25rem;"
          class="mb-3">
            <b-card-text>
              Método de Louvain. El más popular. Rápido y preciso
            </b-card-text>
            <b-button block to="/community-detection" variant="primary">Ir</b-button>
          </b-card>

          <b-card
          title="Detección de comunidades: método de Girvan-Newman"
          tag="community-detection-girvan-newman"
          style="max-width: 25rem;"
          class="mb-3">
            <b-card-text>
              Método de Girvan-Newman. Más lento y menos conocido.
            </b-card-text>
            <b-button block to="/community-detection" variant="primary">Ir</b-button>
          </b-card>

          <b-card
          title="Visualización: Representar grafo o red"
          tag="viz-network"
          style="max-width: 25rem;"
          class="mb-3">
            <b-card-text>
              Representa un grafo, cambia los nodos de color y posición
            </b-card-text>
            <b-button block to="/community-detection" variant="primary">Ir</b-button>
          </b-card>
        </b-card-group>
      </div>
    </div>
  </b-container>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'GettingStarted',
}
</script>

<style scoped>

  #start-button{
    padding: 0.5em 0.7em;
  }

  #about-link{
    color: #42b983;
    text-decoration: none;
  }


</style>