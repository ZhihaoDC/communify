
<template>
    <b-container fluid="md">
        <div>
        <h1 id="header">Datasets guardados</h1>
        <h4>
        Datasets guardados por el usuario
        </h4>
        
        <div>
        <b-pagination
            v-model="currentPage"
            :total-rows="rows"
            :per-page="perPage"
            aria-controls="my-table"
        ></b-pagination>
        </div>
    
        <p class="mt-3">Current Page: {{ currentPage }}</p>
    
        <b-table
            id="my-table"
            :items="items"
            :per-page="perPage"
            :current-page="currentPage"
            small
        ></b-table>
        </div>
    </b-container>
</template>
  
  <script>
    export default {
      data() {
        return {
          perPage: 1,
          currentPage: 1,
          items: []
        }
      },
      computed: {
        rows() {
          return this.items.length
        }
      },
      mounted() {
        const axios = require("axios")
        axios
            .get("http://localhost:5000/get-datasets/1")
            .then((response) => {
            if (response.status === 200) {
                this.items = response.data['datasets']
            }
            })
            .catch((error) => {
            console.log(error);
            if (error.status == 500) {
                this.error =
                "Formato erróneo. Por favor, introduce un .csv con las columnas en orden: \n " +
                "from, to, weight";
            }
            });
        }
      
    }
  </script>