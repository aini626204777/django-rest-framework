import axios from 'axios'

// let host = 'http://127.0.0.1:8000'
let host = ''

// 获取商品类别信息
export const getCategory = params => {
  if ('id' in params) {
    return axios.get(`${host}/categorys/` + params.id + '/', params)
  } else {
    return axios.get(`${host}/categorys/`, params)
  }
}

// 获取热门搜索关键词
export const getHotSearch = params => {
  return axios.get(`${host}/hotsearchs/`)
}

// 获取当前位置
export const getCurrentLoc = params => {
  return axios.get(`${host}/currentLoc/`, params)
}

// 获取价格区间
export const getPriceRange = params => {
  return axios.get(`${host}/priceRange/`, params)
}

// 获取商品列表
export const getGoods = params => {
  return axios.get(`${host}/goods/`, {params: params})
}
