new Vue({
	el: '#word',
	data: {
		word:[],
		letters:[],
		count:0,
		bukvy:{},
	},
	created: function (){
		const v=this;
		axios.get('/games/api/words')
		.then(function(response){
			v.word = response.data[0];
			console.log(v.word);
			v.letters = v.word.name.toUpperCase().split('');
			for (const bukva of v.letters) {
				axios.get('/games/api/letter/?name='+bukva)
				.then(function(response){
					const rd=response.data;
					v.bukvy[bukva]={name:rd[0]['name'],voice:rd[0]['voice']};
					v.count++;
					// if (rd.length != 0){
					// 	// setTimeout(v.bukvy[bukva]={name:rd[0]['name'],voice:rd[0]['voice']}, 10000);
					// 	v.count++;
					// 	v.bukvy[bukva]={name:rd[0]['name'],voice:rd[0]['voice']};
					// }
				});
        	}
		});

	}
})
***********************************************************************

new Vue({
	el: '#word',
	data: {
		word:[],
		letters:[],
		bukvy:[],
		slovar:{},
	},
	created: function (){
		const v=this;
		axios.get('/games/api/words')
		.then(function(response){
			v.word = response.data[0];
			v.letters = v.word.name.split('');
			for (const bukva of v.letters) {
				axios.get('/games/api/letter/?name='+bukva.toUpperCase())
				.then(function(response){
					if (response.data.length != 0){
						v.bukvy.push([bukva, response.data[0]['name'], response.data[0]['voice']]);
						v.slovar[bukva]={name:response.data[0]['name'],voice:response.data[0]['voice']};
					}
				});
        	}
		});

	}
})


++++++++++++++++++++++++++++++++

Vue.prototype.$a = "333"
Vue.prototype.$b = "55"


new Vue({
	el: '#word',
	data: {
		word:[],
		letters:[],
		bukvy:{},
	},
	created: function (){
		const vm=this;
		axios.get('/games/api/words')
		.then(function(response){
			vm.word = response.data[0];
			vm.letters = vm.word.name.split('');
			for (const bukva of vm.letters) {
				console.log('----', bukva);
				axios.get('/games/api/letter/?name='+bukva.toUpperCase())
				.then(function(response){
					const mm=this;
					if (response.data.length != 0){
	        			$a=response.data[0]['name'];
	        			$b=bukva;
						console.log('+*******A******+', $a);
						console.log('+*******B******+', $b);
						vm.bukvy[$a]=$b; 
					}
				})
        	}
			//console.log('+A******+', $a);
			//console.log('+B******+', $b);        	
			//console.log('###BUK###', buk);
			//bukvy[a]=b;
	        //vm.bukvy['f']='hhh';  	
			//console.log('yyy', vm.bukvy);

		});

	}
})



//**********************************


Vue.prototype.$a = "333"
Vue.prototype.$b = "55"


new Vue({
	el: '#word',
	data: {
		word:[],
		letters:[],
		bukvy:{},
	},
	created: function (){
		const vm=this;
		axios.get('/games/api/words')
		.then(function(response){
			vm.word = response.data[0];
			vm.letters = vm.word.name.split('');
			for (const bukva of vm.letters) {
				console.log('----', bukva);
				(async () => {
				  let data = {};
				  async function status() {
				    const url = '/games/api/letter/?name='+bukva.toUpperCase();
				    const response = await axios.get(url);
				    data = response.data[0];
				  }
				  await status();
				  vm.bukvy[bukva]=data['name'];
				  console.log('----->',vm.bukvy); // {...response.data}
				  //if (typeof data !== 'undefined'){
				  //	console.log('-->',data['name']); // {...response.data}
				  //	vm.bukvy[bukva]=data['name'];
				  //	console.log('----->',vm.bukvy); // {...response.data}
				  //}
				  
				  // Now you can manipulate and use the properties of data in subsequent code here
				}
				)()
        	}
		});

	}
})

*********************************************


new Vue({
	el: '#word',
	data: {
		word:[],
		letters:[],
		bukvy:{},
	},
	created: function (){
		const vm=this;
		
		(async () => {
			let data = {};
			async function status() {
				const url = '/games/api/words';
				const response = await axios.get(url);
				data = response.data[0];
			}
			await status();
			vm.word = data;
			vm.letters = vm.word.name.split('');			
				  console.log('----->',vm.word);
				  console.log('----->',vm.letters);
		//})()
				  
			
			for (const bukva of vm.letters) {
				console.log('----', bukva);
				(async () => {
					let data2 = {};
				  	async function status() {
				    	const url = '/games/api/letter/?name='+bukva.toUpperCase();
				    	const response = await axios.get(url);
				    	data2 = response.data[0];
				  	}
				  await status();
				  vm.bukvy[bukva]=data2['name'];
				  console.log('----->',vm.bukvy);
				  //if (typeof data !== 'undefined'){
				  //	console.log('-->',data['name']); // {...response.data}
				  //	vm.bukvy[bukva]=data['name'];
				  //	console.log('----->',vm.bukvy); // {...response.data}
				  //}
				})()
				  vm.bukvy[bukva]=data2['name'];
				  console.log('--out-1-->',vm.bukvy); // {...response.data}
			}
				  console.log('--out-2-->',vm.bukvy); // {...response.data}

				  vm.bukvy['ff']='KK';
		})()
				  console.log('---3-->',vm.letters);
				  console.log('--out-3-->',vm.bukvy); // {...response.data}
	}
})


