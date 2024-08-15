ဘယ်လို devices (mobile, watch, laptop, tablet...) ကနေဝင်ကြည့်ကြည့် website က ကောင်းကောင်းမွန်မွန်အလုပ်လုပ်နေပြီး စနစ်တကျ လှလှပပရှိနေမယ်ဆိုရင် responsive ဖြစ်တယ်လို့ခေါ်တယ်။ 

website တစ်ခုရေးဆွဲပြီဆိုရင် ဘယ် device ကဝင်ကြည့်ကြည့်၊ ဘယ်လို screen size မျိုးကကြည့်ကြည့် ရွဲ့စောင်းပြီး ပုံပျက်မနေဖို့ လိုတယ်။

အဲ့လို မဖြစ်စေဖို့အတွက် developer တွေက screen size အမျိုးမျိုးအတွက် အချို့ element တွေကို different CSS rules တွေ apply လုပ်ပေးကြတယ်။ အဲ့လို apply လုပ်ဖို့ @ At rule ကို သုံးတယ်။

Syntax:

```
@media screen and (min-width: ..px) and (max-width: ...px) {

	CSS Rule Here
}
```
![[responsive css syntax.png]]

<mark style="background: #ABF7F7A6;">@media</mark>: ဒါက at rule, အမျိုးအစားကို ကြေညာလိုက်တာ၊ သူ့နောက်မှာက ဘယ်လို media type မျိုးလဲဆိုတာ လာတယ်။

<mark style="background: #ABF7F7A6;">media type</mark>: "<span style="color:rgb(0, 176, 240)">screen</span>" ဆိုတာက ဖန်သားပြင်ပါတဲ့ အရာတွေအတွက် ဆိုပြီး media type ကြေညာပေးတာဘဲ၊ "<span style="color:rgb(0, 176, 240)">print</span>" ဆိုပြီး ပရင့်တာတွေအတွက် ပရင့်ထုတ်တဲ့အချိန်သုံးဖို့ သုံးတာလည်းရှိတယ်။

<mark style="background: #ABF7F7A6;">Operator</mark>: "<span style="color:rgb(0, 176, 240)">and</span>" / "<span style="color:rgb(0, 176, 240)">or</span>" , and ကတော့ ဒီ screen size နဲ့ ဒီ size ကြားဆိုတာမျိုး၊ or ကတော့ ဒီ screen size မဟုတ်ရင် အခြား screen size အတွက်ဆိုတာမျိုးပေါ့

<mark style="background: #ABF7F7A6;">Media Feature</mark>: ဘယ်လောက် အနည်းဆုံး/အများဆုံး အကျယ်ရှိတဲ့ screen size အတွက်ဆိုပြီး screen size ကို တိတိကျကျသတ်မှတ်ဖို့အတွက် သုံးတာ

![[media queris.png]]

ပုံမှာဆိုရင် container အတွက် background color ကို default အနေနဲ့ black သတ်မှတ်ပေးထားတယ်။ ဒါပေမယ့် tablet screen size မှာဆိုရင်ကျ pink ဆိုပြီး သတ်မှတ်လိုက်တယ်ပေါ့။

###### Responsive CSS Minimum Width

အနည်းဆုံး screen size <span style="color:rgb(0, 176, 240)">ဒီလောက်ကစပြီးတော့</span> ဒီ CSS rule တွေကို သတ်မှတ်မယ်ဆိုပြီး သုံးတာ
![[min-width.png]]

![[min-width 768px.png]]
768px အကျယ်ရှိတဲ့ screen size ကစပြီး rule သတ်မှတ်မယ်

![[min-width 1024px.png]]
![[min-width 1028px.png]]

###### Responsive CSS Maximum Width

screen size <span style="color:rgb(0, 176, 240)">ဒီလောက်အထိအတွက်ဘဲ</span> ဒီ rule တွေကို သတ်မှတ်မယ်ဆိုတာမျိုး

![[max-width.png]]
640px screen size အတွက်ဘဲ CSS rule တွေသက်ရောက်မယ်။ သူ့နောက်က ဟာတွေက မဆိုင်တော့ဘူးဆိုတာမျိုး

###### Responsive Between

ဒီ screen size နဲ့ ဒီ screen size ကြားဆိုတာမျိုး၊ များသောအားဖြင့် device type တစ်ခုခုကိုပေါ့။ tablet ဆို tablet အဲ့လိုမျိုးကို cover လုပ်ဖို့ရေးတာ
![[responsive between.png]]

###### Responsive Columns

Grid display သုံးထားတဲ့ columns တွေကို responsive ဖြစ်အောင်ရေးမယ်။

![[responsive grid css.png]]
```
/* For Larger Tablet */

  @media screen and (min-width: 768px) {

    .md\:col-6 {
      grid-column: auto / span 6;
    }

    .md\:col-12 {
      grid-column: auto / span 12;
    }

  }

  /* For Laptop And Upper Desktop */

  @media screen and (min-width: 1024px) {

    .lg\:col-3 {
      grid-column: auto / span 3;
    }

  }

```

.md\:col-3 , .md\:col-6, .lg\:col-3 လို့ရေးတာမျိုးက [[CSS Selector#Escaping in CSS |Escaping]] လုပ်တာဘဲ


















