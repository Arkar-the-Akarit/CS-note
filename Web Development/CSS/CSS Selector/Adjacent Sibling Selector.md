

Next Sibling ဘေးချင်းကပ် အမျိုးတော်တဲ့ Element တစ်ခုကိုဘဲ Select လုပ်တာမျိုး

 Syntax: <span style="color:rgb(255, 255, 0)">First Element </span> <mark style="background: #FF5582A6;">+</mark> <span style="color:rgb(0, 176, 240)">ဘေးချင်းကပ် Sibling Element</span> 

```
h1 + h2 {

}
```

h1 element ဘေးမှာရှိနေတဲ့ h2 element ကို select လုပ်တာ။ အခြား element များမပါပါ

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
	h1 + h2 {
		background: red
	}

	h3 + p {
		background: blue;
	}

```

အပေါ်က ကုဒ်မှာဆိုရင် h1 + h2 မှာ web မှာ red background ဖြစ်နေမှာက heading 2 ဆိုတာကဘဲ ဖြစ်မယ်။ Another Heading 2 ဆိုတာက ရိုးရိုးဘဲ

အောက်က h3 + p မှာဆိုရင်လည်း first paragraph ရဲ့ background color ဘဲပြောင်းမယ်။ second paragraph က ဒီတိုင်းဘဲ

Adjacent Sibling Selector ဆိုတာ ဒါဘဲ။ <span style="color:rgb(0, 176, 240)">သူ့ဘေးချင်းကပ်</span> <span style="color:rgb(255, 255, 0)">element တစ်ခုထဲကိုသာ</span> ရွေးချယ်တာ

ဘေးချင်းကပ်က နာမည်တူ element <span style="color:rgb(255, 255, 0)">အကုန်လုံးကိုရွေးတာ</span>ကို [[General Sibling Selector]] လို့ခေါ်တယ်။