<template>
    <b-container fluid>
 
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
    </b-container>
  </template>
  
  <script>
  export default {
    name: 'HomeUser',
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
  </style>