<template>
    <b-container fluid="md" align="left">
    <b-card>
    <b-form>
      
      <b-form-group label="Nombre de usuario:" label-for="email">
        <b-form-input
          id="username"
          v-model="form.username"
          placeholder="Introduce tu nombre de usuario"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group label="Email" label-for="email">
        <b-form-input
          id="email"
          v-model="form.email"
          type="email"
          placeholder="Introduce tu email"
          :state="is_email_valid"
          lazy-formatter
          :formatter="email_format"
          required
        ></b-form-input>
        <b-form-invalid-feedback id="input-live-feedback">
          El email debe contener una dirección de correo con'@''.'
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
          La contraseña debe tener al menos 8 caracteres.
        </b-form-invalid-feedback>
      </b-form-group>

      <b-form-group label="Confirmación:" label-for="password-repeat">
        <b-form-input
          v-model="form.password_confirmation"
          type="password"
          placeholder="Repite la contraseña"
          :state="is_password_confirmation_valid"
          lazy-formatter
          :formatter="password_confirmation_format"
          required
        ></b-form-input>
        <b-form-invalid-feedback id="input-live-feedback">
          Las contraseñas no coinciden
        </b-form-invalid-feedback>
      </b-form-group>

      <b-button block size ="lg" type="submit" @click="signUp" variant="primary"
        class="content-item submit-button"
        :disabled="!valid_fields">
        Aceptar
      </b-button>
      <b-link to=""> ¿No tienes cuenta? Crea una cuenta </b-link>
    </b-form>
  </b-card>
    
</b-container>
</template>

<script>
// import UserLoginModal from "@/components/UserLoginModal.vue"
export default {
    name: "UserSignUp",
    // components: UserLoginModal,
    data: function(){
        return{
            form: {
                    username: '',
                    email: '',
                    password: '',
                    password_confirmation: ''
                    },
            is_email_valid: null,
            is_password_valid: null,
            is_password_confirmation_valid: null
        }
    },
    computed: {
      valid_fields(){
        return ((this.is_email_valid) & (this.is_password_valid) & (this.is_password_confirmation_valid))
      }
    },
    methods:{
      email_format(email){
        const isValidEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
        if (isValidEmail){
          this.is_email_valid = true
        }
        else{
          this.is_email_valid = false
        }
        return email
      },
      password_format(password){
        if (password.length == 0){
          this.is_password_valid = null
        }
        else if (password.length < 8){
          this.is_password_valid = false
        }
        else if (password.length >= 8 ){
          this.is_password_valid = true
        }
        return password

      },
      password_confirmation_format(password_confirmation) {
        let password = this.form.password
        if (password_confirmation.length === 0){
          this.is_password_confirmation_valid = null
        }
        else if (password_confirmation != password) {
          this.is_password_confirmation_valid = false
        } 
        else if (password_confirmation === password){
          this.is_password_confirmation_valid = true
        }   
        return password_confirmation
      },

      signUp(){
        const axios = require('axios')
        console.log(this.form)

        axios.post('http://localhost:5000/create-user',
          this.form
        )
        .then(function (response){
          if (response.status == 200){
            console.log(response.successMsg)
            // Modal success
          }
          else if (response.status == 500){
            // Modal error
            console.log(response.errorMessage)
          }
        })
        .catch(function(response){
          //Modal error 
          console.log(response.errorMessage)
        })

      }
    }
}
</script>