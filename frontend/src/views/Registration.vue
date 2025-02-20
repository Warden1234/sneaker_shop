<template>
    <Header />
    <section class="hero is-fullheight" style="margin-top: -40px;">
      <div class="hero-body">
        <div class="container">
          <div class="columns is-centered">
            <div class="column is-3">
              <div class="box">
                <h1 class="title has-text-centered">Register</h1>
                <form @submit.prevent="register">
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
                  <div class="field">
                    <label class="label">Confirm Password</label>
                    <div class="control">
                      <input
                        class="input"
                        type="password"
                        placeholder="Confirm Password"
                        v-model="confirmPassword"
                        required
                      />
                    </div>
                  </div>
                  <div class="field" v-if="invalid">
                    <p class="is-size-7" style="color: red;">{{ invalid }}</p>
                  </div>
                  <div class="field">
                    <button class="button is-primary is-fullwidth" type="submit">
                      Register
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
  

<script setup>
import Header from "../components/Header.vue";
import { ref } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";
import Swal from "sweetalert2";

const username = ref("");
const password = ref("");
const confirmPassword = ref("");
const invalid = ref(null);

const router = useRouter();

const register = async () => {
  if (password.value !== confirmPassword.value) {
    Swal.fire({
      title: "Passwords Do Not Match!",
      text: "Please ensure both password fields match.",
      icon: "error",
      confirmButtonText: "OK",
    });
    return;
  }

  try {
    const response = await axios.post("http://localhost:5000/register", {
      username: username.value,
      password: password.value,
    });
    Swal.fire({
      title: "Registration Successful!",
      text: "You have successfully registered. Please log in.",
      icon: "success",
      timer: 2000,
      timerProgressBar: true,
    });
    invalid.value = null;
    router.push("/login"); 
  } catch (error) {
    console.error("Registration error:", error);
    Swal.fire({
      title: "Registration Failed!",
      text: "The username might already be taken.",
      icon: "error",
      confirmButtonText: "Try Again",
    });
    invalid.value = "Registration failed. Try another username.";
  }
};
</script>


<style scoped>
.hero {
  background-color: #f5f5f5;
}
.box {
  box-shadow: 0 2px 3px rgba(10, 10, 10, 0.1);
}
</style>
