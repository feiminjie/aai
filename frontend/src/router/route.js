import { createRouter, createWebHashHistory } from 'vue-router'

const ifcs = () => import('../views/interfaces.vue')
const adp = () => import('../views/addproject.vue')


const routes = [
    {
        path: '/',
        name: 'adp',
        component: adp
    },
    {
        path: '/ifcs',
        name: 'home',
        component: ifcs
    },
]


const router = createRouter({
  // 4. 内部提供了 history 模式的实现。为了简单起见，我们在这里使用 hash 模式。
  history: createWebHashHistory(),
  routes: routes, // `routes: routes` 的缩写
})


export default router