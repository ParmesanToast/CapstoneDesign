<template>
    <Header></Header>
    
        <div>
          <h1>InterviewPage</h1>
          <p>상세내용</p>
          <button @click="getList()">테스트</button>
        </div>
        <ul class="user-list">
        <li v-for="(user, index) in data.data" :key="`data${index}`" class="user-list-item">
            <img :src="user.avatar" alt="Avatar">
            <div class="user-info">
            <p><strong>ID:</strong> {{ user.id }}</p>
            <p><strong>E-mail:</strong> {{ user.email }}</p>
            <p><strong>First Name:</strong> {{ user.first_name }}</p>
            <p><strong>Last Name:</strong> {{ user.last_name }}</p>
            </div>
        </li>
        </ul>
        {{ data }}

        <Footer></Footer>
      </template>
      
      <script>
    import Header from '@/components/Header.vue'
    import Footer from '@/components/Footer.vue'
    import axios from"axios"
      export default {
        name: 'AppContact',
        
        components: {
        Header,
        Footer
      },
      data(){
        return{
            data:"null",
        };
      },

      methods:{
        
        getList(){
            axios
            .get("https://reqres.in/api/users?delay=3",{})
            .then(res=>{
                console.log(res)
                this.data = res.data;
            })
            .catch(err=>{
                console.log(err)
            })
        },

      },


      }
      </script>
      
    <style>
    /* 컴포넌트에 대한 스타일링 */
    .user-list {
    list-style-type: none;
    padding: 0;
    }
    .user-list-item {
        border: 1px solid #ccc;
        margin-bottom: 10px;
        padding: 10px;
        border-radius: 5px;
        display: flex;
        align-items: center;
    }
    .user-info {
        margin-left: 20px;
    }
    .user-info p {
        margin: 5px 0;
    }
    .user-info img {
        width: 100px;
        height: 100px;
        border-radius: 50%;
    }
    </style>
    