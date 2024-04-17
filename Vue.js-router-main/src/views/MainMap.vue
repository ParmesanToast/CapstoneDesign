<template>
  <div>
    <h1>main map</h1>
    <CesiumJs/>
  </div>
</template>

<script>
import CesiumJs from '@/components/CesiumJs.vue';

export default {
  name: 'MainMap',
  components: {
    CesiumJs
  }
}
</script>