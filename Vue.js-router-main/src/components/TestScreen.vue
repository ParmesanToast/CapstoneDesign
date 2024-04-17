<template>
  <div>
    <h1>Test 화면</h1>
    <button @click="doClick()">js 테스트</button>
  </div>
</template>

<script>
export default {
  name: 'TestScreen',
  setup() {
    function doClick(){
      alert("클릭");
    }
    return {
      doClick
    }
  },
}
</script>