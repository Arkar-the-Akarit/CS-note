#c
variable တစ်ခုရဲ့ value ကို မပြောငး်ဘဲရှိစေချင်ရင် 
အဲ့ variable data type ရှေ့မှာ '<mark style="background: #FFB86CA6;">const</mark>' ဆိုတဲ့ စာလုံးကို သုံးလို့ရတယ်။ 

e.g. const int x = 10;
ဒီလို value declaration လုပ်လိုက်ရင် အောက်မှာ
x = 20; or other ...
အဲ့လို တန်ဖိုးတွေ ထည့်လာရင် compiler မှာ error တက်မယ်။

ဒါပေမယ့် pointer ထောက်ထားပြီး အဲ့ pointer value ကို ချိန်းချလိုက်ရင်တော့ Undefined behavior ဖြစ်သွားနိုင်တယ်။ ဒါကြောင့် const နဲ့ pointer ကို သုံးရင် သတိထားရမယ်။

<mark style="background: #FFF3A3A6;">naming convention</mark> = const variable တစ်ခုပေးမယ်ဆိုရင် capital letter တစ်ခုနဲ့ ပေးတာပိုပြီး အမြင်မှာ သိသာစေတယ်။ 