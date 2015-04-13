

function callme()
	{
	var data=document.getElementById("text").value;
	
	var json_data={"data":data}
	if (data==="")
		{alert("Please enter a message"); }
	else {
	
		$.ajax({
		type:"POST",
		url:"http://0.0.0.0:5000/post",

		//url:"http://192.168.1.33:5000/post",
		headers:{"Authorization":"123"},
		data:JSON.stringify(json_data),
		contentType:"application/json",
		dataType:"json",
		success:function(data){alert("Message: "+data+" hoisted");},
		failure:function(errMsg){ alert(errMsg);}
		     });
	     }
	}
