$(document).ready(function(){
	console.log("啦啦啦");
	console.log(innerWidth)
	console.log(innerHeight)
	console.log(typeof(innerHeight))
	var dpr = window.devicePixelRatio
	console.log(1/dpr)
	if(innerWidth<=innerHeight){
		document.documentElement.style.fontSize = innerWidth / 10 + "px";		
	}else{
		document.documentElement.style.fontSize = innerHeight / 10 + "px";
		
	}

	// http://127.0.0.1:8000/cart/
	var url = location.href;
	console.log(url);
	var spanID = url.split("/")[3];
	console.log(spanID);
	var $span =$(document.getElementById(spanID));
	console.log($span)
	$span.css("background", "url(/static/base/img/"+spanID+"1.png) no-repeat" );
	$span.css("background-size", "0.6rem");

});

