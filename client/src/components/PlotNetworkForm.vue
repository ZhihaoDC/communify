<template>

  <div id="container">

    <h4> Guardar experimento </h4>
    <br />
    <b-form-group id="input-name" label="Nombre del experimento" label-for="input-name">
      <b-form-input id="experiment_name" v-model="experiment.experiment_name" :placeholder="experiment.dataset_name">
      </b-form-input>
    </b-form-group>

    <b-form-group id="input-description" label="Descripción" label-for="input-description">
      <b-form-textarea id="description" v-model="experiment.description"
        placeholder="Introduce una descripción para el experimento"></b-form-textarea>
    </b-form-group>

    <b-button type="submit" :disabled="!activateSubmitButton" @click="submit_experiment" variant="primary"
      class="content-item submit-button">
      {{this.submitted_msg}}
    </b-button>
    <div id="success-alert">
      <b-alert :show="dismissCountDown" dismissible fade variant="success" @dismissed="dismissCountDown=0"
        @dismiss-count-down="countDownChanged">
        ¡Experimento guardado!
      </b-alert>
    </div>
  </div>

</template>

<script>
export default {
  name: "PlotNetworkForm",
  props: ['experiment', 'activateSubmitButton'],
  data: function () {
    return {
      experiment_name_placeholder: this.experiment.dataset_name,
      experiment_description_placeholder: "Introduce una descripción",
      dismissSecs: 4,
      dismissCountDown: 0,
      submitted_msg: "Guardar experimento",
    }
  },
  methods: {
    countDownChanged(dismissCountDown) {
      this.dismissCountDown = dismissCountDown
    },
    showAlert() {
      this.dismissCountDown = this.dismissSecs
    },
    submit_experiment() {
      //Ask confirmation

      this.confirmation = false
      if (this.experiment.experiment_id != null) {
        this.$bvModal.msgBoxConfirm('Guardar de nuevo experimento sobreescribirá el antiguo. ¿Quieres sobreescribir el experimento anterior?', {
          title: '¿Sobreescribir experimento?',
          size: 'sm',
          buttonSize: 'sm',
          okVariant: 'primary',
          okTitle: 'Sobreescribir',
          cancelTitle: 'Cancelar',
          footerClass: 'p-2',
          hideHeaderClose: false,
          centered: true
        })
          .then(action => {
            this.confirmation = action
            console.log(this.confirmation)
            this.submit_experiment_to_backend()
          })
          .catch(err => {
            // An error occurred
            console.log(err)
          })
      }
      if (!this.confirmation && (this.experiment.experiment_id == null)) {
        this.submit_experiment_to_backend()
      }
    },

    submit_experiment_to_backend() {
      const axios = require("axios");
      axios.post('http://localhost:5000/save-experiment',
        JSON.stringify(this.experiment),
        {
          headers: {
            'Content-Type': 'application/json'
          }
        })
        .then((response) => {
          if (response.status === 200) {
            console.log(response)
            this.submitted_msg = "Guardado!"
            this.experiment = response.data.experiment
            this.showAlert()
          }
        })
        .catch((error) => {
          console.log(error.response);
          if (error.response.status == 500) {
            this.error_msg = "Error en la comunicacion con el servidor";
            this.submitted = false;
          }
        })
    }


  },
}
</script>

<style scoped>
#input-name,
#input-description {
  text-align: left;
}

#success-alert {
  padding-top: 15px;
  padding-bottom: 5px;
}
</style>