import { createRouter, createWebHistory } from 'vue-router';
import Menu from '../views/Main.vue';
import Cart from '../views/Basket.vue'; 
import Login from '../views/Login.vue';
import Registration from '@/views/Registration.vue';
import About from '../views/About.vue';
import Orders from '@/views/Orders.vue';

const routes = [
  {
    path: '/',
    component: Menu, 
  },
  {
    path: '/basket',
    component: Cart
  },
  {
    path: '/login',
    component: Login,
  },
  {
  path: '/registration',
  component: Registration
  },
  {
    path: '/about',
    component: About,
  },
  {
    path: '/orders',
    component: Orders,
  }
];

const router = createRouter({
  history: createWebHistory(), 
  routes, 
});

export default router;