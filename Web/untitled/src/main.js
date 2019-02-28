// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
// 全局引入共用CSS
import '../styles/common.css'
// 引入字体样式
import '../styles/fonts/iconfont.css'
// 全局引入路由配置
import router from './router'
import '../mock/mock'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: {App},
  template: '<App/>'
})
