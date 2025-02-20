<template>
    <Header />
    <div class="container mt-5" v-if="token">
      <h1 class="title has-text-centered">Your Orders</h1>
  
      <div v-if="paginatedOrders.length > 0">
        <div v-for="(order, index) in paginatedOrders" :key="order._id" class="box mb-5">
          <h2 class="subtitle has-text-weight-semibold">Order #{{ order._id }}</h2>
          <ul>
            <li v-for="(item, index) in order.items" :key="item._id" class="columns is-vcentered">
              <div class="column is-2">
                <figure class="image is-square">
                  <img :src="item.image_url || 'default-image.png'" alt="Product Image" class="is-rounded" />
                </figure>
              </div>
              <div class="column is-4">
                <h3 class="subtitle">{{ item.name }}</h3>
              </div>
              <div class="column is-3"><p class="subtitle">Quantity: {{ item.quantity }}</p></div>
              <div class="column is-3"><p class="title is-4">₸{{ item.price }}</p></div>
            </li>
          </ul>
          <div class="content mt-4">
            <p><strong>Total Price:</strong> ₸{{ order.total_price }}</p>
            <p><strong>Order Status:</strong> {{ order.orderStatus }}</p>
            <p><strong>Payment Status:</strong> {{ order.paymentStatus }}</p>
            <p><strong>Order Date:</strong> {{ new Date(order.createdAt).toLocaleDateString() }}</p>
          </div>
        </div>
        
        <!-- Pagination Controls -->
        <nav class="pagination is-centered mt-5" role="navigation" aria-label="pagination">
          <a class="pagination-previous" @click="prevPage" :disabled="currentPage === 1">Previous</a>
          <a class="pagination-next" @click="nextPage" :disabled="currentPage === totalPages">Next</a>
          <ul class="pagination-list">
            <li v-for="page in totalPages" :key="page">
              <a class="pagination-link" @click="goToPage(page)" :class="{ 'is-current': page === currentPage }">{{ page }}</a>
            </li>
          </ul>
        </nav>
      </div>
  
      <p v-else class="has-text-centered">You have ordered nothing.</p>
    </div>
  
    <div class="container mt-5 has-text-centered" v-else>
      <h1 class="title">Login to see your orders</h1>
      <p>Please log in to access your order history.</p>
      <button class="button is-primary" @click="$router.push('/login')">Login</button>
    </div>
  </template>
  
  <script setup>
  import Header from '../components/Header.vue';
  import { ref, computed, onMounted } from 'vue';
  import axios from 'axios';
  
  const orderItems = ref([]);
  const token = localStorage.getItem('token');
  const currentPage = ref(1);
  const ordersPerPage = 3;
  
  const fetchBasketItems = async () => {
    try {
      if (!token) {
        console.error('Token not found');
        return;
      }
      const response = await axios.get(`http://localhost:5000/orders`, {
        headers: { Authorization: 'Bearer ' + token },
      });
      orderItems.value = response.data.items || [];
    } catch (error) {
      console.error('Error fetching orders:', error);
    }
  };
  
  const totalPages = computed(() => Math.ceil(orderItems.value.length / ordersPerPage));
  const paginatedOrders = computed(() => {
    const start = (currentPage.value - 1) * ordersPerPage;
    return orderItems.value.slice(start, start + ordersPerPage);
  });
  
  const nextPage = () => {
    if (currentPage.value < totalPages.value) {
      currentPage.value++;
    }
  };
  
  const prevPage = () => {
    if (currentPage.value > 1) {
      currentPage.value--;
    }
  };
  
  const goToPage = (page) => {
    currentPage.value = page;
  };
  
  onMounted(() => {
    fetchBasketItems();
  });
  </script>
  
  <style scoped>
  .box {
    border-radius: 10px;
    background: #f9f9f9;
    padding: 20px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  }
  .image img {
    border-radius: 8px;
    object-fit: cover;
  }
  .pagination-link.is-current {
    background-color: #3273dc;
    color: white;
    border-color: #3273dc;
  }
  </style>