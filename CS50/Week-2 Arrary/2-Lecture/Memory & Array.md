#C #Memory #Array

##### Memory

data type တွေ အကုန်လုံးက သူ့ type နဲ့သူ memory ယူတဲ့ပုံ မတူဘူး။ int ဆို 4 byte ဘာညာပေါ့

ကွန်ပြူတာထဲမှာဆိုရင် သူ့သတ်မှတ်ထားတဲ့ finite amount of memory ပါတယ်။ 
![[memory in pc.png]]

အဲ့အထဲမှာက သူက data တွေကို ဘယ်လို store လုပ်လဲဆိုတာကို အလွယ် / အကြမ်းဖျငး်အားဖြင့် / metaphorically ဒီလို grid လေးတွေနဲ့ သူ့အကန့်နဲ့သူ သတ်မှတ်ထားတယ်လို့ မြင်ကြည့်လို့ရတယ်။
![[metamorphic memory.png]]
အကွက် တစ်ကွက်စီတိုင်းက <span style="color:rgb(0, 176, 240)">1 byte (8 bits) </span>ကို ကိုယ်စားပြုတယ်။
ဒီတော့ integer data type တစ်ခု store လုပ်မယ်ဆိုရင် 4 gird items / 4 bytes (32 bits) စာ နေရာယူမယ်။
![[integer memory.png]]

```
#include <cs50.h>
#include <stdio.h>

int main(void)
{
	int score1 = 72;
	int score2 = 73;
	int score3 = 33;

	//print average
	printf("Average: %f\n", (score1 + score2 + score3) / 3.0) ;
}
```

score value တွေကို အဲ့လိုပေးလိုက်မယ်ဆိုရင် memory မှာ ဒီလို store လုပ်သွားမှာပေါ့။

![[score memory.png]]

ပုံထဲမှာက ကြည့်ရလွယ်အောင် အစဥ်လိုက် store လုပ်ထားပေမယ့် တကယ်တမ်းကျ သူအစဥ်ပြေသလို randomly store လုပ်တာ။ <span style="color:rgb(255, 155, 0)">နေရာတွေမတူဘူး</span>

ဒါဆို နံပါတ်တွေကြီးလာရင် scoreN ဆိုတာထိရောက်လာရင် memory ပိုင်းအပြင်ကိုမှ ‌ရေးရ/မှတ်ရတဲ့ typographical error တွေတက်နိုင်တယ်။ ဒီတော့ data တွေကို တစ်စုတစ်စည်းတည်း လွယ်"ကူ" သိမ်းနိုင်ဖို့ Array ကိုသုံးလို့ရ။

#### Array

array ဆိုတာက data တွေကို လွယ်'ကူ'နဲ့ access လုပ်နိုင်အောင် memory ထဲမှာ အစဥ်လိုက် (back to back) စဥ်ပေးတဲ့ နည်းတစ်မျိုးဘဲ။

array ကို ‌declare လုပ်ရင် ကိုယ်လိုချင်တဲ့ length အတိုင်းကြေညာပေးရတယ်။ ကိုယ်က သုံးနေရာလိုချင်ရင် သုံး, လေးနေရာလိုချင်ရင် လေး
```
 int array[3] / char char_arr[4]
``` 

value ပါတစ်ခါတည်းထည့်ပြီး initialization လုပ်ချင်တယ်ဆိုရင်
```
int array[3] = {32, 34, 55};

char char_arr[4] = {'a', 'b', 'c', 'd'}

```

အဲ့လိုတစ်ခါတည်း value ‌assign မလုပ်ဘဲ သူ့အထဲက နေရာတစ်ခု (i.e index တစ်ခန်း)စီမှာ ထည့်ချင်ရင်
```
array[0] = 32;
array[1] = 34;
array[2] = 55; 

```

သတိပြုစရာ (၂) ခု
1. C language မှာ array ကိုကြေညာတာနဲ့ သူ့ထဲက index အခန်းတွေကို access လုပ်တဲ့ syntax က တူတူဘဲ - arrayName ပေါ့။ 

2. လိုချင်တဲ့ array အခန်း/index ကြေညာတဲ့အခါမှာကျ တစ်ခန်းဆို တစ်, နှစ်ခန်းဆို နှစ် စသည်ဖြင့် natural number (starts from one, no zero) နဲ့ကြေညာပြီး indexတွေကို access လုပ်ရင်ကျ whole number (starts from zero) နဲ့သွားလုပ်တယ်။ အလွယ်ပြောရရင် array\[3] ဆိုပြီး ကြေညာလိုက်ရင် သူ့ထဲက index တွေက 0,1,2 (total 3) ဖြစ်မယ်။ -> ကြေညာရင် လိုတဲ့နံပါတ်အတိုင်း ကြေညာ, အခန်းတွေကတော့ 0 ကစ

function <span style="color:rgb(32, 178, 179)">‌arguments</span> မှာ array ကိုထည့်ရင် <span style="color:rgb(32, 178, 179)">length ထည့်ပေးစရာမလို</span>ဘူး။
e.g. void function (int array\[]); 

program တစ်ခုရှိတယ်ဆိုပါတော့
```
int main(void) 
{
	char c1 = 'H';
	char c2 = 'I';
	char c3 = '!';

	printf("%c%c%c\n", c1, c2, c3);
}

//output be HI!

```

memory ထဲမှာ character ဖြစ်စေ, integer ဖြစ်စေ binary digits တွေနဲ့ဘဲ store လုပ်ထားတာဖြစ်တဲ့အတွက်၊ output မှာ <span style="color:rgb(255, 155, 0)">format ကို %i</span> နဲ့ ထုတ်ကြည့်လို့လည်းရတယ်။
```
printf("%i %i %i \n", c1,c2,c3)l;

//output 72 73 33
```

အပေါ်မှာပြောခဲ့သလိုဘဲ memory ထဲမှာ store လုပ်တာက အပေါ်ယံအမြင်မှာ ဒီလိုပေါ့

![[hi as char in memory.png]]

တကယ်တမ်း low level အထိကြည့်မယ်ဆိုရင် ဒီလို

![[hi as binary digit.png]]

binary digit တွေနဲ့ store လုပ်ထားတာဖြစ်လို့ ကိုယ်သုံးလိုက် <span style="color:rgb(146, 208, 80)">format ပေါ်မူတည်</span>ပြီး output ထွက်လာမှာဘဲ 








