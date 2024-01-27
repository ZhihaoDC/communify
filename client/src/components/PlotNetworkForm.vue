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
      <b-form-textarea id="description" v-model="experiment.description" @change="updateDescription"
        placeholder="Introduce una descripción para el experimento"></b-form-textarea>
    </b-form-group>
   
    <PlotVisualizationParameters @updateVisualizationParameters="updateVisualizationParameters"></PlotVisualizationParameters>


    <b-button block size ="lg" type="submit" v-if="isAuthenticated" :disabled="!activateSubmitButton" @click="handleSubmitNetwork" variant="primary"
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
import PlotVisualizationParameters from "@/components/PlotVisualizationParameters.vue"

export default {
  name: "PlotNetworkForm",
  components: {PlotVisualizationParameters},
  props: ['activateSubmitButton'],
  data: function () {
    return {
      experiment: this.$store.getters['experiment/getExperiment'],
      experiment_name: this.$store.getters['experiment/getExperiment'].experiment_name,
      user_id : 1,
      editing: false,
      dismissSecs: 4,
      dismissCountDown: 0,
      submitted_msg: "Guardar experimento",
      visualizationParameters: this.$store.getters['experiment/getVisualizationParams'],
      communityColor: null
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
        this.$store.commit('experiment/setExperimentName', this.experiment_name)
      }
    },  
    moveCursorToLeft() {
      const inputElement = this.$refs.experiment_name_input.$el;
      inputElement.setSelectionRange(0, this.experiment.experiment_name.length);
    },
    countDownChanged(dismissCountDown) {
      this.dismissCountDown = dismissCountDown
    },
    updateDescription(){
      this.$store.commit('experiment/setExperimentDescription', this.experiment.description)
    },
    showSuccessAlert() {
      this.dismissCountDown = this.dismissSecs
    },
    updateVisualizationParameters(newvisualizationParameters){
        this.visualizationParameters = newvisualizationParameters
        this.experiment.visualization_params = newvisualizationParameters
        this.$store.commit('experiment/setVisualizationParams', newvisualizationParameters)
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
            console.log(`Error: ${err}`)
          })
      }
      if (!this.confirmation && (this.experiment.experiment_id == null)) {
        this.submit_experiment_to_backend()
      }
    },

    async submit_experiment_to_backend() {
      this.experiment = this.$store.getters['experiment/getExperiment'] 
      console.log(this.$store.getters['experiment/getExperiment'])
      await this.$store.dispatch('experiment/saveExperiment')      
      this.experiment = this.$store.getters['experiment/getExperiment']
      console.log(this.experiment)
      this.submitted_msg = "Guardado!"
      this.showSuccessAlert()
    }, 
  
  },
  computed: {
      isAuthenticated() {
        return this.$store.getters['auth/isAuthenticated']
      }
    }
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