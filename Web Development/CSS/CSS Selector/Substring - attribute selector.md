
syntax: <span style="color:rgb(220, 20, 60)">[</span> <span style="color:rgb(0, 128, 128)">attribute</span> <mark style="background: #FFF3A3A6;">*=</mark> <span style="font-style:italic; color:rgb(0, 128, 128)">value</span> <span style="color:rgb(220, 20, 60)">]</span> 

<span style="font-style:italic; color:rgb(0, 176, 240)">element</span> is <span style="color:rgb(255, 155, 0)">optional</span> 

select လုပ်လိုက်တဲ့ attribute မှာ <span style="color:rgb(146, 208, 80)">သတ်မှတ်ပေးလိုက်တဲ့ value စာသား</span> <span style="color:rgb(0, 255, 255)">ပါသမျှ</span> (<span style="color:rgb(255, 105, 180)">အရှေ့မှာပါပါ</span>၊ <span style="color:rgb(255, 105, 180)">အလယ်မှာပါပါ</span>၊ <span style="color:rgb(255, 105, 180)">နောက်ဆုံးမှာပါပါ</span>) element တွေကို select လုပ်

```
<div class="topper">...</div>

<p class="top-on-star>...</p>

<div class="bottom-top>...</div>

<p class="stopper">...</p>

```

```
CSS:

[ class *= "top" ] {
	border-radius: 10px solid blue;
}
```

ဒီမှာဆို "top" စာသားပါတဲ့ value ရှိတဲ့ class attribute တွေကို select လုပ်တာဘဲ၊ <span style="color:rgb(0, 176, 240)">stopper</span> ဆိုပြီး top ပါတာလည်း select ဘဲ