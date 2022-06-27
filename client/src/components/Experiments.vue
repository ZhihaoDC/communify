<template>
      <div>
        <div v-for="(experiment, index) in experiments" :key="index">
          <span>{{experiment.user_id}} , {{experiment.experiment_id}}</span>
        </div>
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

        }
    },

    mounted() {
        this.getExperiments()
    }
}

</script>