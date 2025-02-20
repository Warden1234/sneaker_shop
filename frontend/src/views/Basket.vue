<template>
    <Header />
    <div class="container mt-5" v-if="token">
      <h1 class="title">Shopping Cart</h1>
  
      <div v-if="basketItems.length > 0" class="box">
        <ul>
          <li v-for="(item, index) in basketItems" :key="item._id" class="columns">
            <div class="column is-2">
              <img :src="item.image_url || 'default-image.png'" alt="Product Image" class=" image is-1by1" />
            </div>
            <div class="column is-6 mt-6">
              <h2 class="subtitle">{{ item.name }}</h2>
              <p>Price: ₸{{ item.price }}</p>
              <p>Quantity: {{ item.quantity }}</p>
            </div>
            <div class="column is-4 has-text-right mt-6">
              <button class="button is-small is-success" @click="updateQuantity(item.item_id,item.quantity+1)">+</button>
              <button class="button is-small ml-2" @click="updateQuantity(item.item_id,item.quantity-1)" :disabled="item.quantity ==1">-</button>
              <button class="button is-small is-danger ml-2" @click="removeItem(item.item_id)">Remove</button>
            </div>
          </li>
        </ul>
  
        <h3 class="is-size-4 mt-4">Total: ₸{{ totalBasketPrice }}</h3>
        <button class="button is-primary mt-4" @click="checkout">Checkout</button>
      </div>
  
      <p v-else>Your basket is empty.</p>
    </div>
    <div class="container mt-5" v-else>
        <h1 class="title">Login to Continue Shopping</h1>
        <p>Please log in to access your shopping cart.</p>
        <button class="button is-primary" @click="$router.push('/login')">Login</button>
  
    </div>
  </template>
  
  <script setup>
  import Header from '../components/Header.vue';
  import { ref, computed, onMounted } from 'vue';
  import axios from 'axios';
  import Swal from "sweetalert2";
  
  const basketItems = ref([]);
  const token = localStorage.getItem('token');
  
  const fetchBasketItems = async () => {
    try {
      const token = localStorage.getItem('token');
      if (!token) {
        console.error('Token not found');
        return;
      }
      const response = await axios.get(`http://localhost:5000/basket`, {
        headers: { Authorization: 'Bearer ' + token },
      });
      basketItems.value = response.data.items || [];
    } catch (error) {
      console.error('Error fetching basket items:', error);
    }
  };
  
  const totalBasketPrice = computed(() => {
    return basketItems.value.reduce((total, item) => total + item.price * item.quantity, 0);
  });

  const checkout = async () => {
    try {
      const token = localStorage.getItem('token');
      if (!token) {
        console.error('Token not found');
        return;
      }
      const response = await axios.post('http://localhost:5000/createOrder', {}, {
        headers: { Authorization: 'Bearer '+ token },
      });
      Swal.fire({
      title: "Order was sucessfully created!",
      icon: "success",
      timer: 2000,
      timerProgressBar: true,
    });
      fetchBasketItems();
    } catch (error) {
      Swal.fire({
      title: "Something went wrong...",
      text: "Something went wrong... Try again later",
      icon: "error",
      timer: 2000,
      timerProgressBar: true,
    });
      console.error('Error checking out:', error.response?.data || error.message);
    }
  };
  
  const updateQuantity = async (itemId, newQuantity) => {
  try {
    const token = localStorage.getItem('token');
    const response = await axios.patch(
      'http://localhost:5000/updateQuantity',
      { item_id: itemId, quantity: newQuantity },
      {
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
      }
    );
    console.log(response.data.message);
    fetchBasketItems()
  } catch (error) {
    console.error('Error updating quantity:', error.response?.data || error.message);
  }
};

  
  const removeItem = async (itemId) => {
  try {
    const token = localStorage.getItem('token');
    console.log(itemId)
    const response = await axios.delete(
      'http://localhost:5000/removeItem',
      {
        data: { item_id: itemId },
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
      }
    );
    console.log(response.data.message);
    fetchBasketItems();
  } catch (error) {
    console.error('Error removing item:', error.response?.data || error.message);
  }
};
  
  onMounted(() => {
    fetchBasketItems();
  });
  </script>
  
  