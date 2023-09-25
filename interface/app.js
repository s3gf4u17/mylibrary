const app = Vue.createApp({
    data() {
        return {
            books: null,
        }
    },
    mounted() {
        fetch("http://127.0.0.1:8000/?").then(res=>res.json()).then(data=>this.books=data);
    },
    methods: {
        async filterbooks() {
            let query = document.getElementById("query").value;
            let radio = document.getElementsByName("inlineRadioOptions");
            let limit;
            for (i=0;i<radio.length;i++) {
                if (radio[i].checked) {
                    limit = radio[i].value;
                }
            }
            const data = await fetch("http://127.0.0.1:8000/?query="+query+"&limit="+limit)
            .then(function(response){
                return response.json();
            }).then(function(data){
                console.log(data);
                return data;
            });
            this.books = data;
        }
    }
});

app.mount('#app');