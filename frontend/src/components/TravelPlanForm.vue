<template>
  <div class="travel-plan-form">
    <h2>여행 계획 입력</h2>
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="destination">목적지</label>
        <input id="destination" v-model="form.destination" required />
      </div>
      <div class="form-group">
        <label for="startDate">시작 날짜</label>
        <input id="startDate" type="date" v-model="form.startDate" required />
      </div>
      <div class="form-group">
        <label for="endDate">종료 날짜</label>
        <input id="endDate" type="date" v-model="form.endDate" required />
      </div>
      <div class="form-group">
        <label for="budget">예산 (원)</label>
        <input id="budget" type="number" v-model.number="form.budget" required />
      </div>
      <button type="submit">계획 저장</button>
    </form>
  </div>
</template>

<script setup>
import { reactive } from 'vue'
import axios from 'axios'

const form = reactive({
  destination: '',
  startDate: '',
  endDate: '',
  budget: 0
})

const submitForm = async () => {
  try {
    const response = await axios.post('/api/travel-plans', form)
    alert('계획이 저장되었습니다!')
    // Reset form
    form.destination = ''
    form.startDate = ''
    form.endDate = ''
    form.budget = 0
  } catch (err) {
    console.error(err)
    alert('저장 중 오류가 발생했습니다.')
  }
}
</script>

<style scoped>
.travel-plan-form {
  max-width: 600px;
  margin: 0 auto;
}
.form-group {
  margin-bottom: 1rem;
}
label {
  display: block;
  margin-bottom: 0.5rem;
}
input {
  width: 100%;
  padding: 0.5rem;
  box-sizing: border-box;
}
button {
  padding: 0.75rem 1.5rem;
  background-color: #42b983;
  color: white;
  border: none;
  cursor: pointer;
}
button:hover {
  background-color: #369870;
}
</style>