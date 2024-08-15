
ဘေးချင်းကပ် selected element တစ်ခုထဲကို မဟုတ်ဘဲ၊ ဘေးမှာရှိသမျှ selected element အားလုံးအပေါ် သက်ရောက်တယ်

 Syntax: <span style="color:rgb(255, 255, 0)">First Element </span> <mark style="background: #FF5582A6;">~</mark> <span style="color:rgb(0, 176, 240)">ဘေးချင်းကပ် Element</span> 

```
<body> 
	<div>
		<h1> Heading 1 </h1>
		<h2> Heading 2 </h2>
		<h2> Second Heading 2 </h2>
	</div>

	<div>
		<h3> Heading 3 </h3>
		<p> First Paragraph </p>
		<p> Second Paragarph </p>
	</div>

CSS: 
	h1 ~ h2 {
		background: red
	}

	h3 ~ p {
		background: blue;
	}


```

h1 ~ h2 မှာဆိုရင် h1 နောက်က h2 element <span style="color:rgb(255, 255, 0)">နှစ်ခုစလုံးအပေါ်</span>သက်ရောက်တယ်။
the same goes for " h3 ~ p "
ဘေးမှာ <span style="color:rgb(255, 255, 0)">သုံးခု၊ လေးခု၊ n ခု ရှိသလောက်</span>အပေါ်သက်ရောက်တယ်