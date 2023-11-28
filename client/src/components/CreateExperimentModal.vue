<template>
    <div>
    <b-button size="sm" @click="openModal(row.item)" class="mr-1">
            Deteccion de comunidades
    </b-button>

    <b-modal v-model="modalShow" :id="infoModal.id" :title="infoModal.title" ok-only @hide="resetInfoModal">
        <pre><CreateExperimentButton method="girvan-newman" :dataset_id="this.dataset_id"></CreateExperimentButton></pre>
        <pre><CreateExperimentButton method="louvain" :dataset_id="this.dataset_id"></CreateExperimentButton></pre>
    </b-modal>
    </div>
</template>

<script>
import CreateExperimentButton from './CreateExperimentButton.vue';

    export default {
    name: "CreateExperimentModal",
    props: ["row"],
    data: function () {
        return {
            infoModal: {
                id: 'info-modal',
                title: '',
                content: '',
            },
            modalShow: false,
            selectedRowIndex: null,            
            dataset_id: null
        };
    },
    methods: {
        openModal(item) {
            this.infoModal.title = 'Selecciona un método de detección de comunidades';
            this.infoModal.content = JSON.stringify(item, null, 2);
            this.dataset_id = item.id
            this.modalShow = true;
        },
        resetInfoModal() {
            this.infoModal.title = '';
            this.infoModal.content = '';
        },
    },
    components: { CreateExperimentButton }
}
</script>