
<template>
    <b-container fluid="md">
        <div>
        <h1 id="header">Datasets guardados</h1>
        <h4>
        Datasets guardados por el usuario
        </h4>
        
        
    
        <b-table
            id="my-table"
            :items="datasets"
            :per-page="perPage"
            :current-page="currentPage"
            small
        ></b-table>
        <div>
        <b-pagination
            v-model="currentPage"
            :total-rows="rows"
            :per-page="perPage"
            aria-controls="my-table"
        ></b-pagination>
        </div>
        </div>
    </b-container>
</template>
  
  <script>
    export default {
      data() {
        return {
          perPage: 3,
          currentPage: 1,
          datasets: []
        }
      },
      computed: {
        rows() {
          return this.datasets.length
        }
      },
      mounted() {
        const axios = require("axios")
        axios
            .get("http://localhost:5000/get-datasets/1")
            .then((response) => {
            if (response.status === 200) {
                this.datasets = response.data['datasets']
                this.datasets = this.format_datasets(this.datasets)
                console.log(this.datasets)
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
        },
        methods: {
          format_dataset(dataset){
            let dataset_nodes = dataset.json.elements.nodes.map(node => node.data.name)
            let dataset_json = {
              nombre : dataset['name'],
              fecha_creacion: dataset['creation_date'],
              nodos : dataset_nodes.join(', ').substring(0, 200) + " ..."
            }
            return dataset_json
          },

          format_datasets(datasets){
             let formatted_dataset = datasets.map(dataset => this.format_dataset(dataset))
            return formatted_dataset
          }
        }
      
    }
  </script>