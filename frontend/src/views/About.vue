<template>
    <Header />
    <section class="section about-section">
    <div class="container">
      <h1 class="title has-text-centered mb-5" style="margin-top: -30px;">About Sneaker Shop</h1>
      <p class="subtitle has-text-centered">
        Welcome to <strong>Sneaker Shop</strong> – your ultimate destination for the best sneakers.
        Whether you're a sneakerhead, an athlete, or just love stylish footwear, we have 
        something for you.
      </p>

      <!-- Why Choose Us Section -->
      <div class="columns is-multiline is-centered mt-5">
        <div class="column is-5">
          <div class="box has-background-light">
            <h2 class="title is-4 has-text-centered">Why Choose Us?</h2>
            <ul class="content">
              <li>✔ <strong>Exclusive Sneaker Collections</strong> – Limited edition & classics.</li>
              <li>✔ <strong>100% Authentic Products</strong> – Guaranteed genuine brands.</li>
              <li>✔ <strong>Fast & Secure Checkout</strong> – Safe and seamless shopping.</li>
              <li>✔ <strong>Worldwide Shipping</strong> – We deliver everywhere.</li>
              <li>✔ <strong>Easy Returns</strong> – Customer satisfaction first.</li>
            </ul>
          </div>
        </div>

        <!-- Our Story -->
        <div class="column is-5">
          <div class="box has-background-light">
            <h2 class="title is-4 has-text-centered">Our Story</h2>
            <p>
              <strong>Sneaker Shop</strong> started from a passion for sneaker culture, streetwear, 
              and sports performance. We aim to bring the best sneaker brands and styles to 
              people worldwide, ensuring that every step you take is in comfort and style.
            </p>
            <p class="mt-3">
              We collaborate with top brands to provide high-quality sneakers for everyone, 
              from athletes to casual wearers.
            </p>
          </div>
        </div>
      </div>

      <!-- Commitment & Community -->
      <div class="columns is-multiline is-centered mt-5">
        <div class="column is-5">
          <div class="box has-background-light">
            <h2 class="title is-4 has-text-centered">Our Commitment</h2>
            <p>
              At <strong>Sneaker Shop</strong>, we are committed to delivering exceptional customer 
              service. Every purchase matters to us, and we strive to provide a hassle-free 
              experience with excellent support.
            </p>
          </div>
        </div>

        <div class="column is-5">
          <div class="box has-background-light">
            <h2 class="title is-4 has-text-centered">Join the Sneaker Revolution</h2>
            <p>
              Whether you're looking for high-performance sports shoes or stylish kicks 
              for your everyday look, we’ve got it. Stay ahead of trends with Sneaker Shop!
            </p>
          </div>
        </div>
      </div>

      <!-- Call to Action -->
      <div class="has-text-centered mt-5">
        <button class="button is-primary is-large" @click="$router.push('/shop')">Start Shopping</button>
      </div>
    </div>
  </section>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router';
  import Header from '../components/Header.vue';
  
  const router = useRouter();
  </script>
  
  <style scoped>
  .about-section {
    text-align: center;
    padding: 50px 20px;
  }
  </style>
  