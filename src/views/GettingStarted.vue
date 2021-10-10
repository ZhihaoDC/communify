<template>
  <b-container fluid="md">
    <div id="home">
      <h1 class="header"> Herramienta para visualización de grafos </h1>
        <p> Esta es una herramienta online para visualizar y analizar grafos.
        Sube un archivo .csv, consigue la visualización de la red,
        analiza su estructura y mucho más. 
        <router-link to="/about" id="about-link">Aprende más.</router-link>
        </p>
        <div class="tools">
          <b-card-group deck>
            <b-card
            title="Visualize network"
            tag="viz-network"
            style="max-width: 15rem;"
            class="mb-2">
              <b-card-text>
                Representa un grafo, cambia los nodos de color y posición
              </b-card-text>
              <b-button to="/community-detection" variant="primary">Go somewhere</b-button>
            </b-card>

            <b-card
            title="Visualize network"
            tag="viz-network"
            style="max-width: 15rem;"
            class="mb-2">
              <b-card-text>
                Representa un grafo, cambia los nodos de color y posición
              </b-card-text>
              <b-button to="/community-detection" variant="primary">Go somewhere</b-button>
            </b-card>

          </b-card-group>
          
          <b-card-group deck>
            <b-card
            title="Community detection: Louvain method"
            tag="community-detection-louvain"
            style="max-width: 15rem;"
            class="mb-2">
              <b-card-text>
                Método de Louvain. El más popular. Rápido y preciso
              </b-card-text>
              <b-button to="/community-detection" variant="primary">Go somewhere</b-button>
            </b-card>

            <b-card
            title="Community detection: Girvan-Newman method"
            tag="community-detection-girvan-newman"
            style="max-width: 15rem;"
            class="mb-2">
              <b-card-text>
                Método de Girvan-Newman. Más lento y menos conocido.
              </b-card-text>
              <b-button to="/community-detection" variant="primary">Go somewhere</b-button>
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