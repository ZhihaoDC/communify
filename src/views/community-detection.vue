<template>
<b-container fluid="md">
  <div class="community-detection">
    <h1 class="header"> Detección de comunidades </h1>
    <p>
          Selecciona un archivo .csv que contenga 
          información de los enlaces (una lista de enlaces). Después,
          elige el método que desees y... ¡listo!
        </p>
    <div class="centered-container">
      <div class="content">
        
        <InputCSV/>

        <InputMethod @change="change_method"/>
        <p>Clase padre ha recibido:</p>{{method}}
        
      </div>
    </div>
  </div>
</b-container>
</template>

<script>
import InputCSV from '../components/InputCSV.vue'
import InputMethod from '@/components/InputMethod.vue'
export default {
  components: { InputCSV, InputMethod },
  name: 'community-detection',
  data(){
    return {
      method: "louvain"
    }
  },
  methods:{
    change_method(e){
      this.method = e
    }
  }
}
</script>

<style scoped>

</style>