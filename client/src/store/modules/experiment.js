import {postDatasetForExperiment, postExperimentToDB, postDatasetToDB} from '@/api'
// import EventBus from '@/main'
import cloneDeep from 'lodash/cloneDeep'
export default {
    namespaced: true,

    state: () => ({
        experiment: {'category': '',
                     'communities': {},
                     'dataset_id': '',
                     'dataset_name': '',
                     'experiment_name': '',
                     'metrics': {},
                     'network_json': {},
                     'thumbnail': '',
                     'visualization_params': {}
                    },
        isNewExperiment: true
      }),

      getters:{
        getExperiment: (state) => {return cloneDeep(state.experiment)},

        network: (state) => cloneDeep(state.experiment.network_json),

        getIsNewExperiment: (state) => state.isNewExperiment,

        getVisualizationParams: (state) => cloneDeep(state.experiment.visualization_params)
      },
    
      mutations: {
        setExperiment(state, experiment){
            state.experiment = experiment
        },
        setNetwork(state, network){
            state.experiment.network_json = network
        },
        setVisualizationParams(state, visualizationParams){
            state.visualization_params = visualizationParams
        },
        setThumbnail(state, thumbnail){
            state.experiment.thumbnail = thumbnail
        },
        setIsNewExperiment(state, isNewExperiment){
            state.isNewExperiment = isNewExperiment
        },

      },

      actions: {
        async getExperimentWithDataset({commit}, payload){
            const response = await postDatasetForExperiment(payload.method, payload.formData)
            commit('setExperiment', response.data)
            commit('setIsNewExperiment', true)
            commit('setVisualizationParams', response.data['visualizationParams'])
        },

        saveExperiment({state, commit, rootState}){
            commit('setIsNewExperiment', false)
            return postExperimentToDB(state.experiment, rootState.auth.jwt)            
        },

        postDataset({commit, rootState}, payload){
            commit('setIsNewExperiment', true)
            return postDatasetToDB(payload.formData, rootState.auth.jwt)
        },

    }
}