<template>
    
    <!-- <b-container fluid="md"> -->
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
    
</template>

<script>
export default{
    name: "UserLoginModal",
    data: function(){
        return {
            title: '',
            modalShow: true,
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
    methods: {
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
        },
        
    },
}
</script>