border ထောင့်စွန်းလေးတွေကို border-radius property နဲ့ ကွေးကွေးလေးဖြစ်အောင် လုပ်မယ်

property: <span style="color:rgb(255, 155, 0)">border-radius</span>
value: " <mark style="background: #FFF3A3A6;">px</mark> ", "<mark style="background: #FFF3A3A6;"> % </mark>"

###### How border-radius works

border-radius သဘောတရားက ကိုယ်ပေးလိုက်တဲ့ value (px) က <mark style="background: #ADCCFFA6;">"x" ဝန်ရိုး</mark> အတွက်ရယ်၊ <mark style="background: #ADCCFFA6;">"y" ဝန်ရိုး</mark>အတွက်ရယ် ယူပြီး လေးထောင့်ကွက်လေးအတွင်းကို ကွေးပေးလိုက်တာ

![[how_border_radius_works.png]]

အကယ်လို့ ကိုယ်က x ဝန်ရိုးအတွွက် သပ်သပ်၊ y ဝန်ရိုးအတွက် သပ်သပ်ကွေးချင်ရင်
border-radius ရဲ့ value မှာ "<mark style="background: #FFB86CA6;"> x ဝန်ရိုး / y ဝန်ရိုး </mark>" နဲ့ ရေးပေးလို့ရတယ်။

e.g. border-radius: 30px/15px
     ![[border-radius30px15px.png]]

###### မျက်နှာချင်းဆိုင် ထောင့်နှစ်ခုဆီကို ကွေးခြင်း

border-radius property နောက်မှာ value နှစ်ခုကို space ခြားရေးပြီး မျက်နှာချင်းဆိုင် ထောင့်နှစ်ခုဆီကို ကွေးလို့ရတယ်။

<span style="color:rgb(255, 105, 180)">အရှေ့က</span> value က <mark style="background: #FFF3A3A6;">ဘယ်ဘက်-အပေါ်ထောင့် နဲ့ ညာဘက်-အောက်ထောင့်</mark>
<span style="color:rgb(255, 105, 180)">အနောက်က</span> value က <mark style="background: #ADCCFFA6;">ဘယ်ဘက်-အောက်ထောင့် နဲ့ ညာဘက်-အပေါ်ထောင့်</mark>

![[border-radius two values.png]]

###### တစ်ထောင့်ဆီ သီးသန့်ကွေးနည်း

value လေးခုနဲ့ <mark style="background: #FFF3A3A6;">ဘယ်-ပေါ်, ညာ-ပေါ်, ညာ-အောက်, ဘယ်-အောက်</mark> ‌ထောင့်‌တွေကို အစဥ်တိုင်း ကွေးလို့ရတယ်

![[border-radius four value.png]]

###### Percentage နဲ့ ကွေးမယ်

percentage က <span style="color:rgb(146, 208, 80)">relative unit</span> ဖြစ်တဲ့ အတွက်ကြောင့် <span style="color:rgb(0, 255, 255)">သူကွေးပေးမယ့် ပမာဏ</span> က <span style="color:rgb(0, 176, 240)">width</span> (represent <span style="color:rgb(255, 155, 0)">x-axis</span> ) ရဲ့ percentage နဲ့ <span style="color:rgb(0, 176, 240)">height</span> (represent <span style="color:rgb(255, 155, 0)">y-axis</span>) ရဲ့ percentage ကို မူတည်ပြီး တွက်ပေးမှာ

![[border-radius_percentage.png]]
ဒီမှာဆိုရင် width & height က နှစ်ခုလုံး 100px ဖြစ်တယ်။ ဒီတော့ 50% ယူပြီး ကွေးချလိုက်တဲ့ အချိန်မှာ စက်ဝိုင်း borderလေး၇တယ်။

