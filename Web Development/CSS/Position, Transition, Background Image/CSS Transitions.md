
[[CSS Selector#Pseudo Class|Pseudo Class]] တွေဖြစ်တဲ့ :hover, :link စတာတွေကို သုံးလိုက်ရင် color ပြောင်းတာဘာညာပေါ့နော်

transition က အဲ့လို color ပြောင်းတာကိုမှ ဘယ်လို ပုံစံမျိုးနဲ့ ပြောင်းမယ်။ ကြာချိန်ဘယ်လောက်ထားမယ် စတာတွေကို သတ်မှတ်တာ

property: <span style="color:rgb(255, 155, 0)">transition</span>
value: "<mark style="background: #FFF3A3A6;">transition property</mark>" "<mark style="background: #FFF3A3A6;">duration</mark>" "<mark style="background: #FFF3A3A6;">timing-function</mark>" "<mark style="background: #FFF3A3A6;">delay</mark>"

```
.button {
	transition: background-color 0.3s ease-in-out 0s;
}
```
![[transition property example.png]]

ပုံအရဆိုရင် transition property မှာ bg color။ သဘောက transition ကို bg color ကို လုပ်မယ်လို့ပြောတာ။ 

<mark style="background: #FFF3A3A6;">property</mark>: transition လုပ်မယ့်ဟာကို ပြောတာ

<mark style="background: #FFF3A3A6;">duration</mark>: သတ်မှတ်ပေးလိုက်တဲ့ စက္ကန့်အတွင်း transition လုပ်မယ်

<mark style="background: #FFF3A3A6;">timing-function</mark>: animation/transition ဖြစ်တဲ့ အဝင် အထွက်/ အစ-အဆုံးကို ဘယ်လိုပုံစံထားမယ်ဆိုတာမျိုး
value:
- <mark style="background: #FFB86CA6;">linear</mark> (တသတ်မတ်တည်းအရှိန်နဲ့သွား)
- <mark style="background: #FFB86CA6;">ease-in-out</mark> (အဝင်နဲ့ အထွက်မှာ အရှိန်နှေးနေနှေး smooth, အလယ်မှာမြန်)
- <mark style="background: #FFB86CA6;">ease-in</mark> (အဝင်မှာဘဲ အရှိန်နှေး)
- <mark style="background: #FFB86CA6;">ease-out</mark> (အထွက်မှာ အရှိန်နှေး) .....

<mark style="background: #FFF3A3A6;">transition-delay</mark>: ချက်ချင်း animation စမလား။ မစခင် အချိန်ဘယ်လောက်စောင့်မလဲ သတ်မှတ်မယ်။

![[transition-example-2.png]]

ဒီပုံမှာဆိုရင် transition က 0.3s အတွင်းမှာ width & height က 80px ရှိနေတဲ့ box ကနေ 120px ကို ပြောင်းသွားမယ်။

ပထမ example မှာကလည်း pseudo class ထဲမှာထည့်ရေးတာမဟုတ်ဘဲ မူရင်း element မှာ ထည့်ရေးထားတာပါ။ ရှူပ်မှာဆိုးလို့ အောက်မှာ သပ်သပ်ခွဲပြီး ရေးထားပေမယ့် transition ကို .button ထဲမှာ တစ်ခါတည်းထည့်လို့ရပါတယ်။

