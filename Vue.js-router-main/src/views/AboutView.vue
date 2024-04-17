<template>
  <div class="about">
    <h1>This is an about page</h1>
    <TestScreen/>
  </div>
</template>



<script>
import TestScreen from '@/components/TestScreen.vue'

export default {
  name: 'AboutView',
  components: {
    TestScreen
  }
}
</script>
