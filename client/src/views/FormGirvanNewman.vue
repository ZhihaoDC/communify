<template>
  <b-container fluid="md">
    <div class="community-detection">
      <h1 id="header">Detección de comunidades: Girvan-Newman</h1>
      <h4>
        Método basado en la medida de edge-betweenness. 
        Proceso largo pero con resultados más estables.
        Todas las ejecuciones sobre un mismo dataset dan el mismo resultado.
      </h4>
      <div id="content">
        <InputCSV selectedMethod="girvan-newman"/>
      </div>
    </div>
  </b-container>
</template>

<script>
import InputCSV from "@/components/InputCSV.vue";
export default {
  components: { InputCSV },
  name: "GirvanNewman",
};
</script>

<style scoped>
</style>