<template> 
  <div class="parent_container">
    <div id="container" ref="cy">
    </div>
  </div>
</template>

<script>
import { store } from "../main.js";
import cytoscape from "cytoscape";
import fcose from "cytoscape-fcose";

export default {
  name: "PlotNetwork",
  props:['isNewExperiment', 'visualizationParameters'],
  data: function() {
    return {
      experiment: store.getLastComputedExperiment()
    }
  },
  emits: ['animation_finished'],
  watch:{
    visualizationParameters: {
      handler(newData){
        this.animation_finished = false
        var layoutOptions = this.getLayoutOptions(newData)
        this.cy.layout(layoutOptions).run();
        // this.updateExperiment()
      }, deep: true
    }
  },
  mounted() {
    let self = this
    cytoscape.use(fcose);

    this.cy = cytoscape({
      container: this.$refs.cy, // container to render in
      //set node and edges color based on node properties
      wheelSensitivity: 0.2,
      hideEdgesOnViewport: true,
      style: [
        {
          selector: "node",
          style: {
            label: "data(name)",
            height: "data(size)",
            width: "data(size)",
            "text-valign": "center",
            "background-color": 
              function(node){
                if (node.data("background_color")){return node.data("background_color")}
                else {return "#5CF"}             
              },
            "text-outline-color": 
              function(node){
                if (node.data("background_color")){return node.data("background_color")}
                else {return "#fff"}
              },
            "text-outline-width": 2,
            "font-size": "data(font_size)"
          },
        },
        {
          selector: "node:selected",
          style: {
            label: "data(name)",
            height: "data(size)",
            width: "data(size)",
            "text-valign": "center",
            "background-color": 
              function(node){
                if (node.data("background_color")){return node.data("background_color")}
                else {return "#5CF"}         
              },
            "text-outline-color": 
              function(){
                if (!((self.experiment.category === "Louvain") | (self.experiment.category==="Girvan-Newman"))){ return "#fff" }
                else {return "#999999"}
              },
            "text-outline-width": 7,
            "font-size": "data(font_size)"
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
      ]
    });
    
    //define local variable
    let cy = this.cy
    //read graph from json
    cy.json(this.experiment.network_json);

    //define layout
    var layout_options = {
        name: "fcose",

        // 'draft', 'default' or 'proof'
        // - "draft" only applies spectral layout
        // - "default" improves the quality with incremental layout (fast cooling rate)
        // - "proof" improves the quality with incremental layout (slow cooling rate)
        quality: "default",
        
        // if this is set to false, then quality option must be "proof"
        randomize: self.isNewExperiment, // Use random node positions at beginning of layout. If this is set to false, then quality option must be "proof"
        
        animate: self.isNewExperiment, // Whether or not to animate the layout
        
        animationDuration: 3000, // Duration of animation in ms, if enabled
        
        animationEasing: 'ease-in-out', // Easing of animation, if enabled
        
        fit: true, // Fit the viewport to the repositioned nodes
        
        padding: 10, // Padding around layout
        
        nodeDimensionsIncludeLabels: true, // Whether to include labels in node dimensions. Valid in "proof" quality
        
        uniformNodeDimensions: true, // Whether or not simple nodes (non-compound nodes) are of uniform dimensions
        
        packComponents: true, // Whether to pack disconnected components - cytoscape-layout-utilities extension should be registered and initialized
        
        step: "all", // Layout step - all, transformed, enforced, cose - for debug purpose only


        /* spectral layout options */

        samplingType: true, // False for random, true for greedy sampling
        
        sampleSize: 25, // Sample size to construct distance matrix
        
        nodeSeparation: self.visualizationParameters.nodeSeparation, // Separation amount between nodes

        piTol: 0.0000001, // Power iteration tolerance



        /* incremental layout options */

        nodeRepulsion: 10000,// Node repulsion (non overlapping) multiplier

        // Ideal edge (non nested) length
        idealEdgeLength: function(edge){
          if (self.experiment.category === "Louvain" | self.experiment.category==="Girvan-Newman"){
            if (cy.$id(edge.data().source).data().community === cy.$id(edge.data().target).data().community){
              return 50
            }else{
              return self.visualizationParameters.communitySeparation
            }
          }else{
            return 150
          }
        },
        
        edgeElasticity: 0.45, // Divisor to compute edge forces
        
        nestingFactor: 0.1, // Nesting factor (multiplier) to compute ideal edge length for nested edges
        
        numIter: 2500, // Maximum number of iterations to perform - this is a suggested value and might be adjusted by the algorithm as required
      
        tile: true,  // For enabling tiling
        
        tilingPaddingVertical: 10, // Represents the amount of the vertical space to put between the zero degree members during the tiling operation(can also be a function)
        
        tilingPaddingHorizontal: 10, // Represents the amount of the horizontal space to put between the zero degree members during the tiling operation(can also be a function)
        
        gravity: self.visualizationParameters.gravity, // Gravity force (constant)
        
        gravityRangeCompound: 1.5, // Gravity range (constant) for compounds
        
        gravityCompound: 1.0, // Gravity force (constant) for compounds

        gravityRange: 3, // Gravity range (constant)
        
        initialEnergyOnIncremental: 0.3, // Initial cooling factor for incremental layout

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
          self.animation_finished = true
          self.updateExperiment()
          self.$emit('ready')
        },
        
      };
    //Run layout
    var layout = cy.layout(layout_options);
    layout.run();
    this.cy = cy;
    cy.animated();
  

  },
  created(){
    this.$on("export-network", this.updateNetwork)
  },
  methods:{
    updateNetwork(){
      // console.log("Actualizando Experimento...")
      let cy = this.cy
      cy.nodes().lock()

      let new_json = cy.json();
      delete new_json.style //dont overwrite current style (colors)
      store.setExperimentJSON(new_json);

      // update thumbnail
      const options = {'scale': 0.15, 'output':'base64'}
      const thumbnail = cy.png(options)
      store.setExperimentThumbail(thumbnail)

      // console.log("Experimento actualizado")
      this.$emit("network-exported", new_json)
      
      cy.nodes().unlock()

    },
    updateExperiment(){
      // console.log("Actualizando Experimento...")
      let cy = this.cy
      cy.nodes().lock()

      let new_json = cy.json();
      delete new_json.style //dont overwrite current style (colors)
      store.setExperimentJSON(new_json);

      // update thumbnail
      const options = {'scale': 0.15, 'output':'base64'}
      const thumbnail = cy.png(options)
      store.setExperimentThumbail(thumbnail)
      
      cy.nodes().unlock()

    },
    getLayoutOptions(visualizationParameters){
      let cy = this.cy
      let self = this
      var layoutOptions = {
        name: "fcose",
        quality: "default",
        randomize: false,
        animate: true,
        animationDuration: 1000,
        animationEasing: 'ease-in-out',
        fit: false,
        padding: 10, 
        nodeDimensionsIncludeLabels: true,
        uniformNodeDimensions: true,
        packComponents: true,
        step: "cose",

        /* spectral layout options */
        samplingType: true, 
        sampleSize: 25,
        nodeSeparation: visualizationParameters.nodeSeparation, 
        piTol: 0.0000001, 
        /* incremental layout options */
        nodeRepulsion: 6000,

        // Ideal edge (non nested) length
        idealEdgeLength: function(edge){
          if (self.experiment.category === "Louvain" | self.experiment.category==="Girvan-Newman"){
            if (cy.$id(edge.data().source).data().community === cy.$id(edge.data().target).data().community){
              return 50
            }else{
              return visualizationParameters.communitySeparation 
            }
          }else{
            return 150
          }
        },
        
        edgeElasticity: 0.45, 
        nestingFactor: 0.1, 
        numIter: 250, 
        tile: true,  
        tilingPaddingVertical: 10, 
        tilingPaddingHorizontal: 10, 
        gravity: visualizationParameters.gravity, 
        gravityRangeCompound: 1.5, 
        gravityCompound: 1.0, 
        gravityRange: 3,
        initialEnergyOnIncremental: 0.3, 

        /* layout event callbacks */
        ready: function() {
        }, // on layoutready
        stop: function () { // on layoutstop
          //set edges visible only when animation has stopped (for performance enhancements) 
          cy.style().selector("edge").style("visibility", "visible").update();

          self.animation_finished = true
          self.$emit('ready')
          
        },

        
      };
      return layoutOptions
    }
  },
};
</script>

<style scoped>
.parent_container {
  text-align: left;
}

#container {
  min-height: 80vh;
  /* border-radius: 10px;
  box-shadow: rgba(60, 64, 67, 0.3) 0px 1px 2px 0px,
    rgba(60, 64, 67, 0.15) 0px 1px 3px 1px; */
}

</style>