<template>
    <div>
        <b-card-group>
            <b-card v-for="(experiment, index) in experiments" :key="index" 
                    :title="getTitle(experiment.experiment_name, experiment.dataset_name)"
                    :sub-title="parseDate(experiment.creation_date)"
                    img-top
                    img-height="50"
                    img-width="50">
                <b-card-img :src="'data:image/png;base64,' + experiment.thumbnail"> </b-card-img>
                <b-card-text>
                    {{experiment.description}}
                </b-card-text>
                <template #footer>
                    <small class="text-muted">Created 3 mins ago</small>
                </template>
            </b-card>
        </b-card-group>
    </div>
</template>

<script>
import axios from 'axios';  
import moment from 'moment'
export default {
    name: "Experiments",
    data: function () {
        return {
            experiments: [],
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
        getTitle(experiment_name, dataset_name){
            if (experiment_name)
                return experiment_name 
            else
                return dataset_name
                

        },
        parseDate(date){
            const local_date = new Date();
            const current_date =  date + (local_date.getTimezoneOffset() * 60)
            return moment(current_date.toString()).format('DD/MM/YYYY H:mm')
        },

    },

    mounted() {
        this.getExperiments()
    }
}

</script>