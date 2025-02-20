<script setup>
defineProps({
  card: {
    type: Object,
    required: true
  }
})
</script>
<template>
              <div class="card">
            <div class="card-content">
              <div class="content columns">
                <div class="column">
                  <img :src="card.photo" alt="Product Image">
                </div>
                <div class="column mt-2">
                  <div class="has-text-primary is-size-4">{{ card.name }}</div>
                  <div class="description">{{ card.description }}</div>
                  <div class="columns mt-1">
                    <div class="column">
                      <p class="is-size-3"><strong>{{ card.price }}$</strong></p>
                    </div>
                    <div class="column mt-1">
                      <button class="button is-warning" @click="$emit('addToCart', card)">Buy</button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
</template>