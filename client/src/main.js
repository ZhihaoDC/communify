import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import router from './router'
import './assets/css/main.css';



Vue.config.productionTip = false
Vue.prototype.$API_URL =  'http://localhost:5000'

export var store = {
  state: {
    lastComputedExperiment: Object,
    isNewExperiment: true,
    visualization_params : {},
    user: {},
    jwt: ''
  },
  getLastComputedExperiment(){
    return this.state.lastComputedExperiment
  },
  setLastComputedExperiment(lastComputedExperiment){
    this.state.lastComputedExperiment = lastComputedExperiment
  },
  setIsNewExperiment(isNewExperiment){
    this.state.isNewExperiment = isNewExperiment
  },
  getExperimentJSON(){
    return this.state.lastComputedExperiment.network_json
  },
  setExperimentJSON(new_json){
    this.state.lastComputedExperiment.network_json = new_json
  },
  getExperimentThumbnail(){
    return this.state.lastComputedExperiment.thumbnail
  },
  setExperimentThumbail(new_thumbnail){
    this.state.lastComputedExperiment.thumbnail = new_thumbnail
  },
  getExperimentVisualizationParams(){
    return this.state.lastComputedExperiment.visualization_params
  },
  setExperimentVisualizationParams(new_value){
    this.state.lastComputedExperiment.visualization_params = new_value
  },
  setUser(payload){
    this.user = payload.user
  },
  setJwtToken(payload){
    this.jwt = payload.jwt
  },
  isAuthenticated(){
      if (!this.jwt || this.jwt.split('.').length < 3) {
        return false
      }
      const data = JSON.parse(atob(this.jwt.split('.')[1]))
      const exp = new Date(data.exp * 1000) // JS deals with dates in milliseconds since epoch
      const now = new Date()
      return (now < exp)
    
  }
}


new Vue({
  router,
  data(){
    return{
      sharedState: store.state
    }
  }
  ,
  render: h => h(App)
}).$mount('#app')
