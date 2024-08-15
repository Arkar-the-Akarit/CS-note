
syntax: <span style="color:rgb(0, 176, 240)">element</span><span style="color:rgb(220, 20, 60)">[</span> <span style="color:rgb(0, 128, 128)">attriubte</span> <mark style="background: #FFB86CA6;">=</mark> "<span style="color:rgb(0, 128, 128)">value</span>" <span style="color:rgb(220, 20, 60)">]</span> 

<span style="color:rgb(0, 176, 240)">element</span> is <span style="color:rgb(255, 155, 0)">optional</span> 

တိကျတဲ့ attribute ရယ် တိတိကျကျ <span style="color:rgb(255, 155, 0)">တစ်ခုထဲသော</span> value ရှိတဲ့ element ကို ရွေးချယ်တာ

ဒါပေမယ့် သူက အကယ်လို့ value နှစ်ခု၊ သုံးခု ရှိနေမယ့် attribute မျိုး (e.g. class attribute) ဆိုရင် အလုပ်မလုပ်ဘူး။ အကယ်လို့ class ‌attribute မှာ <span style="color:rgb(146, 208, 80)">value တစ်ခုဘဲရှိရင်တော</span>့ အလုပ်လုပ်တယ်။ ဒါပေမယ့် class က [[Class Selector]] သုံးတာဘဲ ကောင်းပါတယ်။
```
html:

<input type="text" name="username" />
<input type="password" name="password" />
<input type="date" naem="dob" />
<input type="email" name="email" />
<input type="text" name="shortNote" />
```

```
CSS:

input[type="text"] {
	padding: 10px;
	border-radius: 10px solid #dfdfdf;
}

```

<mark style="background: #FFB86CA6;">attribute type</mark> ရဲ့ <mark style="background: #FFB86CA6;">value text</mark> ရှိနေတဲ့ <mark style="background: #FFB86CA6;">input element </mark>တွေကို select လုပ်တာ