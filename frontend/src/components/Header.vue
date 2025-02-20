<template class="is-fixed-top">
  <div class="container py-6">
    <nav class="navbar is-light is-fixed-top" role="navigation" aria-label="main navigation">
  <div class="navbar-brand ml-6">
    <a class="navbar-item" href="/">
        <img src="../assets\main.png" alt="image is-4by3">
        <p class="subtitle is-3"> <strong>Top Sneaker shop</strong></p>
    </a>


  </div>

  <div id="navbarBasicExample" class="navbar-menu ">
    <div class="navbar-start">
      <a class="navbar-item ml-7" href="/basket">
        Basket
      </a>

      <a class="navbar-item ml-8" href="/about">
        About
      </a>

    <a class="navbar-item ml-8" href="/orders">
        Orders   
    </a>

    </div>

    <div class="navbar-end">
      <div class="navbar-item">
        <div class="buttons">
          <a class="button is-success mr-5" @click="$router.push('/login')" v-if="!isLoggedIn">
            <strong>Login</strong>
          </a>
          <a class="button is-success mr-5" @click="logout" v-else>
            <strong>Logout</strong>
          </a>
          <a class="button is-success mr-5" @click="$router.push('/registration')">
            <strong>Registration</strong>
          </a>
        </div>
      </div>
    </div>
  </div>
</nav>  
</div>
</template>

<script setup>
import { ref, computed, onMounted,watch  } from 'vue';
import Swal from 'sweetalert2';

const isLoggedIn = ref(!!localStorage.getItem("token"));
const logout = () => {
  Swal.fire({
        title: 'Are you sure?',
        text: 'You will be logged out of your account.',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Yes, Logout!',
        cancelButtonText: 'Cancel',
      }).then((result) => {
        if (result.isConfirmed) {
          localStorage.removeItem("token");
          Swal.fire({
        title: 'Logged Out!',
        text: 'You have successfully logged out.',
        icon: 'success',
        timer: 2000, 
        timerProgressBar: true,
      });
          isLoggedIn.value = false;
          router.push("/"); 
        }
      });
};

</script>

<style scoped> 

 .ml-7 {
    margin-left: 205px;
}

.ml-8 {
    margin-left: 150px;
} 
</style>