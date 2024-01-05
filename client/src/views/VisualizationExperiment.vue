<template>
<b-container fluid id="parent-container" class="flex-grow-1"> 
      
    <b-row no-gutters>
        <b-col cols="12">
            <h2 id="header" v-if='((experiment.category === "Louvain") | (experiment.category === "Girvan-Newman"))'>  Comunidades ({{ experiment.category }}) </h2> 
            <h2 id="header" v-else> Visualización </h2>
        </b-col>
        <b-col cols="9">
            <PlotNetwork id="network-viz" ref="plotNetwork" @network-exported="submitExperiment" :isNewExperiment="isNewExperiment" @ready="animation_finished = true"
            :visualizationParameters="visualizationParameters"></PlotNetwork>
        </b-col>
        <b-col cols="3">
            <PlotNetworkForm 
                id="save-network-form" 
                ref="plotNetworkForm" 
                @export-network="updateNetwork" 
                :activateSubmitButton="animation_finished" 
                @updatevisualizationParameters="updatevisualizationParameters">
            </PlotNetworkForm>
        </b-col>

    </b-row>
</b-container>
</template>

<script>
import PlotNetwork from "@/components/PlotNetwork.vue";
import PlotNetworkForm from "@/components/PlotNetworkForm.vue";
// import { mapGetters } from 'vuex';
export default {
    name: "VisualizationExperiment",
    components: { PlotNetwork, PlotNetworkForm },
    data: function () {
        return {
                experiment: this.$store.getters['experiment/getExperiment'],
                isNewExperiment: this.$store.getters['experiment/getIsNewExperiment'],
                visualizationParameters: this.$store.getters['experiment/getVisualizationParams'],
                animation_finished: false,
                };
    },
    methods: {
        updateNetwork(){
            this.$refs.plotNetwork.updateNetwork();
        },
        submitExperiment(){
            this.$refs.plotNetworkForm.submit_experiment_with_confirmation();
        },
        updateVisualizationParameters(newNetworkParams){
            this.visualizationParameters = newNetworkParams
        }

    },
    mounted () {
        console.log(this.experiment)
    },
    computed() {
        // mapGetters('experiment', ['getExperiment', 'getIsNewExperiment', 'getVisualizationParams'])
    }

}
</script>

<style scoped>
    #title{
        position:absolute;  
        text-align: left;
    }

    /* #parent-container{
        padding-left: 20px;
        padding-right: 20px
    } */

    #save-network-form{
        padding-top: 25px;
        border-top: 1em;
        border-radius: 15px;
        box-shadow: rgba(60, 64, 67, 0.3) 0px 1px 2px 0px,
    rgba(60, 64, 67, 0.15) 0px 1px 3px 1px;
        
    }
    #network-viz{
        min-height: 75vh;
        z-index:1;
        border-radius: 10px;
        box-shadow: rgba(60, 64, 67, 0.3) 0px 1px 2px 0px,
            rgba(60, 64, 67, 0.15) 0px 1px 3px 1px;
        margin-right: 1rem;
    }
    #page-title{
        position:absolute;
        z-index: 2;
        background-color:white;
        /* border-radius: 10px;
        box-shadow: rgba(60, 64, 67, 0.3) 0px 1px 2px 0px,
            rgba(60, 64, 67, 0.15) 0px 1px 3px 1px; */
    }
</style>