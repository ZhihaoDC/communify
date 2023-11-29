<template>
    <div id="experiments-container">
        <div v-if="!isFetching">
            <div v-if="((experiments != null) && (Object.keys(experiments).length != 0))">
                <b-card-group v-for="(experiments, idx) in makeRows" :key="idx" deck
                    class="align-items-center justify-content-center">
                    <b-card v-for="(experiment, index) in experiments" :key="index" class="mb-3" id="b-card"
                        :title="experiment.experiment_name" :sub-title="experiment.category" :img-src="'data:image/png;base64,' +  experiment.thumbnail">
                        <!-- <b-img fluid :src="'data:image/png;base64,' +  experiment.thumbnail"></b-img> -->
                        <b-card-text> {{ experiment.description }} </b-card-text>
                        
                        <div class="buttons">

                            <b-button v-if="!submitted" @click="visualize(experiment)"
                            value="Visualizar" type="submit" variant="primary" class="mr-2">
                                Visualizar
                            </b-button>
                            <b-spinner v-else variant="primary" label="Spinning" id="spinner" class="m-5"></b-spinner>
                            <b-button @click="delete_experiment(experiment)"
                            value="Eliminar" variant="outline-danger" class="mr-2">
                                Eliminar
                            </b-button>
                        
                        </div>

                        <template #footer>
                            <small class="text-muted">Creado el {{parseDate(experiment.creation_date)}}</small>
                        </template>
                    </b-card>
                </b-card-group>
            </div>
            <div v-else id="empty-experiments-container">
                <img id="empty-experiments-img" src="../assets/test-tube.png"> 
                <div> No hay experimentos todavía </div>
            </div>
        </div>
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
            isFetching: true,
            user_id: 1,
            n_experiments: 0,
            number_experiment_columns: 4,
        };
    },
    computed: {
        axiosParams() {
            const params = new URLSearchParams();
            params.append('user_id', '1');
            return params;
        },

        makeRows() {
            let row = [];
            let rowSize = this.number_experiment_columns
            let i, l, chunkSize = rowSize;
            for (i = 0, l = this.n_experiments; i < l; i += chunkSize) {
                row.push(this.experiments.slice(i, i + chunkSize));
            }
            console.log(row)
            return row
        }
    },

    methods: {
        getExperiments() {
            const url = 'http://localhost:5000/get-experiments/' + this.user_id
            axios.get(url)
                .then((response) => {
                    this.experiments = response.data.experiments
                    this.n_experiments = this.experiments.length
                    let n_rows = this.n_experiments / this.number_experiment_columns
                    this.number_experiment_rows = Math.floor(n_rows) + 1

                    this.isFetching = false
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
            const options = { year: 'numeric', month: 'numeric', day: 'numeric', hour: 'numeric', minute: 'numeric', seconds: 'numeric', hour12: false }
            return local_date.toLocaleString('es-ES', options)
        },

        visualize(experiment) {
            this.submitted = true
            store.setLastComputedExperiment(experiment);
            store.setIsNewExperiment(false);
            this.$router.push(
                "/community-detection/" + experiment.category.toLowerCase() + "/experiment"
            );
        },

        delete_experiment(experiment) {
            this.$bvModal.msgBoxConfirm('La siguiente acción borrará el experimento. ¿Estás seguro?', {
                title: '¿Eliminar experimento?',
                size: 'sm',
                buttonSize: 'sm',
                okVariant: 'danger',
                okTitle: 'Eliminar',
                cancelTitle: 'Cancelar',
                footerClass: 'p-2',
                hideHeaderClose: false,
                centered: true
            })
                .then(action => {
                    if (action) {
                        const axios = require('axios')
                        const id_to_remove = experiment.experiment_id
                        const url = 'http://localhost:5000/delete-experiment/' + String(this.user_id) + '/' + String(id_to_remove)
                        console.log(url)
                        axios.delete(url)
                            .then(response => {
                                if (response.status === 200) {
                                    console.log(response)
                                    this.experiments = this.experiments.filter(function (experiment) {
                                        return experiment.experiment_id != id_to_remove;
                                    });
                                }

                            })
                            .catch(error => {
                                console.log(error)
                            })
                    }
                })

        }

    },

    beforeMount() {
        this.getExperiments(); //get experiments from backend

    }


}

</script>

<style scoped lang="scss">
#b-card {
    box-shadow: rgba(60, 64, 67, 0.3) 0px 1px 2px 0px, rgba(60, 64, 67, 0.15) 0px 1px 3px 1px;
    min-height: 25rem;
    max-width: 25rem;
};

// #delete-button {
//     color: gray;
//     font-size: 0.8rem;
//     text-decoration: underline;
// };

// #delete-button:hover {
//     color: crimson
// };

#empty-experiments-container{
    padding:2em;
}
#empty-experiments-img{
    vertical-align: middle;
    padding: 1.25em;
}

</style>