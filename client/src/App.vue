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
          <b-nav-item right @click=modalLogin()> Login </b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    
    
      <router-view />

      <b-modal v-model="modalShow" :title=title ok-only @hide="resetInfoModal">
    <b-form>
        <b-form-group label="Email" label-for="email">
            <b-form-input
            id="email"
            v-model="form.identification"
            placeholder="Introduce tu nombre de usuario o email"
            :state="is_identification_valid"
            lazy-formatter
            :formatter="identification_format"
            required
            ></b-form-input>
            <b-form-invalid-feedback id="input-live-feedback">
                El nombre de usuario o email es incorrecto o no existen.
            </b-form-invalid-feedback>
        </b-form-group>


        <b-form-group label="Contraseña:" label-for="password">
            <b-form-input
            v-model="form.password"
            type="password"
            placeholder="Introduce una contraseña"          
            :state="is_password_valid"
            lazy-formatter
            :formatter="password_format"
            required
            ></b-form-input>
            <b-form-invalid-feedback id="input-live-feedback">
                La contraseña es incorrecta.
            </b-form-invalid-feedback>
        </b-form-group>

        <b-button block type="submit" @click.stop.prevent="login" variant="primary"
        class="content-item submit-button">
            Iniciar sesión
        </b-button>
        <b-link to="/"> ¿No tienes cuenta? Crea una cuenta </b-link>

    </b-form>
    
<!-- </b-container> -->
    </b-modal>
    
  </div>
</template>


<script>
export default {
  data: function(){
    return {
      title: 'Identifícate',
      modalShow: false,
      identification : '',
      is_identification_valid: null,
      is_password_valid: null,
      form: {
              username: '',
              email: '',
              password: '',
          },
    }
  },
  computed: {
    isAuthenticated() {
      return this.$store.getters['auth/isAuthenticated']
    }
  },
  methods: { 
    modalLogin() {
      this.modalShow = true
    },

    async login(){
        await this.$store.dispatch('auth/loginToDB', this.form)
            .then(() => {
                this.$router.push('/')
            })
            .catch(response => {
                console.log(`Error: ${response.errorMessage}`)
            })
    },

    identification_format(identification){
        const isValidEmail = String(identification)
            .toLowerCase()
            .match(
                /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            );
        if (isValidEmail) {this.form.email = identification}
        else {this.form.username = identification}
        return identification
    },
    
    closeModal() {
        this.modalShow = false;
    },

    resetInfoModal() {
        this.title = '';
        this.modalShow = false
    },
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
