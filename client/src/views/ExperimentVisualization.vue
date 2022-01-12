<template>
  <b-container fluid="md">
    <h1>Visualización</h1>
    <div id="my-network">
      {{ experiment.data.communities }}
      {{ network }}
    </div>
  </b-container>
</template>

<script>
import { store } from "../main.js"
import { vis } from "vis-network";

export default {
  name: "ExperimentVisualization",
  data: function () {
    return {
      experiment: store.lastComputedExperiment,
    };
  },
  mounted() {

    function redrawAll() {
      var container = document.getElementById("mynetwork");
      var options = {
        nodes: {
          shape: "dot",
          scaling: {
            min: 10,
            max: 30,
          },
          font: {
            size: 12,
            face: "Tahoma",
          },
        },
        edges: {
          color: { inherit: true },
          width: 0.15,
          smooth: {
            type: "continuous",
          },
        },
        interaction: {
          hideEdgesOnDrag: true,
          tooltipDelay: 200,
        },
        configure: {
          filter: function (option, path) {
            if (option === "inherit") {
              return true;
            }
            if (option === "type" && path.indexOf("smooth") !== -1) {
              return true;
            }
            if (option === "roundness") {
              return true;
            }
            if (option === "hideEdgesOnDrag") {
              return true;
            }
            if (option === "hideNodesOnDrag") {
              return true;
            }
            return false;
          },
          container: document.getElementById("optionsContainer"),
          showButton: false,
        },
        physics: false,
      };
      console.log(store.state.lastComputedExperiment)

      var nodes = new vis.DataSet([store.state.lastComputedExperiment.graph.nodes])
      var edges = new vis.DataSet([store.state.lastComputedExperiment.graph.edges])

      var data = {  nodes: nodes, 
                    edges: edges};

      var network = new vis.Network(container, data, options);

      return network
    }

    redrawAll()
  },
};
</script>