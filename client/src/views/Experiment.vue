<template>
<b-container fluid> 
    <h2 id="header" v-if='((experiment.algorithm === "Louvain") | (experiment.algorithm === "Girvan-Newman"))'> Algoritmo de {{ experiment.algorithm }} </h2> 
    <h2 id="header" v-else> Visualización </h2> 
    <PlotNetwork></PlotNetwork>
    <PlotNetworkSave></PlotNetworkSave>
</b-container>
</template>

<script>
import PlotNetwork from "@/components/PlotNetwork.vue";
import PlotNetworkSave from "@/components/PlotNetworkSave.vue";
import { store } from "../main.js";
export default {
    name: "Experiment",
    components: { PlotNetwork, PlotNetworkSave },
    data: function () {
        return {
                experiment: store.state.lastComputedExperiment,
                };
    },
    mounted(){
        console.log(this.experiment)
    }
}

</script>

<style scoped>

    #title{
    position:absolute;  
    text-align: left;
    }

</style>