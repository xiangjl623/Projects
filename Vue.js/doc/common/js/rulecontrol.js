function ruleControl(){
   var rule = sessionStorage.getItem('rule');	 
   $('.rule').each(function(){
	  var index = $.inArray(rule, $(this).attr('rules').split(','));
	  if (index != -1)
	  {
		$(this).attr("style","display:block;");  
	  }
	  else
		$(this).attr("style","display:none;");			
	});	  
}