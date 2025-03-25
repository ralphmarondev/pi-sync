const routes = [
  {
    path: '/',
    name: 'home',
    meta: {
      title: 'Home | PiSync'
    },
    component: () => import('@/views/home/HomeIndex.vue')
  }
]

export default routes