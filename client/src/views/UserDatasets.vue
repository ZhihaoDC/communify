
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
            :fields="fields"
            :per-page="perPage"
            :current-page="currentPage"
            small
        >
        
        <template #cell(actions)="row">
          <b-button size="sm" @click="info(row.item, row.index, $event.target)" class="mr-1">
            Info modal
          </b-button>
        </template>
        </b-table>
        <b-modal :id="infoModal.id" :title="infoModal.title" ok-only @hide="resetInfoModal">
          <pre>{{ infoModal.content }}</pre>
        </b-modal>
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
          datasets: [],
          fields: [
            {key: 'name', label: 'nombre dataset'},
            {key: 'creation_date', label: 'fecha creacion'},
            {key: 'nodes', label: 'nodos'},
            {key: 'actions', label: 'acciones'}
          ],
          infoModal: {
            id: 'info-modal',
            title: '',
            content: ''
          }
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
              name : dataset['name'],
              id: dataset['id'],
              creation_date: dataset['creation_date'],
              nodes : dataset_nodes.join(', ').substring(0, 200) + " ..."
            }
            return dataset_json
          },

          format_datasets(datasets){
             let formatted_dataset = datasets.map(dataset => this.format_dataset(dataset))
            return formatted_dataset
          },
          info(item, index, button) {
            this.infoModal.title ='Row index: ${index}'
            this.infoModal.content = JSON.stringify(item, null, 2)
            this.$root.$emit('bv::show::modal', this.infoModal.id, button)
            console.log(index)
          },
        }
      
    }
  </script>