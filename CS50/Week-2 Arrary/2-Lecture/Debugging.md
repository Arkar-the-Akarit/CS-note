
debug လုပ်တယ်ဆိုတာ syntax error ကြောင့်ဖြစ်စေ, logical error ကြောင့်ဖြစ်စေ၊ concept error ကြောင့်ဖြစ်စေ မှားသွားပြီး လိုချင်သလို မ run တော့တဲ့ program တစ်ခုမှာ အမှားရှာတာ

အဲ့လိုအမှားရှာရတာ‌ လွယ်ကူအောင်လို့ debugger လို့ခေါ်တဲ့ tool တွေကိုသုံးလို့ရတယ်။ cs50-VSCode မှာဆိုရင်လည်း သူတို့ထည့်ပေးထားတဲ့ debugger လေးပါတယ်။ -> `debug50` လို့ခေါ်ပြီး အနောက်က executable file ./file နဲ့ run ရတယ်။

debug50 ကိုသုံးမယ်ဆိုရင် <mark style="background: #FFF3A3A6;">make</mark> နဲ့ exe file လုပ်ဖို့လိုမယ်။ <mark style="background: #FFF3A3A6;">breakpoint</mark> မှတ်ဖို့လိုမယ်။

*note* - debugger တွေက <span style="color:rgb(220, 20, 60)">syntax error</span> ကြောင့်ဖြစ်တဲ့ error တွေကိုတော့<span style="color:rgb(220, 20, 60)">သိနိုင်မှာ မဟုတ်ဘူး</span>။ အဲ့တာတွေကလည်း compile လုပ်လိုက်ရင်ပြတယ်ဆိုတော့ compiled language တွေမှာတော့ သိပ်မလိုပါဘူး

test program for debug50
```
#include <stdio.h>
#include <cs50.h>

void print_column(int height);

int main(void){
	int h = get_int("height: ");
	print_column(h);
}

void print_column(int height)
{
	for(int i=0; i <= height; i++)
	{
	 printf("#\n");
	}
}
```

vsCode ထဲမှာ line no တွေရဲ့ ဘေးမှာ cursor လေးတင်လိုက်ရင် အနီစက်လေးတွေပေါ်လာတယ်။ left click နှိပ်လိုက်ရင် breakpoint လုပ်ပြီးသားဖြစ်တယ်။ left click နှိပ်ပြီး ပြန်ဖျက်လို့ရတယ်။
breakpoint set, make & debug50 ကို runလိုက်ပြီဆိုရင် ဒီလိုမြင်ရမယ်

![[debugging with debug50.png]]
breakpoint set လုပ်လိုက်တဲ့ line ကို မျဥ်းအဝါလေးနဲ့ ပြထားပေးတယ်။ သဘောတရားက program ကို run ရင်းနဲ့ breakpoint လုပ်ထားတဲ့ နေရာရောက်တော့ ဆက် run ဘဲ ခဏရပ်ထားပေးတယ်။ <mark style="background: #FFF3A3A6;">မျဥး်အဝါလေး</mark>က program ရပ်ထားပေးတဲ့နေရာကို ကိုယ်စားပြုတယ်။

ဘယ်ဘက်အပေါ်ခြမ်းမှာ user input ဘာမှ မဝင်သေးခင် h တန်ဖိုးက 32767 ဖြစ်နေတယ်။ ဒါ‌ကို #C မှာ <mark style="background: #BBFABBA6;">garbage value</mark> လို့ခေါ််တယ်။
variable တစ်ခုကို declare လုပ်လိုက်ပြီဆိုတာနဲ့ program က automatic value တွေဖြည့်ပေးတယ်။ အဲ့တာတွေက ဘာမှတော့ သိပ်ပြီး ပြသနာမရှိပေမယ့် တစ်ခါတလေ error တက်နိုင်တာကြောင့် declaration လုပ်မယ့်အစား တစ်ခါတည်း value assign ပြီး initialization လုပ်လိုက်တာပိုကောင်းတယ်။

continue - ဆိုတဲ့ key ကတော့ breakpoints ကိုဖျက်ပြီး program ကို အဆုံးထိ run သွားမယ်လို့ပြောတာ

step over - breakpoint မှတ်ထားတဲ့ဟာကို execute လုပ် အတွင်းထဲထိမပြဘဲ execute လုပ်ပြီး ဖြစ်သွားတဲ့တစ်ဆင့်စီကိုဘဲပြ။ ကျော်သွားလို့ပြောတာမဟုတ်ဘူး။ execute လုပ်လိုက်, အဲ့အတွင်းထဲမှာ ဘာတွေဖြစ်သွားတယ်ဆိုတာကိုသာ မပြနဲ့ပေါ့။

step inအသ - breakpoint set ထားတဲ့အတွင်းထဲက detail ကျကျ ဖြစ်သွားတာတွေကိုပြ e.g. program မှာဆိုရင် get_int() ဆိုတဲ့ function သာပါနေရင် အဲ့အတွင်းထဲထိဘာတွေဖြစ်နေလဲပြ

step out - ပြန်ထွက်တာ

အပေါ်က program မှာဆိုရင် step over ကိုနှိပ်လိုက်ရင် terminal မှာ value တောင်းမယ်။ 
![[debugging 1.png]]

![[debugging 2.png]]
height ကို 3 လို့ထည့်လိုက်တာနဲ့ h ဟာ garbage value ကနေ 3 ဖြစ်သွား။
မျဥး်အဝါလေးကလည်း အောက်တစ်ကြောင်းဆင်းသွားတာကို တွေ့ရမယ်။ 

*note* -> ဒီတော့ debugger က <span style="color:rgb(0, 176, 240)">line by line execute</span> တစ်ဆင့်ချင်းလုပ်ပြီး user ကိုပြပေးတယ်။

အဲ့လိုနဲ့ ဆက်ကြည့်သွားရင် for loop ရှိတဲ့ print_column function ဆီကိုရောက်သွားပြီးတေ့ာ i တန်ဖိုး 0 မှာ # တစ်ခု to i တန်ဖိုး 3 ထိ (total 4 #) ထွက်လာတာကို မြင်ရမယ်။ အဲ့မှာ <\= sign ကြောင့် user က 3 input ထည့်ပေးမယ့် hash sign 4 ခု ထိထွက်လာတာကို သတိပြုနိုင်ပြီး ပြင်နိုင်မယ်။ that's how we use debugger