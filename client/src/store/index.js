import Vue from 'vue'
import Vuex from 'vuex'
import authentication from '@/store/modules/authentication'
import experiment from '@/store/modules/experiment'
// import {getExperiments, deleteExperiment, postDataset, deleteDataset} from '@/api'

Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        auth: authentication,
        experiment: experiment
    },
})