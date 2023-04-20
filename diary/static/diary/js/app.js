new Vue({
	el: '#api_entry',
	data: {
		entrys:[]
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