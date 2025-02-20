<template>
  <div class="container margini">
    <h1 class="menu" style="margin-left: 35%">Available goods</h1>
    <div class="categories ml-6">
      <p class="has-text-black is-size-3 has-text-weight-bold has-text-left category-title is-marginless ml-3">Categories:</p>
      <div class="columns mt-1">
        <div class="column is-1 ml-6">
          <button class="button is-primary" @click="$emit('changeCategory', 'sneakers')">Sneakers</button>
        </div>
        <div class="column is-1 ml-5">
          <button class="button is-info" @click="$emit('changeCategory', 'boots')">Boots</button>
        </div>
        <div class="column is-1">
          <button class="button is-warning" @click="$emit('changeCategory', 'sandals')">Sandals</button>
        </div>
        <div class="column is-1 ml-3">
          <button class="button is-success" @click="$emit('changeCategory', 'shoes')">Dress Shoes</button>
        </div>
      </div>
      <hr style="margin-top: -10px;">
    </div>
  </div>
  <div class="container">
    <div class="category">
      <p class="is-size-2">Available products for category: <strong>{{ selectedCategory.charAt(0).toUpperCase() + selectedCategory.slice(1) }}</strong></p>
    </div>
    <div class="fixed-grid has-2-cols ml-2">
      <div class="grid mt-4">
        <div class="cell" v-for="card in paginatedCards" :key="card.id">
          <div class="card">
            <div class="card-content">
              <div class="content columns">
                <div class="column">
                  <img :src="card.image_url" alt="Product Image" class="image is-1by1">
                </div>
                <div class="column mt-6">
                  <div class=" is-size-3">{{ card.brand }}</div>
                  <div class="description mt-1">{{ card.name }}</div>
                      <p class="is-size-3"><strong>{{ card.price }}₸</strong></p>
                    <div class="columns mt-1">
                    <div class="column mt-1">
                      <button class="button is-warning" @click="$emit('addToCart', card)">Buy</button>
                    </div>
                    <div class="column mt-1">
                  <button class="button is-info" @click="$emit('viewDetails', card)">View Details</button>
                  </div>
                </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="pagination" v-if="totalPages > 1">
  <button 
    class="button" 
    :disabled="state.currentPage === 1" 
    @click="changePage(state.currentPage - 1)">
    Previous
  </button>
  <span>Page {{ state.currentPage }} of {{ totalPages }}</span>
  <button 
    class="button" 
    :disabled="state.currentPage === totalPages" 
    @click="changePage(state.currentPage + 1)">
    Next
  </button>
</div>
  </div>
</template>


<script setup>
import { reactive, computed } from 'vue';

const props = defineProps({
  selectedCategory: {
    type: String,
    required: true
  },
  cards: {
    type: Array,
    required: true
  },
});



function scrollToTop() {
  window.scrollTo({
    top: 0,
    behavior: 'smooth' // Smooth scroll for better UX
  });
}
// State for pagination
const state = reactive({
  currentPage: 1,
  itemsPerPage: 30
});

// Filter cards based on category
const filteredCards = computed(() => {
  return props.cards.filter(card => card.category === props.selectedCategory);
});

// Calculate total pages
const totalPages = computed(() => {
  return Math.ceil(filteredCards.value.length / state.itemsPerPage);
});

// Get cards for the current page
const paginatedCards = computed(() => {
  const start = (state.currentPage - 1) * state.itemsPerPage;
  const end = start + state.itemsPerPage;
  return filteredCards.value.slice(start, end);
});

// Change page handler
function changePage(page) {
  if (page >= 1 && page <= totalPages.value) {
    state.currentPage = page;
    scrollToTop();
  }
}
</script>


<style scoped>
.margini {
  margin-left: -50px;
}
.menu {
  position: relative;
  font-size: 60px;
  text-align: center;
  text-shadow: 2px 2px 3px rgb(68, 66, 66);
  font-family: 'Tinos', serif;
  font-weight: 1000;
  text-shadow: rgb(61, 57, 57);
}
.category {
  justify-content: center;
  display: flex;
}
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}
.pagination .button {
  margin: 0 10px;
}
</style>

