// 使用Mock
var Mock = require('mockjs')
var categorys = require('./mock/categorys')
var categorysId = require('./mock/categorys_id')
var hotSearch = require('./mock/hotSearch')
var goods = require('./mock/goods')

Mock.mock(/\/categorys\/[0-9]+/, categorysId) // 所有类别菜单列表
Mock.mock('/categorys/', categorys) // 所有类别菜单列表
Mock.mock('/hotsearchs/', hotSearch) // 首页热搜
Mock.mock('/currentLoc/', // 当前位置
  [
    {
      id: 0,
      name: '首页'
    },
    {
      id: 2,
      name: '酒水饮料'
    },
    {
      id: 21,
      name: '白酒'
    },
    {
      id: 213,
      name: '茅台'
    }
  ]
)
Mock.mock('/priceRange/', // 价格区间
  [
    {
      min: 1,
      max: 25
    },
    {
      min: 25,
      max: 50
    },
    {
      min: 50,
      max: 75
    },
    {
      min: 75,
      max: 100
    }
  ]
)
Mock.mock(/\/goods\/.+/, goods) // 列表页商品
