<script setup>
import Header from '../components/Header.vue'
import Menu from '../components/Menu.vue' 
import Drawer from '../components/Drawer.vue'
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getFirestore } from "firebase/firestore";
import { ref, onMounted, computed } from 'vue';
import { collection, query, onSnapshot } from "firebase/firestore";
import Swal from 'sweetalert2';
import axios from 'axios';

document.title = 'Top Sneakers shop'; 


const category = ref('sneakers');
const cards = ref([]);
const basketItems = ref([]);
const showBasket = ref(false);

const showModal = ref(false);
const selectedProduct = ref(null);

function handleViewDetails(product) {
  selectedProduct.value = product;
  showModal.value = true;
  console.log(selectedProduct.value,showModal.value)
}

function closeModal() {
  showModal.value = false;
}



function changeCategory(newCategory) {
  category.value = newCategory;
  fetchCards()
}

async function fetchCards() {
  try {
    const response = await fetch(`http://localhost:5000/products?category=${category.value}`);
    const data = await response.json();
    if (data) {
      cards.value = data;
      console.log("cards fetched: ", cards.value,typeof(cards));
    }
  }
  catch (error) {
    console.error("Error fetching cards:", error);
  }



  // const q = query(collection(db, "restoraunt"));
  // onSnapshot(q, (querySnapshot) => {
  //   const newcards = [];
  //   querySnapshot.forEach((doc) => {
  //     const data = doc.data();
  //     if (data && data.category) { // Ensure data has category property
  //       const newcard = {
  //         id: doc.id,
  //         description: data.description,
  //         price: data.price,
  //         name: data.name,
  //         photo: data.photo,
  //         category: data.category,
  //       };
  //       newcards.unshift(newcard);
  //     }
  //   });
  //   cards.value = newcards;
  //   console.log("cards updated: ", cards.value);
  // });
}
const addItemToBasket = async (item) => {
  try {
    const token = localStorage.getItem('token');
    if (!token) {
        Swal.fire({
        title: "Login Required!",
        text: "Please login to add items to the cart.",
        icon: "error",
        confirmButtonText: "Login",
      });
      return;
    } 
    console.log(item._id,item.name,item.price)
    const response = await axios.post(
      'http://localhost:5000/addToBasket',
      {
        item_id: item._id,
        name: item.name,
        price: item.price,
        image_url: item.image_url,
        quantity: 1,
      },
      {
        headers: {
          Authorization: `Bearer ${token}`, 
        },
      }
    );
    Swal.fire({
    title: 'Success!',
    text: 'Your product has been added to the cart.',
    icon: 'success',
    confirmButtonText: 'OK',
    timer: 2000, 
    timerProgressBar: true
  });
    console.log('Item added to basket:', response.data.message);
  } catch (error) {
    Swal.fire({
      title: "Login Failed!",
      text: "Invalid username or password.",
      icon: "error",
      confirmButtonText: "Try Again",
    });
    console.error('Error adding item to basket:', error);
  }
};

function increaseItem(index) {
  basketItems.value[index].quantity++;
}
function decreaseItem(index) {
  basketItems.value[index].quantity--;
  if (basketItems.value[index].quantity <=0) {
    basketItems.value.splice(index, 1);
  }
}

function removeItemFromBasket(index) {
  basketItems.value.splice(index, 1);
}


onMounted(fetchCards);
</script> 

<template>
    <Header @showBasket="showBasket = true"/>
    <Menu :selectedCategory="category" :cards="cards" @changeCategory="changeCategory" @addToCart="addItemToBasket" @viewDetails='handleViewDetails' />
    <div v-if="showModal" class="modal">
    <div class="modal-background" @click="closeModal"></div>
    <div class="modal-content">
      <div class="box">
        <div class="columns mt-3">
          <div class="column">
        <img :src="selectedProduct?.image_url" alt="Product Image" style="width: 100%; height: auto; max-height: 220px; object-fit: cover;" />
      </div>
      <div class="column">
        <h3 class="is-size-4">{{ selectedProduct?.brand }} <br> {{ selectedProduct?.name }}</h3>
        <p class="is-size-5 mt-2"><strong>Price:</strong> {{ selectedProduct?.price }}₸</p>
      </div>
      </div>
      <p class="is-size-5"><strong>Description:</strong> {{ selectedProduct?.description }}</p>
      <div class="columns">
        <div class="column">
          <button class="button is-danger mt-3" @click="closeModal">Close</button>
        </div>
        <div class="column">
          <button class="button is-warning mt-3" @click="addItemToBasket(selectedProduct)">Buy</button>
        </div>
      </div>
      </div>
    </div>
  </div>
    </template>
    

    <style scoped>
    .modal {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.5);
      display: flex;
      justify-content: center;
      align-items: center;
      z-index: 1000;
    }
    
    .modal-content {
      background: white;
      padding: 20px;
      border-radius: 8px;
      max-width: 500px;
      width: 90%;
    }
    </style>