<template>
    <div class="content-item">
        <b-form-group label="Elige un método para detectar comunidades:" v-slot="{ ariaDescribedby }" class="content">
            <b-form-radio-group
            id="radio-group-1"
            :aria-describedby="ariaDescribedby"
            name="method-selection"
            v-model="picked"
            v-bind:value="value"
            @change="change_value"
            buttons
            button-variant = "outline-dark"
            pressed="false"
            >
            <b-form-radio value="louvain" > 
                <span id="custom-card-title" >Louvain</span>
                <br>
                <small> + rápido</small>
            </b-form-radio>
            <b-form-radio value="girvan-newman">
                <span id="custom-card-title">Girvan-Newman</span> 
                <br>
                <small> + lento, pero exacto </small>
            </b-form-radio>
            <!--
            <b-form-radio :value="{ fourth: 4 }">This is the 4th radio</b-form-radio> 
            -->
            </b-form-radio-group>
        </b-form-group>
        <br>
        <p>Se ha seleccionado {{ picked }}</p>
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