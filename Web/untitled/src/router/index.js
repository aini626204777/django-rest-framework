// 引入Vue
import Vue from 'vue'
// 引入路由组件
import Router from 'vue-router'
// 引入路由需要的组件
// 公共部分
import app from '../views/app/app'
import home from '../views/home/home'
import head from '../views/head/head'
import footer from '../views/footer/footer'
import list from '../views/list/list'

// 注册路由
Vue.use(Router)
// 配置路由
var router = new Router({
  // 使用history模式，去掉路由中的#
  // mode: 'history',
  routes: [{
    path: '/app',
    component: app,
    children: [
      {
        path: 'home',
        components: {
          head: head,
          content: home,
          footer: footer,
          need_log: false
        },
        children: [
          {
            path: 'list/:id',
            name: 'list',
            component: list,
            meta: {
              title: '列表',
              need_log: false
            }
          },
          {
            path: 'search/:keyword',
            name: 'search',
            component: list,
            meta: {
              title: '搜索',
              need_log: false
            }
          }
        ]
      }
    ]
  }]
})

// 修改网页标题
router.afterEach((to, from) => {
  document.title = to.matched[to.matched.length - 1].meta.title
})

// 抛出路由
export default router
