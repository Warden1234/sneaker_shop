<script setup>
import Header from "../components/Header.vue";
import { ref } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";
import Swal from 'sweetalert2';

const username = ref("");
const password = ref("");
const invalid = ref(null);

const router = useRouter();


const login = async () => {
  try {
    const response = await axios.post("http://localhost:5000/login", {
      username: username.value,
      password: password.value,
    });
    localStorage.setItem("token", response.data.access_token);
    Swal.fire({
      title: "Login Successful!",
      text: "You have logged in successfully.",
      icon: "success",
      timer: 2000, 
      timerProgressBar: true,
    });
    invalid.value = null;
    router.push("/"); 
  } catch (error) {
    console.error("Login error:", error);
    Swal.fire({
      title: "Login Failed!",
      text: "Invalid username or password.",
      icon: "error",
      confirmButtonText: "Try Again",
    });
    invalid.value = "Invalid username or password";
  }
};
</script>

<template>
  <Header />
  <section class="hero is-fullheight" style="margin-top: -40px;">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-3">
            <div class="box">
              <h1 class="title has-text-centered">Login</h1>
              <form @submit.prevent="login">
                <div class="field">
                  <label class="label">Username</label>
                  <div class="control">
                    <input
                      class="input"
                      type="text"
                      placeholder="Username"
                      v-model="username"
                      required
                    />
                  </div>
                </div>
                <div class="field">
                  <label class="label">Password</label>
                  <div class="control">
                    <input
                      class="input"
                      type="password"
                      placeholder="Password"
                      v-model="password"
                      required
                    />
                  </div>
                </div>
                <div class="field" v-if="invalid">
                  <p class="is-size-7" style="color: red;">{{ invalid }}</p>
                </div>
                <div class="field">
                  <button class="button is-primary is-fullwidth" type="submit">
                    Login
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero {
  background-color: #f5f5f5;
}
.box {
  box-shadow: 0 2px 3px rgba(10, 10, 10, 0.1);
}
</style>
