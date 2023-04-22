new Vue({
	el: '#entry',
	data: {
		entrys:[],
		links_count: 7,
	},
	created: function (){
		const vm=this;
		axios.get('/diary/api/entry')
		.then(function(response){
			vm.entrys = response.data
			//console.log(response.data)
		})
	}
}
)