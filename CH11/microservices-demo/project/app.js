new Vue({
    el: '#app',
    created() {
        this.fetchData();
    },
    data: {
        posts: []
    },
    methods: {
        fetchData() {
        axios.get('http://172.16.17.91:80/catalogue',
        {headers: {
          'Access-Control-Allow-Origin': '*',
        }}
        ).then(response => {
            this.posts = response;
            console.log(response);
            });
        }
    }
});