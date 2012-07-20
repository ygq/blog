$(function(){
	var read_para = {
		type : 'read'
	}
	var arts = new Array();
	$.get('main.php', read_para , function(data){
		var tmp = data.split('__a__');
		for(var i=0; i<tmp.length-1; i++){
			eval('o ='+tmp[i]);
			arts.push(o);
		}
		var htmls= new Array();
		for(var i=0; i<arts.length; i++){
			insert(arts[i],$('#show'));
		}
	})
	$('#submit').click(function(){
		var params = {
			type : 'write',
			art_name : $('input[name="art_name"]').val(),
			art_author : $('input[name="art_author"]').val(),
			art_content : $('input[name="art_content"]').val(),
			time :'刚刚'
		}
		$.get('main.php',params,function(data){
			insert(params,$('#show'));
		})
	})
})
function insert(o,e){
	e.append('<div class="area">文章名：<div class="art_name">'+ o.art_name +'</div>作 者：<div class="art_author">'+o.art_author
	   		 +'</div>内 容：<div class="art_author">'+o.art_author+'</div>时间：<div class="art_time">'+o.time+'</div></div>');
}
