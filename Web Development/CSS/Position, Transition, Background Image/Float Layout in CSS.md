
အခုခေတ်မှာ အသုံး<mark style="background: #FFF3A3A6;">နည်း</mark>သွားပြီ

ဒါပေမယ့် သိအောင်လို့။

html မှာဆိုရင် < img > က inline element, < p > က block element။
ဒီတော့ ပုံမှန်အတိုင်းဆိုရင်/ normal document flow အတိုင်းဆိုရင် ပုံက အပေါ်မှာပေါ်မယ်, ပြီးရင် p စာသားတွေက အောက်မှာ ပေါ်‌ေနမှာပေါ့။
![[float normal flow.png]]

အဲ့ဒီ ပုံထဲမှာကို image ကို <mark style="background: #FFF3A3A6;">float : right</mark> လို့ ကြေညာပေးလိုက်ရင် normal flow အတိုင်းမသွားတော့ဘဲ "p" စာသားတွေက ပုံရဲ့ <span style="color:rgb(0, 128, 128)">ညာဘက်</span>ကိုရောက်လာမယ်။
ကျန်တဲ့ element တွေကလည်း အဲ့လိုဘဲ။ ညာဘက်ကိုရောက်လာကြမယ်။ 
အဲ့ floating effect ကိုဖျက်ချင်ရင်
"<mark style="background: #FFB86CA6;"> clear: both </mark>" ကို သုံးရတယ်။
အောက်ကပုံမှာဆိုရင် အလယ်မှာ <span style="color:rgb(146, 208, 80)">clear property</span> သုံးပြီး အောက်မှာကျ flow ကို ဘယ်ဘက်က လာအောင် <mark style="background: #FFB86CA6;">float:left</mark> ကိုသုံးထားတယ်
![[float layout example.png]]

property: <span style="color:rgb(255, 155, 0)">clear</span>
value: <mark style="background: #FFF3A3A6;">left </mark>,<mark style="background: #FFF3A3A6;"> right</mark>, <mark style="background: #FFF3A3A6;">both</mark>
တစ်ခုထဲ ဖျက်ချင်ရင် ဖျက်ချင်တဲ့ ဘက်ကိုသုံး၊ အကုန်ဖျက်ချင်ရင် both

<hr>

![[layout with float.png]]

ပုံထဲမှာဆိုရင် container‌ တွေကို float property တွေနဲ့ ကိုယ်သွားစေချင်တဲ့ ဘက်ကို value ပေးပြီး box/container တွေကို <span style="color:rgb(255, 155, 0)">width</span> ပေးလိုက်ရင် လိုသလို layout ပုံစံ‌လေးဖန်တီးလို့ရတယ်၊။


