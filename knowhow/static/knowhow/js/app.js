new Vue({
	el: '#api_articles',
	data: {
		art:[]
	},
	created: function (){
		const vm=this;
		axios.get('/knowhow/api/articles/')
		.then(function(response){
			vm.art = response.data
			//console.log(response.data)
		})
	}
}
)