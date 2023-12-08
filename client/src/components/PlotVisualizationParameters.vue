<template>
  <b-form-group id="nw-parameters">
    <label id="nwParam" for="nw-nodeSeparation">Separacion de nodos</label>
    <b-form-spinbutton id="nw-nodeSeparation" size="sm" class="mb-3"
      v-model="visualizationParameters.nodeSeparation" min="1000" max="20000" step="1000" @change="emit_changes()"
    ></b-form-spinbutton>

    <label id="nwParam" for="nw-communitySeparation">Separacion de comunidades</label>
    <b-form-spinbutton id="nw-communitySeparation" size="sm" class="mb-3"
      v-model="visualizationParameters.communitySeparation" min="100" max="10000" step="100" @change="emit_changes()"
    ></b-form-spinbutton>

    <label id="nwParam" for="nw-gravity">Gravedad</label>
    <b-form-spinbutton id="nw-gravity" size="sm" class="mb-3"
      v-model="visualizationParameters.gravity" min="0.1" max="1" step="0.1" @change="emit_changes()"
    ></b-form-spinbutton>
  </b-form-group>
</template>


<script>
import { store } from "../main.js";
  export default {
    name: "PlotVisualizationParameters",
    data() {
      return {
          debounceTimer: null,
          changesQueue: [],
          visualizationParameters: store.getLastComputedExperiment().visualization_params
      }
    },
    methods:{
      emit_changes() {
          this.$emit('updateVisualizationParameters', this.visualizationParameters)
      }
    }
  }
</script>

<style scoped>
#nwParam{
  text-align: left;
}
</style>