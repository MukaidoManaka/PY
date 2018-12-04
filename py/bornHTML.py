import webbrowser
#命名生成的html
HTML = "test.html" 
#打开文件，准备写入
f = open(HTML,'w')
 
#准备相关变量
str1 = 'Aki'
str2 = 'desu'
 
message = """
<html>
	<head>
	<meta charset="UTF-8" />
	<title>Document</title>
	<style>
 
	h1{{
		text-align: center;
	}}
	body{{
		background: #eeedef;
	}}
	img{{
		padding:10px 10px  15px 10px ;
		background: #fff;
		border:1px solid #ddd;
		position:absolute;
		transition:1000ms;
		max-width:800px;
	}}
	.pic1{{
		transform:rotate(20deg);
		 top:50px;
        left:200px;
	}}
	.pic2{{
		transform:rotate(40deg);
		 top:150px;
        left:100px;
	}}
	.pic3{{
		transform:rotate(30deg);
		 top:50px;
        left:130px;
	}}
	.pic4{{
		transform:rotate(-20deg);
		 top:70px;
        left:300px;
	}}
	.pic5{{
		transform:rotate(70deg);
		 top:210px;
        left:400px;
        z-index: 45;
	}}
	.pic6{{
		transform:rotate(10deg);
		 top:170px;
        left:580px;
        z-index: 50;
	}}
	.pic7{{
		transform:rotate(-60deg);
		 top:590px;
        left:400px;
        z-index: 240;
	}}
	.pic8{{
		transform:rotate(20deg);
		 top:50px;
        left:400px;
        z-index: 120;
	}}
	.pic9{{
		transform:rotate(70deg);
		 top:420px;
        left:500px;
	}}
	.pic10{{
		transform:rotate(45deg);
		 top:120px;
        left:600px;
        z-index:300;
	}}
	img:hover{{
		transform:rotate(0deg);
		transform:scale(1.8);
		box-shadow: 10px 10px 15px #ccc;
        z-index: 900;
	}}
	#container{{
		width:80%;
		height:600px;
		margin:50px auto;
        position:relative;
		}}
		
		</style>
	</head>
	<body>
	<h1>{0} {1}!</h1>
	<div id="container">
	  <img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1543918720344&di=ac80d54f1081c3476eda243d99a3227b&imgtype=0&src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fq_70%2Cc_zoom%2Cw_640%2Fimages%2F20180728%2F689d3e65fcf64aaebb870c229aa52365.jpg" alt="" class="pic1" />
	  <img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1543918762851&di=b056515c7e43a2823ad5cd8b4d3c080c&imgtype=0&src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20171030%2F2da1aaee77b8471aaf2307489cc09f53.jpeg" alt="" class="pic2" />
	  <img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1543918825410&di=a191a7ac40b33df29c9c0d89bd69a2bb&imgtype=0&src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20170904%2Fc4c3c85cf7074336a942ad06747841a2.jpeg" alt="" class="pic3" />
	  <img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1543918842946&di=af1ddfe2c81c4cdbb9eb90bad528d780&imgtype=0&src=http%3A%2F%2Fi2.hdslb.com%2Fbfs%2Fface%2F375755d90f7a9b77718b5da0f3f57f845c5d6f11.jpg" alt="" class="pic4" />
	  <img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1543918878172&di=b181e83ef5dcd8159009be81a03f291c&imgtype=0&src=http%3A%2F%2Fob7zbqpa6.qnssl.com%2Fnfd8wb3k5fumy8akixw16xmokrosf62w.jpg" alt="" class="pic5" />
	  <img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1543918924605&di=9646f4befb3922fef7a6ecb2e95e40b4&imgtype=0&src=http%3A%2F%2Fi0.hdslb.com%2Fbfs%2Farticle%2F090361f42aa12c28270aae6bf0f413ffc9e8bada.png" alt="" class="pic6" />
	  <img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1543918938721&di=eea63879316fe3e3e9b5786470f7284d&imgtype=0&src=http%3A%2F%2Fss.moemoe.la%2Fimage%2F2018-06-29%2F3c1d5d1b-eea8-4808-9e0b-4ca05d8cc8ad.png" alt="" class="pic7" />
	  <img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1543918956243&di=8af53233cb743fb792883742a3f673de&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201505%2F03%2F20150503004044_UftPe.thumb.700_0.jpeg" alt="" class="pic8" />
	  <img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1543918968804&di=870863b40e054bea5dc4f7f357a2d314&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201601%2F23%2F20160123000540_KBwA3.gif" alt="" class="pic9" />
	  <img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1543918995277&di=e7ae711306eb995bea0a8d4c830af91a&imgtype=0&src=http%3A%2F%2Fimage.jijidown.com%2Fv1%2Fimage%3Fav%3D8513015%26url%3Dhttps%3A%2F%2Fi2.hdslb.com%2Fbfs%2Farchive%2Ff8fd2d84cd5742b227d3c89786d760b7cb2e7cd7.jpg%26sign%3D0BF9AD1417ED400FADB6F4BDF261A86B" alt="" class="pic10" />
	</div>
	</body>
</html>""".format(str1,str2)
 
#写入文件
f.write(message) 
#关闭文件
f.close()
 
#运行完自动在网页中显示
webbrowser.open(HTML,new = 1) 