<template>
  <b-container>
    <div class="parent_container">
      <h2 id="header">Experimento: algoritmo de {{ experiment.algorithm }}</h2>
      <div style="height: 30em" id="container" ref="cy"></div>
    </div>
  </b-container>
</template>

<script>
import { store } from "../main.js";
import cytoscape from "cytoscape";
import fcose from "cytoscape-fcose";
//import { Network } from "vis-network/peer/esm/vis-network";

export default {
  name: "ExpVisualization",
  data: function () {
    return {
      experiment: store.state.lastComputedExperiment,
    };
  },
  mounted() {
    console.log(store.state.lastComputedExperiment);
    cytoscape.use(fcose);
    let cy = cytoscape({
      container: this.$refs.cy, // container to render in
      style: [
        {
          selector: "node",
          style: {
            label: "data(name)",
            height: "data(size)",
            width: "data(size)",
            "text-valign": "center",
            "background-color": "data(background_color)",
            "text-outline-color": "data(background_color)",
            "text-outline-width": 2,
            "font-size": "data(font_size)",
          },
        },
        {
          selector: "edge",
          style: {
            visibility: "hidden",
            width: 0.5,
            "line-color": function(edge){
              if (cy.$id(edge.data().source).data().degree > cy.$id(edge.data().target).data().degree){
                return cy.$id(edge.data().source).data().background_color
              }else{
                return cy.$id(edge.data().target).data().background_color
              }
            }
          },
        },
      ],

      hideEdgesOnViewport: true,
      wheelSensitivity: 0.7,
    });
    cy.json(this.experiment.graph);
    cy.zoom({
      level: 10,
    });
    var layout_options = {
      name: "fcose",

      // 'draft', 'default' or 'proof'
      // - "draft" only applies spectral layout
      // - "default" improves the quality with incremental layout (fast cooling rate)
      // - "proof" improves the quality with incremental layout (slow cooling rate)
      quality: "default",
      // Use random node positions at beginning of layout
      // if this is set to false, then quality option must be "proof"
      randomize: true,
      // Whether or not to animate the layout
      animate: true,
      // Duration of animation in ms, if enabled
      animationDuration: 10000,
      // Easing of animation, if enabled
      animationEasing: undefined,
      // Fit the viewport to the repositioned nodes
      fit: true,
      // Padding around layout
      padding: 30,
      // Whether to include labels in node dimensions. Valid in "proof" quality
      nodeDimensionsIncludeLabels: true,
      // Whether or not simple nodes (non-compound nodes) are of uniform dimensions
      uniformNodeDimensions: false,
      // Whether to pack disconnected components - cytoscape-layout-utilities extension should be registered and initialized
      packComponents: true,
      // Layout step - all, transformed, enforced, cose - for debug purpose only
      step: "all",

      /* spectral layout options */

      // False for random, true for greedy sampling
      samplingType: true,
      // Sample size to construct distance matrix
      sampleSize: 25,
      // Separation amount between nodes
      nodeSeparation: 350,
      // Power iteration tolerance
      piTol: 0.0000001,

      /* incremental layout options */

      // Node repulsion (non overlapping) multiplier
      nodeRepulsion: 6000,
      // Ideal edge (non nested) length
      idealEdgeLength: function(edge){
        if (cy.$id(edge.data().source).data().community === cy.$id(edge.data().target).data().community){
          return 50
        }else{
          return 400
        }
      },
      
      // Divisor to compute edge forces
      edgeElasticity: 0.45,
      // Nesting factor (multiplier) to compute ideal edge length for nested edges
      nestingFactor: 0.1,
      // Maximum number of iterations to perform - this is a suggested value and might be adjusted by the algorithm as required
      numIter: 2500,
      // For enabling tiling
      tile: true,
      // Represents the amount of the vertical space to put between the zero degree members during the tiling operation(can also be a function)
      tilingPaddingVertical: 10,
      // Represents the amount of the horizontal space to put between the zero degree members during the tiling operation(can also be a function)
      tilingPaddingHorizontal: 10,
      // Gravity force (constant)
      gravity: 0.1,
      // Gravity range (constant) for compounds
      gravityRangeCompound: 1.5,
      // Gravity force (constant) for compounds
      gravityCompound: 1.0,
      // Gravity range (constant)
      gravityRange: 3,
      // Initial cooling factor for incremental layout
      initialEnergyOnIncremental: 0.3,

      /* constraint options */

      // Fix desired nodes to predefined positions
      // [{nodeId: 'n1', position: {x: 100, y: 200}}, {...}]
      fixedNodeConstraint: undefined,
      // Align desired nodes in vertical/horizontal direction
      // {vertical: [['n1', 'n2'], [...]], horizontal: [['n2', 'n4'], [...]]}
      alignmentConstraint: undefined,
      // Place two nodes relatively in vertical/horizontal direction
      // [{top: 'n1', bottom: 'n2', gap: 100}, {left: 'n3', right: 'n4', gap: 75}, {...}]
      relativePlacementConstraint: undefined,

      /* layout event callbacks */
      ready: () => {}, // on layoutready
      stop: function () { // on layoutstop
        console.log("Terminado!");
        cy.style().selector("edge").style("visibility", "visible").update();
      },
    };
    //Run layout
    var layout = cy.layout(layout_options);
    layout.run();
    console.log(cy);
    this.cy = cy;

    cy.animated();
  },
};
</script>

<style scoped>
.parent_container {
  text-align: left;
}
.options {
  margin-left: auto;
  margin-right: auto;
}
#container {
  position: relative;
  height: 100%;
  width: 100%;

  border-radius: 10px;
  box-shadow: rgba(60, 64, 67, 0.3) 0px 1px 2px 0px,
    rgba(60, 64, 67, 0.15) 0px 1px 3px 1px;
}
</style>