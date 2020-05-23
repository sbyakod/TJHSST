var conversion = {
    "AL": "Alabama",
    "AK": "Alaska",
    "AZ": "Arizona",
    "AR": "Arkansas",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "FL": "Florida",
    "GA": "Georgia",
    "GU": "Guam",
    "HI": "Hawaii",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "IA": "Iowa",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "ME": "Maine",
    "MD": "Maryland",
    "MA": "Massachusetts",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MS": "Mississippi",
    "MO": "Missouri",
    "MT": "Montana",
    "NE": "Nebraska",
    "NV": "Nevada",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NY": "New York",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VT": "Vermont",
    "VA": "Virginia",
    "WA": "Washington",
    "WV": "West Virginia",
    "WI": "Wisconsin",
    "WY": "Wyoming"
}

var elem = document.getElementById('ustate')
var outline = document.getElementById('outlines')
var finished = []
var hints = 0

/*if(finished.length == 1)
	Stopwatch.start()
if(finished.length == 50)
	Stopwatch.stop()*/

elem.addEventListener('keypress', function(e){
  if (e.keyCode == 13) {
    var state = document.getElementById(getKeyByValue(conversion, elem.value))
    state.style['fill'] = 'pink'
    finished.push(elem.value)
  }
})

function giveHint() {
	var keys = Object.values(conversion)
	var randomAnswer = keys[Math.floor(Math.random() * keys.length)];

	if(hints < 3){
		for(var i=0; i<Infinity; i++){
			if(finished.includes(randomAnswer) == false){
				var state = document.getElementById(getKeyByValue(conversion, randomAnswer))
				state.style['fill'] = 'pink'
				finished.push(randomAnswer)
				hints++
				break;
			}
			else
				randomAnswer = keys[Math.floor(Math.random() * keys.length)];
		}
	}
}

//https://codepen.io/_Billy_Brown/pen/dbJeh
class Stopwatch {
    constructor(display, results) {
        this.running = false;
        this.display = display;
        this.results = results;
        this.laps = [];
        this.reset();
        this.print(this.times);
    }
    
    reset() {
        this.times = [ 0, 0, 0 ];
    }
    
    start() {
        if (!this.time) this.time = performance.now();
        if (!this.running) {
            this.running = true;
            requestAnimationFrame(this.step.bind(this));
        }
    }
    
    /*lap() {
        let times = this.times;
        let li = document.createElement('li');
        li.innerText = this.format(times);
        this.results.appendChild(li);
    }*/
    
    stop() {
        this.running = false;
        this.time = null;
    }

    restart() {
        if (!this.time) this.time = performance.now();
        if (!this.running) {
            this.running = true;
            requestAnimationFrame(this.step.bind(this));
        }
        this.reset();
    }
    
    /*clear() {
        clearChildren(this.results);
    }*/
    
    step(timestamp) {
        if (!this.running) return;
        this.calculate(timestamp);
        this.time = timestamp;
        this.print();
        requestAnimationFrame(this.step.bind(this));
    }
    
    calculate(timestamp) {
        var diff = timestamp - this.time;
        // Hundredths of a second are 100 ms
        this.times[2] += diff / 10;
        // Seconds are 100 hundredths of a second
        if (this.times[2] >= 100) {
            this.times[1] += 1;
            this.times[2] -= 100;
        }
        // Minutes are 60 seconds
        if (this.times[1] >= 60) {
            this.times[0] += 1;
            this.times[1] -= 60;
        }
    }
    
    print() {
        this.display.innerText = this.format(this.times);
    }
    
    format(times) {
        return `\
${pad0(times[0], 2)}:\
${pad0(times[1], 2)}:\
${pad0(Math.floor(times[2]), 2)}`;
    }
}

function pad0(value, count) {
    var result = value.toString();
    for (; result.length < count; --count)
        result = '0' + result;
    return result;
}

function clearChildren(node) {
    while (node.lastChild)
        node.removeChild(node.lastChild);
}

let stopwatch = new Stopwatch(
    document.querySelector('.stopwatch'),
    document.querySelector('.results'));


/*var outline = document.getElementById('outlines')
outline.onclick = function(ev) {
	var state = document.getElementById(ev.path[0].id)
	if(state.style['fill'] != '')
		state.style['fill'] = ''
	else
    	state.style['fill'] = 'pink'
}*/

function getKeyByValue(object, value)
{
  return Object.keys(object).find(key => object[key] === value)
}

function randomColor() //STACKOVERFLOW
{
     return ("#" + ("000000" + Math.floor(Math.random() * 16777216).toString(16)).substr(-6))
}