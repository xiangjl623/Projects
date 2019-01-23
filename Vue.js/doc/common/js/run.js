function run(e){
	var codeid = e.getAttribute("code-id");	
	var resultid = e.getAttribute("result-id");	
	var code = $("#"+codeid).val();
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
