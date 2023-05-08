new Vue({
	el: '#word',
	data: {
		word:[],
	},
	created: function (){
		const vm=this;
		axios.get('/games/api/words')
		.then(function(response){
			vm.word = response.data[0]
			console.log(vm.word)
			//console.log(response.data)
		})
	}
}
)