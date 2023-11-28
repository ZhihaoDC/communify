<template>
    <b-button @click="getExperimentWithDataset(dataset_id)">
        {{this.method}}
    </b-button>
</template>

<script>
    import { store } from "../main.js";
    export default{
        name: 'CreateExperimentButton',
        props : ['method', 'dataset_id'],
        methods: {
            getExperimentWithDataset(){
                const axios = require("axios");
                let url = "http://localhost:5000/community-detection/"+ this.method +"/"+ this.dataset_id
                axios.get(url)
                .then((response) => {
                if (response.status === 200) {
                    if (["louvain", "girvan-newman"].includes(this.method)){
                        store.setLastComputedExperiment(response.data);
                        store.setIsNewExperiment(true)
                    }
                    this.$router.push("/community-detection/"+this.method+"/experiment");
                }
                })
                .catch((error) => {
                console.log(error.response);
                if (error.response.status == 500) {
                    console.log("Error en el servidor");
                }
                });
            }
        }
    }
</script>