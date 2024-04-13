<!-- ThreadComponent.vue -->
<template>
  <h1 id="title">Threads</h1>
  <div class="container">
    <div class="thread-container">
      <div v-for="thread in threads" :key="thread.id" class="thread-info">
        <h2>{{ thread.title }}</h2>
        <p>Created by: {{ thread.created_by }}</p>
        <p>Created at: {{ thread.created_at }}</p>
        <p>Reply count: {{ thread.reply_count }}</p>
        <button @click="toggleLike(thread)">Like</button>
        <button @click="toggleBookmark(thread)">Bookmark</button>
      </div>
    </div>
  </div>
  </template>
  
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        threads: []
      };
    },
    mounted() {
      this.fetchThreads();
    },
    methods: {
    async fetchThreads() {
      try {
        //const response = await axios.get('/api/thread');
        //Below api is just for trial
        const response = await axios.get('https://mocki.io/v1/6d525fbd-2885-445d-8700-b6f4075fd3e6');
        this.threads = response.data;
      } catch (error) {
        console.error('Error fetching threads:', error);
      }
    },
    toggleLike(item) {
      // Implement like functionality
      console.log('Like clicked for:', item);
    },
    toggleBookmark(item) {
      // Implement bookmark functionality
      console.log('Bookmark clicked for:', item);
    }
  }
  };
  </script>

<style scoped>

#title{
  text-align: center;
}
.container {
  margin: 20px;
}

.thread-container {
  display: flex;
  flex-direction: column;
}

.thread-info {
  border-bottom: 1px solid #ccc;
  padding-bottom: 10px;
  margin-bottom: 10px;
}

.replies {
  margin-left: 20px;
}

</style>
  