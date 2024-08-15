
[[Child Selector]] လိုမျိုး Parent element အောက်က child element သီးသန့် အပေါ်ဘဲ သက်‌ရောက်တာ မဟုတ်ဘဲ၊ 
Descendant Selector က သူ့အောက်ထဲကနေ <span style="color:rgb(0, 176, 240)">‌ရွေးချယ်လိုက်တဲ့ element</span> က <span style="color:rgb(255, 255, 0)">child ဖြစ်ဖြစ်/ Grandchild ဖြစ်ဖြစ်</span> သက်‌ရောက်မှုရှိတယ်

Syntax: <span style="color:rgb(255, 255, 0)">Parent Element</span>  <mark style="background: #FF5582A6;">(space)</mark>  <span style="color:rgb(0, 176, 240)">Descendant Element</span>

space မခြားရင် descendant က element မဟုတ်ဘဲ Class ဖြစ်နေတဲ့ အခါ [[Class Selector]] ဖြစ်သွားလိမ့်မယ်

```
<body>
    <div>
        <span>Span within Div</span>
        <p>Next Paragraph <span>Next Span</span></p>
    </div>
    <p>
        Paragraph
        <span class="red">Red Span</span>
        <br />
        <span>
        <a class=red href="#">Link</a>
        </span>
    </p>
</body>

CSS:
div span {
    colro: green;
}

p .red {
    color: red;
}

```
ပထမဆုံး div span မှာဆိုရင် သူက div element အောက်က span ‌element အားလုံးအပေါသက်ရောက်တယ်။ p element ထဲက ရှိနေတဲ့ Span element ‌အပေါ်ကို ပါသက်ရောက်တယ်။

ဒုတိယ p .red မှာဆိုရင် သူက p element အောက်က class value "red" ရှိသမျှကို Select လုပ်ဖို့ပြောတဲ့ သဘော။<span style="color:rgb(192, 0, 0)"> space မခြားရင်</span> class name "red " ရှိတဲ့ p element ကိုရွေးသလို ဖြစ်သွားမယ်။ သတိပြုပါ။