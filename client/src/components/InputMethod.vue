<template>
  <div class="content-item">
    <h5>Elige un método para detectar comunidades</h5>
    <b-form-group class="content">
      <b-form-radio-group
        id="radio-group-1"
        name="method-selection"
        v-model="picked"
        @change="change_value"
        buttons
        button-variant="outline-primary"
        size="lg"
      >
        <b-form-radio value="louvain" class="options">
          <span>Louvain</span>
        </b-form-radio>
        <b-form-radio value="girvan-newman" class="options">
          <span>Girvan-Newman</span>
        </b-form-radio>
        <!--
            <b-form-radio :value="{ fourth: 4 }">This is the 4th radio</b-form-radio> 
            -->
      </b-form-radio-group>
    </b-form-group>
    <p>Se ha seleccionado {{ picked }}</p>
  </div>
</template>

<script>
export default {
  name: "InputMethod",
  props: ["value"],
  data() {
    return {
      picked: "louvain",
    };
  },
  methods: {
    change_value(e) {
      this.$emit("change", e);
    },
  },
};
</script>

<style scoped>
.options {
  width: 50%;
}
</style>