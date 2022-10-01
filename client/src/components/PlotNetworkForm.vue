<template>

  <div id="container">

    <b-form-group id="input-name" label="Nombre del experimento" label-for="input-name">
      <b-form-input id="experiment_name" v-model="experiment_name"
        :placeholder="experiment_name_placeholder"></b-form-input>
    </b-form-group>

    <b-form-group id="input-description" label="Descripción" label-for="input-description">
      <b-form-input id="description" v-model="description" placeholder="Introduce tu descripción"></b-form-input>
    </b-form-group>
 
    <b-button type="submit" :disabled="!activateSubmitButton" @click="submit_experiment" variant="primary"
      class="w-25 content-item submit-button">
      <span v-if="!submitted"> Guardar experimento </span>
      <span v-else> Guardado! </span>
    </b-button>

  </div>
  
</template>

<script>
export default {
  name: "PlotNetworkForm",
  props: ['experiment', 'activateSubmitButton'],
  data: function () {
    return{
      submitted: false,
      experiment_name_placeholder: "Experimento " + this.experiment.dataset_name + " " + this.experiment.category
    }
  },
  methods: {
    async submit_experiment() {
      this.experiment['experiment_name'] = this.experiment_name
      this.experiment['description'] = this.description
      console.log(this.experiment)
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
            this.submitted = true
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
  #container {
    padding: 10px;
    min-height: 75vh;
    border-radius: 10px;
    box-shadow: rgba(60, 64, 67, 0.3) 0px 1px 2px 0px,
      rgba(60, 64, 67, 0.15) 0px 1px 3px 1px;
  }
</style>