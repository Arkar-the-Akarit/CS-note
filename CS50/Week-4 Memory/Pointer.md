pointer = a variable that stores the memory address of another variable

<mark style="background: #FFF3A3A6;"> & </mark> = address of operator
သူ့ကိုသုံးပြီး ကွန်ပြူတာကို variable တစ်ခုရဲ့ memory address ကိုထုတ်ပြခိုင်းလို့ရတယ်။
memory address ကိုထုတ်ချင်ရင်သုံးရတဲ့ formatter က <mark style="background: #ADCCFFA6;"> %p </mark> 
```
#include <stdio.h>

int main(void)
{
	int n = 50;
	printf("%p\n", &n);
}

```

<mark style="background: #FFF3A3A6;"> * </mark>

\* syntax က သုံးတဲ့ context ပေါ်မူတည်ပြီး နှစ်မျိုးကွဲတယ်။

ပထမတစ်ခုက သူ့ကို <mark style="background: #FFF3A3A6;">pointer declaration</mark> လုပ်ဖို့အတွက်သုံးတယ်။

သဘောတရားက computer ကို ဒီ data type အတွက် memory address ကို store လုပ်နိုင်မယ့် pointer variable တစ်ခု ထုတ်ပေးပါလို့ဆိုတာဖြစ်တယ်။
```
data_type *pointer_name = &variable;

int *p = &n;   // n ဆိုတဲ့ interger datatype ရဲ့ memory address ကို store လုပ်နိုင်မယ့် p
				// ဆိုတဲ့ variable တစ်ခုဖန်တီးခိုင်းတာ
String *s = &text;

```

ဒုတိယတစ်ခုအနေနနဲ့ သူ့ကို <mark style="background: #BBFABBA6;">dereference operator</mark> လို့ခေါ်နိုင်တယ်။
memory address တစ်ခုကို ယူပြီး သူ့ထဲမှာရှိနေတဲ့ value ကို ထုတ်ပေးနိုင်တယ်။
```
int n = 50;
int *p = &n;

printf("%i", *p);  // output is 50
printf("%p", p); // output is 0x233blahbalh address of n

```