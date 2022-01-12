<template>
  <div id="app">
    <b-navbar type="dark" variant="dark">
      <b-navbar-nav>
        <b-navbar-brand to="/">network.ly</b-navbar-brand>
        <b-nav-item to="/community-detection"> Detectar comunidades </b-nav-item>
        <b-nav-item to="/about"> About </b-nav-item>
      </b-navbar-nav>
    </b-navbar>
    
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
