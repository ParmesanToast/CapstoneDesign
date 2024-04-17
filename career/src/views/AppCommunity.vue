<!-- 커뮤니티 -->
<template>
<Header/>
    
<div id="app" class="container">
  <h1>대충 커뮤니티</h1>
  <div v-for="post in posts" :key="post.id" class="post">
    <p>{{ post.content }}</p>
    <button class="button is-dark" @click="toggleComments(post.id)">Show Comments</button>
    <div v-show="post.showComments">
      <div v-for="comment in post.comments" :key="comment.id" class="comment">{{ comment.content }}</div>
      <textarea v-model="post.newComment" placeholder="Write a comment..."></textarea>
      <button class="button is-dark" @click="addComment(post.id)">Comment</button>
    </div>
  </div>
  <textarea v-model="newPost" placeholder="Write something..."></textarea>
  <button class="button is-dark" @click="addPost">Post</button>
</div>


<Footer/>
</template>

<script>
import Header from '../components/Header.vue'
import Footer from '../components/Footer.vue'
export default {
name: 'App',

components: {
Header,
Footer
},
el: 'app',
src:"https://cdn.jsdelivr.net/npm/vue@2.6.14/dist/vue.min.js",

data() {
    return {
      newPost: '',
      posts: []
    }
  },
  methods: {
    addPost() {
      if (this.newPost.trim() !== '') {
        this.posts.push({
          id: this.posts.length + 1,
          content: this.newPost,
          comments: [],
          showComments: false,
          newComment: ''
        });
        this.newPost = '';
      }
    },
    toggleComments(postId) {
      const post = this.posts.find(post => post.id === postId);
      post.showComments = !post.showComments;
    },
    addComment(postId) {
      const post = this.posts.find(post => post.id === postId);
      if (post.newComment.trim() !== '') {
        post.comments.push({
          content: post.newComment
        });
        post.newComment = '';
      }
    }
  }
}
</script>

<style>
/* 컴포넌트에 대한 스타일링 */
.container {
max-width: 600px;
margin: 0 auto;
padding: 20px;
}
.post {
border: 1px solid #ccc;
margin-bottom: 20px;
padding: 10px;
}
.comment {
margin-left: 20px;
padding: 5px;
border-left: 1px solid #ccc;
}
</style>
