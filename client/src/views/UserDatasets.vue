
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
          <CreateExperimentModal :row="row"></CreateExperimentModal>
        </template>

        </b-table>


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
import CreateExperimentModal from '../components/CreateExperimentModal.vue';

    export default {
    data() {
        return {
            perPage: 3,
            currentPage: 1,
            datasets: [],
            fields: [
                { key: 'name', label: 'nombre dataset' },
                { key: 'creation_date', label: 'fecha creacion' },
                { key: 'nodes', label: 'nodos' },
                { key: 'actions', label: 'acciones' }
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
                nodes: dataset_nodes.join(', ').substring(0, 200) + " ..."
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
        // Añadir funcion que:
        // 1. Obtenga el dataset original mediante una llamada a la api
        // 2. Con el dataset obtenido, haga una peticion post a la api para generar la network de louvain/girvan newman
        // 3. Asigne la variable lastComputedExperiment a este experimento
        // 4. Redirija a la pagina de visualizacion de experimentos
        // Otra idea seria que el componente visualizador de experimentos sea el que reciba por parametro el metodo que queremos realizar
        // y que reciba por la url el dataset que queremos visualizar. Habria que generar una pantalla de carga para el experimento...
    },
    components: { CreateExperimentModal }
}
  </script>