<template>
  <div class="product-card">
    <img :src="product.image" alt="{{ product.name }}" />
    <h3>{{ product.name }}</h3>
    <p>{{ product.description }}</p>
    <p class="price">{{ product.price | currency }}원</p>
    <button @click="addToCart(product)">장바구니에 담기</button>
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue'

const props = defineProps({
  product: {
    type: Object,
    required: true
  }
})
const emit = defineEmits(['add'])

const addToCart = (product) => {
  emit('add', product)
}
</script>

<style scoped>
.product-card {
  border: 1px solid #ddd;
  padding: 1rem;
  border-radius: 8px;
  text-align: center;
}
.product-card img {
  max-width: 100%;
  height: auto;
  border-radius: 4px;
}
.price {
  font-weight: bold;
  margin-top: 0.5rem;
}
button {
  margin-top: 0.75rem;
  padding: 0.5rem 1rem;
  background-color: #42b983;
  color: white;
  border: none;
  cursor: pointer;
}
button:hover {
  background-color: #369870;
}
</style>