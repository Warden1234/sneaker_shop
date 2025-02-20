<template>
  <Header/>
  <div v-if="showBasket" class="modal is-active">
    <div class="modal-background" @click="$emit('closeBasket')"></div>
    <div class="modal-content">
      <div class="box">
        <h1 class="is-size-3 has-text-weight-bold">Your Basket</h1>
        <ul>
          <li v-for="(item, index) in basketItems" :key="index">
            <div class="columns">
              <div class="column is-2">
            <img :src="item.image_url" alt="Product Image" class="image is-64x64  mt-3">
          </div>
            <div class="column is-12 mt-5">
            <div class="columns">
              <div class="column is-4">
            {{ item.name }}. Total:  ₸{{ item.price*item.quantity }}
          </div>
          <div class="column">
            <button class="button is-small ml-6" @click="$emit('increaseItem', index)">+</button>
            <button class="button is-small"> {{ item.quantity }}</button>
            <button class="button is-small" @click="$emit('decreaseItem', index)">-</button>
            <button class="button is-small ml-2" @click="$emit('removeItem', index)">Remove</button>
          </div>
          </div>
          </div>
        </div>
          </li>
        </ul>
        <p v-if="basketItems.length === 0">Your basket is empty.</p>
        <h3 class="is-size-4 mt-4">Total: ₸{{ totalBasketPrice }}</h3>
        <button class="button is-primary mt-3" @click="$emit('closeBasket')">Close</button>
        <button class="button is-success ml-4" @click="$emit('closeBasket')">Buy</button>
      </div>
    </div>
    <button class="modal-close is-large" aria-label="close" @click="$emit('closeBasket')"></button>
  </div>
</template>

<script setup>
import { reactive, computed } from 'vue'
import Header from '../components/Header.vue'
const props = defineProps({
  showBasket: {
    type: Boolean,
    required: true
  },
  basketItems: {
    type: Array,
    required: true
  }
});

const totalBasketPrice = computed(() => {
  let totalPrice = 0;
  props.basketItems.forEach(item => {
    totalPrice += item.price * item.quantity;
  });
  return totalPrice;
});

</script>

<style scoped>
.ml--6 {
  margin-left: -180px;
}
</style>