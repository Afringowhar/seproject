<template>
    <div class="container">
        <div class="replytitle">
            <h1>Thread Replies</h1>
        </div>
        <div class="replies-container">
            <!-- Displaying the thread description as the first reply -->
            <p v-html="replies[0].cooked"></p>
            <!-- Displaying the rest of the replies -->
            <div v-for="(reply, index) in replies.slice(1)" :key="index" class="reply-info">
                <p><strong>ID:</strong> {{ reply.id }}</p>
                <p v-html="reply.cooked"></p>
            </div>
        </div>
        <div>
            <!-- Button to toggle the reply form -->
            <p class="edit"><button @click="showReplyForm = !showReplyForm">Reply</button></p>
            <!-- Reply form -->
            <div v-if="showReplyForm" class="reply-form">
                <textarea v-model="replyContent" placeholder="Enter your reply"></textarea>
                <button @click="submitReply">Submit</button>
            </div>
        </div>
    </div>
</template>


<script>
//import axios from 'axios';

export default {
    data() {
        return {
            replies: [],
            showReplyForm: false,
            replyContent: '',
            id:-1
        };
    },
    created() {
        const threadId = this.$route.query.id;
        this.fetchReplies(threadId);
        this.id=threadId
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
        },
        async submitReply() {
            try {
                var form = new FormData();
                form.append("description", this.replyContent);
                form.append("id", this.id);
                // const response = await axios.post('http://127.0.0.1:5000/api/thread', data_table, {headers: {'Content-Type': 'application/json'}});
                await fetch('http://127.0.0.1:5000/api/reply', {
                    method: 'POST',
                    body: form,
                    headers: {
                        'secret_authtoken': localStorage.getItem("token")
                    }
                }).then(res=>res.json())
                .then(res=>{
                  if(res >= 5){
                    fetch("https://chat.googleapis.com/v1/spaces/AAAAE--qWwU/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=i0QZFXd_dVkgMTq5Ye7lbiOxrLkTGY1IIDTqUqW-k_Q", {
                      headers: {
                        'Content-Type' : "application/json"
                      },
                      method: 'POST',
                      body: JSON.stringify({'text': `PRIORITY NOTIFICATION : ${this.replies[0].cooked}`})
                    })
                  }
                })
                // console.log('Replyed ', response.data);
                // Reset the reply form after submission
                this.replyContent = '';
                // Close the reply form
                this.showReplyForm = false;
                this.fetchReplies(this.id);
            } catch (error) {
                console.error('Error creating thread:', error);
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

.replytitle {
    text-align: center;
}
</style>
