<template>
  
  <h1 id="title">Threads</h1>
  <!--Add thread -->
  <div class="container">
    <button @click="showCreateThread = !showCreateThread">Add Thread</button>
    <div v-if="showCreateThread" class="create-thread">
      <input type="text" v-model="newThread.title" placeholder="Enter thread title">
      <input type="text" v-model="newThread.created_by" placeholder="Enter user ID">
      <button @click="createThread">Create Thread</button>
    </div>
    </div>
  <!--View Thread -->
  <div class="container">
    <div class="thread-container">
      <div v-for="thread in threads" :key="thread.id" class="thread-info">
        <h2>{{ thread.title }}</h2>
        <p>Created by:: {{ thread.created_by }}</p>
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
        threads: [],
        newThread: {
        title: '',
        created_by: ''
      },
      showCreateThread: false
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
    async createThread() {
      try {
        const response = await axios.post('/api/thread', this.newThread);
        console.log('New thread created:', response.data);
        // Clear input fields after successful creation
        this.newThread.title = '';
        this.newThread.created_by = '';
        // Fetch threads again to update the list
        await this.fetchThreads();
      } catch (error) {
        console.error('Error creating thread:', error);
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