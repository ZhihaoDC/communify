<template>
  <b-container fluid="md">
    <div class="community-detection">
      <h1 class="header">Detección de comunidades</h1>
      <h4>
        Selecciona un archivo .csv que contenga una lista de enlaces 
        y elige el método de detección de comunidades que desees.
      </h4>
      <div class="content">
        <InputCSV selectedMethod="louvain"/>
      </div>
    </div>
  </b-container>
</template>

<script>
import InputCSV from "@/components/InputCSV.vue";
export default {
  components: { InputCSV },
  name: "Community-detection",
};
</script>

<style scoped>
.choices {
  width: 100%;
  display: inline-block;
}

.choice {
  margin-left: 0.5em;
  margin-right: 0.5em;
  border: 1px solid #ccc;
}
</style>