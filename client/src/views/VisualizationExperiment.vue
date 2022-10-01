<template>
<b-container fluid id="parent-container"> 
    
    <h2 id="header" v-if='((experiment.category === "Louvain") | (experiment.category === "Girvan-Newman"))'> Algoritmo de {{ experiment.category }} </h2> 
    <h2 id="header" v-else> Visualización </h2>  
    <b-row>
        <b-col cols="8">
            <PlotNetwork id="network-viz" :experiment="experiment" @ready="animation_finished = true"></PlotNetwork>
        </b-col>
        <b-col cols="4">
            <PlotNetworkForm id="save-network-form" :experiment="experiment" :activateSubmitButton="animation_finished"></PlotNetworkForm>
        </b-col>
        
    </b-row>
</b-container>
</template>

<script>
import PlotNetwork from "@/components/PlotNetwork.vue";
import PlotNetworkForm from "@/components/PlotNetworkForm.vue";
import { store } from "../main.js";
export default {
    name: "VisualizationExperiment",
    components: { PlotNetwork, PlotNetworkForm },
    data: function () {
        return {
                experiment: store.state.lastComputedExperiment,
                animation_finished: false,
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

    #parent-container{
        padding-left: 20px;
        padding-right: 20px
    }

    #save-network-form{
        height: 100%;
        min-height: 75vh;
        min-width: 35%;
        max-width: 35vw;
        
    }

    #network-viz{
        height: 100%;
        min-height: 75vh;
        min-width: 65%;
        max-width: 65vw;
    }
</style>