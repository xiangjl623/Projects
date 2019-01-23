var zTree;
var contentIframe;
var isTitle = false;
var setting = {
	view: {
		dblClickExpand: false,
		showLine: true,
		selectedMulti: false,
		expandSpeed: ($.browser.msie && parseInt($.browser.version)<=6)?"":"fast"
	},
	data: {
		simpleData: {
			enable:true,
			idKey: "id",
			pIdKey: "pId",
			rootPId: ""
		}
	},
	callback: {
		beforeClick: function(treeId, treeNode) {
			var zTree = $.fn.zTree.getZTreeObj("tree");
			if (treeNode.file != "")
			{
				contentIframe.attr("src", "template.html?file="+treeNode.file);
			}
			else
			{
				contentIframe.attr("src", "blank.html");
			}
			return true;
		},
		onClick: function(treeID, treeNode){
			loadReady();
			return true;
		} 
	}
};

function getParamVal(aHref, aParamName){
	var intPos = aHref.indexOf("?");  // 参数开始位置
	var sRight = aHref.substr(intPos + 1);
	var arrTmp = sRight.split("&"); //参数分割符
	for(var i = 0; i < arrTmp.length; i++) 
	{ 
		 var arrTemp = arrTmp[i].split("="); 
		 if(arrTemp[0].toUpperCase() == aParamName.toUpperCase()) 
			 return arrTemp[1]; 
	} 
	return ""; 
}

$(document).ready(function(){
	    //处理页签切换
	    $('.tab ul.tabs').addClass('active').find('> li:eq(0)').addClass('current');
		$('.tab ul.tabs li a').click(function (g) { 
			var tab = $(this).closest('.tab'), 
			index = $(this).closest('li').index();
			tab.find('ul.tabs > li').removeClass('current');
			$(this).closest('li').addClass('current');
			tab.find('.tab_content').find('div.tabs_item').not('div.tabs_item:eq(' + index + ')').slideUp();
			tab.find('.tab_content').find('div.tabs_item:eq(' + index + ')').slideDown();	
			g.preventDefault();
		} );
		//处理搜索按钮事件绑定
		$('#tipue_search_input').bind('keypress', function (event) {
			if (event.keyCode == "13") {
			   $('#tipue_search_input').tipuesearch({
					'mode': 'live'
			   });
			}
		});
		$('#tipue_search_button').bind('click', function () {
		    $('#tipue_search_input').tipuesearch({
			    'mode': 'live'
			});
		});
		//初始化ZTree
		var t = $("#tree");
        t = $.fn.zTree.init(t, setting, zNodes);
		//Ztree节点反选，如新特性通过节点ID访问，此时节点反选
		var zTree = $.fn.zTree.getZTreeObj("tree");
		var id = getParamVal(window.location.href, "id");
		if (id == "")
		  id = 1;
		var oNode = zTree.getNodeByParam("id", id);
		zTree.selectNode(oNode);
		contentIframe = $("#contentIframe");
		contentIframe.attr("src", oNode.file);
		var rule = getParamVal(window.location.href, "rule");
		if (rule == "")
		  rule = -1
		//初始化搜索页（异步方式）
		setTimeout("initPages()",  1000);
		//document.getElementsByTagName("body")[0].setAttribute("style", "visibility:visible"); //解决IE下部分显示的问题
		sessionStorage.setItem('rule', rule); // 存入一个值
});

String.prototype.replaceAll = function(reallyDo, replaceWith, ignoreCase) {  
    if (!RegExp.prototype.isPrototypeOf(reallyDo)) {  
        return this.replace(new RegExp(reallyDo, (ignoreCase ? "gi": "g")), replaceWith);  
    } else {  
         return this.replace(reallyDo, replaceWith);     
	}  
} 


function setIframeHeight(iframeId) /** IMPORTANT: All framed documents *must* have a DOCTYPE applied **/
{
     var ifDoc, ifRef = document.getElementById(iframeId);
     try
     {  
       ifDoc = ifRef.contentWindow.document.documentElement;
     }
     catch(e)
     {
        try
        {
          ifDoc = ifRef.contentDocument.documentElement;
        }
       catch(ee)
       {
		 
       }
     }
	 if(ifDoc)
	 {  
		var bodyH = contentIframe.contents().find("body").get(0).scrollHeight;
	    htmlH = contentIframe.contents().find("html").get(0).scrollHeight;
	    maxH = Math.max(bodyH, htmlH); 
	    minH = Math.min(bodyH, htmlH);
	    h = contentIframe.height() >= maxH ? minH:maxH;
        contentIframe.height(h);
	 }
	 else{
		ifRef.height = 2000;	
	 }
}
	
function loadReady() {
	//自适应IFrame高度与宽度
	setIframeHeight("contentIframe");
	contentIframe = $("#contentIframe");
	//通过搜索的路径里面是否包含关键字，来判断是目录还是搜索页签，也可以有其他方式
	var sIFrameHref = contentIframe.contents().get(0).location.href;
	var keywords = getParamVal(sIFrameHref, "keywords");
	if (keywords != ""){ 	
        var obj = getIFrameLabel('contentIframe', 'body', 0);//document.getElementsByTagName("body")[0];	
        search(obj, keywords);
        isTitle = false;		
	}
	else{
        //IFrame内部链接调转后，Ztree节点反选		
		var sHref = location.href;
		var nIndex = sHref.indexOf("index.html");
		var sRoot;
		if (nIndex != -1)
			sRoot = sHref.substring(0, nIndex);
		else 
			sRoot = sHref;
		var sIFrameHrefRef = sIFrameHref.substring(sRoot.length, sIFrameHref.length);
		sIFrameHrefRef = sIFrameHrefRef.replaceAll("%20", " ", false);
		sIFrameHrefRef = decodeURI(sIFrameHrefRef);
		var zTree = $.fn.zTree.getZTreeObj("tree");
		var oNode = zTree.getNodeByParam("file", sIFrameHrefRef);
		zTree.selectNode(oNode);
	}
}

