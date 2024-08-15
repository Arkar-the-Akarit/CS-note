
##### Property Position

elements တွေကို နေရာချတာပေါ်မူတည်ပြီး သုံးတဲ့ CSS property တွေကို CSS positions လို့ခေါ်တယ်။

property: <span style="color:rgb(255, 155, 0)">position</span>
value: <mark style="background: #FFF3A3A6;">static</mark> / <mark style="background: #FFF3A3A6;">relative</mark> / <mark style="background: #FFF3A3A6;">absolute</mark> / <mark style="background: #FFF3A3A6;">fixed</mark> / <mark style="background: #FFF3A3A6;">sticky</mark>

###### Static

- html elements တွေအတွက်<span style="color:rgb(0, 176, 240)"> default</span> positioning
- <span style="color:rgb(146, 208, 80)">document ရဲ့ normal flow အတိုင်း</span> element တွေကို<span style="color:rgb(146, 208, 80)"> position ချ</span> 
- top, right, bottom, left, z-index properties တွေက သူ့အပေါ် သက်ရောက်မှု <span style="color:rgb(220, 20, 60)">မရှိ</span> / အသုံးပြုလို့လည်း <span style="color:rgb(220, 20, 60)">မရ</span> 
- ![[positions static.png]]

###### Relative

- elements တွေက သူတို့ရဲ့ <span style="color:rgb(146, 208, 80)">normal position ကနေ</span>ပြီးတော့ <span style="color:rgb(146, 208, 80)">ဆက်စပ်ပြီ</span>း ရွေ့လျားတယ်
- <span style="color:rgb(255, 155, 0)">top</span>, <span style="color:rgb(255, 155, 0)">right</span>,<span style="color:rgb(255, 155, 0)"> bottom</span>, <span style="color:rgb(255, 155, 0)">left</span> စတဲ့ property တွေသုံးပြီး elements တွေကို သူတို့ရဲ့ မူလနေရာကနေ <span style="color:rgb(146, 208, 80)">‌ရွေ့ပြောင်းလို့ရ</span>

- ![[positionrelative.png|400]] ![[position-relative 2.png|400]]
- element က နေရာကနေ ရွေ့သွားပြီးရင် သူရဲ့ <span style="color:rgb(146, 208, 80)">အရင်ယူခဲ့တဲ့ နေရာက</span> ဒီတိုင်း <span style="color:rgb(0, 255, 255)">gap ခြားပြီး ကျန်ခဲ့</span>တယ်။ အခြား elements တွေက သူ<span style="color:rgb(255, 105, 180)">နေရာကို ဝင်ယူတာဘာညာမရှိ</span>သလို၊ ဝင်ယူလို့လည်းမရဘူး

  e.g. ![[positonrelative 3.png|450]] 
  ဒီမှာဆိုရင် အစက်ပြောက်လေးက မူလတည်နေရာ box ပေါ့။  element ကရွေ့သွားပြီးလည်းအဲ့နေရာက အဲ့လို ကွက်လပ်လေးဘဲ ကျန်နေမှာ။ ဘေးက အပြာရောင် element နှစ်ခုက ဝင်ရောက်စွက်ဖက်တာ၊ နေရာဝင်ယူတာမရှိ

###### Absolute

- <span style="color:rgb(0, 176, 240)">static မဟုတ်ဘဲ</span> အခြား position value နဲ့ နေရာရွေ့ပြောင်း (<span style="color:rgb(0, 128, 128)">positioned</span>) <span style="color:rgb(146, 208, 80)">လုပ်ခံထားရတဲ့ အနီးဆုံး</span> <span style="color:rgb(0, 255, 255)">ancestor</span> နဲ့ ဆက်စပ်ပြီး elements တွေက <span style="color:rgb(255, 155, 0)">နေရာယူတယ်</span> 
- အကယ်လို့ အဲ့လို ancestor မရှိဘူးဆိုရင် elementက ဦးဆုံးသော [[CSS Positions#Initial Containing Elements|Initial Containing Elements]] နဲ့ ဆက်စပ်ပြီး positions ချတယ်။ 
- သူက relative နဲ့ ဆန့်ကျင်ဘက်၊ သုံးလိုက်တဲ့ element က ‌document flow ကနေ ဖယ်ထုတ်ခံရမယ်။ relative လိုမျိုး box သုံးခုမှာ အလယ်တစ်ခုကို ဖယ်လိုက်ရင် နေရာကျန်နေ‌မှာမျိုး မဟုတ်ဘူး။
- i.e. parent box ကို <span style="color:rgb(220, 20, 60)">ဘာမှမလုပ်ထားဘဲ</span> child element မှာ absolute သုံးလိုက်ရင် သူက နေရာအကွာအဝေးကို <span style="color:rgb(0, 176, 240)">browser box ကနေ စတိုင်း</span>
  ![[positoinabsolute.png]]
- အကယ်လို့သာ parent element မှာ relative လို့ပေးလိုက်ရင် child element မှာ absolute သုံးလည်း parent box ကနေ စပြီး သက်ရောက်မယ်။ ဘာလို့ဆို absolute က အနီးစပ်ဆုံး positioned ancestor ကနေ သက်ရောက်တာမလို့
  ![[childabsolute, parentrelative.png]]

###### Fixed

- viewport နဲ့ ဆက်စပ်ပြီး‌ နေရာချလိုက်တာဖြစ်တယ်။
- page ကို scroll လုပ်သွားရင်တောင် element က သူ့နေရာမှာဘဲ အမြဲကျန်တယ်။
- ‌absolute လိုဘဲ သုံးလိုက်တဲ့ element ကို normal document flow ကနေနေ ဖယ်ထုတ်
- သူကလည်း parent box နဲ့ မသက်ဆိုင်ဘဲ browser box ကနေ စတိုင်း။ 
  ![[fixed.png]]

###### Sticky

- <span style="color:rgb(0, 176, 240)">fixed</span> က <span style="color:rgb(0, 176, 240)">browser box</span> က စတာ ဆိုပေမယ့် <span style="color:rgb(255, 155, 0)">sticky</span> ကကျ သူ့ <span style="color:rgb(255, 155, 0)">parent box</span> နဲ့ဘဲ သက်ဆိုင်
- ![[positionsticky.png]]






##### Initial Containing Elements

root element ဖြစ်တဲ့ < html > element ရှိနေတဲ့ element box ကြီးကို initial containing block လို့ခေါ််တယ်။
သူ့ကို viewport အဖြစ် ယူဆလို့ရတယ် ဘာလို့ဆို သူ့ရဲ့ sizeက  visible part of the browser window က သတ်မှတ်ပေးတာ။
အခြားသော containing block a.k.a container တွေက သူ့ထဲမှာ nested (ထပ်) ပြီး တည်ရှိနေတာ
