<template>

  <b-container id="container">

    <b-form-group>
      <h4 v-if="!editing" @click="startEditing" title="Nombre del experimento"> {{experiment_name}} 
        <b-icon id="edit-icon" icon="pencil-fill"></b-icon>
      </h4>

      <b-form-input v-else id="experiment_name" 
      ref="experiment_name_input" 
      class="custom-input" 
      v-model="experiment.experiment_name"
      @keyup.enter="stopEditing"
      @blur="stopEditing" 
      @focus="moveCursorToLeft"
      :placeholder="experiment_name">
      </b-form-input>
  </b-form-group>

    <b-form-group id="input-description" label="Descripción" label-for="input-description">
      <b-form-textarea id="description" v-model="experiment.description"
        placeholder="Introduce una descripción para el experimento"></b-form-textarea>
    </b-form-group>


   
    <PlotVisualizationParameters @updateVisualizationParameters="updateVisualizationParameters"></PlotVisualizationParameters>

    <b-button block size ="lg" type="submit" :disabled="!activateSubmitButton" @click="handleSubmitNetwork" variant="primary"
      class="content-item submit-button">
      {{this.submitted_msg}}
    </b-button>


    <div id="success-alert">
      <b-alert :show="dismissCountDown" dismissible fade variant="success" @dismissed="dismissCountDown=0"
        @dismiss-count-down="countDownChanged">
        ¡Experimento guardado! 
        <router-link to="/user-experiments" id="experiments-link">Ir a experimentos</router-link>
      </b-alert>
    </div>
    
  </b-container>

</template>

<script>
import { store } from '../main'
import PlotVisualizationParameters from "@/components/PlotVisualizationParameters.vue"

export default {
  name: "PlotNetworkForm",
  components: {PlotVisualizationParameters},
  props: ['activateSubmitButton'],
  data: function () {
    return {
      experiment: store.getLastComputedExperiment(),
      experiment_name: store.getLastComputedExperiment().experiment_name,
      user_id : 1,
      editing: false,
      dismissSecs: 4,
      dismissCountDown: 0,
      submitted_msg: "Guardar experimento",
      visualizationParameters: store.getLastComputedExperiment().visualization_params
    }
  },
  methods: {
    startEditing(){
      this.editing = true
      this.experiment.experiment_name = this.experiment_name
      this.$nextTick(() => {
        this.$refs.experiment_name_input.$el.setSelectionRange(0, 0)
        this.$refs.experiment_name_input.focus()
      })
    },
    stopEditing(){
      this.editing = false
      if ((this.experiment.experiment_name !== this.experiment.dataset_name) & (this.experiment.experiment_name !== "")){
        this.experiment_name = this.experiment.experiment_name
      }
    },  
    moveCursorToLeft() {
      const inputElement = this.$refs.experiment_name_input.$el;
      inputElement.setSelectionRange(this.experiment.experiment_name.length, this.experiment.experiment_name.length);
    },
    countDownChanged(dismissCountDown) {
      this.dismissCountDown = dismissCountDown
    },
    showAlert() {
      this.dismissCountDown = this.dismissSecs
    },
    updateVisualizationParameters(newvisualizationParameters){
        this.visualizationParameters = newvisualizationParameters
        this.experiment.visualization_params = newvisualizationParameters
        this.$emit('updateVisualizationParameters', newvisualizationParameters)
    },
    async handleSubmitNetwork(){
      // console.log("Mandando señal para actualizar experimento...")
      this.$emit("export-network")
    },
    submit_experiment_with_confirmation() {
      //Ask confirmation
      // console.log("Subiendo experimento")
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
          .then(confirmation => {
            if (confirmation){
              this.submit_experiment_to_backend()
            }
          })
          .catch(err => {
            // An error occurred
            console.log("Error: ")
            console.log(err)
          })
      }
      if (!this.confirmation && (this.experiment.experiment_id == null)) {
        this.submit_experiment_to_backend()
      }
    },

    submit_experiment_to_backend() {
      const axios = require("axios");
      console.log(store.getLastComputedExperiment())
      axios.post('http://localhost:5000/save-experiment/'+this.user_id,
        JSON.stringify(store.getLastComputedExperiment()),
        {
          headers: {
            'Content-Type': 'application/json'
          }
        })
        .then((response) => {
          if (response.status === 200) {
            this.submitted_msg = "Guardado!"
            this.experiment = response.data.experiment
            store.setLastComputedExperiment(this.experiment)
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

#container{
  margin-left: 1rem;
}
.custom-input{
  border: none;
  box-shadow: none;
  outline: none;
  font-size: 1.5rem;
  text-align: center;
}

#input-name,
#input-description {
  text-align: left;
}

#edit-icon{
  padding-bottom: 0.15em;
  padding-top: 0.1em;
  padding-left: 0.05em;
  padding-right: 0.1em;
}
#success-alert {
  padding-top: 15px;
  padding-bottom: 5px;
}
</style>