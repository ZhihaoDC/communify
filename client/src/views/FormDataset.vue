<template>
    <b-container fluid="md">
        
      <div id="community-detection">
        <h1 id="header">Datasets</h1>
        <h4>
          Introduce tu dataset.
        </h4>
        <div id="content">
          <InputCSV selectedMethod="dataset" 
            submitUrl="http://localhost:5000/save-dataset/1"  
            successUrl="/user-datasets"/>
        </div>
      </div>
    </b-container>
  </template>
  
  <script>
  import InputCSV from "@/components/InputCSV.vue";
  export default {
    components: { InputCSV },
    name: "FormDataset",
  };
  </script>
  
  <style scoped>
  </style>