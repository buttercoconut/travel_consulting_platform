<template>
  <div class="product-list-view">
    <h2>여행 상품 목록</h2>
    <div class="product-list">
      <ProductCard
        v-for="product in products"
        :key="product.id"
        :product="product"
        @add="addToCart"
      />
    </div>
    <button @click="checkout" :disabled="cart.length === 0">결제하기</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ProductCard from '../components/ProductCard.vue'
import axios from 'axios'

const products = ref([
  { id: 1, name: '제주도 3박 4일', description: '제주도에서 즐기는 휴양', price: 300000, image: 'https://via.placeholder.com/300x200' },
  { id: 2, name: '서울 시티투어', description: '서울의 명소를 한 번에', price: 200000, image: 'https://via.placeholder.com/300x200' }
])
const cart = ref([])

const addToCart = (product) => {
  cart.value.push(product)
}

const checkout = async () => {
  try {
    await axios.post('/api/checkout', { items: cart.value })
    alert('결제가 완료되었습니다!')
    cart.value = []
  } catch (err) {
    console.error(err)
    alert('결제 중 오류가 발생했습니다.')
  }
}
</script>

<style scoped>
.product-list {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}
button {
  margin-top: 1rem;
  padding: 0.75rem 1.5rem;
  background-color: #42b983;
  color: white;
  border: none;
  cursor: pointer;
}
button:disabled {
  background-color: #aaa;
}
</style>