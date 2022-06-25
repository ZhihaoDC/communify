<template>
  <b-container fluid>
      <h1 id="header"> Bienvenido a network.ly </h1>
      <h4> Herramienta de visualización de grafos y de detección de comunidades. </h4>
      <router-link to="/about" id="about-link">Aprende más sobre la detección de comunidades</router-link>
      <br/>
      <div class="tools">
        <b-card-group deck>
          <b-card
          title="Detección de comunidades: método de Louvain"
          style="max-width: 25rem;"
          class="mb-3"
          id="b-card">
            <b-card-text>
              Método de Louvain. El más popular. Rápido y preciso
            </b-card-text>
            <b-button block to="/community-detection/louvain" variant="primary" id="go">Ir</b-button>
          </b-card>

          <b-card
          title="Detección de comunidades: método de Girvan-Newman"
          style="max-width: 25rem;"
          class="mb-3"
          id="b-card">
            <b-card-text>
              Método de Girvan-Newman. Más lento y menos conocido.
            </b-card-text>
            <b-button block to="/community-detection/girvan-newman" variant="primary" id="go">Ir</b-button>
          </b-card>

          <b-card
          title="Visualización: Representar grafo o red"
          style="max-width: 25rem;"
          class="mb-3"
          id="b-card">
            <b-card-text>
              Representa un grafo, cambia los nodos de color y posición
            </b-card-text>
            <b-button block to="/graph-visualization" variant="primary" id="go">Ir</b-button>
          </b-card>
        </b-card-group>
      </div>
  </b-container>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
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

  #b-card{
    box-shadow: rgba(60, 64, 67, 0.3) 0px 1px 2px 0px, rgba(60, 64, 67, 0.15) 0px 1px 3px 1px;
  }

  #go{
    box-shadow: rgba(0, 0, 0, 0.12) 0px 1px 3px, rgba(0, 0, 0, 0.24) 0px 1px 2px;
  }
</style>