<template>
  <div class="content-item">
    <!-- Introducir archivo (barra)
      <div class="centered_container">
        <div class="file-upload">
        <b-form-file
          placeholder="Elige un archivo"
          drop-placeholder="Suelta el archivo aquí..."
          accept=".csv"
          size="lg"
        ></b-form-file>
        </div>
      </div>
      <small>o arastra hasta aqui</small>
    -->
    <small>Pon el cursor encima del siguiente botón para ver el formato</small>
    <br/>
    <label for="file-upload" class="custom-button" id="upload-button"
    v-bind:class="{'file_selected': file}"
    v-b-popover.hover.right="'El contenido debe de ser una lista de enlaces (de la siguiente forma):‎‎‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎'+
      '╔════════╤═══════╤══════╗\n'+
      '║‏‏‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎ ‏‏‎‎‎nodo_1‏‏‎‏‏‎‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎ ‎‎‏‏‎ ‎│‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎nodo_2‏‏‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎│‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎‎‏‏‎‎peso‏‏‎ ‎‏‏‎ ‏‏‎ ‎‎‏‏‎ ‎║\n'+
      '╠════════╪═══════╪══════╣\n'+
      '║‏‏‎ ‎‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎  ‎‎ ‎foo‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‏‎‎│‏‏‎ ‏‏‎ ‎‏‏‎‏‏‎ ‎‏‏‎ ‎ ‎‎‏‏‎ ‎bar‏‏‎ ‎‏‏‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎ ‎‏‏‎ ‎‎│‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‎4‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‎‎║\n'+
      '╟────────┼───────┼──────╢\n'+
      '║‏‏‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎  ‎ ‎‎‏‏‎bar‏‏‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎│‏‏‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎ ‎‎cat‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎│‏‏‎ ‎‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎‏‏‎ ‎ ‎‏‏‎ ‎3‏‏‎ ‎‏‏‎ ‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‎‏‏‎ ‎‏‏‎ ‎‎║\n'+
      '╟────────┼───────┼──────╢\n'+
      '║‏‏‎ ‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎  ‎ ‎‎‎‎cat‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎‎‎│‏‏‎ ‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‎dog‏‏‎ ‎‏‏‎ ‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‎‏‏‎‎‎│‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‎1‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‎‏‏‎ ‎‏‏‎ ‏‏‎ ‎‎‏‏‎║\n'+
      '╚════════╧═══════╧══════╝'" title="Formato del csv"> 
        <span> {{ file ? 'Archivo seleccionado: '+ file.name : 'Seleccionar un archivo (.csv)' }} 
          <small>{{ file ? '('+ bytesToSize(file.size) +')' : ''}}</small>
        </span>
      </label>
      <b-form-file 
      id="file-upload"
      plain
      v-model="file"
      accept=".csv"
      required="required"
      ></b-form-file>
      <br>
  </div>
</template>

<script>
export default {
  name: 'InputCSV',

  data(){
    return{
      file: null
    }
  },

  methods:{
    bytesToSize(bytes) {
    var sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
    if (bytes == 0) 
      return '0 Byte';
    var i = parseInt(Math.floor(Math.log(bytes) / Math.log(1024)));
    return Math.round(bytes / Math.pow(1024, i), 2) + ' ' + sizes[i];
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
input[type="file"] {
    display: none;
}

#file-upload{
  align-items:center;
  width:60%;
}

.file_selected{
   background-color: #42b983;
   color:aliceblue;
}

#upload-button{
  margin-bottom:0em;
}
</style>
