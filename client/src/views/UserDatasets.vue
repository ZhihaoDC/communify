
<template>
    <b-container fluid="md">
      <div>
        <h1 id="header">Datasets guardados</h1>
        <h4>
        Datasets guardados por el usuario
        </h4>
        
      
        <b-table
            id="my-table"
            class="mt-3" outlined
            :items="datasets"
            :fields="fields"
            :per-page="perPage"
            :current-page="currentPage"
        >
            <template #cell(actions)="row">
                <col :style="{ width: '10em'}" >
                    <div class="buttons">
                     
                    <CreateExperimentModal class="mr-2" :row="row"></CreateExperimentModal>
                    <b-button @click="delete_dataset(row.item.id)" value="Eliminar" variant="outline-danger">
                        <b-icon icon="trash" aria-hidden="true" scale="1"></b-icon>
                    </b-button>
                       
                    </div>
            </template>

        </b-table>


        <div>
        <b-pagination
            v-model="currentPage"
            :total-rows="rows"
            :per-page="perPage"
            aria-controls="my-table"
            class="mr-auto"
        ></b-pagination>
        </div>
      </div>
    </b-container>
</template>
  
  <script>
import CreateExperimentModal from '../components/CreateExperimentModal.vue';

    export default {
    data() {
        return {
            user_id: 1,
            perPage: 3,
            currentPage: 1,
            datasets: [],
            fields: [
                { key: 'name', label: 'Nombre del dataset' },
                { key: 'creation_date', label: 'Fecha de creacion' },
                { key: 'nodes', label: 'Ejemplo de nodos' },
                { key: 'actions', label: 'Acciones'}
            ]
        };
    },
    computed: {
        rows() {
            return this.datasets.length;
        }
    },
    mounted() {
        const axios = require("axios");
        axios
            .get("http://localhost:5000/get-datasets/1")
            .then((response) => {
            if (response.status === 200) {
                this.datasets = response.data['datasets'];
                this.datasets = this.format_datasets(this.datasets);
                console.log(this.datasets);
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
        format_dataset(dataset) {
            let dataset_nodes = dataset.json.elements.nodes.map(node => node.data.name);
            let dataset_json = {
                name: dataset['name'],
                id: dataset['id'],
                creation_date: this.parseDate(dataset['creation_date']),
                nodes: dataset_nodes.join(', ').substring(0, 50) + " ..."
            };
            return dataset_json;
        },
        format_datasets(datasets) {
            let formatted_dataset = datasets.map(dataset => this.format_dataset(dataset));
            return formatted_dataset;
        },
        parseDate(date) {
            const db_date = new Date(date);
            const local_date = new Date((db_date) - (db_date.getTimezoneOffset() * 60 * 1000))
            const options = { year: 'numeric', month: 'numeric', day: 'numeric', hour: 'numeric', minute: 'numeric', seconds: 'numeric', hour12: false }
            return local_date.toLocaleString('es-ES', options)
        },
        delete_dataset(dataset_id){
            this.$bvModal.msgBoxConfirm('La siguiente acción borrará el dataset. ¿Estás seguro?', {
                title: '¿Eliminar dataset?',
                size: 'sm',
                buttonSize: 'sm',
                okVariant: 'danger',
                okTitle: 'Eliminar',
                cancelTitle: 'Cancelar',
                footerClass: 'p-2',
                hideHeaderClose: false,
                centered: true
            })
                .then(action => {
                    if (action) {
                        const axios = require('axios')
                        var id_to_remove = dataset_id
                        const url = 'http://localhost:5000/delete-dataset/' + String(this.user_id) + '/' + String(dataset_id)
                        console.log(url)
                        axios.delete(url)
                            .then(response => {
                                if (response.status === 200) {
                                    console.log(response)
                                    this.datasets = this.datasets.filter((dataset) => dataset.dataset_id != id_to_remove)
                                    window.location.reload()
                                }

                            })
                            .catch(error => {
                                console.log(error)
                            })
                    }
                })

            
        }
    },
    components: { CreateExperimentModal }
}
</script>
<style>
.buttons{
    display:inline-block
};
</style>