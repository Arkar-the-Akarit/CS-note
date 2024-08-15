
<mark style="background: #FFF3A3A6;">:hover</mark>, <mark style="background: #FFF3A3A6;">:active</mark>, <mark style="background: #FFF3A3A6;">:focus</mark> 

<hr>

<mark style="background: #FFF3A3A6;">:hover</mark> : user ရဲ့ Mouse Cursor ‌က <mark style="background: #ABF7F7A6;">selector element</mark> အပေါ်တင်လိုက်တဲ့အခါ / ‌ရောက်သွားတဲ့အခါ အလုပ်လုပ်ပါတယ်။

e.g. အပြာရောင် button ခလုတ်လေးတစ်ခု အပေါ် user က click မနှိပ်ခင် mouse cursor လေးတင်လိုက်တဲ့အချိန်မှာ button က အခြား‌အရောင်ပြောင်းသွားအောင် လုပ်တာ။

![[pseudo class hover example.png | 500]]

<hr> 

<mark style="background: #FFB86CA6;">:‌‌active</mark> : selector element ကို user က <mark style="background: #ABF7F7A6;">နှိပ်ထားလိုက်တဲ့အချိန်</mark> / ဖုန်းစခရင်ကနေ လက်နဲ့ <mark style="background: #ADCCFFA6;">ဖိလိုက်တဲ့အချိန်မျိုးမှာ</mark> အလုပ်လုပ်

e.g. အပြာရောင် button တစ်ခုကို userက mouse pointer နဲ့ click ထားတဲ့အချိန် / ဖိထားတဲ့အချိန်မျိုးမှာ အပြာရောင်ကို နည်းနည်းမှိန်ပေးလိုက်တာမျိုး။ အကယ်လို့ user က <span style="color:rgb(0, 176, 240)">click/ ဖိထားတာကို</span> <span style="color:rgb(0, 128, 128)">လွှတ်လိုက်ရင်တော</span>့ <span style="color:rgb(146, 208, 80)">အရောင်ပြန်ပြောင်း</span>သွားမယ်။

user ကို အသုံးပြုနေဆဲ ဆိုတဲ့ ခံစားချက်မျိုးကိုပေးတယ်။
![[pseudo-class active example.png|500]]

<hr> 


<mark style="background: #FFF3A3A6;">:focus</mark> : **<span style="font-weight:bold; color:rgb(255, 155, 0)">Input</span>** Element တစ်ခုကို အသုံးပြုနေချိန်မှာ အလုပ်လုပ်ပါတယ်။

< <mark style="background: #ADCCFFA6;">input</mark> >, < <mark style="background: #ADCCFFA6;">select</mark> >, < <mark style="background: #ADCCFFA6;">textarea</mark> > စတဲ့ <mark style="background: #FFB86CA6;">Form input elements </mark>တွေမှာ <mark style="background: #FFB86CA6;">အသုံးပြု</mark> 

e.g. input box တစ်ခုရှိမယ်။ user က input box ကို <span style="color:rgb(0, 176, 240)">click လိုက်ရင် စာရိုက်လို့ရ</span>တယ်။ အဲ့လို<span style="color:rgb(0, 176, 240)">စာရိုက်လို့ရသွားတဲ့အခြေအနေ</span>ကို <span style="color:rgb(255, 155, 0)">focus</span> ဖြစ်သွားတယ်လို့ အလွယ်မှတ်လို့ရတယ်။ အဲ့အချိန်မှာ CSS rule သတ်မှတ်ပေးလို့ရတယ်။

![[pseduo-class focus example.png]]

< select > element အတွက်ကတော့ သူကရွေးချယ်ရတာဖြစ်တာကြောင့် click နှိပ်လိုက်တဲ့အချိန် <span style="color:rgb(255, 155, 0)">option box တွေကျလာရင်</span> <span style="color:rgb(255, 105, 180)">focus mode</span> ဖြစ်သွားလိမ့်မယ်။