<template>
  <div>
    <b-button :disabled="!activateSubmitButton" @click="submit_experiment" type="submit" variant="primary"
      class="w-25 content-item submit-button">
      <span v-if="!submitted"> Guardar experimento </span>
      <span v-else> Guardado! </span>
      {{ submitted }}
    </b-button>
  </div>
</template>

<script>
// import { store } from "../main.js"; 

export default {
  name: "PlotNetworkSave",
  props: ['experiment', 'activateSubmitButton'],
  methods: {
    async submit_experiment() {
      this.submitted = false;
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


  }

}
</script>

<style scoped>
#options {
  border-radius: 10px;
  box-shadow: rgba(60, 64, 67, 0.3) 0px 1px 2px 0px,
    rgba(60, 64, 67, 0.15) 0px 1px 3px 1px;
}
</style>