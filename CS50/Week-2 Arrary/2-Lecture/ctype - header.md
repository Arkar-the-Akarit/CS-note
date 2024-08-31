#C #c_header

`#include <ctype.h>`

ctype ဆိုတဲ့ header မှာ လုပ်ဆောင်ချက်အများကြီးရှိပေမယ့် video မှာတော့ character တွေကို upper case ချိန်းတာကိုပြသွားတယ်။ 

###### upper case changing

သာမန်အားဖြင့် user input လုပ်လိုက်တဲ့ string တစ်ခုကို upper case ပြောင်းချင်ရင် ဒီလိုရေးတယ်။

```
// string chars to upper case

#include <cs50.h>
#include <stdio.h>
#include <ctype.h>

int main(void)
{
	string name = get_string("Name: ");

	for (int i = 0 , n = strlen(name); i < n; i ++)
	{
	  if (name[i] >= 'a' && name[i] <= 'z')
	  {
		  printf("%c", name[i] - 32); // same as name[i]- ('a' - 'A')
	  }
	  else 
	  {
		  printf("%c", name[i]);
	  }
	}

}


```

line by line explanation:

- input string ကိုယူတယ်။
- strlen() function နဲ့ length value ယူ -> n
- name \[ i\] >= 'a' && name\[i] <= 'z' ဆိုတာက input string ထဲမှာ ‌a-z ကြားက character ပါလာခဲ့ရင်ဆိုတာ
- `printf("%c", name[i] - 32); ` ဒီမှာက ASCII chart ထဲကိုကြည့်မယ်ဆိုရင် A အကြီးက decimal value 66 , a အသေးက decimal value 97, သူတို့ နှစ်ခုကြားက ကွာခြားချက်က 32, ကျန်တဲ့ character တွအတွက်လည်း တူတူဘဲ။ memory ထဲမှာက binary digit နဲ့ သိမ်းတာဖြစ်လို့ ‌a အသေး binary digit ထဲကနေ decimal value 32 ရဲ့ binary digit ကို နှုတ်လိုက်တာနဲ့ A အကြီးနဲ့ ညီမျှတဲ့ binary digit ရလာမှာဘဲ။  ဒီလိုနဲ့ Upper case char ရနိုင်တယ်။ ဒါဟာ C language ကြောင့်မဟုတ်ဘူး။ <span style="color:rgb(255, 155, 0)">ASCII Standard ကြောင့်ဘဲ</span>။ ဒီသဘောတရားနဲ့ဆိုရင် name\[i\] >= 'a' && name\[i] <= 'z' လို့မ‌ရေးဘဲ a-z အစား တူညီတဲ့ decimal digit ဖြစ်တဲ့ name\[i\] >= 97 && name\[i] <= 122 လို့ရေးလည်းရ

###### toupper() function

ဒီလို ကိုယ့်ဘာသာရေးမယ့်အစား char တွေကို upper case ပြောင်းပေးမယ့် toupper() ဆိုတဲ့ function ctype.h ထဲမှာရှိတယ်။

toupper(char) -> return Uppercase of Char

```
for (int i = 0, n = strlen(name); i < n; i++)
{
	printf("%c", toupper(name[i]) );
}

```

ဒီ function သုံးလိုက်တာလွယ်တဲ့အပြင် အပေါ်မှာလို char အသေးမဟုတ်ဘဲ အကြီးဆိုရင် ဒီတိုင်း print ထုတ်ဖို့ else ကို သုံးစရာမလိုတော့ဘဲ, <span style="color:rgb(0, 176, 240)">input char က Uppercase</span> ဖြစ်နေရင် <span style="color:rgb(0, 176, 240)">ဒီတိုင်းပြန်ထုတ်</span>ပေး။ 