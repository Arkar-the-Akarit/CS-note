
element box တွေမှာ shadow အရိပ်ထည့်ဖို့သုံးတယ်

property: box-shadow
value: "<mark style="background: #FFF3A3A6;">X-offset</mark>" "<mark style="background: #FFF3A3A6;">Y-offset</mark>" "<mark style="background: #FFF3A3A6;">Blur Distance</mark>" "<mark style="background: #FFF3A3A6;">Spread Shadow (အပေါ်၊ အောက်၊ ဘယ်၊ ညာ အရိပ်ချဲ့ကားမှု)</mark>" "<mark style="background: #FFF3A3A6;">Color</mark>"

value <span style="color:rgb(0, 176, 240)">5 ခုလုံး ထည့်</span>ပေးရမယ်။

- x-offset: <span style="color:rgb(255, 155, 0)">positive</span> value ထည့်ရင် အရိပ်က <span style="color:rgb(255, 155, 0)">ညာဘက်</span>၊ <span style="color:rgb(0, 255, 255)">negative </span>value ထည့်ရင် အရိပ်က <span style="color:rgb(0, 255, 255)">အောက်ဘက်</span>

- y-offset: <span style="color:rgb(255, 155, 0)">positive</span> value ထည့်ရင် အရိပ်က <span style="color:rgb(255, 155, 0)">‌အောက်ဘက်</span>‌ ရွေ့၊ <span style="color:rgb(0, 255, 255)">negative value</span> ထည့်ရင် <span style="color:rgb(0, 255, 255)">အပေါ်</span>တက်

- blur distance: <span style="color:rgb(0, 255, 255)">မှုန်ဝါးမှုပမာဏ</span>ကို သတ်မှတ်ပေးတာ၊ 0px ဘဲထည့်ထားရင် အရိပ်မပါဘဲ solid လိုင်းကြီးဘဲ မြင်ရမယ်။

- spread shadow: အရိပ်ရဲ့ <span style="color:rgb(0, 255, 255)">အရွယ်အစားကို တိုး</span>ချင်ရင် သုံး၊ အရပ် (၄) မျက်နှာစလုံးကို ထည့်လိုက်တဲ့ ပမာဏအရ တိုးချဲ့ပေးမှာ

- color: အရိပ်ရဲ့ အရောင်

shadow ထည့်ရင် မြင်ရမှာက box အ‌ေနာက်တည့်တည့်မှာ shadow ကြီးရှိနေတယ်။ <mark style="background: #ADCCFFA6;">x</mark> positive ဆိုရင် အဲ့ shadow ကြီးက ညာဘက်ရွေ့ ၊ negative ဆိုရင် ဘယ်ဘက်ရွေ့ ၊ 
<mark style="background: #BBFABBA6;">y</mark> positive ဆိုရင် အောက်ကိုရွေ့၊ negative ဆိုရင် အပေါ််ကိုတက််ကိုတက်

![[box_shadow_values.png]]

##### Shadow Box Examples

###### Box 1

	![[shadow box 1.png]]
```
box-shadow: 5px 5px 0px #333;
```

x-offset: 5px, y-offset: 5px, blur: 5px ထားထားတဲ့ အတွက် အရိပ်က ညာဘက်နဲ့ အောက်ဘက်ကို ထွက်ပြီး blur နှုန်း 5px စာသတ်မှတ်

###### Box 2

	![[box-2.png]]
```
box-shadow: 15px 5px 5px 0px #333;
```

x-offset value ကို 15px ထားထားတဲ့ အတွက် ညာဘက်ကို ပိုထွက်

###### Box 3

	![[box-3.png]]
```
box-shadow: 5px 15px 5px 0px #333;
```

y-offset ကို 15px ‌ထားလိုက်လို့ အရိပ်က အောက်ကို ပိုကျ

###### Box-4

	![[box-r.png]]
```
box-shadow: 0px 0px 10px 0px #333;
```

x-offset & y-offset ရော 0 ထားထားတယ်။ blur ကို 10px ပေးထားတဲ့အတွက် အရိပ်က ဘယ်ဘက်ကိုမှ မသွားတော့ဘဲ <span style="color:rgb(0, 255, 255)">အလယ်မှာဘဲ</span> ရှိတယ်။ blur မှုန်ဝါးတန်ဖိုးပေးထားတဲ့ အတွက်ကြောင့် ပတ်ပတ်လည်မှာ အရိပ်မှုန်ဝါးမှုသေးသေးလေးတွေ့ရတယ်။

###### Box-5

	![[box-5.png]]
```
box-shadow: 0px 0px 0px 5px #333;
```

horizontal ရော, vertical ရော, blur ဖြစ်တာရော မပါဘဲ <span style="color:rgb(0, 255, 255)">spread shadow
</span> ကိုဘဲ 5px ပေးထားတဲ့အတွက် အရိပ်ရဲ့ <span style="color:rgb(0, 128, 128)">size က 5px စာ ပိုကြီး</span>နေပြီး <span style="color:rgb(0, 128, 128)">blur radius လည်းမပါ</span>တဲ့အတွက် solid style နဲ့ မဲမဲကြီးဘဲ မြင်နေရ

Box-6

	![[box-6.png]]
```
box-shadow: 0px 0px 5px 5px #333;
```

spread shadow ကို 5px ပေးလိုက်တဲ့အတွက် အရိပ်က လေးမျက်နှာကို ပြန့်နေပြီး box-5 နဲ့ မတူတာက blur-radius တန်ဖိုးပါ ထည့်ထားတဲ့အတွက် မည်းမည်းကြီးဘဲဖြစ်မနေဘဲ blur style နဲ့ spread ထွက်နေတာကို ဝါးပေးထားသလို မြင်ရ

###### Box-7

	![[box-7.png]]
```
box-shadow: 5px 0px 5px 5px #333;
```

x-offset value ဘဲပါပြီး y-offset value မပါတဲ့ အတွက် အရိပ်က ညာဘက်ကိုဘဲ ထွက်နေတယ်။

###### Box-8

	![[box-8.png]]
```
box-shadow: 5px 5px 5px 5px #333;
```

box-7 က အတိုင်းကိုမှ y-offset value ထည့်လိုက်တဲ့အတွက် <span style="color:rgb(0, 255, 255)">အရိပ်က အောက်ဘက်ကို</span> 5px <span style="color:rgb(0, 255, 255)">ရွေ့သွား</span>ပါတယ်။

##### Multiple Shadow ထည့်နည်း

	![[multiple_shadow.png]]
```
box-shadow: 5px 5px 0px 0px red,
			10px 10px 0px 0px green,
			15px 15px 0px 0px blue;
```

အရိပ်တွေ တစ်ခုထပ်ပိုပြီးထည့်ရေးလို့လည်းရတယ်
သတိထားရမှာက value အများကြီးရေးရင် <span style="color:rgb(0, 255, 255)">နောက်ဆုံးတစ်ခု မရောက်ခင်အထိ</span> <mark style="background: #ABF7F7A6;">coma ( , )</mark> ခံ‌ရေးပြီး <span style="color:rgb(255, 105, 180)">နောက်ဆုံးတစ်ခုကျမှ</span> <mark style="background: #ADCCFFA6;">semi-colon ( ; )</mark> နဲ့ ပိတ်တယ်။

![[multi-shadow explanation.png]]

###### Multi-shadow box 2

	![[multi-shadow box 2.png]]
```
box-shadow: -5px -5px 0px 0px red;
			-10px -10px 0px 0px green;
			-15px -15px 0px 0px blue;
```

x-offset & y-offset တွေမှာ negative value တွေသုံးတဲ့အတွက် အရိပ်က ဘယ်ဘက် နဲ့ အပေါ်ဘက်ကို ထွက်နေတာပါ။

###### Multi-shadow box 3

	![[multi-shadow box 3.png]]
```
box-shadow: -5px -5px 4px 0px red;
			5px 5px 4px 0px green;
```

အနီအတွက် ဘယ်ဘက်နဲ့ အပေါ်ကိုထွက်နေတာကြောင့် negative value ပေးထားတာဖြစ်တယ်။ 
အစိမ်းက positive value မလို့ ညာဘက်နဲ့ အောက်ဘက်
blur 4px ဖြစ်လို့ မှုန်မှုန်လေးဖြစ်နေမယ်။

###### Multi-shadow box 4

	![[box-4.png]]
box-3 နဲ့ တူတူဘဲ. သူက radius ကို 50% နဲ့ ကွေးထားတာ၊ [[CSS Border Radius#Percentage နဲ့ ကွေးမယ်|border ကို စက်ဝိုင်းလုပ်]]အကြောင်းကို ဝင်ကြည့်ပါ။

##### Inset Shadow

အရိပ်က box <span style="color:rgb(0, 176, 240)">အပြင်</span>ကို ထွက်နေတာ <span style="color:rgb(0, 176, 240)">outset</span>
အဲ့အရိပ်ကို box <span style="color:rgb(255, 155, 0)">အတွင်း</span>ထဲကို ဝင်နေတာကို <span style="color:rgb(255, 155, 0)">inset</span> လို့ ခေါ််တယ်

inset ကိုသုံးဖို့ဆိုရင် value ငါးခု အရှေ့မှာ inset ထည့်ပေးရတယ်။
```
box-shadow: inset 5px 0px 0px 4px red;
```

inset မှာဆိုရင်

x-offset: value က positive ဆိုရင် shadow က ညာဘက်ကိုရွေ့၊ negative ဆိုရင် ဘယ်ဘက်ကိုရွေ့

![[inset x positive.png]]

![[inset x negative.png]] 
x-negative

![[inset x value.png]]

##### Inset Shadow Box 1

	![[inset shadow box 1.png]]
```
box-shadow: inset 5px 5px 0px 0px black;
```
x-offset & y-offset 5px ဆီထည့်ထားတဲ့အတွက် အရိပ်က ညာဘက်နဲ့ အောက်ဘက်ကို 5px ရွေ့

###### Inset Shadow Box 2

	![[inset shadow box 2.png]]
```
box-shadow: inset 0px 0px 0px 5px black;
```
spread-shadow value တစ်ခုသာ ပါတဲ့ အတွက် အရိပ်က အရပ်လေးမျက်နှာ အတွင်းကို ပြန့်

Inset Shadow Box 3

	![[inset shadow box 3.png]]
```
box-shadow: inset 3px 3px 10px 2px black;
```

blur 10px ကြောင့် မှုန်ဝါးမှုတက်တယ်။ spread-shadow ကြောင့် အရိပ်ပြန့်ကားမှု ပါပြီး အောက်ဘက်နဲ့ ညာဘက်မှာ အရိပ်အနညး်ငယ်ကို တွေ့နိုင်တယ်။

###### Outset & Inset Box

	![[outset & inset box.png]]
```
box-shadow: inset 2px 2px 4px 0px #fffff,
			inset -2px -2px 8px 0px #c3c3c3,
			-3px -3px 4px 0px #ffffff,
			2px 3px 10px 0px #cacaca;
```

ပထမလိုင်းက အတွင်း အပေါ်နဲ့ အတွင်းဘယ်ဘက်မှာ အရိပ်ပေါ်
ဒုတိယလိုင်းက အတွင်း အောက်နဲ့ ညာဘက်မှာ အရိပ်ပေါ်
တတိယလိုင်းက အပြင် အပေါ်နဲ့ ဘယ်ဘက်
စတုတ္ထလိုင်းက ‌အပြင် အောက်ဘက်နဲ ညာဘက်

inset & outset ကိုသုံးပြီး ဒီလို 3D design မျိုးရေးလို့ရတယ်ဆိုတာ