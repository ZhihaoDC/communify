<template>
    
    <b-container fluid="md">
        <!-- <b-modal v-model="modalShow" :title=title ok-only @hide="resetInfoModal"> -->
    <p> Hola </p>
    <b-form>
        <b-form-group label="Email" label-for="email">
            <b-form-input
            v-model="form.identification"
            placeholder="Introduce tu nombre de usuario o email"
            :state="is_identification_valid"
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

        <b-button block type="submit" @click="login" variant="primary"
        class="content-item submit-button">
            Iniciar sesión
        </b-button>
        <b-link to="/"> ¿No tienes cuenta? Crea una cuenta </b-link>

    </b-form>
    
</b-container>
    <!-- </b-modal> -->
    
</template>

<script>
export default{
    name: "UserLoginModal",
    data: function(){
        return{
            title: '',
            modalShow: true,
            identification : '',
            form: {
                    username: '',
                    email: '',
                    name: '',
                    password: '',
                },
        }
    },
    methods: {
        login(){
            const axios = require('axios')
        },

        identification_format(identification){
            const isValidEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)
            if (isValidEmail) {this.email = identification}
            else {this.username = identification}
        },
        
        closeModal() {
            this.modalShow = false;
        },

        resetInfoModal() {
            this.title = '';
        },
        
    },
}
</script>