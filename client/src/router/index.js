import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import ExpLouvain from '../views/ExpLouvain.vue'
import ExpVisualization from '../views/ExpVisualization'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/community-detection/louvain',
    name: 'ExpLouvain',
    component: ExpLouvain
  },
  {
    path: '/community-detection/girvan-newman',
    name: 'ExpGirvanNewman',
    component: () => import('../views/ExpGirvanNewman.vue')
  },
  {
    path: '/community-detection/:method/experiment',
    name: 'ExpVisualization',
    component: ExpVisualization
  },
  {
    path: '/network-visualization',
    name: 'NetworkVisualization',
    component: () => import( '../views/NetworkVisualization.vue')
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
