//获取IFrame的标签
var getIFrameLabel = function(aId, aTag, aIndex) {
	var iFrame = document.getElementById(aId);
	if (iFrame.contentDocument) 
	{ // FF
		return iFrame.contentDocument.getElementsByTagName(aTag)[aIndex];
	}
	else if (iFrame.contentWindow) 
	{ // IE
		return iFrame.contentWindow.document.getElementsByTagName(aTag)[aIndex];
	}

};

function encode(s){
	return s.replace(/&/g, "&").replace(/</g, "<").replace(/>/g, ">").replace(/([\\\.\*\[\]\(\)\$\^])/g, "\\$1");
}

function decode(s){
	return s.replace(/\\([\\\.\*\[\]\(\)\$\^])/g, "$1").replace(/>/g, ">").replace(/</g,"<").replace(/&/g, "&");
}

function highLightKey(obj, s){
	if (s.length == 0){
		return false;
	}
	//s = encode(s); 暂时考虑特殊字符
	var  t = obj.innerHTML.replace(/<span\s+class=.?highlight.?>([^<>]*)<\/span>/gi, "$1");
	obj.innerHTML = t;
	var cnt = loopSearch(s, obj);
	t = obj.innerHTML;
	var r=/{searchHL}(({(?!\/searchHL})|[^{])*){\/searchHL}/g;
	t = t.replace(r, "<span style=\"background-color: yellow;\">$1</span>");
	//t = t.replace(r,"<span class=\"highlight\">$1</span>");
	obj.innerHTML = t;
}

function loopSearch(s, obj){
	var cnt = 0;
	if (obj.nodeType == 3){
		cnt = replaceKey(s, obj);
		return cnt;
	}
	for (var i = 0, c; c = obj.childNodes[i]; i++){
		if (!c.className || c.className != "highlight")
		  cnt += loopSearch(s, c);
		}
	return cnt;
}

function replaceKey(s, dest){
	var r = new RegExp("(" + s + ")", "gi"); //需要加括号 匹配$1
	var tm = null;
	var t = dest.nodeValue;
	var cnt = 0;
	if (tm = t.match(r)){
		cnt = tm.length;
		t = t.replace(r, "{searchHL}$1{/searchHL}"); //"{searchHL}" + decode(s) + "{/searchHL}")
		dest.nodeValue = t;
	}
	return cnt;
}

//支持多个关键字的搜索实现
function search(obj, aWords){
	sWords = $.trim(aWords);
	keyArray = sWords.split(' ');
	for(var i = 0; i < keyArray.length; i++){
	   var key = $.trim(keyArray[i]);
	   if (key != "")
	   { 
		 highLightKey(obj, key);
	   }
	}
};