
Element တစ်ခုထဲမှာရှိတဲ့ သူ့ရဲ့ Child element ကို တိုက်ရိုက် Applied လုပ်တာ

syntax: <span style="color:rgb(255, 255, 0)">Parent Element</span>  <mark style="background: #FF5582A6;">></mark> <span style="color:rgb(0, 176, 240)">Child Element</span>

```
<h1> Main Title </h1>

	<ul>
		<li> Coffee </li>
		<li> Tea </li>
	</ul>

	<section>
		<p> Paragraph 1 </p>
		<p> Paragraph 2 </p>

	<div>
		<p> paragarph 3 </p>
	</div>

	</section>

CSS: 

ul > li {
	color: red;
}

section > p {
	background: yellow;
}

```

Output will be like this:
![[child selector test.png]]

ဒီတော့ သူက section > p  ဖြစ်တဲ့အတွက် section element အောက်က <span style="color:rgb(0, 176, 240)">p element အပေါဘဲ </span>သက်‌ရောက်တယ်။ Section ရဲ့ Child element နောက်တစ်ခုဖြစ်တဲ့ Div ရဲ့ child element ( section ရဲ့ grand child) ဖြစ်တဲ့ paragraph 3 အပေါ်သက်‌ရောက်မှု <span style="color:rgb(192, 0, 0)">မရှိဘူ</span>း။

![[child selector Graphical.png]]