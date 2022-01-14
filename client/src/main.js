import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import router from './router'
import './assets/css/main.css';



Vue.config.productionTip = false

export var store = {
  state: {
    lastComputedExperiment: Object
  },
  setLastComputedExperiment(lastComputedExperiment){
    this.state.lastComputedExperiment = lastComputedExperiment
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
