<template>
    <div>
        <b-card-group>
            <b-card v-for="(experiment, index) in experiments" :key="index" 
                    :title="experiment.experiment_id"
                    img-top>
                <b-card-img :src="'http://localhost:5000/get-thumbnail/' + experiment.experiment_id"> </b-card-img>
                <b-card-text>
                    {{experiment.description}}
                </b-card-text>
                <template #footer>
                    <small class="text-muted">Last updated 3 mins ago</small>
                </template>
            </b-card>
        </b-card-group>
        <!---
        <div v-for="(experiment, index) in experiments" :key="index">
          <span>{{experiment.user_id}} , {{experiment.experiment_id}}</span>
        </div>
        -->
    </div>
</template>

<script>
import axios from 'axios';
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
    },

    mounted() {
        this.getExperiments()
    }
}

</script>