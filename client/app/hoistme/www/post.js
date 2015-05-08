

function callme()
	{
	var data=document.getElementById("text").value;
	
	var json_data={"data":data};
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


//sample json 

var data={
		"1":{ "Head":"This is heading1 from json",
		    "Title":"This is title1 from json",
		    "Message":"This is message1",
		    "Time":"5.00PM"
				
		  },

		"2":{ "Head":"This is heading2 from json",
		    "Title":"This is title2 from json",
		    "Message":"This is message2",
		     "Time":"6.00PM"
				
		  }
	

	
	}
var content=JSON.parse(data);


//alert(content);

function parse(data)
{
	
//call json here//////

//parse function

heading = data["1"]["Head"];
title=data["1"]["Title"];
message=data["1"]["Message"];
time=data["1"]["Time"];

addnews(heading,title,message,time);

}

var count=0;

function addnews(heading,title,message,time)
{   count=count+1;
    
    var h2=document.createElement('h2');
    var h2_txt=document.createTextNode(heading);
    h2.appendChild(h2_txt);
    
    
    var p_title=document.createElement('p');
    p_title.setAttribute('id','title')
    var txt_title=document.createTextNode(title);
    var strong=document.createElement('strong');
    strong.appendChild(txt_title);
    p_title.appendChild(strong);
    
    var p_message=document.createElement('p');
    p_message.setAttribute('id','message');
    var txt_message=document.createTextNode(message);
    p_message.appendChild(txt_message);
    
    
    
    var p_time=document.createElement('p');
    p_time.setAttribute('id','time');
    p_time.setAttribute('class','ui-li-aside');
    var txt_time=document.createTextNode(time);
    var strong_time=document.createElement('strong');
    strong_time.appendChild(txt_time);
    p_time.appendChild(strong_time);
    
    
    var li_a=document.createElement('a');
    li_a.setAttribute('href','#');
    li_a.setAttribute('class','ui-btn ui-btn-icon-right ui-icon-carat-r');
    li_a.appendChild(h2);
    li_a.appendChild(p_title);
    li_a.appendChild(p_message);
    li_a.appendChild(p_time);
    
     //removing last child class from last list during update
    var lichange=document.getElementById('news_list');
    var last_li=lichange.childNodes[lichange.childNodes.length-1];
    last_li.className="";
    
    
    var li=document.createElement('li');
    li.setAttribute('id','news_1');
    li.setAttribute('class','ui-last-child');
    li.appendChild(li_a);
    
    var ul=document.getElementById('news_list');
    ul.appendChild(li);
    
    //update the news counter
    
    var counter=document.getElementById('count');
    counter.innerHTML= count.toString();
    
}
