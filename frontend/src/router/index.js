import { createRouter, createWebHistory } from 'vue-router'
import TravelPlanView from '../views/TravelPlanView.vue'
import ProductListView from '../views/ProductListView.vue'

const routes = [
  { path: '/', redirect: '/plan' },
  { path: '/plan', component: TravelPlanView },
  { path: '/products', component: ProductListView }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router