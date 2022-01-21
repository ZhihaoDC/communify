<template>
  <b-container>
    <div class="parent_container">
      <h2 id="header">Visualización</h2>
      <div style="height: 30em" id="container" ref="cy"></div>
    </div>
  </b-container>
</template>

<script>
import { store } from "../main.js";
import cytoscape from "cytoscape";
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

    console.log("HOLA");
    let cy = cytoscape({
      container: this.$refs.cy, // container to render in
      style: [
        {
          selector: "node[background_color]",
          style: {
            label: "data(name)",
            "text-valign": "center",
            "background-color": "data(background_color)",
            "text-outline-color": "data(background_color)",
            "text-outline-width": 2,
          },
        },
      ],
      layout: {
        name: "cose",
      },
    });
    cy.json(this.experiment.graph);
    cy.zoom({
      level: 10,
    });

    let options = {
      name: "cose",

      // Called on `layoutready`
      ready: function () {},

      // Called on `layoutstop`
      stop: function () {},

      // Whether to animate while running the layout
      // true : Animate continuously as the layout is running
      // false : Just show the end result
      // 'end' : Animate with the end result, from the initial positions to the end positions
      animate: true,

      // Easing of the animation for animate:'end'
      animationEasing: undefined,

      // The duration of the animation for animate:'end'
      animationDuration: undefined,

      // A function that determines whether the node should be animated
      // All nodes animated by default on animate enabled
      // Non-animated nodes are positioned immediately when the layout starts
      animateFilter: true,

      // The layout animates only after this many milliseconds for animate:true
      // (prevents flashing on fast runs)
      animationThreshold: 250,

      // Number of iterations between consecutive screen positions update
      refresh: 20,

      // Whether to fit the network view after when done
      fit: true,

      // Padding on fit
      padding: 30,

      // Constrain layout bounds; { x1, y1, x2, y2 } or { x1, y1, w, h }
      boundingBox: undefined,

      // Excludes the label when calculating node bounding boxes for the layout algorithm
      nodeDimensionsIncludeLabels: true,

      // Randomize the initial positions of the nodes (true) or use existing positions (false)
      randomize: false,

      // Extra spacing between components in non-compound graphs
      componentSpacing: 40,

      // Node repulsion (non overlapping) multiplier
      nodeRepulsion: 2048,

      // Node repulsion (overlapping) multiplier
      nodeOverlap: 4,

      // Ideal edge (non nested) length
      idealEdgeLength: 100,

      // Divisor to compute edge forces
      edgeElasticity: 32,

      // Nesting factor (multiplier) to compute ideal edge length for nested edges
      nestingFactor: 1.2,

      // Gravity force (constant)
      gravity: 1,

      // Maximum number of iterations to perform
      numIter: 5000,

      // Initial temperature (maximum node displacement)
      initialTemp: 1000,

      // Cooling factor (how the temperature is reduced between consecutive iterations
      coolingFactor: 0.99,

      // Lower temperature threshold (below this point the layout will end)
      minTemp: 1.0,
    };

    var layout = cy.layout(options);
    layout.run();
    console.log(cy);
    this.cy = cy;
  },
};
</script>

<style scoped>
.parent_container {
  text-align: left;
}

.visualization {
  height: 30em;
  width: 100%;
  border: grey 1.5px solid;
  border-radius: 10px;
}
.options {
  margin-left: auto;
  margin-right: auto;
}
#container {
  position: relative;
  height: 100%;
  width: 100%;

  border: slategray 1px solid;
  border-radius: 10px;
}

.canvas {
  border: grey 2px solid;
}
</style>