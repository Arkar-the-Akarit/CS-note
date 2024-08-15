
syntax: <span style="color:rgb(0, 176, 240)">element</span><span style="color:rgb(220, 20, 60)"> [</span><span style="color:rgb(0, 128, 128)">attribute</span><span style="color:rgb(220, 20, 60)">]</span>

<span style="color:rgb(0, 176, 240)">element</span> is <span style="color:rgb(255, 155, 0)">optional</span> 

ဒီ <span style="color:rgb(0, 128, 128)">attribute name</span> ရှိတဲ့ <span style="color:rgb(0, 176, 240)">element</span> တွေကို <span style="color:rgb(255, 155, 0)">select</span> လုပ်ပေးပါပေါ့

```
html:
<a href="www.facebook.com">Facebook</a>
<a href="www.youtube.com">Youtube</a>

<a href="#" target="_blank"> New tab </a>
<a href="tiktok.com" target="_self">Tik Tok</a>
```

```
css: 
a[target]{
    background-color: aqua;
}

```

ဒါဆိုရင် target attribute ရှိတဲ့ a element ‌တွေအပေါ်ဘဲ rule apply လုပ်တယ်။