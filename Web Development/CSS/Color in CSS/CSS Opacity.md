
အလွယ်ပြောရရင် <span style="color:rgb(255, 255, 0)">ဖောက်မြင်ရအောင် </span>လုပ်လိုက်တာ

ရိုးရိုး property ကတော့ " <mark style="background: #FFF3A3A6;">opacity</mark> " ဘဲ
value က<mark style="background: #FFB86CA6;"> 0 - 1</mark> ကြား သတ်မှတ်ပြီး သုံးလို့ရတယ်။
0 ဆိုရင် ဖောက်ထွင်းမြင်နိုင်နှုန်း အမြင့်ဆုံးဖြစ်သွားပြီး နောက်ခံအရောင်က ပျောက်သွားလိမ့်မယ်။
- property "opacity" သုံးမယ်ဆိုရင် ကိုယ်က class နဲ့ သုံးလိုက်တာဆိုရင် အခြားသော content တေ‌ွရဲ့ အရောင် တေ‌ွအပေါ်ပါ သက်ရောက်နိုင်တာ သတိပြုရမယ်။

ဒါပေမယ့် [[Color in CSS]] ရေးတဲ့ အချိန်မှာ <span style="color:rgb(255, 255, 0)">အ‌ရောင် အပေါ်ဘဲ</span> တစ်ခါတည်း opacity သတ်မှတ်တဲ့ နည်းတွေလည်းရှိတယ်။

- [[RGB တန်ဖိုးဖြင့် အရောင်သတ်မှတ်ခြင်း]] မှာဆိုရင် a ထပ်ထည့်ပြီး <mark style="background: #FFB8EBA6;">rgba( , , , ,) </mark> ၊ ‌a (refers to <span style="color:rgb(0, 176, 240)">Alpha</span>) ရဲ့ တန်ဖိုးက<mark style="background: #FFF3A3A6;"> 0 - 1</mark> အထိထားလို့့ရတယ်။ 0 ဆိုရင် ဖောက်ထွင်းမြင်နိုင်နှုန်း အမြင့်ဆုံးဖြစ်သွားပြီး နောက်ခံအရောင်က ပျောက်သွားလိမ့်မယ်။
	```
	 .box-1{

   background-color: rgba(55,130,203,0.5);

	```
- [[Hexadecimal (hex) တန်ဖိုးဖြင့် သတ်မှတ်ခြင်း]] နဲ့ သတ်မှတ်မယ်ဆိုရင် <mark style="background: #FFB8EBA6;">#  rgb </mark>ဂဏန်း‌‌‌ေခြာက်လုံး နောက်မှာ <mark style="background: #FFB8EBA6;">Alpha အတွက် ဂဏန်း နှစ်လံုး</mark>ထပ်လိုက်ရမယ်။ <mark style="background: #FFF3A3A6;">00 - ff</mark> ကြား တိုးလျော့ လုပ်သုံး