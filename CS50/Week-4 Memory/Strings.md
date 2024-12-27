strings ဆိုတာ array of characters ဆိုတာ သိပြီးပြီ
နောက်ဆုံး index မှာ null terminator \0 ရှိတယ်ဆိုတာလည်းသိပြီးပြီး။

ဒီတေ့ာ characters တွေဖြစ်တဲ့အလျောက် string index (each char) တစ်ခုဆီကို one byte ဆီနဲ့ computer က memory ထဲမှာသိမ်းတယ်။

E.g. `string s = "HI!";`  အတွက်
![[string_in_memory.png]]
ဒီလိုသိမ်းတယ်။ ဒါဆို s ဆိုတဲ့ variable ကြီးကရောဘာလဲ။ `int n = 50;` ဆိုရင် n ဟာ ငါးဆယ်ကို ရည်ညွှန်းပြတဲ့ variable ဘဲ။ C မှာ <mark style="background: #BBFABBA6;">string variable </mark> တွေဟာ တကယ်တော့ <mark style="background: #BBFABBA6;">kind of pointer</mark> တွေဘဲ။ pointer ဆိုတော့ ဘယ် address ကိုရည်ညွှန်းမလဲဆိုတော့ သူက first index ရဲ့ memory address ကိုရည်ညွှန်းတယ်။ example အရဆိုရင်တော့ 'H' (0x123) ပေါ့။ အဲ့ကုိရည်ညွှန်းထားပြီး အဆုံးသတ်ကိုကျ null terminator ကြောင့်သိနိုင်တယ်။

string တွေက pointer ဖြစ်တဲ့အတွက် <mark style="background: #FFF3A3A6;"> string s = char *s </mark>

```
#include <cs50.h>
#include <stdio.h>

int main(void)
{
	string s = "HI!";

	printf("%p\n", s); // no &, cz s itself is pointer
	printf("%p\n", &s[0]);

	/* 
	both output will be the same
	*/
}

```

###### char \*s

char \*s ဆိုတာက string s နဲ့တူတူဘဲဖြစ်တယ်။
ဒီတော့
```
#include <stdio.h>

int main(void)
{
	char *s = "HI!";  // !!important

    printf("%s\n", s);
}

```

ဟုတ်ပြီ normal အားဖြင့် pointer တစ်ခုမှာ variable address တစ်ခု store လုပ်မယ်ဆိုရင် & သုံးရတယ် (ဒါဟာ variable itself နဲ့ သူ့ address ကိုခွဲသိစေတာဖြစ်တယ်) ။ ဒါပေမယ့် char \*s မှာကျ ဘာလို့ &"HI!" မဖြစ်တာလဲဆိုရင် double quote (" ") ကိုမြင်တာနဲ့ clang လို compiler တွေက ဒါဟာ sequence of character ဖြစ်ကြောင်းသိပြီး first index (H) ရဲ့ memory address ကို s pointer မှာသိမ်းစေချင်တာဖြစ်ကြောင်းသိတယ်။