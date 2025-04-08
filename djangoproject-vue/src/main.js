import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import '@/assets/styles/border.css'
import '@/assets/styles/reset.css'
import SvgIcon from '@/icons'



const app=createApp(App)
SvgIcon(app);
app.use(store)
app.use(router)
app.use(ElementPlus)
app.mount('#app')