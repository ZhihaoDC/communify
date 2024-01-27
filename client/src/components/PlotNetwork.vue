<template> 
  <div class="parent_container">
    
    <b-form-group id="input-communityColor" label="Color de la comunidad" label-for="input-communityColor">
      <b-form-input type="color" v-model="communityColor" @input="updateCommunityColor()"></b-form-input>
    </b-form-group>

    <div id="container" ref="cy">
    </div>
  </div>
</template>

<script>
import cytoscape from "cytoscape";
import fcose from "cytoscape-fcose";

export default {
  name: "PlotNetwork",
  props:['isNewExperiment', 'visualizationParameters'],
  data: function() {
    return {
      experiment: this.$store.getters['experiment/getExperiment'],
      communityColor: '#000'
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
    cy.selectionType('additive')

    //define events
    cy.on('click', 'node', (event) =>{
      cy.nodes().unselect()
      cy.nodes().removeClass('community')

      var clickedNode = event.target
      var community = clickedNode.data('community')

      var communityNodes = cy.nodes().filter(element=> {
        return (element.data('community') === community && element.id() != clickedNode.id())
      })
      communityNodes.select()
      communityNodes.addClass('community')

      
      this.communityColor = this.hex_to_rgb(clickedNode.data('background_color'))

      
      
    })

    cy.on('dblclick', 'node', event=>{
      var clickedNode = event.target
      cy.nodes().unselect()
      clickedNode.select()
    })


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
      this.$store.commit('experiment/setNetwork', new_json);

      // update thumbnail
      const options = {'scale': 0.15, 'output':'base64'}
      const thumbnail = cy.png(options)
      this.$store.commit('experiment/setThumbnail', thumbnail)

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
      this.$store.commit('experiment/setNetwork', new_json);

      // update thumbnail
      const options = {'scale': 0.15, 'output':'base64'}
      const thumbnail = cy.png(options)
      this.$store.commit('experiment/setThumbnail', thumbnail)
      
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
    },

    updateCommunityColor(){
      var color = this.rgb_to_hex(this.communityColor)
      var fontColor = this.contrast(color)
      var selectedNodes = this.cy.nodes(':selected');
      // var community = selectedNodes.data('community')
      selectedNodes.style('background-color', color)
      selectedNodes.style('text-outline-color', color)
      selectedNodes.style('color', fontColor)
      
      // console.log(this.communityColor_rgb)
    //   this.cy.style()
    //     .selector(`.community`)
    //     .style('background-color', color)
    //     .style('text-outline-color', color)
    //     .update()
    },

    hex_to_rgb(hex) {
      // Validate the input hex value
      if (!/^#([0-9a-fA-F]{3})$/.test(hex)) {
        console.error("Invalid hex color code. Please enter a 3-digit hex value.");
        return null;
      }

      // Expand the 3-digit hex code to 6 digits
      hex = hex.replace(/^#/, '');
      hex = hex.split('').map(function (char) {
        return char + char;
      }).join('');

      // Convert hex to RGB
      var bigint = parseInt(hex, 16);
      var r = (bigint >> 16) & 255;
      var g = (bigint >> 8) & 255;
      var b = bigint & 255;

      // Format the RGB values to rrggbb
      var rgb = '#'+ 
                  ('0' + r.toString(16)).slice(-2) +
                  ('0' + g.toString(16)).slice(-2) +
                  ('0' + b.toString(16)).slice(-2);

      return rgb.toUpperCase();
    },

    rgb_to_hex(rgb){
      rgb = rgb.replace(/^#/, '');
      var result = '#' + rgb[0] + rgb[2] + rgb[4];
    return result.toUpperCase();
    },

    contrast(hex) {
      var threshold = 149;
      let r = 0, g = 0, b = 0;

      // 3 digits
      if (hex.length == 4) {
        r = "0x" + hex[1] + hex[1];
        g = "0x" + hex[2] + hex[2];
        b = "0x" + hex[3] + hex[3];
      // 6 digits
      } else if (hex.length == 7) {
        r = "0x" + hex[1] + hex[2];
        g = "0x" + hex[3] + hex[4];
        b = "0x" + hex[5] + hex[6];
      }
      return ((r*0.299 + g*0.587 + b*0.114) > threshold) ? '#000000' : '#ffffff';
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