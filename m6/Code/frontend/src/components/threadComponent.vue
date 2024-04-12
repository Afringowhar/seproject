<!-- ThreadComponent.vue -->
<template>
    <div>
      <h1>Threads</h1>
      <table>
        <thead>
          <tr>
            <th>Title</th>
            <th>Category</th>
            <th>Created By:</th>
            <th>Replies</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="thread in threads" :key="thread.id">
            <td><a :href="`/thread/${thread.id}`">{{ thread }}</a></td>
            <td>{{ thread.category }}</td>
            <td>{{ thread.created_by }}</td>
            <td>{{ thread.replies }}</td>
          </tr>
        </tbody>
      </table>
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
          const response = await axios.get('http://localhost:4200/latest.json', {
            headers: {
              'Api-Key': 'ce4fe486cb5eb2d38ea811d358e8e82978f8944f5cf06daa30f77523ea70dbc4',
              'Api-Username': '21f1002269'
            }
          });
          this.threads = response.data.topic_list.topics;
        } catch (error) {
          console.error('Error fetching threads:', error);
        }
      }
    }
  };
  </script>
  