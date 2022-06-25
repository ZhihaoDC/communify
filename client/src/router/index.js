import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import FormLouvain from '../views/FormLouvain.vue'
import Experiment from '../views/Experiment.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/community-detection/louvain',
    name: 'FormLouvain',
    component: FormLouvain
  },
  {
    path: '/community-detection/girvan-newman',
    name: 'FormGirvanNewman',
    component: () => import('../views/FormGirvanNewman.vue')
  },
  {
    path: '/graph-visualization',
    name: 'FormVisualization',
    component: () => import( '../views/FormVisualization.vue')
  },
  {
    path: '/community-detection/:method/experiment',
    name: 'Experiment',
    component: Experiment
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
