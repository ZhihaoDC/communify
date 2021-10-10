<template>
  <div id="app">

    <div id="nav">
      <router-link to="/">Getting Started</router-link> |
      <router-link to="/community-detection"> Detectar comunidades </router-link> |
      <router-link to="/about">About</router-link>
    </div>
    
    <router-view/>

  </div>
</template>

<style lang="scss">
 @import './assets/scss/custom.scss';
 
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}

</style>
