<template>
    <b-container class="container">
        
        <b-row>
            <!-- Content for the left half goes here -->
            <h1 id="header"> Bienvenido a network.ly </h1>
            <h4> Herramienta de visualización de grafos y de detección de comunidades. </h4>
        </b-row>
        <b-row>
                <!-- Content for the right half goes here -->
                <h2>Explora los grafos</h2>
                <p>Nunca había sido tan sencillo.</p>

        </b-row>
        <div class="sloped-divider"></div>

        <!-- <router-link to="/about" id="about-link">Aprende más sobre la detección de comunidades</router-link>
        <br/> -->
        <!-- <div class="tools">
          <b-card-group deck>
            <b-card
            title="Detección de comunidades"
            class="mb-4"
            id="b-card">
              <b-card-text>
                Detectar comunidades en una red y visualizar el resultado.
              </b-card-text>
              <b-button block to="/community-detection" variant="primary" id="go">Ir</b-button>
            </b-card>
  
            
            <b-card
            title="Visualizar grafo"
            class="mb-4"
            id="b-card">
              <b-card-text>
                Representa un grafo, cambia los nodos de color y posición
              </b-card-text>
              <b-button block to="/graph-visualization" variant="primary" id="go">Ir</b-button>
            </b-card>
  
            
          </b-card-group>
          <b-card-group deck v-if="isAuthenticated">
            <b-card
            title="Mis Datasets"
            class="mb-4"
            id="b-card" >
              <b-card-text>
                Subir y gestionar datasets. También puedes iniciar un experimento con un dataset existente.
              </b-card-text>
              <b-button block to="/user-datasets" variant="primary" id="go">Ir</b-button>
            </b-card>
  
            <b-card
            title="Mis Experimentos" 
            class="mb-4"
            id="b-card" >
              <b-card-text>
                Gestiona y visualiza de nuevo los experimentos que has creado.
              </b-card-text>
              <b-button block to="/user-experiments" variant="primary" id="go">Ir</b-button>
            </b-card>
  
  
          </b-card-group>
        </div> -->

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

    body, html {
        margin: 0;
        padding: 0;
        overflow: hidden;        
        
    }

    .container {
        position: relative;
        overflow: hidden; /* Hide overflow to prevent gradient overflow */
        min-height: 100vh;
        min-width: 100vw
    }

    .left-half,
    .right-half {
        padding: 20px;
        box-sizing: border-box;
    }

    .left-half {
        background-color: #f0f0f0; /* Light background color for the left half */
    }

    .right-half {
        background-color: #333; /* Dark background color for the right half */
        color: #fff; /* Text color for the right half, adjust as needed */
    }

    .sloped-divider {
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        width: 50%;
        background: linear-gradient(to bottom right, #f0f0f0 49.5%, #333 50.5%);
        z-index: -1; /* Ensure the divider is above the content */
    }
  </style>