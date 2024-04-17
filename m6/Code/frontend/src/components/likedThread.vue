<template>
    <div class="container">
      <h1>Liked Threads</h1>
      </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        likedThreads: []
      };
    }, 
  };
  </script>
  
  <style scoped>
  .container {
    margin: 20px;
  }
  
  .thread-info {
    border: 1px solid #ccc;
    padding: 10px;
    margin-bottom: 10px;
  }
  </style>
  