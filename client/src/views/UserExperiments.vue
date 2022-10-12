<template>
    <b-container fluid="md">
        <div>
            <h2 id="header">Experimentos</h2>
        </div>
        <div>
            <Experiments></Experiments>
        </div>
    </b-container>
</template>


<script>
import Experiments from "@/components/Experiments.vue";
export default{
    name: "UserExperiments",
    components: {Experiments},
}
</script>


<style>

</style>