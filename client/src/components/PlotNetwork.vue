<template> 
  <div class="parent_container">
    <div id="container" ref="cy">
    </div>
  </div>
</template>

<script>
// import { store } from "../main.js";
import cytoscape from "cytoscape";
import fcose from "cytoscape-fcose";

export default {
  name: "PlotNetwork",
  props:['experiment', 'isNewExperiment'],
  emits: ['animation_finished'],
  mounted() {
    let self = this
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
            "background-color": function(node){
                                              if ((self.experiment.category === "Louvain") | (self.experiment.category==="Girvan-Newman")){
                                                return node.data("background_color")
                                              }else{
                                                return "#5CF"
                                              }
            },
            "text-outline-color": function(node){
                                              if ((self.experiment.category === "Louvain") | (self.experiment.category==="Girvan-Newman")){
                                                return node.data("background_color")
                                              }else{
                                                return "#fff"
                                              }

            },
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
              if ((self.experiment.category === "Louvain") | (self.experiment.category==="Girvan-Newman")){
                //take the color of highest degree node ('source' or 'target' node)
                if (cy.$id(edge.data("source")).data("degree") > cy.$id(edge.data("target")).data("degree")){
                  return cy.$id(edge.data("source")).data("background_color")
                }else{
                  return cy.$id(edge.data("target")).data("background_color")
                }
              }else{
                return "#666"
              }
            }
          },
        },
      ],

      hideEdgesOnViewport: true,
    });
    cy.json(this.experiment.network_json); //read graph from json
    
    var layout_options = {
      name: "fcose",

      // 'draft', 'default' or 'proof'
      // - "draft" only applies spectral layout
      // - "default" improves the quality with incremental layout (fast cooling rate)
      // - "proof" improves the quality with incremental layout (slow cooling rate)
      quality: "default",
      // Use random node positions at beginning of layout
      // if this is set to false, then quality option must be "proof"
      randomize: self.isNewExperiment,
      // Whether or not to animate the layout
      animate: self.isNewExperiment,
      // Duration of animation in ms, if enabled
      animationDuration: 5000,
      // Easing of animation, if enabled
      animationEasing: undefined,
      // Fit the viewport to the repositioned nodes
      fit: true,
      // Padding around layout
      padding: 10,
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
        if (self.experiment.category === "Louvain" | self.experiment.category==="Girvan-Newman"){
          if (cy.$id(edge.data().source).data().community === cy.$id(edge.data().target).data().community){
            return 50
          }else{
            return 500
          }
        }else{
          return 150
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
      ready: function() {
 
        
      }, // on layoutready
      stop: function () { // on layoutstop
        //set edges visible only when animation has stopped (for performance enhancements) 
        cy.style().selector("edge").style("visibility", "visible").update();

        //store json into experiments
        const cy_json = cy.json(); // take json from cytoscape
        delete cy_json.style
        self.experiment["network_json"] = cy_json //update experiment info

                
        //store thumbnail
        const options={'scale': 0.2,
                      'output':'base64'}
        const thumbnail = cy.png(options)
        self.experiment["thumbnail"] = thumbnail

        // self.animation_finished = true
        self.$emit('ready')

      },
    };
    //Run layout
    var layout = cy.layout(layout_options);
    layout.run();
    this.cy = cy;

    cy.animated();

  },
};
</script>

<style scoped>
.parent_container {
  text-align: left;
}

#container {
  min-height: 75vh;
  border-radius: 10px;
  box-shadow: rgba(60, 64, 67, 0.3) 0px 1px 2px 0px,
    rgba(60, 64, 67, 0.15) 0px 1px 3px 1px;
}

</style>