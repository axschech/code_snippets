	events = [
	  { event: 'bill.split', user: 'Ray Green', city: 'Boston', time_of_day: 'morning', timestamp: 23981398 },
	  { event: 'promo.used', user: 'Jon Wicks', city: 'New York', time_of_day: 'afternoon', amount: 10.0, timestamp: 93219323 },
	  { event: 'promo.used', user: 'Robin Chou', city: 'New York', time_of_day: 'afternoon', amount: 15.0, timestamp: 28138233 },
	  { event: 'bill.split', user: 'John Malcom', city: 'Chicago', time_of_day: 'evening', timestamp: 32189389 },
	  { event: 'bill.split', user: 'Mark Wang', city: 'Boston', time_of_day: 'evening', timestamp: 43890121 }
	];

	config = [
		'event',
		'city',
		'time_of_day'
	];

console.log(JSON.stringify(run(events,config)));
function run(object, config) {
	mainObjs = {};
	object = object;
	config = config;
	configCount = config.length;
	iterateOn = config[configCount-1];
	iterated = {};
	firstArr = {};
	for(var z in object) {
			var obj = object[z];

		// if(typeof mainObjs[obj[config[0]]]=="undefined")
		// {
		mainObjs[obj[config[0]]] = [];
		firstArr[obj[config[0]]] = [];
			// mainObjs[obj[config[0]]][obj[config[1]]] = {};
			// console.log(mainObjs);
		// }
		for(var d in config) {
 
			if(typeof obj[config[d]] == "undefined") {
				return false;
			}
			else if(config[d] == iterateOn) {
				iterated[obj[iterateOn]] = 0;
			}
		}
	}

	for(var x in object) {

		var henh = object[x];
		// console.log(henh);
		var obj = {};
		var str = config.join('.');
		// console.log(str);
		var arr = str.split('.');
		var tmp = obj;
		var superKeys = Object.keys(henh);
		var superKey = superKeys[0];
		for (var i=1,n=arr.length; i<n; i++){

		   if(i!=n-1) {
		   	tmp[henh[arr[i]]]={};
		   	 tmp = tmp[henh[arr[i]]];
		   }
		   else {

		   	iterated[henh[arr[i]]]++;
		   	tmp[henh[arr[i]]] = iterated[henh[arr[i]]];
		   }
			
		}
		// console.log();
		var keys = Object.keys(obj)
		var subKeys = Object.keys(obj[keys[0]]);
		// console.log();
		// console.log(keys[0]);]
		// mainObjs[$S] = [];
		// mainObjs[keys[]]
		mainObjs[henh[superKey]].push(obj);

	}
	
	function getObs(obj, prefix) {
	  prefix = prefix || 'obj';
	  return Object.keys(obj).reduce(function(acc, key){
	      var value = obj[key];
	      if(typeof value === 'object') { 
	          acc.push.apply(acc, getObs(value, prefix + '.' + key));
	      }
	      else { 
	          acc.push(prefix + '.' + key + ' = ' + value);
	      }
	      return acc;
	  }, []);
	}

	var split_up = getObs(mainObjs);
	for(var z in split_up) {
		var items = split_up[z].split('.');
		console.log(items)
	}
	// console.log(test);

	// return mainObjs;
}


// var app = function(object, config) {
// 	assemble(object,config)
	
// 	function assemble(object, config) {
// 	this.theObs = {};
//   	this.mainObjs = [];
// 	this.object = object;
// 	this.config = config;
// 	this.configCount = this.config.length;
	
// 	this.iterateOn = this.config[this.configCount-1];
// 	// console.log(this.iterateOn)
// 	this.iterated = {};
// 	var check = init();
// 	if(!check) {
// 		console.log("\n Error with config \n");
// 		return false;
// 	}
// 	for(var x in this.object) {
// 		var item = this.object[x];

// 			// console.log(setupType(item));
// 			// console.log(x);
// 			// console.log();
// 			this.theObs[item[this.config[0]]].push(ob);
// 			// mainObj.push(ob);
// 			// mainObj[item[this.config[this.config.length-1]]] = item[this.config[this.config.length-1]];
	
	

// 	for(var x in this.object) {
// 		var item = this.object[x];

// 			// console.log(setupType(item));
// 			// console.log(x);
// 			// console.log();
// 			var ob = setupType(item);
// 			this.theObs[item[this.config[0]]].push(ob);
// 			// mainObj.push(ob);
// 			// mainObj[item[this.config[this.config.length-1]]] = item[this.config[this.config.length-1]];
	
// 	}
// 	this.theObs = this.mainObjs;
// 	console.log(JSON.stringify(this.mainObjs));
 
	
	
// 	}

// 	function init() {
// 		for(var z in this.object) {
// 			var obj = this.object[z];

// 			if(typeof this.mainObjs[obj[this.config[0]]]=="undefined")
// 			{
// 				this.mainObjs[obj[this.config[0]]] = [];
// 			}
// 			for(var d in this.config) {

// 				if(typeof obj[this.config[d]] == "undefined") {
// 					return false;
// 				}
// 				else if(this.config[d] == this.iterateOn) {
// 					this.iterated[obj[this.iterateOn]] = 0;
// 				}
// 			}
// 		}
// 		return true;
// 	}

// 	function setupType(object) {
// 		//http://stackoverflow.com/a/7641272
// 		var obj = {};
// 		var str = this.config.join('.');
// 		// console.log(str);
// 		var arr = str.split('.');
// 		var tmp = obj;
// 		for (var i=1,n=arr.length; i<n; i++){

// 		   if(i!=n-1) {
// 		   	tmp[object[arr[i]]]={};
// 		   	 tmp = tmp[object[arr[i]]];
// 		   }
// 		   else {

// 		   	this.iterated[object[arr[i]]]++;
// 		   	tmp[object[arr[i]]] = this.iterated[object[arr[i]]];
// 		   }
		   
// 		   // console.log(arr[i]);
		  
// 		   // console.log(obj)
		 
// 		}

// 		return obj;
// 	}
// }
// var henh = new app(events,config);

// console.log(henh);
