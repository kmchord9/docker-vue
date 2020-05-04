import Vue from 'vue'
import Router from 'vue-router'
// import VueChartKick from 'vue-chartkick'
// import Vuecharts from 'vue-chartjs'
import Home from '../components/Home'
import VueChartJS from '@/components/VueChartJS'
// import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/chartjs',
      name: 'VueChartJS',
      component: VueChartJS
    }
  ]
})
