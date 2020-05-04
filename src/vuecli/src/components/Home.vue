<template>
    <section class="hero">
        <div class="hero-body">
            <div class="container">
                <h1>Creating Beautiful Charts Using Vue.js Wrapper For Cjart.js</h1>
                <ul>
                    <li><router-link to="chartjs">vue-chartjs</router-link></li>
                </ul>

            </div>
        </div>
    </section>
</template>

<script>
export default {
  name: 'home'
}
</script>

<style scoped>
.hero {
  width: 100%;
  height: 10%;
}
.container {
  display: 100%;
  align-items: center;
  align-content: center;
  justify-content: center;
}
h1,h2 {
  font-weight: none;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
</style>
