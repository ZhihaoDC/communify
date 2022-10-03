<template>

  <div id="container">

    <b-form-group id="input-name" label="Nombre del experimento" label-for="input-name">
      <b-form-input id="experiment_name" v-model="experiment_name"
        :placeholder="experiment_name_placeholder"></b-form-input>
    </b-form-group>

    <b-form-group id="input-description" label="Descripción" label-for="input-description">
      <b-form-textarea> id="description" v-model="description" placeholder="Introduce tu descripción"</b-form-textarea>
    </b-form-group>
 
    <b-button type="submit" :disabled="!activateSubmitButton" @click="submit_experiment" variant="primary"
      class="content-item submit-button">
      {{this.submitted_msg}}
    </b-button>
    <div id="success-alert">
    <b-alert
      :show="dismissCountDown"
      dismissible
      variant="success"
      @dismissed="dismissCountDown=0"
      @dismiss-count-down="countDownChanged"
    >
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
    return{
      experiment_name_placeholder: "Experimento " + this.experiment.dataset_name + " " + this.experiment.category,
      dismissSecs: 5,
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
    async submit_experiment() {
      this.experiment['experiment_name'] = this.experiment_name
      this.experiment['description'] = this.description

      const axios = require("axios");
      await axios.post('http://localhost:5000/save-experiment',
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
    },
  },
}
</script>

<style scoped>
  #success-alert{
    padding-top:15px;
    padding-bottom:5px;
  }
</style>