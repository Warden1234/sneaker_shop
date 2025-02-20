import { createApp } from 'vue'
import App from './App.vue'
import 'bulma/css/bulma.min.css' // Import Bulma
import router from './router' // Import your router

const app = createApp(App)

app.use(router)
app.mount('#app');