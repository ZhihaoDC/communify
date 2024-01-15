<template>
  <div id="app">
    <b-navbar toggleable="md" type="dark" variant="dark" id="nav-bar">
      <b-navbar-brand id="brand" to="/">network.ly</b-navbar-brand>
      <b-navbar-toggle target="routes"></b-navbar-toggle>
      <b-collapse is-nav id="routes">
        <b-navbar-nav>
          <b-nav-item-dropdown text="Detección de comunidades" ref="dropdown" align="right">
            <b-dropdown-item to="/community-detection/louvain"
              >Método de Louvain</b-dropdown-item
            >
            <b-dropdown-item to="/community-detection/girvan-newman" align="right"
              >Método de Girvan-Newman</b-dropdown-item
            >
          </b-nav-item-dropdown>
          <b-nav-item v-if="isAuthenticated" to="/user-datasets"> Datasets </b-nav-item>
          <b-nav-item v-if="isAuthenticated" to="/user-experiments"> Experimentos </b-nav-item>
          <b-nav-item v-if="isAuthenticated" to="/graph-visualization"> Visualizar grafo </b-nav-item>
          <b-nav-item right to="/about"> About </b-nav-item>
          <b-nav-item right to="/user-signup"> Registrarse </b-nav-item>          
          <b-nav-item right to="/user-login"> Login </b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
      <router-view />
  </div>
</template>


<script>
export default {
  computed: {
    isAuthenticated() {
      return this.$store.getters['auth/isAuthenticated']
    }
  }
};
</script>


<style lang="scss">
@import "./assets/scss/custom.scss";

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #046865;
    }
  }
}

#brand {
  color: #fcfff7;
}

#nav-bar {
  box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 15px -3px,
    rgba(0, 0, 0, 0.05) 0px 4px 6px -2px;
}

.fade-enter {
  opacity: 0;
}

.fade-enter-active {
  transition: opacity 0.1s ease;
}

.fade-leave-active {
  transition: opacity 0.1s ease;
  opacity: 0;
}
</style>
