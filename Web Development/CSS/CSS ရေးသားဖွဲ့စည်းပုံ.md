##### What is CSS Rule

CSS ကို ‌ရေးသားရာမှာ Rule တွေသတ်မှတ်ထားတယ်။
အပိုင်း ( ၂ ) ပိုင်းပါတယ်။
- ရွေးချယ်မှု [[CSS Selector|Selector]] နဲ့
- ‌ကြော်ငြာချက်သတ်မှတ်ခြင်း Declaration
![[CSS rule.png]]![[CSS rule explanation.png]]
```
color: red;
font-size: 15px;
```

Semi-colon အဆုံးထိကို <mark style="background: #FFB8EBA6;">CSS Rule တစ်ခု</mark>လို့ခေါ်တယ်
Color က Attribute <mark style="background: #FF5582A6;">Property </mark>ဖြစ်ပြီး
red က Attribute <mark style="background: #FF5582A6;">Value</mark> 

Declaration လုပ်တာက တွန့်ကွင်းထဲမှာ Rule တစ်ခုမက ရေးလို့ရတယ်။

##### CSS ရေးသားနည်း သုံးမျိုး

- Inline CSS
- Internal CSS
- External CSS

###### Inline CSS

HTML Element အထဲမှာ Attribute "style" ဆိုတာကို  သုံးပြီး CSS rule တွေ ရေးထည့်လိုက်တာ။

syntax:< style = " property1: value1 ; propery2: value2.... ">

```
< h1 style= "background-color: cyan; border-bottom: 1px solid blue "

```

Attribute Style ထဲမှာမှ property ရယ်၊ value ရယ်ထည့်ရေးတာ။ Rule နှစ်ခု နဲ့ အထက်ပါမယ္ဆိုရင် တစ်ခုနဲ့ တစ်ခုကြားမှာ "semi colon ; " ခြားရမယ်

<mark style="background: #FF5582A6;">Important Note : </mark> Real World Project တွေမှာ Inline Style CSS သုံးတာကို တတ်နိုင်သလောက် <span style="color:rgb(255, 0, 0)">ရှောင်ကြဥ်ကြတယ်</span> ။ အရမ်း **လိုအပ်** မှသုံးတယ်။ ဘာလို့ဆို သူက Internal & External CSS တွေအပေါ််အုပ်ပြီး Override လုပ်သလိုဖြစ်သွားတယ်။ ပြီးတော့ element အတွင်းထဲမှာ လိုက်ရေးရတာ ဖြစ်ပြီး ပြင်မယ်ဆိုလည်း တစ်ခုချင်းဆီ လိုက်ပြင်နေရမှာ။ 

ဒါပေမယ့် <span style="color:rgb(0, 176, 240)">ခေတ်ပေါ် React မှာတော</span>့<span style="color:rgb(0, 176, 240)"></span> အသုံးများတယ်။။

###### Internal Style CSS

HTML < head > element tag အတွင်းမှာ < style > element ခံပြီး ရေးတာကိုပြောတာ‌

ရေးထုံးက < style > < /style > ထဲမှာ သတ်မှတ်ချက်အတိုင်း selector ရယ်၊ declaration ရယ်နဲ့ ရေးပေးရင်ရပြီ။ 
![[Internal CSS.png]]

###### External Style CSS

အသုံးအများဆုံးရေးနည်းဖြစ်တယ်။ 
external ဆိုတဲ့ အတိုင်း CSSကို <span style="color:rgb(255, 255, 0)">သီးသန့် file တစ်ခုဆောက်ပြီး</span> ရေးမှာဖြစ်တယ်။

ချိတ်ဆက်တဲ့အချိန်မှာကျတော့ < head > element ထဲမှာ < <span style="color:rgb(0, 112, 192)">link</span>  / > ကိုသုံးပြီး ချိတ်ရတယ်။
```
< link rel="stylesheet" href="path / .css" type="text/css" />
```

Attribute property " <span style="color:rgb(255, 255, 0)">rel</span> " က Html နဲ့ ချိတ်ဆက်မယ့် file က <span style="color:rgb(112, 48, 160)">ဘယ်လို relationship ရှိ</span>တယ်ဆိုတာ သတ်မှတ်ပေးတာ။ value "<span style="color:rgb(255, 255, 0)"> stylesheet</span> " နဲ့ relative ဖြစ်တယ်ပေါ့။

Attribute property "<span style="color:rgb(255, 255, 0)"> href</span> " ‌ကတော့ ဖိုင်ရဲ့ တည်နေရာ / URL / Path လမ်းကြောင်းကို သတ်မှတ်ပေးတာ

Attribute property " <span style="color:rgb(255, 255, 0)">type</span> " က ချိတ်မယ့် ဖိုင် အမျိုးအစားကို သတ်မှတ်ပေးတာ။ Value " <span style="color:rgb(255, 255, 0)">text/css </span>" ဆိုတာက CSS text ဖိုင်အမျိုးအစားလို့ပြောတာ
![[linking external CSS.png]]

vsCode မှာဆိုရင် အတိုကောက် Emmet Abbreviation <mark style="background: #ABF7F7A6;">link:css</mark> လို့ရိုက်လိုက်တာနဲ့ Auto Link Element တည်ဆောက်ပေးတယ်

##### [[Color in CSS |Color အရောင်များ]]

##### [[CSS Opacity]]

##### [[Fonts in CSS]]

##### [[CSS & Boxes]]

##### [[CSS Overflowing Content]]

##### [[CSS Borders]]





