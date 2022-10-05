<template>
  <div id="content-item">
    <label
      for="file-upload"
      class="upload-button"
      v-bind:class="{ file_selected: file }"
      v-b-popover.hover.right="
        'El contenido debe de ser una lista de enlaces (de la siguiente forma):‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ' +
        '╔════════╤═══════╤══════╗\n' +
        '║‎ ‎ ‎ ‎ ‎ ‎ ‎ from ‎ ‎ ‎ ‎ ‎ │‎ ‎ ‎ ‎ ‎ ‎ ‎ to ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎│ ‎ ‎ weight ‎ ║\n' +
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
      @input="check_form()"
      ref="file_input"
    ></b-form-file>
    <br />
    <small>
      Pon el cursor encima del botón anterior para ver el formato del .csv
    </small>
    <br />

    <b-container fluid class="bv-example-row" v-if="!submitted">
      <b-form-checkbox
      class="content-item"
        v-model="manually_select_columns"
        name="check-button"
        switch
        v-bind:disabled="!(file && error.length === 0)"
      >
        Seleccionar columnas manualmente (nodo_origen, nodo_destino, peso)
      </b-form-checkbox>
      <b-row align-h="center">
        <b-form-group
          class="mx-4"
          id="content-item"
          label="Nodo origen"
          v-if="manually_select_columns"
          v-slot="{ ariaDescribedby }"
        >
          <b-form-radio-group
            id="source-node"
            v-model="source"
            v-on:change="disable(source)"
            :options="columns"
            :aria-describedby="ariaDescribedby"
            button-variant="outline-primary"
            size="sm"
            name="radio-btn-outline"
            buttons
            stacked
          ></b-form-radio-group>
        </b-form-group>

        <b-form-group
          id="content-item"
          class="mx-4"
          label="Nodo destino"
          v-if="manually_select_columns"
          v-slot="{ ariaDescribedby }"
        >
          <b-form-radio-group
            id="target-node"
            v-model="target"
            v-on:change="disable(target)"
            :options="columns"
            :aria-describedby="ariaDescribedby"
            button-variant="outline-success"
            size="sm"
            name="radio-btn-outline"
            buttons
            stacked
          ></b-form-radio-group>
        </b-form-group>
        <b-form-group
          id="content-item"
          class="mx-4"
          label="Peso arista"
          v-if="manually_select_columns"
          v-slot="{ ariaDescribedby }"
        >
          <b-form-radio-group
            id="weight"
            v-model="weight"
            v-on:change="disable(weight)"
            :options="columns"
            :aria-describedby="ariaDescribedby"
            button-variant="outline-danger"
            size="sm"
            name="radio-btn-outline"
            buttons
            stacked
          ></b-form-radio-group>
        </b-form-group>
      </b-row>
    </b-container>
    <p>
      <small class="error" v-if="error.length > 0">{{ error }}</small>
    </p>
    <b-button
      type="submit"
      variant="primary"
      class="w-25 content-item submit-button"
      v-bind:disabled="!(file && error.length === 0)"
      value="Visualizar"
      v-on:click="submit_file(file)"
      v-if="!submitted"
    >
      Visualizar
    </b-button>
    <b-spinner
      v-else
      variant="primary"
      label="Spinning"
      id="spinner"
      class="m-5"
    ></b-spinner>
  </div>
</template>

<script>
import { store } from "../main.js";
export default {
  name: "InputCSV",
  props: ["selectedMethod"],
  data() {
    return {
      file: null,
      method: this.selectedMethod,
      manually_select_columns: false,
      columns: [], //options
      source: null,
      target: null,
      weight: null,
      error: "",
      submitted: false,
    };
  },
  methods: {
    check_form() {
      //Update error
      this.error = "";
      this.columns = [];
      if (this.file) {
        if ((this.file["type"] != "text/csv") && (this.file["type"] != 'application/vnd.ms-excel')) {
          this.error = "El archivo debe tener extensión .csv";
        } else if ((this.file["type"] === "text/csv") | (this.file["type"] === 'application/vnd.ms-excel')) {
          const reader = new FileReader();
          reader.readAsText(this.file);
          let self = this;
          //reader.onload = e => console.log(e.target.result.split('\n')[0].split(','))
          reader.onload = (e) => {
            e.target.result
              .split("\n")[0]
              .split(",")
              .forEach(function (column) {
                var column_text = column.toString().replaceAll('"','')
                self.columns.push({
                  text: column_text,
                  value: column_text,
                  disabled: false,
                });
              });
          };
        }
      }
    },
    disable(element){
      var clicked_column = this.columns.find(clicked_column => clicked_column.text === element).disabled
      this.columns.find(clicked_column => clicked_column.text === element).disabled = !clicked_column //switch between true or false
    },
    async submit_file() {
      this.submitted = true;
      const axios = require("axios");
      let formData = new FormData();
      formData.append("file", this.file);
      if (this.manually_select_columns){
        var columns = JSON.stringify({"source": this.source,
                                    "target": this.target,
                                    "weight": this.weight})
        const columns_blob = new Blob([columns], {
          type: 'application/json'
        });
        formData.append("columns", columns_blob);
      }
      await axios
        .post(
          "http://localhost:5000/community-detection/" + this.method,
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        )
        .then((response) => {
          if (response.status === 200) {
            store.setLastComputedExperiment(response.data);
            store.setIsNewExperiment(true)
            this.$router.push(
              "/community-detection/" + this.method + "/experiment"
            );
          }
        })
        .catch((error) => {
          console.log(error.response);
          if (error.response.status == 500) {
            this.error =
              "Formato erróneo. Por favor, introduce un .csv con las columnas en orden: \n " +
              "from, to, weight";
            this.submitted = false;
          }
        });
    },

    bytesToSize(bytes) {
      var sizes = ["Bytes", "KB", "MB", "GB", "TB"];
      if (bytes == 0) return "0 Byte";
      var i = parseInt(Math.floor(Math.log(bytes) / Math.log(1024)));
      return Math.round(bytes / Math.pow(1024, i), 2) + " " + sizes[i];
    },
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
  border-radius: 10px;
  padding: 0.7em 1em;
  margin-bottom: 0.2em;
  cursor: pointer;
  box-shadow: rgba(0, 0, 0, 0.12) 0px 1px 3px, rgba(0, 0, 0, 0.24) 0px 1px 2px;
}

.upload-button:hover {
  background-color: #050517;
  color: aliceblue;
  text-decoration: none;
}

.submit-button {
  font-size: large;
  box-shadow: rgba(0, 0, 0, 0.12) 0px 1px 3px, rgba(0, 0, 0, 0.24) 0px 1px 2px;
}
.submit-button:disabled {
  background-color: #c0c2c8;
  border: 0.5px solid #ccc;
  cursor: not-allowed;
}

.file_selected {
  background-color: #050517;
  color: aliceblue;
}
.error {
  color: red;
}

#spinner {
  width: 3rem;
  height: 3rem;
}
</style>
