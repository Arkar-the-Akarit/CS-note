
<span style="color:rgb(220, 20, 60)">Powerful</span> ဖြစ်တဲ့ layout model, 
<span style="color:rgb(0, 176, 240)">flexible</span> than Grid

Grid : Use to layout webpage with columns & rows
Flex : Use for <span style="color:rgb(255, 155, 0)">detailed</span> - <span style="color:rgb(0, 128, 128)">card</span>, <span style="color:rgb(0, 128, 128)">section element layout</span> 

Advantage of Flex:
- Simplifies ဖြစ်
- Mobile-friendly

Flex က <span style="color:rgb(255, 155, 0)">One dimensional</span> ပုံစံနဲ့သွား
row or column အနေနဲ့ <span style="color:rgb(146, 208, 80)">တစ်ဖက်တည်းကိုပဲ direction သတ်မှတ်</span>ပြီး အသုံးပြုနိုင်

##### Flex ပုံစံ

![[how flex works.png]]

flex မှာက<span style="color:rgb(255, 155, 0)"> parent element</span> က <span style="color:rgb(255, 155, 0)">flex container</span> ဖြစ်ပြီး
အထဲမှာ <span style="color:rgb(146, 208, 80)">flex items</span> တွေပါ

Flex dimension ကို <span style="color:rgb(0, 176, 240)">Column</span> လို့ သတ်မှတ်လိုက်ရင် flex items တွေက ‌<span style="color:rgb(0, 176, 240)">ဒေါင်လိုက်</span>စီသွားပြီးတော့၊ <span style="color:rgb(146, 208, 80)">Row</span> လို့ သတ်မှတ်လိုက်ရင် flex items တွေက <span style="color:rgb(146, 208, 80)">အလျားလိုက်</span>ဖြစ်သွားမယ် (ပုံတွင်ကြည့်)

ဒါကြောင့်မလို့ block, inline element တွေမလိုတော့ဘဲ element တွေကို ကိုယ်လိုချင်သလို direction, layout တွေစီလို့ရသွားတယ်။

##### Axis of Flex - ဝန်ရိုး

![[felx axis.png]]

flex container ကို Row လို့ထားထားလိုက်ရင် Container ရဲ့<span style="color:rgb(0, 176, 240)"> ဘယ်ဘက်ကနေ ညာဘက်</span>သို့ <span style="color:rgb(0, 128, 128)">horizontal မျဥ်းတစ်ကြောင်း</span>ရှိသွားတယ်။ အဲ့မျဥ်းကို <span style="color:rgb(0, 176, 240)">Main Axis</span> လို့ခေါ်တယ်။ Container ရဲ့ ဘယ်ဘက်ကစတာဖြစ်တဲ့အတွက် အဲ့အစနေရာကို <span style="color:rgb(255, 155, 0)">Main Axis Start</span> လို့ခေါ်ပြီး ညာဘက်မှာဆုံးသွား‌တဲ့နေရာကို <span style="color:rgb(255, 155, 0)">Main Axis End</span> လို့ခေါ််တယ်။

Main Axis မျဥ်းရဲ့ အလယ်ကို ဖြတ်သွားတဲ့မျဥ်းက <span style="color:rgb(0, 176, 240)">Cross Axis</span>, သူ့မှာလည်း <span style="color:rgb(255, 155, 0)">Cross Axis Start</span> နဲ့ <span style="color:rgb(255, 155, 0)">Cross Axis End</span> ရှိတယ်။

အကယ်လို flex items တွေကို <span style="color:rgb(0, 255, 255)">Column</span> ပုံစံစီထားတယ်ဆိုရင် <span style="color:rgb(255, 155, 0)">Main Axis</span> 
က <span style="color:rgb(255, 105, 180)">Vertical</span> လာမယ်
![[column main axis.png]]

##### Flex Container

Grid လိုဘဲ Flex Container သတ်မှတ်ဖို့အတွက်ဆို သတ်မှတ်ချင်တဲ့ element ထဲမှာ 

display: flex; လို့ရေးပေးလိုက်ရင်ရပြီ
အထဲမှာ flex items တွေကတော့ <span style="color:rgb(255, 155, 0)">default </span>အနေနဲ့ <span style="color:rgb(255, 155, 0)">Horizontal</span>


![[flex container.png]]

###### Flex Directions

items တွေကို row/column ဘယ်လိုဆီလဲဆို

property: <span style="color:rgb(255, 155, 0)">flex-direction</span>
value: <mark style="background: #FFF3A3A6;">row</mark>  , <mark style="background: #FFF3A3A6;"> reverse row</mark> / <mark style="background: #FFB86CA6;">column </mark>, <mark style="background: #FFB86CA6;">column-reverse</mark>

Value : row ဆိုရင်တော့ items တွေက <span style="color:rgb(255, 155, 0)">Main Axis ရဲ့ အပေါ်</span>ကနေပြီးတော့ ဘယ်ကနေ ညာကို (<span style="color:rgb(146, 208, 80)">from main axis start</span>) စီသွားမယ်။ 
row-reverse ဆိုရင်တော့ <span style="color:rgb(255, 155, 0)">Main Axis အပေါ်</span>ကနေကိုမှာ ညာ ကနေ ဘယ် (<span style="color:rgb(146, 208, 80)">from main axis end</span>) စီသွားမယ်

![[row,row-reverse.png]]

Value: Column ဆိုရင် <span style="color:rgb(255, 155, 0)">Main Axis</span> က <span style="color:rgb(146, 208, 80)">Vertical</span> ဖြစ်သွားမယ်။ Items တွေက  <span style="color:rgb(255, 155, 0)">main axis ဘယ်ဘက်ခြမ်း</span> <span style="color:rgb(0, 255, 255)">အပေါ်ကနေ အောက်</span> (from main-axis start) ‌ကနေ စလာမယ်။

column reverse ဆိုရင် items တွေက <span style="color:rgb(255, 155, 0)">main axis ဘယ်ဘက်ခြမ်း</span> <span style="color:rgb(0, 255, 255)">အောက် ကနေ အပေါ်</span>ကို (from main-axis end) ကနေ စလာမယ်

![[flex direction column;.png]]

###### Flex Wrap

flex-direction : row; ဆိုပြီး သုံးလိုက်တာနဲ့ flex items တွေက row <span style="color:rgb(0, 176, 240)">တစ်တန်းတည်း</span> အနေနဲ့ စီသွားမှာ။ items တွေများလာရင်လည်း ပြည့်သိပ်ပြီး size တွေချုံ့ပြီး row တစ်ခုတည်းမှာဘဲ သွားစီမှာ၊ 
ဒီလိုမဖြစ်ဘဲ <span style="color:rgb(146, 208, 80)">တစ်တန်းစာပြည့်တာနဲ့ </span>ကျန်တဲ့ <span style="color:rgb(0, 255, 255)">flex items တွေက အောက်ကို ဆင်း</span>သွားအောင်

property: <span style="color:rgb(255, 155, 0)">flex-wrap</span>
value: <mark style="background: #FFF3A3A6;">wrap</mark> , <mark style="background: #FFF3A3A6;">no-wrap</mark> (default), <mark style="background: #FFF3A3A6;">wrap-revere</mark>

![[flex wrap.png]]

<mark style="background: #FFF3A3A6;">wrap-reverse</mark>: သူကကျ အောက်ဆုံးရောက်မယ့်လိုင်းကို အပေါ်ဆုံးကနေ စပြတာ
![[wrap-reverse;.png]]

###### Flex-Flow

flex-direction နဲ့ flex-wrap ကို shorthand ပေါင်းရေးချင်တယ်ဆိုရင်

property: <span style="color:rgb(255, 155, 0)">flex-flow</span>
e.g. value: <mark style="background: #FFF3A3A6;">row wrap</mark>
![[flex-flow.png]]

##### Justify Content

justify content ဆိုတာက flex container ထဲက flex items တွေကို <span style="color:rgb(0, 128, 128)">layout (နေရာ) ဘယ်လိုချ</span>မလဲနဲ့ <span style="color:rgb(0, 128, 128)">လွတ်နေတဲ့ spacing တွေသတ်မှတ်</span>ဖို့သုံး

အဓိကအားဖြင့် <span style="color:rgb(146, 208, 80)">main-axis ပေါ်မှာဘဲ နေရာယူ</span> 

property: justify-content
value: <mark style="background: #FFF3A3A6;">flex-start</mark> , <mark style="background: #FFF3A3A6;">flex-end</mark> , <mark style="background: #FFF3A3A6;">center</mark> , <mark style="background: #FFF3A3A6;">space-between</mark> , <mark style="background: #FFF3A3A6;">space-around</mark> , <mark style="background: #FFF3A3A6;">space-evenly</mark>

<mark style="background: #FFF3A3A6;">flex-start</mark>: default value, flex items တွေကို main-axis အစ ကနေ စပြီးစီ

<mark style="background: #FFF3A3A6;">flex-end</mark>: main-axis end (အဆုံး) ကနေ flex items တွေကို စစီ

<mark style="background: #FFF3A3A6;">center</mark>: flex items တွေကို အလယ်ကျအောင်စီမံတာ

<mark style="background: #FFF3A3A6;">space-between</mark>: flex items တွေ <span style="color:rgb(146, 208, 80)">တစ်ခုနဲ့ တစ်ခုကြားမှာ</span> <span style="color:rgb(0, 255, 255)">တူညီတဲ့ အကွာအဝေးတစ်ခုခြား</span>မယ်လို့ သတ်မှတ်တာ။ flex container နဲ့ items ကြားမှာတော့ အကွာအဝေး <span style="color:rgb(220, 20, 60)">မရှိ</span> 

<mark style="background: #FFF3A3A6;">space-‌around</mark>: သူကကျတော့ container အပါအဝင် flex items တွေကြားမှာ တူညီတဲ့ အကွာအဝေးခြား၊ ဒါပေမယ့် container နဲ့ flex-items ကြားက အကွာအဝေးက flex-items အချင်းချင်းကြားက အကွာအဝေးထက် နည်းနည်းပိုကျဥ်း
![[space around.png]]


<mark style="background: #FFF3A3A6;">space-evenly</mark>: သူက containers ဘက်ကနေ items တွေကို ခြားတဲ့ အကွာအဝေးနှစ်ဖက်ကို အရင်ယူ, ပြီးမှ items တွေကြားထဲ spacing ထပ်ခြား။ အကွာအဝေးအကုန်ညီတူညီမျှ
![[space-evenly.png]]


![[justify-content.png]]

##### Align items

flex container ထဲက flex-items တွေရဲ့ layout ကို နေရာချထားဖို့သုံး
အဓိကအားဖြင့် <span style="color:rgb(255, 155, 0)">cross axis</span> ပေါ်မှာ spacing ယူ

property: <span style="color:rgb(255, 155, 0)">align-items</span>
value: <mark style="background: #FFF3A3A6;">flex-start</mark> , <mark style="background: #FFF3A3A6;">flex-end </mark>, <mark style="background: #FFF3A3A6;">center</mark> , <mark style="background: #FFF3A3A6;">stretch</mark> , <mark style="background: #FFF3A3A6;">baseline</mark>

<mark style="background: #FFF3A3A6;">flex-start</mark>: default value, Cross Axis အစ (cross axis start) ဘက်မှာ items ‌ေတွကို စီ

<mark style="background: #FFF3A3A6;">flex-end</mark>: cross axis အဆုံး (cross axis end) 

<mark style="background: #FFF3A3A6;">center</mark>: items တွေကို အလယ်မှာထား

<mark style="background: #FFF3A3A6;">stretch</mark>: items တွေကြားမှာ spacing မထားတော့ဘဲ နေရာအပြည့်ယူ

<mark style="background: #FFF3A3A6;">baseline</mark>: text baseline / content baseline ကို align ချိန်ပြီး spacing တွေ ချိန်ညှိတာ
![[align-items.png]]

###### Flex Align Self

flex-items အကုန်လုံးကို align မလုပ်ဘဲ, item တစ်ခုချင်းဆီကို align လုပ်ဖို့သုံးတယ်။ align-items property လိုဘဲ cross-axis ‌အပေါ်မှာသာများသောအားဖြင့် spacing ယူတယ်။
![[align-self.png]]
##### Flex Gap

flex items တွေ တစ်ခုနဲ့ တစ်ခုကြားက ‌ဒေါင်လိုက်အကွာအဝေး, အလျားလိုက်အကွာအဝေးတွေကို သတ်မှတ်

property: <span style="color:rgb(255, 155, 0)">row-gap</span> , <span style="color:rgb(255, 155, 0)">column-gap</span> , <span style="color:rgb(255, 155, 0)">gap</span> (shorthand)
value: <mark style="background: #FFF3A3A6;">row column</mark> (shorthand)

![[flex-gap.png]]

##### Flex-grow

သူက flex items တွေကြားမှာ နေရာအလွတ်လေးတွေ (gap) တွေရှိတယ်ဆိုပါဆို့၊ အဲ့တာ‌ဆို flex-grow property apply လုပ်ခံလိုက်ရတဲ့ <span style="color:rgb(146, 208, 80)">items </span>တွေက အဲ့နေရာလွတ်လေးတွေ <span style="color:rgb(0, 255, 255)">သတ်မှတ်ထားတဲ့ value ပေါ်မူတည်</span>ပြီးခွဲယူကြမှာ၊ <span style="color:rgb(0, 128, 128)">တစ်ခုထဲကိုဘဲ ‌apply</span> လုပ်ရင်တော့ သူကဘဲ <span style="color:rgb(0, 128, 128)">နေရာလွတ်အကုန်ယူမ</span>ှာ‌ပေါ့။ flex-grow apply မလုပ်ထားတဲ့ items တွေကတော့ သူ့တို့နေရာနဲ့ သူတို့ ဒီတိုင်းပါဘဲ။

အကယ်လို flex-grow: <span style="color:rgb(0, 128, 128)">1</span> & flex-grow: <span style="color:rgb(0, 128, 128)">3</span> ဆိုပြီး flex-grow နှစ်ခုသုံးလိုက်တယ်ဆိုပါတော့၊ အဲ့တာဆို နေရာလွတ်ကို <mark style="background: #ABF7F7A6;">4 (1+3)</mark> နေရာ ပိုင်းပြီး<span style="color:rgb(146, 208, 80)"> value 1 က တစ်ပိုင်း၊</span> <span style="color:rgb(255, 105, 180)">value 3 က သုံးပိုင်း</span>ယူလိုက်မှာ

![[flex-grow example.png]]
![[flex-grow explanation.png]]

![[flex-grow.png|450]]

7 & 8 ကိုကြည့် flex-grow value 1 & 2 ဆိုတော့ သိပ်မကွာသေးဘူး။

![[flex-grow;2;.png|450]]
flex-grow value 1 & 8 ဆိုတော့ကွာသွားပြီ၊ box 8 က total 9 (1+8) ထဲက ၈ နေရာစာရပြီး ကျန်တာတွေက ဒီတိုင်းဘဲ 

