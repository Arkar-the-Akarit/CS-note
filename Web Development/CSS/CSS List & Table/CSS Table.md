[[Table in HTML]]
မှာဆိုရင် table ဆောက်ဖို့ table element ထဲမှာ header အတွက် < th > , row အတွက် < tr >, column cell data တွေ အတွက် < td >, စတာတွေအပြင်  < thead > , < tbody >, < tfoot > စတဲ့ element တွေသုံးတာကို သိပြီ

##### Border-collapse Property

table element ထဲမှာ border attribute နဲ့ 1 value ပေးလိုက်ရင် border တစ်ခုရတယ်ဆိုပေမယ့် အဲ့ border က table element အတွက်ရော cell တစ်ကွက်စီ အတွက်ရောနဲ့ နှစ်ထပ်ဖြစ်နေတယ်။

css ကနေ table ကို border တပ်တဲ့ property ကလည်း [[CSS Borders]] ပါဘဲ။ table element or ထားချင်တဲ့ td, th element ကိုခေါ်ပြိး တပ်ရုံပါဘဲ။
```
table {
	min-width: 500px; /* setting min-width */
}

table, td, th {
	border: 1px solid #aaaaa;
}

```

![[table border.png]]
ဒီလို နှစ်ထပ်ရမယ်။

ဒါဆိုရင် ဒီလို border တွေက table နဲ့ cell တွေကြားမှာ spacing ခြားနေတာ မလိုချင်ဘူး။ <mark style="background: #BBFABBA6;">ရိုးရိုး တစ်ထပ် border ဘဲ</mark> လိုချင်တယ်ဆိုရင် spacing မရှိတော့ဘဲ ကပ်သွားအောင် :

property: <span style="color:rgb(255, 155, 0)">border-collapse</span>
value: <mark style="background: #FFF3A3A6;">collapse</mark> (ကပ်ဖို့)............ on <span style="color:rgb(0, 176, 240)">table</span> element
![[border-collapsecollapse.png]]

value: <mark style="background: #FFF3A3A6;">separate</mark> (default value, ခွာဖု့ိ)


##### Border-spacing property

အခုကျတော့ အဲ့လို spacing ခြားနေတာလေးကိုမှ ကြားထဲက space ကို ကိုယ်လိုချင်သလို ချိန်ညှိမယ်ဆိုရင် border-collapse: separate (<span style="color:rgb(255, 155, 0)">default value</span> မလို့ <span style="color:rgb(146, 208, 80)">မထည့်လည်းရ</span> ) နဲ့

property: <span style="color:rgb(255, 155, 0)">border-spacing</span>
value: "<span style="color:rgb(255, 155, 0)">for horizontal spacing</span>" "<span style="color:rgb(255, 155, 0)">for vertical spacing</span>"

![[border-spacing.png]]

ပထမ value က အလျားလိုက် (horizontal) အကွာအဝေး
ဒုတိယ value က ဒေါင်လိုက် ( vertical ) အကွာအဝေး


##### Pseudo Class { nth-child(even/odd) }

[[CSS Selector#Pseudo Class|Pseudo Class]] တစ်ခုဖြစ်တဲ့ <span style="color:rgb(255, 155, 0)">nth-child</span> ကိုသုံးပြီးတော့ စုံကိန်းမြောက် row တွေကို အရောင်ခြယ်တာမျိုး၊ မ ကိန်း‌မြောက် row တွေကို color ခြယ်တာမျိုး လုပ်လို့ရတယ်။

syntax: 

table element, row ကိုထားမှာ ဖြစ်လို့ tr, full colon (:) nth-child (even/odd) 

```
table tr:nth-child(even/odd
)

```

![[nth-child pseudo class.png]]



