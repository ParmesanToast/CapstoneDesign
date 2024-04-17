<template>

  <div class="black-bg" v-if="모달창열렸니 == true">
    <div class="white-bg">
      <h4>상세페이지임</h4>
      <p>상세페이지 내용임</p>
      <button @click="모달창열렸니=false">닫기</button>
    </div>
  </div>


  <div class="menu">
    <a v-for="a in 메뉴들" :key="a">{{ a }}</a>
  </div>

  

  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->

  <!-- <div v-for="(a,i) in products" :key="i">
    <h3>{{ products[i] }}</h3>
    <p>50만원</p>
  </div> -->

  <div>
    <img src="./assets/room0.jpg" class="room-img">
    <h3 @click="모달창열렸니 = true">{{ products[0] }}</h3>
    <p> 50만원</p>
    <button @click="신고수[0]++">허위매물신고</button> <span>신고수 :{{신고수[0]}}</span>
  </div>
  <div>
    <img src="./assets/room1.jpg" class="room-img">
    <h3>{{ products[1] }}</h3>
    <p> 60만원</p>
    <button @click="신고수[1]++">허위매물신고</button> <span>신고수 :{{신고수[1]}}</span>
  </div>

  <div>
    <img src="./assets/room2.jpg" class="room-img">
    <h3>{{ products[2] }}</h3>
    <p> 70만원</p>
    <button @click="신고수[2]+= 100">허위매물신고</button> <span>신고수 :{{신고수[2]}}</span>
  </div> 
</template>

<script>


export default {
  name: 'App',
  data(){
    return{
      모달창열렸니 : false,
      신고수 : [0,0,0],
      메뉴들 : ['Home', 'Shop', 'About'],
      products : ['역삼동 원룸', '천호동원룸', '마포구원룸'],
    }
  },

  methods :{
    increase(){
      this.신고수[this.a]+=1;
    }
  },

  components: {
    
  }
}
</script>

<style>
body {
  margin : 0
}
div{
  box-sizing: border-box;
}
.black-bg{
  width:100%; height:100%;
  background: rgba(0,0,0,0.5);
  position: fixed; padding: 20px;
}
.white-bg{
  width: 100%; background: white;
  border-radius: 8px;
  padding: 20px;
}


.room-img{
  width: 100%;
  margin-top: 100px;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}

.menu {
  background: darkslateblue;
  padding: 15px;
  border-radius: 5px;
}
.menu a {
  color: white;
  padding: 10px;
}
</style>
