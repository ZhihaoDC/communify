<template>
  <div class="content-item">
    <label
      for="file-upload"
      class="upload-button"
      v-bind:class="{ file_selected: file }"
      v-b-popover.hover.right="
        'El contenido debe de ser una lista de enlaces (de la siguiente forma):‎‎‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎' +
        '╔════════╤═══════╤══════╗\n' +
        '║‏‏‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎ ‏‏‎‎‎nodo_1‏‏‎‏‏‎‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎ ‎‎‏‏‎ ‎│‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎nodo_2‏‏‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎│‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎‎‏‏‎‎peso‏‏‎ ‎‏‏‎ ‏‏‎ ‎‎‏‏‎ ‎║\n' +
        '╠════════╪═══════╪══════╣\n' +
        '║‏‏‎ ‎‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎  ‎‎ ‎foo‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‏‎‎│‏‏‎ ‏‏‎ ‎‏‏‎‏‏‎ ‎‏‏‎ ‎ ‎‎‏‏‎ ‎bar‏‏‎ ‎‏‏‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎ ‎‏‏‎ ‎‎│‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‎4‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‎‎║\n' +
        '╟────────┼───────┼──────╢\n' +
        '║‏‏‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎  ‎ ‎‎‏‏‎bar‏‏‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎│‏‏‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎ ‎‎cat‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎│‏‏‎ ‎‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎‏‏‎ ‎ ‎‏‏‎ ‎3‏‏‎ ‎‏‏‎ ‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‎‏‏‎ ‎‏‏‎ ‎‎║\n' +
        '╟────────┼───────┼──────╢\n' +
        '║‏‏‎ ‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎  ‎ ‎‎‎‎cat‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎‎‎│‏‏‎ ‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‎dog‏‏‎ ‎‏‏‎ ‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‎‏‏‎‎‎│‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‎1‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‎‏‏‎ ‎‏‏‎ ‏‏‎ ‎‎‏‏‎║\n' +
        '╚════════╧═══════╧══════╝'
      "
      title="Formato del csv"
    >
      <span>
        {{
          file
            ? "Archivo seleccionado: " + file.name
            : "Seleccionar un archivo (.csv)"
        }}
        <small>{{ file ? "(" + bytesToSize(file.size) + ")" : "" }}</small>
      </span>
    </label>
    <b-form-file
      id="file-upload"
      plain
      v-model="file"
      accept=".csv"
      required="required"
      enctype="multipart/form-data"
    ></b-form-file>
    <br />
    <small>
      Pon el cursor encima del botón anterior para ver el formato del .csv
    </small>
    <br />
    <br/>
    <b-button
      type="submit"
      variant="primary"
      class="w-25 content-item submit-button"
      v-bind:disabled="!file"
      value="Visualizar"
      v-on:click="submit_file()"
    >
      Visualizar
    </b-button>
  </div>
</template>

<script>
import { store } from "../main.js"
export default {
  name: "InputCSV",
  props: ['selectedMethod'],
  data() {
    return {
      file: null,
      method: this.selectedMethod
    };
  },
  methods: {
    bytesToSize(bytes) {
      var sizes = ["Bytes", "KB", "MB", "GB", "TB"];
      if (bytes == 0) return "0 Byte";
      var i = parseInt(Math.floor(Math.log(bytes) / Math.log(1024)));
      return Math.round(bytes / Math.pow(1024, i), 2) + " " + sizes[i];
    },
    async submit_file(){
      const axios = require('axios')
      let formData = new FormData()
      formData.append('file', this.file)

      await axios.post('http://localhost:5000/community-detection/'+this.method,
        formData,
        {
          headers:{
            'Content-Type':'multipart/form-data'
          }
        }
      ).then(response =>{
        store.setLastComputedExperiment(response.data)
        console.log(store)
        this.$router.push('/community-detection/' + this.method + '/experiment')
      }
      )
      .catch(function(){
        console.log('Error')
      })
    }
  },
};
</script>

<style scoped>
input[type="file"] {
  display: none;
}

#file-upload {
  align-items: center;
  width: 60%;
}

.upload-button {
  display: inline-block;
  color: aliceblue;
  background: #42b983;
  font-size: x-large;
  border: 1px solid #ccc;
  border-radius: 10px;
  padding: 0.7em 1em;
  margin-bottom: 0.2em;
  cursor: pointer;
}

.upload-button:hover {
  background-color: #050517;
  color: aliceblue;
  text-decoration: none;
}


.submit-button{
  font-size: large;
  border: 1px solid #ccc;
}
.submit-button:disabled{
  background-color: #c0c2c8;
  border: 1px solid #ccc;
  cursor:not-allowed;
;
}

.file_selected {
  background-color: #050517;
  color: aliceblue;
}
</style>
