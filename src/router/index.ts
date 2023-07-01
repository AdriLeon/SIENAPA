import { createRouter, createWebHistory } from '@ionic/vue-router';
import { RouteRecordRaw } from 'vue-router';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    component: () => import ('../views/InicioSesion.vue')
  },
  {
    path: '/admin/lista-pozos',
    component: () => import ('../views/admin/ListaPozo.vue')
  },
  {
    path:'/admin/generar-pozo',
    component: () => import ('../views/admin/GenerarPozo.vue')
  },
  {
    path:'/admin/cambiar-horario',
    component: () => import ('../views/admin/CambiarHorario.vue')
  },
  {
    path:'/admin/control-pozo',
    component: () => import ('../views/admin/ControlPozo.vue')
  },
  {
    path:'/admin/lista-usuarios',
    component: () => import ('../views/admin/ListaUsuarios.vue')
  },
  {
    path:'/admin/generar-reporte',
    component: () => import ('../views/admin/GenerarReporte.vue')
  },
  {
    path:'/operador/cambiar-horario',
    component: () => import ('../views/operador/CambiarHorario.vue')
  },
  {
    path:'/operador/control-pozo',
    component: () => import ('../views/operador/ControlPozo.vue')
  },
  {
    path:'/operador/generar-reporte',
    component: () => import ('../views/operador/GenerarReporte.vue')
  },
  {
    path:'/operador/lista-pozo',
    component: () => import ('../views/operador/ListaPozo.vue')
  },
  {
    path:'/operador/lista-usuarios',
    component: () => import ('../views/operador/ListaUsuarios.vue')
  },
  {
    path:'/informatica/agregar-usuario',
    component: () => import ('../views/informatica/AgregarUsuario.vue')
  },
  {
    path:'/informatica/modificar-usuario',
    component: () => import ('../views/informatica/ModificarUsuario.vue')
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
