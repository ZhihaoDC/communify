<template>
  <b-container fluid="md">
    <div class="community-detection">
      <h1 class="header">Visualización de redes o grafos</h1>
      <h4>
        Visualiza la red, cambia los nodos de posición, color y físicas.
      </h4>
      <div class="content">
        <InputCSV selectedMethod="network-visualization"/>
      </div>
    </div>
  </b-container>
</template>

<script>
import InputCSV from "@/components/InputCSV.vue";
export default {
  components: { InputCSV },
  name: "NetworkVisualization",
};
</script>

<style scoped>
</style>