```
in terminal : 
$ code hello.c
$ make hello
$ ./hello
```

<mark style="background: #CACFD9A6;">code hello.c</mark> --> create hello.c file , ဒီ command က တကယ်တော့ vsCode ကိုဖွင့်တဲ့ code command, အနောက်က file လိုက်လိုက်တော့ ရှိရင် open, မရှိရင် create လုပ်တာမျိုး
<mark style="background: #CACFD9A6;">make hello</mark> --> create လုပ်လိုက်ပြီး text editor ထဲမှာ code ရေးမယ်။ အဲ့ code file ကို make fileName နဲ့ compile လုပ်ပြီး machine code ပြောင်းမယ်။ သတိထားရမှာက file ကို create လုပ်ရင်သာ file extension (.c) ထည့်ရပေမယ့် make နဲ့ compile လုပ်တဲ့ အချိန်မှာတော့ file name ဘဲပါရင် ရပြီ

<mark style="background: #CACFD9A6;">./hello </mark> --> make နဲ့ လုပ်လိုက်တဲ့ executable file ကို run ပေး

```
#include <stdio.h>

int main(void){
	printf("Hello World! \n");
}

```

- printf = text စာသားတစ်ခုကို Output လုပ်ပေးနိုင်တဲ့ function
\\n  = text တွေ output ထုတ်ပြီးရင် နောက်တစ်လိုင်းက စပေးတဲ့ဟာ

###### Functions

```
printf("hello, world!\n");
```

အပေါ်က syntax မှာဆိုရင် printf() ဆိုတာက function တစ်ခုဘဲ။
ကွင်းစကွင်းပိတ်ထဲက ("hello, world\n") ဆိုတာတွေက arguments လို့ခေါ်တယ်။ 

arguments --> function --> return value

argument တေွကို function ထဲထည့်လိုက်တဲ့အခါမှာ computer က ပြန်ထုတ်ပေးတဲ့ output/return value တွေထွက်လာတယ်

`#include <stdio.h>` ဆိုတာက program ကို stdio.h လို့ခေါ်တဲ့ header file / library ထဲက capabilities တစ်ခုကိုသုံးချင်တယ်လို့ပြောလိုက်တာ။ i.e. printf() ဆိုတဲ့ function က stdio.h ဆိုတဲ့ header file ထဲမှာရှိနေတာ အဲ့တာကိုသုံးချင်တယ်ဆိုပြီး လှမ်းခေါ်လိုက်တာ။

library ဆိုတာက အလွယ်ပြောရရင် အသင့်ယူသုံးလို့ရတဲ့ သူများရေးပေးထားတဲ့ pre-written function တွေ။ free ဖြစ်ချင်ဖြစ်မယ်, ဝယ်ရတာလည်းဖြစ်နိုင်တယ်။ ဒါပေမယ့် ကိုယ်လိုချင်တဲ့ ရလဒ်ကို အပင်ပန်းခံ စဥ်းစားပြီးရေးနေစရာမလိုတော့ဘဲနဲ့ သူများရေးပြီးသားကို အသင့်သုံးလို့ရအောင်လုပ်ပေးထားတာတွေ။ cs50 မှာလည်း <mark style="background: #CACFD9A6;">cs50.h</mark>   လို့ခေါ််တဲ့ ကိုယ်ပိုင် library တစ်ခုရှိတယ်။

programming language တွေကို ရေးတဲ့သူတွေက အသုံးပြုတဲ့သူတွေနားလည်ပြီးဖတ်လို့ရအောင် documentation ဆိုတာတွေ ထုတ်ပေးတယ်။ ဒါပေမယ့် အဲ့တာတွေကလည်း ရှူပ်တယ်။ အဲ့လို ရှူပ်နေတာတွေကို အလွယ်ရှင်းပြထားတဲ့ (e.g. printf() functionဆို ဘယ်လိုအလုပ်လုပ်, ဘာအတွက်သံုး) CS50 က ထုတ်ထားတဲ့ website ရှိတယ်။ အဲ့မှာက CS50 course တစ်လျှောက်အသုံးများမယ့် function တွေကို documentation သေချာရှင်းပြထားတယ်။ --> https://manual.cs50.io

