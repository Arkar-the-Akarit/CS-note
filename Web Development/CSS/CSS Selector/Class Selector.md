[[Class Attribute]] ကို Select လုပ်ဖို့သုံးတယ်

Bootstrap, Tailwind CSS တို့မှာဆိုရင် CSS Class Selector ကို <mark style="background: #FFF3A3A6;">များစွာ</mark> အသုံးပြုကြတယ်

ရေးထုံးကတော့ <mark style="background: #FF5582A6;">full stop + Class name</mark> ပါ။ Space <span style="color:rgb(192, 0, 0)">မခြားပါ </span> 

```
.className {
	....
}

p.className {
	...
}


```

.class {} ဆိုရင် Attribute class ရဲ့ value "className" ထားထားသမျှ Elements အားလုံး‌အပေါ် သက်‌‌ရောက်တယ်။

p.className {} ဆိုရင် P element ရဲ့ Attribute Class မှာ value "className" ရှိနေတဲ့ <mark style="background: #FF5582A6;">p element </mark>အားလုံးအပေါ်သက်‌ရောက်တယ်။
```
html:
<body>

    <div class="container border">

        <h1 class="bg-default">Title by Foxy</h1>
        
        <p class="underline">
	        Underline Text in Paragraph
            <span class="text-red">By Foxy</span>
		</p>

        <span class="underline">
            Span Element & Underline Text
            <span class="text-red">By foxy</span>
        </span>
    </div>

    <div class="contianer">
        <p class="bold border">
            <span class="text-red">Bold</span>
            paragarph used bold
            <span class="text-red">By foxy</span>
        </p>
    </div>

CSS:
.container{
    max-width: 400px;
    margin: 0 auto;
    padding: 1rem;
}

.border{
    border: 1px solid #dfdfdf;
    border-radius: 4px;
}

.bg-default{
    background-color: #dfdfdf;
}

.bold{
    font-weight: bold;
}

p.underline{
    text-decoration: underline;
}

.text-red{
    color: red;
}

```

![[class attribute for CSS.png]]