
syntax: <span style="color:rgb(0, 176, 240)">element</span><span style="color:rgb(220, 20, 60)">[</span> <span style="color:rgb(0, 128, 128)">attribute</span> <mark style="background: #FFB86CA6;">~=</mark> "<span style="color:rgb(0, 128, 128)">value</span>" <span style="color:rgb(220, 20, 60)">]</span> 

 <span style="color:rgb(255, 105, 180)">value နှစ်ခု သုံးခု နဲ့ အထက်ရှိနေတဲ့</span> / တိကျစရာမလိုဘဲ <span style="color:rgb(255, 105, 180)">ကြားထဲက space တွေကိုပါ ခွင်ပြု</span>ပြီး attribute Name ရယ်, attribute value ရယ်ရှိတဲ့ element တွေကို select လုပ်တာ။ 

 ဥပမာ: value ၃ ခုရှိတဲ့ class attribute ဆိုပါတော့ <mark style="background: #FFF3A3A6;">class~= ဒုတိယနေရာ value</mark> ဆိုပြီး select လုပ်လည်းရတယ်။

```
<ul>
	<li class="red green"> Apple </li>
	<li class="green red"> Watermelon </li>
	<li class="blue red darkblue"> Blueberry </li>
	<li tomato="yellow green red"> Tomato </li>
</ul>
```

```
CSS:
li[class ~= red] {
	background-color: red;
}
```

ဒီမှာဆို li element ရဲ့ attribute "class" ရဲ့ value ‌'red' က ရှေ့ဆုံးမှာရော, အခြား value တွေကြားရော, ‌နောက်ဆုံးရော ရောက်နေပေမယ့် အကုန်လုံး‌အပေါ် CSS rule သက်ရောက်တယ်