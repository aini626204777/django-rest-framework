<template>
  <div id="wrapper">
    <current-loc :curLoc="curLoc"></current-loc>

    <div class="main cle">
      <list-nav :currentCategoryName="currentCategoryName" :cateMenu="cateMenu" :isObject="isObject" :proNum="proNum" @on-change="changeMenu"></list-nav>

      <div class="maincon">
        <price-range :priceRange="priceRange" @on-change="changePrice"></price-range>

        <list-sort :proNum="proNum" @on-sort="changeSort"></list-sort>

        <div class="list-detail">
          <product-list :listData="listData"></product-list>

          <Page pre-text="上一页" next-text="下一页" end-show="true" :page="curPage" :total-page="totalPage" @pagefn="pagefn"></Page>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import currentLoc from './current-loc/current-loc'
import listNav from './list-nav/listNav'
import priceRange from './price-range/priceRange'
import listSort from './list-sort/listSort'
import productList from './product-list/productList'
import page from './page/page'
import {getCategory, getCurrentLoc, getPriceRange, getGoods} from '../../api/api'

export default {
  data () {
    return {
      top_category: '', // 商品种类id
      cateMenu: {}, // 菜单列表
      currentCategoryName: '',
      isObject: true,
      curLoc: [], // 当前位置
      priceRange: [], // 价格区间
      pageType: 'list', // 默认是类别列表点进来的
      searchWord: '',
      listData: [], // 商品列表
      proNum: 0, // 商品数量
      ordering: '-add_time',
      pricemin: '', // 价格最低
      pricemax: '', // 价格最高
      curPage: 9 // 当前页码
    }
  },
  components: {
    'current-loc': currentLoc,
    'list-nav': listNav,
    'price-range': priceRange,
    'list-sort': listSort,
    'product-list': productList,
    'Page': page
  },
  created () {
    this.getAllData()
  },
  methods: {
    getAllData () {
      // console.log(this.$route.params)
      if (this.$route.params.id) {
        this.top_category = this.$route.params.id
        this.getMenu(this.top_category) // 获取左侧菜单列表
      } else {
        this.getMenu(null) // 获取左侧菜单列表
        this.pageType = 'search'
        this.searchWord = this.$route.params.keyword
      }
      this.getCurLoc() // 获取当前位置
      this.getPriceRange() // 获取价格区间
      this.getListData() // 获取产品列表
    },
    getMenu (id) {
      if (id != null) {
        getCategory({
          id: id
        }).then((response) => {
          // console.log(response.data)
          this.cateMenu = response.data.sub_cat
          this.currentCategoryName = response.data.name
        }).catch(error => {
          console.log(error)
        })
      } else {
        getCategory({}).then(response => {
          // console.log(response.data)
          this.cateMenu = response.data
          this.isObject = false
        }).catch(error => {
          console.log(error)
        })
      }
    },
    getCurLoc () { // 当前位置
      getCurrentLoc({
        proType: this.top_category // 商品类型
      }).then(response => {
        // console.log(response.data)
        this.curLoc = response.data
      }).catch(error => {
        console.log(error)
      })
    },
    getPriceRange () {
      getPriceRange({
        proType: this.top_category // 商品类型
      }).then(response => {
        // console.log(response.data)
        this.priceRange = response.data
      }).catch(error => {
        console.log(error)
      })
    },
    getListData () {
      if (this.pageType === 'search') {
        getGoods({
          search: this.searchWord // 搜索关键词
        }).then(response => {
          // console.log(response.data)
          this.listData = response.data.results
          this.proNum = response.data.count
        }).catch(error => {
          console.log(error)
        })
      } else {
        getGoods({
          top_category: this.top_category, // 商品类型
          ordering: this.ordering, // 排序类型
          pricemin: this.pricemin,
          pricemax: this.pricemax,
          page: this.curPage // 当前页码
        }).then(response => {
          // console.log(response.data)
          this.listData = response.data.results
          this.proNum = response.data.count
        }).catch(error => {
          console.log(error)
        })
      }
    },
    changeSort (type) {
      this.ordering = type
      this.getListData()
    },
    changePrice (data) {
      this.pricemin = data.min
      this.pricemax = data.max
      this.getListData()
    },
    changeMenu (id) {
      this.top_category = id
      this.getCurLoc()
      this.getMenu(id)
      this.getListData()
    },
    pagefn (value) { // 点击分页
      this.curPage = value.page
      this.getListData()
    }
  },
  computed: {
    totalPage () {
      return Math.ceil(this.proNum / 12)
    }
  },
  watch: {
    '$route': 'getAllData'
  }
}
</script>

<style scoped>
.maincon {
    width: 970px;
    float: right;
}
</style>
