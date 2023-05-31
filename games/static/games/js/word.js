new Vue({
	el: '#word',	
	data: {
		word:[],
		letters:[],
		voices:{},
		entered_letter:'',
		actual_position:0,
		number_letters:100,
		// imgEnd:'http://192.168.1.3:8000/media/games/img/i.webp',
		imgEnd:'http://192.168.1.3:8000/media/games/img/romashka.png',
		theEnd:false,
	},

	methods: {
		audioplay: function (voice) {
			const audio = new Audio(voice);
			audio.play();
		},

		letter_is_enter: function() {
			if (this.letters[this.actual_position]['name']==this.entered_letter.toUpperCase()){
				this.audioplay(this.voices[this.entered_letter.toUpperCase()]);
				this.$refs['r'+String(this.actual_position)][0].classList.value='letter letter-color';
				if (this.actual_position < this.number_letters-1){
					this.$refs['r'+String(this.actual_position+1)][0].classList.value='letter letter-actual';
				}
				if (this.actual_position === this.number_letters-1){
					// setTimeout(() => this.finish(), 2000);
					this.finish();
				}
				this.actual_position++;
			}
				this.entered_letter='';
		},

		finish(){
			// setTimeout(()=> {alert("МОЛОДЕЦ!!!");}, 2000);
			setTimeout(()=> {this.theEnd=true;}, 2000);
		},
	},

	directives: {
		focus: {
			inserted: function (el) {
				el.focus()
			}
		},
	},

	created: function (){
		const vm=this;
		const myWord="колбаса";
		// const myWord="хлеб";
		axios.get(`/games/api/words/?filter&name=${myWord}`)
		.then(function(response){
			vm.word = response.data[0];
			vm.number_letters=vm.word.name.toUpperCase().length;
			for (const item of vm.word['letters']){
				vm.voices[item['name']]=item['voice'];
			}
			let id=0; //start id
			for (const item of vm.word.name.toUpperCase().split('')){
				console.log('id=', 'r'+String(id));
				vm.letters.push({'name':item, 'id':'r'+String(id), "voice":vm.voices[item]});
				id++;
			}
		});
	},

	updated: function (){
		this.$refs['r'+String(this.actual_position)][0].classList.value='letter letter-actual';
	},

})
