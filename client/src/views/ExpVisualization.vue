<template>
  <b-container fluid="md">
    <h3 class="header">Visualización</h3>
    <div id="wrapper">
      <div class="visualization" ref="plot"></div>
      <div id="loadingBar" ref="loadingBar">
        <div class="outerBorder">
          <div id="text" ref="text">0%</div>
          <div id="border" ref="border">
            <div id="bar" ref="bar"></div>
          </div>
        </div>
      </div>
    </div>
    <h5 class="header">(Opciones abajo)</h5>
    <div class="options" id="optionsContainer" ref="options"></div>
  </b-container>
</template>

<script>
import { store } from "../main.js";
import { DataSet } from "vis-data/peer/esm/vis-data";
//import { Network } from "vis-network/peer/esm/vis-network";
import { Network } from "vis-network/standalone";

export default {
  name: "ExpVisualization",
  data: function () {
    return {
      experiment: store.state.lastComputedExperiment,
    };
  },
  mounted() {
    console.log(store.state.lastComputedExperiment);
    var self = this;
    this.$nextTick(function () {
      function redrawAll() {
        var container = self.$refs.plot;
        var options = {
          nodes: {
            shape: "dot",
            scaling: {
              min: 10,
              max: 80,
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
            hover: true,
            zoomView: true,
            hideEdgesOnDrag: true,
          },
          configure: {
            filter: function (option, path) {
              
              if(option === "physics"){
                return true;
              }
              if(option === "solver"){
                return true;
              }
              if(option === "forceAtlas2Based"){
                return true;
              }
              if(option === "gravitationalConstant"){
                return true;
              }
              if(option === "centralGravity"){
                return true;
              }
              if(option === "springLength  "){
                return true;
              }
              if(option === "springConstant"){
                return true;
              }
              if(option === "damping"){
                return true;
              }
              if(option === "avoidOverlap"){
                return true;
              }
              if(option === "nodeDistance"){
                return true;
              }
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
              return false;
            },
            container: self.$refs.options,
            showButton: true,
          },
          physics: {
            stabilization: true,
            barnesHut: {
              gravitationalConstant: -8000,
              springConstant: 0.01,
              springLength: 200,
            },
          },
          height: container.clientHeight.toString(),
          width: container.clientWidth.toString(),
        };

        var state_nodes = new DataSet(
          store.state.lastComputedExperiment.graph.nodes
        );
        var state_edges = new DataSet(
          store.state.lastComputedExperiment.graph.edges
        );

        var data = { nodes: state_nodes, edges: state_edges };

        var network = new Network(container, data, options);

        network.on("stabilizationProgress", function (params) {
          var maxWidth = 496;
          var minWidth = 20;
          var widthFactor = params.iterations / params.total;
          var width = Math.max(minWidth, maxWidth * widthFactor);

          self.$refs.bar.style.width = width + "px";
          self.$refs.text.innerText = Math.round(widthFactor * 100) + "%";
        });
        network.once("stabilizationIterationsDone", function () {
          self.$refs.text.innerText = "100%";
          self.$refs.bar.style.width = "496px";
          self.$refs.loadingBar.style.opacity = 0;
          // really clean the dom element
          setTimeout(function () {
            self.$refs.loadingBar.style.display = "none";
          }, 500);
        });

        return network;
      }

      redrawAll();
    });
  },
};
</script>

<style scoped>
.visualization {
  height: 30em;
  width: 100%;
  border: grey 1px solid;
}
.options {
  margin-left:auto;
  margin-right:auto;
}
#loadingBar {
  position: absolute;
  top: 0px;
  left: 0px;
  width: 100%;
  height: 30em;
  background-color: rgba(238, 238, 238, 0.8);
  -webkit-transition: all 0.5s ease;
  -moz-transition: all 0.5s ease;
  -ms-transition: all 0.5s ease;
  -o-transition: all 0.5s ease;
  transition: all 0.5s ease;
  opacity: 1;
}

#wrapper {
  position: relative;
  width: 100%;
  height: 30em;
}

#text {
  position: absolute;
  top: 0px;
  left: 530px;
  width: 30px;
  height: 50%;
  margin: auto auto auto auto;
  font-size: 22px;
  color: #000000;
}

div.outerBorder {
  position: relative;
  top: 50%;
  width: 600px;
  height: 50px;
  margin: auto auto auto auto;
  border: 8px solid rgba(0, 0, 0, 0.1);
  background: rgb(252, 252, 252); /* Old browsers */
  background: -moz-linear-gradient(
    top,
    rgba(252, 252, 252, 1) 0%,
    rgba(237, 237, 237, 1) 100%
  ); /* FF3.6+ */
  background: -webkit-gradient(
    linear,
    left top,
    left bottom,
    color-stop(0%, rgba(252, 252, 252, 1)),
    color-stop(100%, rgba(237, 237, 237, 1))
  ); /* Chrome,Safari4+ */
  background: -webkit-linear-gradient(
    top,
    rgba(252, 252, 252, 1) 0%,
    rgba(237, 237, 237, 1) 100%
  ); /* Chrome10+,Safari5.1+ */
  background: -o-linear-gradient(
    top,
    rgba(252, 252, 252, 1) 0%,
    rgba(237, 237, 237, 1) 100%
  ); /* Opera 11.10+ */
  background: -ms-linear-gradient(
    top,
    rgba(252, 252, 252, 1) 0%,
    rgba(237, 237, 237, 1) 100%
  ); /* IE10+ */
  background: linear-gradient(
    to bottom,
    rgba(252, 252, 252, 1) 0%,
    rgba(237, 237, 237, 1) 100%
  ); /* W3C */
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#fcfcfc', endColorstr='#ededed',GradientType=0 ); /* IE6-9 */
  border-radius: 72px;
}

#border {
  position: absolute;
  top: 5px;
  left: 10px;
  width: 500px;
  height: 23px;
  margin: auto auto auto auto;
  border-radius: 10px;
}

#bar {
  position: absolute;
  top: 1px;
  left: 0px;
  width: 20px;
  height: 20px;
  margin: auto auto auto auto;
  border-radius: 11px;
  border: 2px solid rgba(30, 30, 30, 0.05);
  background: rgb(0, 173, 246); /* Old browsers */
}
</style>