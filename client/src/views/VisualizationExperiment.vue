<template>
<b-container fluid id="parent-container"> 
    <b-row>
        <b-col cols="8">
            <h2 id="header" v-if='((experiment.category === "Louvain") | (experiment.category === "Girvan-Newman"))'> -- Algoritmo de {{ experiment.category }} -- </h2> 
            <h2 id="header" v-else> Visualización </h2>
        </b-col>
    </b-row>
      
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
        padding-top: 10px;
        padding-left: 10px;
        padding-right: 10px;
        border-radius: 10px;
        box-shadow: rgba(60, 64, 67, 0.3) 0px 1px 2px 0px,
    rgba(60, 64, 67, 0.15) 0px 1px 3px 1px;
        
    }

    #network-viz{
        min-height: 75vh;
        border-radius: 10px;
        box-shadow: rgba(60, 64, 67, 0.3) 0px 1px 2px 0px,
            rgba(60, 64, 67, 0.15) 0px 1px 3px 1px;
    }
</style>