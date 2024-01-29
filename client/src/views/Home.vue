<template>
  <b-container fluid class="custom-container p-auto">
      
      
      <b-row>
        <b-col md-6>
          <h1 id="header"> Bienvenido a network.ly </h1>
          <h4> Herramienta de detección de comunidades y visualización de grafos. </h4>
          <br/>
          <!-- <h5>La detección de comunidades agrupa los nodos en comunidades en función de las relaciones entre sus individuos, 
            lo cual descubre propiedades que no son visibles a simple vista.
            
            Se diferencia del clustering tradicional de grafos en que no utiliza las propiedades de cada inviduo.
          </h5> -->

          <h5>
            Agrupa las redes por los atributos que lo relacionan. Representa redes y edítalas a tu gusto.
            La herramienta de un auténtico investigador.
          </h5>
          <router-link to="/about" id="about-link">Aprende más sobre la detección de comunidades</router-link>
          <br>

          <b-row class="mt-4">
            <b-button size="lg" class="try-me md-3 ml-auto mr-4">
              Try me!
            </b-button>

            <b-button size="lg" class="login md-3 mr-auto ml-4">
              Iniciar sesión
            </b-button>

          </b-row>
          

          <br/>
      </b-col>

      
      <b-col md-6>
      <div class="tools">
        <b-card-group columns>
          <a href="/community-detection">
          <b-card
          title="Detección de comunidades"
          img-src="../assets/network-graphs.webp"
          size="sm"
          class="mb-4 mt-4"
          id="b-card">
            <b-card-text class=" d-flex justify-content-center align-items-center">
              Detectar comunidades en una red y visualizar el resultado.
            </b-card-text>
            <!-- <b-button block to="/community-detection" variant="primary" id="go">Ir</b-button> -->
          </b-card>
        </a>

          <a href="/graph-visualization">
          <b-card
          title="Visualizar grafo"
          img-src="../assets/network-visualization.webp"
          size="sm"
          class="mb-4"
          id="b-card">
            <b-card-text>
              Representa un grafo, cambia los nodos de color y posición
            </b-card-text>
            <!-- <b-button block to="/graph-visualization" variant="primary" id="go">Ir</b-button> -->
          </b-card>
        </a>

        <a href="/user-datasets">
          <b-card
          v-if="isAuthenticated"
          title="Mis Datasets"
          img-src="../assets/datasets.webp"
          class="mb-4"
          id="b-card" >
            <b-card-text>
              Subir y gestionar datasets. También puedes iniciar un experimento con un dataset existente.
            </b-card-text>
            <!-- <b-button block to="/user-datasets" variant="primary" id="go">Ir</b-button> -->
          </b-card>
        </a>

        <a href="/user-experiments">
          <b-card
          v-if="isAuthenticated"
          title="Mis Experimentos" 
          img-src="../assets/experiments.webp"
          class="mb-4 mt-4"
          id="b-card" >
            <b-card-text>
              Gestiona y visualiza de nuevo los experimentos que has creado.
            </b-card-text>
            <!-- <b-button block to="/user-experiments" variant="primary" id="go">Ir</b-button> -->
          </b-card>
        </a>

        </b-card-group>
      </div>
    </b-col>
  </b-row>
      
  </b-container>
</template>

<script>
export default {
  name: 'Home',
  computed: {
    isAuthenticated() {
      return this.$store.getters['auth/isAuthenticated']
    }
  }
}
</script>

<style scoped>

  a:link { 
    text-decoration: none; 
  } 
  a:visited { 
    text-decoration: none; 
  } 
  a:hover { 
    text-decoration: none; 
  } 
  a:active { 
    text-decoration: none; 
  }
  #start-button{
    padding: 0.5em 0.7em;
  }

  #about-link{
    color: #42b983;
    text-decoration: none;
  }

  
  #section-header{
      padding-top: 2rem;
      padding-bottom:1rem;
  }

  #b-card{
    box-shadow: rgba(60, 64, 67, 0.3) 0px 1px 2px 0px, rgba(60, 64, 67, 0.15) 0px 1px 3px 1px;
    max-width: 25rem;
  }

  #go{
    box-shadow: rgba(0, 0, 0, 0.12) 0px 1px 3px, rgba(0, 0, 0, 0.24) 0px 1px 2px;
  }

  .try-me{
    display: inline-block;
    color: aliceblue;
    background: #9363dc;
    border-radius: 10px;
    border-color: none;
    padding: 0.7em 1em;
    margin-bottom: 0.2em;
    cursor: pointer;
    box-shadow: rgba(57, 40, 58, 0.12) 0px 1px 3px, rgba(50, 40, 55, 0.24) 0px 1px 2px;
  }

  .try-me:hover {
    background-color: aliceblue;
    color: #050517;
    text-decoration: none;
  }

  .login{
    display: inline-block;
    color: aliceblue;
    background: #5bcaca;
    border-radius: 10px;
    border-color: none;
    padding: 0.7em 1em;
    margin-bottom: 0.2em;
    cursor: pointer;
    box-shadow: rgba(212, 233, 243, 0.979) 0px 1px 3px,rgba(176, 243, 255, 0.886) 0px 1px 2px;
  }

  .login:hover{
    background-color: #050517;
    color: aliceblue;
    text-decoration: none;
  }

  .custom-container {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
    width: 100vw;
    }

</style>