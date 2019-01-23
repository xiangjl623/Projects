function run(e){
	var codeid = e.getAttribute("code-id");	
	var resultid = e.getAttribute("result-id");	
	var code = $("#"+codeid).val();
	code = "<script src='" + "common/js/vue.js'" + "></script>" + code;
	var iframe = document.getElementById(resultid);
    var iwindow = iframe.contentWindow;
    var idoc = iwindow.document;
	idoc.open();
	idoc.write(code);
	idoc.close();
}

function binddata(id, file)
{
   $.get(file, function(data) {
	 $("#" + id).text(data);
   }, 'text');
}

function getURLParam(name, url) {
	if (!url) 
	   url = location.href;
	name = name.replace(/[\[]/,"\\\[").replace(/[\]]/,"\\\]");
	var regexS = "[\\?&]"+name+"=([^&#]*)";
	var regex = new RegExp( regexS );
	var results = regex.exec( url );
	return results == null ? null : results[1];
}
