<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav>
  <router-view/>
</template>

<style>
html,body,#app{
height: 100%;
}
.app-container{
padding:20px
}
</style>
