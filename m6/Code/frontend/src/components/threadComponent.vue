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
      <p><textarea v-model="newThread.description" placeholder="Description of the thread"></textarea></p>
      <div class="ctbutton"><button @click="createThread">Create Thread</button></div>
    </div>
    </div>
    </div>
    <!--Edit thread -->
    <div class="edit-thread" v-if="showEditForm">
      <div class="edit-popup">
        <span class="close" @click="cancelEdit">&times;</span>
      <h3>Edit Thread</h3><br>
      <p><input type="text" v-model="updatedThread.description" placeholder="Enter updated description" style="width: 450px; height: 300px;"></p>
      <div class="editactions">
      <div class="editbutton"><button @click="editThread()">Update Thread</button></div>
      <div class="cancel"><button @click="cancelEdit">Cancel</button></div>
    </div>
    </div></div>

  <!--View Thread -->
  <div class="container">
    <div class="thread-container">
      <div v-for="thread in threads" :key="thread.id" class="thread-info">
        <h2>{{ thread.title }}</h2>
        <p>Created at: {{ thread.created_at }}</p>
        <p>Reply count: {{ thread.posts_count-1 }}</p>
        <p>Like count: {{thread.like_count}}</p>
        <p class="replybutton"><router-link :to="`/thread_replies?id=${thread.id}`"><button>View Replies</button></router-link></p>
        <div class="actions">
          <div class="actionsleft">
        <p class="like" v-if="!thread.liked"><button @click="toggleLike(thread)" :class="{ liked: thread.liked }"><i class="bi bi-hand-thumbs-up-fill"></i></button></p>
        <p class="like" v-else><button @click="toggleLike(thread)" :class="{ liked: thread.liked }"><i class="bi bi-hand-thumbs-down-fill"></i></button></p>
        <p class="bookmark"><button @click="toggleBookmark(thread)" :class="{ bookmarked: thread.bookmarked }"><i class="bi bi-bookmark-fill"></i></button></p>
      </div>
        <div class="actionsright">
        <p class="edit"><button @click="showEditForm = true; setThreadToUpdate(thread)"><i class="bi bi-pencil-square"></i></button></p>
        <p class="delete"><button @click="deleteThread(thread.id)"><i class="bi bi-trash-fill"></i></button></p>
      </div>
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
    console.log("Fetching...")
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
        const response = await fetch('http://127.0.0.1:5000/api/thread', {
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
      // console.log('Like clicked for:', item.liked);
      var form = new FormData();
      form.append("id", item.id);
      var m = "";
      if(item.liked) m = "DELETE";
      else m = "POST";
      console.log(m);
      await fetch("http://127.0.0.1:5000/api/like", {
        method: m,
        body: form,
        headers: {
          'secret_authtoken' : localStorage.getItem("token")
        }
      });
      this.fetchThreads();
    },
    async toggleBookmark(item) {
      // Implement bookmark functionality
      console.log('Bookmark clicked for:', item);
      var form = new FormData();
      form.append("id", item.id);
      await fetch("http://127.0.0.1:5000/api/bookmark", {
        method: 'POST',
        body: form,
        headers: {
          'secret_authtoken' : localStorage.getItem("token")
        }
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
          body: form,
          headers: {
            'secret_authtoken' : localStorage.getItem("token")
          }
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
        //const response = await axios.delete(`/api/thread?id=${threadId}`);
        await fetch(`http://127.0.0.1:5000/api/thread?id=${threadId}`, {
          method: 'DELETE',
          headers: {
            'secret_authtoken' : localStorage.getItem("token")
          }
        })
        //console.log('Thread deleted:', response.data);
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
.edit-thread {
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
.editbutton button {
  padding: 10px 20px;
  margin-right: 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}
.editbutton button:hover {
  background-color: #0f3863;
  color: cyan;
}
.cancel button {
  padding: 10px 20px;
  margin-right: 20px;
  background-color: #ff5500;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}
.cancel button:hover {
  background-color: #933404;
  color: #fac5ab;
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
.edit-popup {
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
  justify-content: space-between;
  align-items: center;
}
.actionsright {
  display: flex;
}
.actionsleft {
  display: flex;
}
.editactions {
  justify-content: center;
  display: flex;
}
.like button {
  padding: 4px 12px;
  text-align: center;
  font-size: 30px;
  background-color: white;
  color: pink;
  border: none;
  border-radius: 50%;
  cursor: pointer;
  transition: background-color 0.3s;
}
.like button:hover {
  background-color: pink;
  color: white;
}
.bookmark button {
  padding: 4px 12px;
  font-size: 30px;
  text-align: center;
  background-color: white;
  color: yellow;
  border: none;
  border-radius: 50%;
  cursor: pointer;
  transition: background-color 0.3s;
}
.bookmark button:hover {
  background-color: yellow;
  color: white;
}
.edit,.delete {
  margin-left: 10px;
}
.edit button {
  padding: 4px 8px;
  text-align: center;
  background-color: white;
  font-size: 30px;
  color: blue;
  border: none;
  border-radius: 50%;
  cursor: pointer;
  transition: background-color 0.3s;
}
.edit button:hover {
  background-color: blue;
  color: white;
}
.delete button {
  padding: 4px 8px;
  text-align: center;
  background-color: white;
  font-size: 30px;
  color: red;
  border: none;
  border-radius: 50%;
  cursor: pointer;
  transition: background-color 0.3s;
}
.delete button:hover {
  background-color: red;
  color: white;
}
.replies {
  margin-left: 20px;
}
.replybutton button {
  padding: 4px 8px;
  text-align: center;
  background-color: white;
  font-size: 20px;
  color: indigo;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: background-color 0.3s;
}
.replybutton button:hover {
  background-color: indigo;
  color: white;
}

</style>
