
syntax: <span style="color:rgb(0, 176, 240)">element</span><span style="color:rgb(220, 20, 60)">[</span> <span style="color:rgb(0, 128, 128)">attribute</span> <mark style="background: #FFF3A3A6;">^=</mark> <span style="color:rgb(0, 128, 128)">value</span> <span style="color:rgb(220, 20, 60)">]</span> 

<span style="color:rgb(0, 176, 240)">element</span> is <span style="color:rgb(255, 155, 0)">optional</span>


selector ထဲမှာ သတ်မှတ်ပေးလိုက်တဲ့ <mark style="background: #FFB86CA6;">attribute</mark> ရဲ့  <mark style="background: #BBFABBA6;">value စာသားနဲ့ </mark> <mark style="background: #FFB8EBA6;">"စ"</mark> တဲ့ element များကို select လုပ်ခြင်း

[[Suffix - attribute selector|Suffix]] နဲ့ပြောင်းပြန်

```
<div class="top-right-border">....</div>
<div class="top-left-border">....</div>
<div class="top-right-border">....</div>

<p class="topX">...</p>

```

```
CSS:

[class ^= "top"]{
	background-color: red;
}

```

ဒီမှာဆို attribute "class" ကိုမှ "top" နဲ့ <mark style="background: #D2B3FFA6;">စ</mark> တဲ့ value ရှိသမျှ element အကုန် (in this code: div & p) ကိုရွေးတာ