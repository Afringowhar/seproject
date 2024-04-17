<template>
    <div class="container">
      <h1>Thread Replies</h1>
      <div class="replies-container">
        <!-- Displaying the thread description as the first reply -->
          <p v-html="replies[0].cooked"></p>
        <!-- Displaying the rest of the replies -->
        <div v-for="(reply, index) in replies.slice(1)" :key="index" class="reply-info">
            <p><strong>ID:</strong> {{ reply.id }}</p>
            <p v-html="reply.cooked"></p>
        </div>
      </div>
    </div>
  </template>


  <script>
  //import axios from 'axios';

  export default {
    data() {
      return {
        replies: []
      };
    },
    created() {
      const threadId = this.$route.query.id;
      this.fetchReplies(threadId);
    },
    methods: {
        async fetchReplies(threadId) {
  try {
    const response = await fetch(`http://127.0.0.1:5000/api/reply?id=${threadId}`, {
      method: 'GET'
    });
    const data = await response.json();
    this.replies = data;
  } catch (error) {
    console.error('Error fetching thread replies:', error);
  }
}
    }
  };
  </script>

  <style scoped>
  .container {
    margin: 20px;
  }

  .replies-container {
    margin-top: 20px;
  }

  .reply-info {
    border: 1px solid #ccc;
    padding: 10px;
    margin-bottom: 10px;
  }
  </style>
