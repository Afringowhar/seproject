<template>

  <h1 id="title">Threads</h1>
  <!--Add thread -->
  <div class="container">
    <div class="addthread"><button @click="showCreateThread = !showCreateThread">Add Thread</button> </div>
    <br>
    <div v-if="showCreateThread" class="create-thread">
      <div class="popup-content">
        <span class="close" @click="toggleCreateThread">&times;</span>
        <h2>Create Thread</h2><br>
      <p><input type="text" v-model="newThread.title" placeholder="Enter thread title"></p>
      <p><input type="text" v-model="newThread.description" placeholder="Description of the thread"></p>
      <div class="ctbutton"><button @click="createThread">Create Thread</button></div>
    </div>
    </div>
    </div>
    <!--Edit thread -->
    <div class="edit-thread" v-if="showEditForm">
      <h3>Edit Thread</h3>
      <input type="text" v-model="updatedThread.id" placeholder="Enter updated id">
      <input type="text" v-model="updatedThread.description" placeholder="Enter updated description">
      <button @click="editThread">Update Thread</button>
      <button @click="cancelEdit">Cancel</button>
    </div>
  <!--View Thread -->
  <div class="container">
    <div class="thread-container">
      <div v-for="thread in threads" :key="thread.id" class="thread-info">
        <h2>{{ thread.title }}</h2>
        <p>Created by: {{ thread.created_by }}</p>
        <p>Created at: {{ thread.created_at }}</p>
        <p>Reply count: {{ thread.reply_count }}</p>
        <div class="actions">
        <div class="like"><button @click="toggleLike(thread)"></button></div>
        <div class="bookmark"><button @click="toggleBookmark(thread)">⛊</button></div>
        <button @click="showEditForm = true; setThreadToUpdate(thread)">Edit</button>
        <button @click="deleteThread(thread.id)">Delete</button>
      </div>
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
        description: ''
      },
      updatedThread: {
        id: '',
        description: ''
      },
      showCreateThread: false,
      showEditForm: false,
      threadIdToUpdate: null
      };
    },
    mounted() {
      this.fetchThreads();
    },
    methods: {
      toggleCreateThread() {
        this.showCreateThread = !this.showCreateThread;
      },
    async fetchThreads() {
      try {
        const response = await axios.get('/api/thread');
        //Below api is just for trial
        // const response = await axios.get('https://mocki.io/v1/e0ef012b-6bcb-4828-9f54-a2c68ba5a159');
        this.threads = response.data;
      } catch (error) {
        console.error('Error fetching threads:', error);
      }
    },
    async createThread() {
      try {
        var form = new FormData();
        form.append("title", this.newThread.title);
        form.append("description", this.newThread.description);
        // const response = await axios.post('http://127.0.0.1:5000/api/thread', data_table, {headers: {'Content-Type': 'application/json'}});
        const response = await fetch("http://127.0.0.1:5000/api/thread", {
          method: 'POST',
          body: form,
          headers: {
            'secret_authtoken' : localStorage.getItem("token")
          }
        })
        console.log('New thread created:', response.data);
        // Clear input fields after successful creation
        this.newThread.title = '';
        this.newThread.description = '';
        // Fetch threads again to update the list
        await this.fetchThreads();
      } catch (error) {
        console.error('Error creating thread:', error);
      }
    },
    async toggleLike(item) {
      // Implement like functionality
      console.log('Like clicked for:', item.id);
      var form = new FormData();
      form.append("id", item.id);
      await fetch("http://127.0.0.1:5000/api/like", {
        method: 'POST',
        body: form
      });
    },
    async toggleBookmark(item) {
      // Implement bookmark functionality
      console.log('Bookmark clicked for:', item);
      var form = new FormData();
      form.append("id", item.id);
      await fetch("http://127.0.0.1:5000/api/bookmark", {
        method: 'POST',
        body: form
      });
    },
    async editThread() {
      try {
        var form = new FormData();
        form.append("id", this.threadIdToUpdate);
        form.append("description", this.updatedThread.description);
        console.log(this.threadIdToUpdate);
        console.log(this.updatedThread.description);
        const response = await fetch('http://127.0.0.1:5000/api/thread', {
          method: 'PUT',
          body: form
        });
        console.log('Thread updated:', response.data);
        this.updatedThread.id = '';
        this.updatedThread.description = '';
        await this.fetchThreads();
      } catch (error) {
        console.error('Error updating thread:', error);
      }
    },
    setThreadToUpdate(thread) {
      this.threadIdToUpdate = thread.id;
    },
    async deleteThread(threadId) {
      try {
        const response = await axios.delete(`/api/thread?id=${threadId}`);
        console.log('Thread deleted:', response.data);
        await this.fetchThreads(); // Fetch threads again to update the list
      } catch (error) {
        console.error('Error deleting thread:', error);
      }
    },
    cancelEdit() {
      this.showEditForm = false;
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
.addthread {
  text-align: right;
}
.addthread button {
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}
.addthread button:hover {
  background-color: #0f3863;
  color: cyan;
}
.create-thread {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height:100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 999;
  display: flex;
  justify-content: center;
  align-items: center;
}
.thread-container {
  display: flex;
  flex-direction: column;
}
.popup-content {
  text-align: center;
  background-color: white;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 81, 255, 0.367);
  position: relative;
  max-width: 500px;
  width: 90%;
}
.close {
  position: absolute;
  top: 10px;
  right: 20px;
  font-size: 30px;
  cursor: pointer;
}
.create-thread input[type="text"] {
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
.thread-info {
  border-bottom: 1px solid #ccc;
  padding-bottom: 10px;
  margin-bottom: 10px;
}
.ctbutton button{
  padding: 10px 20px;
  background-color: #08e393;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}
.ctbutton button:hover {
  background-color: #0f3863;
  color: cyan;
}
.actions {
  display: flex;
}
.like button {
  padding: 4px 12px;
  background-color: white;
  font-size: 30px;
  color: #e30821;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}
.like button:hover {
  background-color: #e30821;
  color: white;
}
.bookmark button {
  padding: 4px 10px;
  background-color: white;
  font-size: 30px;
  color: yellow;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}
.bookmark button:hover {
  background-color: yellow;
  color: white;
}
.replies {
  margin-left: 20px;
}

</style>
