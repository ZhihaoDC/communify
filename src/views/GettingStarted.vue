<template>
  <b-container fluid="md">
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <h2 class="header"> Bienvenido a community detection </h2>
    <div class="centered-container">
      <div class="content">
        <p> La detección de comunidades en un grafo es un problema de 
          aprendizaje automático no supervisado que muestra patrones en un grafo o red.
        </p>
        <p>Una comunidad puede representar un grupo de amigos,
          un cúmulo de individuos con intereses en común, y muchas
          cosas más. 
          
          <router-link to="/about" id="about-link">Aprende más.</router-link>
        </p>
        <p> En esta página podrás detectar comunidades 
          subiendo un archivo CSV y podrás elegir los distintos
          algoritmos de detección de comunidades. 
        </p>
        <router-link to="/community-detection" 
        class="custom-button"
        >Vamos a ello!</router-link>
      </div>
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