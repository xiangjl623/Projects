var tipuesearch_in = {
	pages: []
}; 	

function loadPage(aName, aFile){
	var sUrl = urlRoot + aFile;
	//var sEncodeURL = encodeURI(sUrl);
	//$.get(sEncodeURL, function(html, status)							 
	//{    		
	//    alert(html);
	//	tipuesearch_in.pages.push(
	//	{   
	//	   "title": aName,
	//	   "text": html,
	//	   "tags": "", //cont,
	//	   "url": aFile
	//	});    
	//});  
    $.get(sUrl, function(html) {
		tipuesearch_in.pages.push(
		{   
		   "title": aName,
		   "text": html,
		   "tags": "", //cont,
		   "url": aFile
		});    
	
    }, 'text');   
};

function showProgressBar(percent){  
	$('#bar').css("width", percent + "%");  
	$('#total').html("Searching(" + percent + "%)..."); 
};
		   
function loadPages() {
	//$('#progress').show();
	for (var i = 0; i < zNodes.length; i++)
	{    
		//var percent = Math.round(100 * (i + 1) / zNodes.length);				
		//showProgressBar(percent);	
		if (zNodes[i]["file"] != "")
		{   
			loadPage(zNodes[i]["name"], zNodes[i]["file"]);
		}	 
	};
	//$('#progress').hide();
};

//异步初始化所有Page
function initPages(){   
	if (tipuesearch_in.pages.length == 0)
	{  
        $.ajaxSetup({
            async: true
        });
	    loadPages();					
	}      
};