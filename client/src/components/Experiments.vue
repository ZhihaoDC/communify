<template>
    <div id="experiments-container">
        <b-card-group deck class="align-items-center justify-content-center">

            <b-card v-for="(experiment, index) in experiments" :key="index"
                class="mb-3" id="b-card"    
                :title="getTitle(experiment.experiment_name, experiment.dataset_name)"
                :sub-title="experiment.category"
                >
                <b-img fluid :src="'data:image/png;base64,' +  experiment.thumbnail"></b-img>
                <b-card-text>
                    {{ experiment.description }}
                </b-card-text>
                
                <b-button fluid class="w-50 mt-auto mx-auto" type="submit" variant="primary" value="Visualizar"
                    v-on:click="visualize(experiment)" v-if="!submitted">
                    Visualizar
                </b-button>
                <b-spinner v-else variant="primary" label="Spinning" id="spinner" class="m-5"></b-spinner>
                <template #footer>
                    <small class="text-muted">Creado el {{parseDate(experiment.creation_date)}}</small>
                </template>
            </b-card>

        </b-card-group>
    
    </div>
</template>

<script>
import axios from 'axios';
import { store } from "../main.js";
export default {
    name: "Experiments",
    data: function () {
        return {
            experiments: [],
            submitted: false,
            user_id: 1
        };
    },
    computed: {
        axiosParams() {
            const params = new URLSearchParams();
            params.append('user_id', '1');
            return params;
        }
    },

    methods: {
        getExperiments() {
            const url = 'http://localhost:5000/get-experiments/' + this.user_id
            axios.get(url)
                .then((response) => {
                    this.experiments = response.data.experiments

                    console.log(this.experiments)
                })
                .catch((error) => {
                    console.error(error)
                })

        },

        getTitle(experiment_name, dataset_name) {
            if (experiment_name)
                return experiment_name
            else
                return dataset_name

        },

        parseDate(date) {
            const db_date = new Date(date);
            const local_date = new Date((db_date) - (db_date.getTimezoneOffset() * 60 * 1000))
            const options = {year: 'numeric', month: 'numeric', day: 'numeric', hour: 'numeric', minute: 'numeric', seconds:'numeric', hour12: false}
            return local_date.toLocaleString('es-ES', options)
        },

        visualize(experiment) {
            this.submitted = true
            store.setLastComputedExperiment(experiment);
            this.$router.push(
                "/community-detection/" + experiment.category.toLowerCase() + "/experiment"
            );
        }
    },

    mounted() {
        this.getExperiments()
    
    }
}

</script>

<style scoped>

#b-card {
    box-shadow: rgba(60, 64, 67, 0.3) 0px 1px 2px 0px, rgba(60, 64, 67, 0.15) 0px 1px 3px 1px;
    min-height: 25rem;
    max-width: 25rem;
}

</style>