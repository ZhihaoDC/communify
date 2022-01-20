<template>
  <div id="app">
    <b-navbar type="dark" variant="dark">
      <b-navbar-nav>
        <b-navbar-brand to="/">network.ly</b-navbar-brand>
        <b-nav-item-dropdown text="Detección de comunidades" ref="dropdown">
          <b-dropdown-item to="/community-detection/louvain">Método de Louvain</b-dropdown-item>
          <b-dropdown-item to="/community-detection/girvan-newman">Método de Girvan-Newman</b-dropdown-item>
        </b-nav-item-dropdown>
        <b-nav-item to="/about"> About </b-nav-item>
      </b-navbar-nav>
    </b-navbar>
    
    <router-view/>

  </div>
</template>
<script>
export default {
    methods: {
      onOver() {
        this.$refs.dropdown.visible = true;
      },
      onLeave() {
        this.$refs.dropdown.visible = false;
      }
    }
  }
</script>

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
