<template>
    <div class="content">
        <b-form-group label="Elige un método:" v-slot="{ ariaDescribedby }">
            <b-form-radio-group
            id="radio-group-1"
            :aria-describedby="ariaDescribedby"
            name="method-selection"
            v-model="picked"
            v-bind:value="value"
            @change="change_value"
            >
            <b-form-radio value="louvain"> Louvain (más rápido)</b-form-radio>
            <b-form-radio value="girvan-newman"> Girvan-Newman (más lento, pero exacto) </b-form-radio>
            <p>Se ha seleccionado {{ picked }}</p>
            <!--
            <b-form-radio :value="{ fourth: 4 }">This is the 4th radio</b-form-radio> 
            -->
        </b-form-radio-group>
    </b-form-group>
    </div>
</template>

<script>
export default {
    name:'InputMethod',
    props: ['value'],
    data(){
        return{
            picked: 'louvain'
        }
    },
    methods:{
        change_value(e){
            this.$emit("change", e)
        }
    }
}
</script>

<style scoped>
    #method-selection{
        margin-top:2em;
    }

</style>