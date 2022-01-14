<template>
  <b-container fluid="md">
    <div class="community-detection">
      <h1 class="header">Detección de comunidades: Girvan-Newman</h1>
      <h4>
        Método basado en edge-betweenness. Proceso largo pero con resultados más estables.
      </h4>
      <div class="content">
        <InputCSV selectedMethod="girvan-newman"/>
      </div>
    </div>
  </b-container>
</template>

<script>
import InputCSV from "@/components/InputCSV.vue";
export default {
  components: { InputCSV },
  name: "ExpGirvanNewman",
};
</script>

<style scoped>
</style>