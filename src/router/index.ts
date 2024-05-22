import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import NotFoundView from '@/views/NotFoundView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    // 404页面路由，放在最后
    {
      path: '/:pathMatch(.*)*', // 使用自定义正则表达式捕获所有路径
      name: '404',
      component: NotFoundView
    }
  ]
});

export default router;
