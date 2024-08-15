
###### What is Selector

```
h1 {
 color: red;
}
```
အပေါ်က code မှာဆိုရင် h1 က selector

selector တွေကို " <mark style="background: #FFB86CA6;">coma ,</mark>" ခံပြီး အများကြီး သတ်မှတ်လို့ရ
```
h1, h2, h3 {
	color: red;
}
```

###### @ At-Rules

Selector <span style="color:rgb(192, 0, 0)">မဟုတ်ပါ</span>။ <mark style="background: #ABF7F7A6;">At-rules</mark> လို့ခေါ်ပြီး သူက <mark style="background: #FF5582A6;">Selector မဟုတ်တဲ့ အခြားRule</mark> တွေကြေညာချင်ရင် "@" ကို သုံးရတယ်။ e.g. @import, @font-face

###### အသုံးများတဲ့ CSS Selector များ

![[element selector.png]]
![[element selector two.png]]

[[Universal Selector]]

[[Type Selector]]

[[ID Selector]]

[[Class Selector]]

[[Child Selector]]

[[Descendant Selector]]

[[Adjacent Sibling Selector]]

[[General Sibling Selector]]


######  Pseudo Class

Pseudo-Classes တွေကို Element တစ်ခုရဲ့ အခြေအနေအမျိုးမျိုးနဲ့ ပတ်သက်ပြီး သုံးတယ်။ Document Tree ထဲမှာ ရှိနေတဲ့ element တည်နေရာ၊ အခြေအနေကို လိုက်ပြီး style rule သတ်မှတ်တာ၊ ဒါမှမဟုတ် HTML Structure မှာ ဘာလုပ်မယ်ဆိုပြီး သတ်မှတ်ပေးထားတာမျိုး မရှိတာတွေ (<span style="color:rgb(255, 155, 0)">user interactions</span>, <span style="color:rgb(146, 208, 80)">browser states</span>, ပြီးတော့ <span style="color:rgb(0, 255, 255)">htmlကို မပြင်ဘဲ CSS ကနေပြီး target & style လုပ်လို့ရ</span>မယ့် ဟာမျိုးတွေ) 

Html structure မှာ ဘာလုပ်မယ်ဆိုပြီး မသတ်မှတ်ထားတာဆိုတာကို ဒီလိုဥပမာပေးမယ်။ < a > element ဟာ link ချိတ်ဖို့သုံးတယ်။ link တွေကို browserက အောက်က <mark style="background: #ADCCFFA6;">underline ရယ်၊ မျဥ်းအပြာရယ်နဲ့</mark> ပြတယ်။ link ကို ဝင်ပြီးသွားရင် အချို့ browser တွေမှာဆို <mark style="background: #D2B3FFA6;">ခရမ်းရောင်ပြောင်း</mark>သွားတယ်။ ဒါဟာ ဒီလို ဖြစ်ရမယ်လို့ Html Structureထဲမှာ ထည့်‌ရေးထားတာလည်း မဟုတ်ဘူး။ Browser က ဝင်ပြီးသား <mark style="background: #FFF3A3A6;">link တွေကို track</mark> လုပ်ပြီး <mark style="background: #FFB8EBA6;">":visited" ဆိုတဲ့ pseudo-class</mark> ကို apply လုပ်ပေးလို့သာဖြစ်သွားတာ။


<span style="color:rgb(0, 128, 128)">တိကျတဲ့ အခြေအနေတစ်ခု</span>မှာ <span style="color:rgb(255, 155, 0)">တစ်ခုခုလုပ်စေချင်</span>တာမျိုး၊ <span style="color:rgb(255, 155, 0)">Style rule သတ်မှတ်</span>တာမျိုး (ဥပမာ: button ခလုတ်ပေါ်ကို mouse တင်လိုက်ရင် အရောင်ပြောင်းသွားတာ၊ input boxမှာ စာရိုက်ထည့်တော့မယ်ဆို colored outline လေးတွေပေါ်တာ၊ link တစ်ခုကို နှိပ်ကြည့်ပြီးသွားရင် အရောင်ပြောင်းသွားတာ )

Conditional အနေနဲ့လည်း သုံးတယ်။ Table Rows တွေမှာ စုံဂဏန်း rows တွေကို အရောင်တစ်ခု သတ်မှတ်တာမျိုး။ [[CSS Table#Pseudo Class { nth-child(even/odd) }]] မှာ ကြည့်ပါ။

Pseudo Classes တွေက အများကြီးရှိတယ်။ အသုံးများတာတွေဘဲ လေ့‌လာထားမယ်။ လိုတာတွေကို document ဖတ်ရင်း၊ လေ့လာပြီး ‌ရေးရမယ်။

syntax ကတော့ <mark style="background: #BBFABBA6;">(:) full colon</mark> နောက်မှာ Pseudo-class name

<span style="color:rgb(0, 176, 240)">===></span> pseudo class နဲ့ ဆက်စပ်ပြီး သူတို့ ပြောင်းလဲသွားတဲ့ transition တွေကို ဘယ်လိုထိန်းချုပ်လဲ [[CSS Transitions|ဒီမှာ]] ကြည့်ပါ။
 
###### [[Hyperlink a ၏ Pseudo-Classes များ]] 

###### [[Action အ‌‌ခြေအနေကို ဖမ်းသော Pseudo-classes]]



<hr>


##### Attribute Selector များ

attribute ဆိုတာ element ထဲမှာပါတဲ့ ဟာလေးတွေ။ 

< input type="text" > မှာဆိုရင် input က element , <span style="color:rgb(0, 176, 240)">type</span> က <span style="color:rgb(0, 176, 240)">attribute</span> , <span style="color:rgb(255, 155, 0)">text</span> က attribute <span style="color:rgb(255, 155, 0)">value</span> 

CSS မှာက  အဲ့ attribute တွေကိုလည်း select လုပ်ပြီး CSS rule သတ်မှတ်ပေးလို့ရတယ်

![[common attribute selector 1.png]]
![[common attribute selector 2.png]]

attribute selector တွေမှာ <span style="color:rgb(0, 128, 128)">element ထည့်တာက</span> <span style="color:rgb(255, 155, 0)">အဲ့</span> <span style="color:rgb(146, 208, 80)">element ကိုဘဲ select လုပ်ချင်မှ</span>ထည့်။ <mark style="background: #ABF7F7A6;"> မထည့်ဘဲ</mark> ဒီ attribute နဲ့ value ရှိသမျှ element အကုန် select လို့ရတယ်။

[[Existence - attribute selector|Existence]]

[[Equality - attribute selector |Equality]]

[[Space - attribute selector|Space]]

[[Prefix - attribute selector |Prefix]]

[[Substring - attribute selector|Substring]]

[[Suffix - attribute selector|Suffix]]



##### Escaping in CSS

pseudo class တွေကို ရေးရင် (:) full colon နောက်မှာမှ နာမည်လိုက်တာ။ ဒီတော့ အကယ်လို့ ကိုယ်က attribute value (mostly for class name) တွေကို (:) full-colon ထည့်ရေးမယ်ဆိုရင် (e.g. lg:col-3) ဆိုတာမျိုးပေးလိုက်ပြီဆိုရင်<span style="color:rgb(0, 176, 240)"> CSS မှာ lg:col-3 လို့ direct သွားရေးရင်</span> pseudo class ကို mention ခေါ်သလိုဖြစ်သွားမယ်။ အလုပ်မလုပ်တော့ဘူး။ 

ဒီတော့ full colon (:) ပါတဲ့ name တွေကို CSS မှာသုံးချင်ရင် သူ့ရှေ့မှာ <span style="color:rgb(255, 155, 0)">back slash ( \ )</span> ထည့်‌ပေးရတယ်။

e.g <mark style="background: #ADCCFFA6;"> .lg\:col-3 </mark> 
