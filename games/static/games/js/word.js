new Vue({
	el: '#word',	
	data: {
		word:[],
		word_of_letters:[],
		letters:{},
	},

	methods: {
		audioplay: function (voice) {
			const audio = new Audio(voice);
			audio.play();
			console.log('=audio=',voice);
			// alert(message);
		},
	},

	created: function (){
		const v=this;
		axios.get('/games/api/words/?filter&name=колбаса')
		.then(function(response){
			v.word = response.data[0];
			v.word_of_letters = v.word.name.toUpperCase().split('');
			for (const item of v.word['letters']){
				v.letters[item['name']]=item['voice'];
			}
	// console.log(v.word.voice);
	// const audio = new Audio(v.word.voice);
	// audio.play();
		});
	}
})
