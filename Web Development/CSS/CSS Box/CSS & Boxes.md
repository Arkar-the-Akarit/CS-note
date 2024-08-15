
[[HTML Element Box]] ကို မြင်သာအောင် CSS rule တွေ သတ်မှတ်ပြီး စမ်းကြည့်မယ်။

```
html:
<h1> h1 </h1>
<p> 
	Paragraph
	<a href="#"> Link </a>
</p>

<ul>
	<li> li-1 </li>
	<li> li-2 </li>
	<li> li-3 </li>
</ul>

```

###### Style - One

```
* {
 
border: 1px solid #999999;
margin: 0px;
padding: 0px;
border-radius: 3px;
 
}
```

![[html_box_style_one.png]]
သေချာကြည့်ကြည့်ရင် body အတွက်ပါ border ပါတယ်။

<span style="color:rgb(220, 20, 60)">margin</span> ရော, <span style="color:rgb(0, 176, 240)">padding</span> ရော <mark style="background: #FFF3A3A6;">0px</mark> ဆီပေးခဲ့တဲ့အတွက် အားလုံးက <span style="color:rgb(255, 155, 0)">border မျဥ်းနဲ့ ကပ်</span>နေတယ်။

###### Style - Two

```
* {
	 border: 1px solid #999999;
	 margin: 20px;
	 padding: 0px;
	 border-radius: 3px; 
}

```
![[html_box_style_two.png]]

<span style="color:rgb(220, 20, 60)">margin</span> ကို <mark style="background: #FFF3A3A6;">20px</mark> ထားလိုက်တယ်။ ဒီတော့ element <span style="color:rgb(255, 155, 0)">တစ်ခုရဲ့ border line နဲ့ အခြားတစ်ခုကြား</span>က border တွေက 20px ဆီခြားသွားပြီ။<span style="color:rgb(0, 176, 240)"> padding</span> က <mark style="background: #FFF3A3A6;">0px</mark> ဘဲဖြစ်နေတဲ့အတွက် content နဲ့ border line တွေက တော့ ကပ်နေတုန်းဘဲ။ 

###### Style - Three

```
* {
	border: 1px solid #999999;
	margin: 0px;
	padding: 20px;
	border-radius: 3px;
}
```

![[html_element_box_style_theree.png | 500]]

<span style="color:rgb(0, 176, 240)">padding</span> ကို <mark style="background: #FFF3A3A6;">20px</mark> ထားလိုက်တယ်။ ဒီတော့ <span style="color:rgb(255, 155, 0)">element ထဲက <u>content</u> ‌နဲ့ အဲ့ element ရဲ့ border line ကြား</span> 20px ခြားသွားပြီ။ <span style="color:rgb(220, 20, 60)">margin</span> ကို <mark style="background: #FFF3A3A6;">0px</mark> ထားခဲ့တဲ့အတွက် <span style="color:rgb(146, 208, 80)">element တစ်ခုနဲ့ အခြား element ရဲ့ border line ကြားမှာ</span>တော့ <span style="color:rgb(220, 20, 60)">အကွာအဝေးမရှိ</span>ဘဲ ကပ်နေမယ်။

###### Style - Four

```
* {

 border: 1px solid #999999;
 margin: 20px;
 padding: 20px;
 border-radius: 3px;
}
```

![[html_element_box_four.png]]
element တစ်ခုနဲ့ တစ်ခုရဲ့ border ကြား အကွာအဝေးကို သတ်မှတ်တဲ့ margin ရော, element border နဲ့ content ကြားက အကွာအဝေးကို သတ်မှတ်တဲ့ padding ရော 20px ဆီထားလိုက်တဲ့အတွက် ပုံထဲကလို ခြားပါတယ်။

###### Box တွေရဲ့ width အကျယ် သတ်မှတ်တာကို [[Width of HTML box in CSS]] မှာ ကြည့်ပါ။ 

##### [[CSS Margin]] အကြောင်းကို ဒီမှာကြည့်ပါ။

[[CSS Padding]] အကြောင်းကို ဒီမှာကြည့်ပါ။


