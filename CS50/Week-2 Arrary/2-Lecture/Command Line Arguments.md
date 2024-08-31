#C #CLA

program တွေက terminal ထဲက command line နေရာမှာ user ရိုက်လိုက်တဲ့ command ကို argument အနေနဲ့ယူလိုက်လို့ရတယ်။

for example: clang အနောက်က ရိုက်လိုက်တဲ့ command တိုင်းက command line arguments

အခုထိ main() ရဲ့ arguments မှာ void လို့ဘဲသုံး‌လာခဲ့တယ်။
သူ့ဆီကို command line ကို arguments အနေနဲ့ ‌pass လို့ရတယ်။

```
int main (int argc, string argv[])
{

}
```

ပုံမှန်အားဖြင့်ဒီလိုရေးကြတယ်။
<mark style="background: #FFF3A3A6;">int main (int argc, string argv[])</mark> 

- <mark style="background: #FFB86CA6;">int argc</mark> -> argument count ကို ပြောတာ၊ command line မှာ words ဘယ်နှစ်ခုရိုက်လိုက်လဲဆိုတာကို count လုပ်ပေးတယ်။ 
	e.g.  ./greet ဆိုရင် တစ်ခု, ./greet arkar ဆို နှစ်ခု, ./greet arkar phyo ဆို သံုးခု စသည်ဖြင့် word count ပေပေါ့။

- <mark style="background: #FFB86CA6;">string argv[]</mark> -> argv ဆိုတာက argument vector ကိုပြောတာ, သဘော‌တရားကတော့ argument array ပေါ့။ user က ထည့်လိုက်တဲ့ command line က words တွေကို array ထဲသိမ်းတာပေါ့။

int argc, string argv\[] တို့က ပေးချင်တဲ့ နာမည်ပေးလို့ရပါတယ်။ သ‌ဘောပေါက်လွယ်အောင် naming convention အနေနဲ့ argc & argv ဘဲ သုံးကြတာများတယ်။

###### Example Programs

```
// greet.c

#inlcude<cs50.h>
#include<stdio.h>

int main(int argc, string argv[])
{
	printf("Hello %s\n", argv[1]);
}

/*
in cmd:

make greet
./greet Arkar

hello Arkar <--  output 

*/
```

terminal ထဲမှာ user က ./greet နဲ့ နာမည်ရိုက်လိုက်တဲ့အခါမှာ 
printf ထဲက terminal ထဲက command line ကို argument အနေနဲ့ ယူပြီး output  ပြန်ထုတ်ပေးတာကို တွေ့ရမယ်။

`printf("hello %s\n", argv[0])` ဆိုရင် ဘာထွက်လာမလဲ
`Hello ./greet` ဆိုပြီး output ပြန်ထွက်လာမယ်။
ဒီတော့ argv array ထဲက<span style="color:rgb(32, 178, 179)"> index 0 မှာ program name ကရောက်</span>နေမယ်ဆိုတာကို သိရမယ်။ ဘာလို့လဲဆို program ကို run ဖု့ိ ./program_name က မဖြစ်မနေရိုက်ရမှာကိုး ။

`./greet arkar` ဆိုပြီး<span style="color:rgb(255, 155, 0)"> argc count ၂ ခုစာဘဲ</span> ရိုက်ထားပြီး <span style="color:rgb(146, 208, 80)">argv[3]</span> ကို printf ထဲမှာ ထည့်ထားရင် ဘာထွက်မလဲ  
`hello (null)` ဆိုပြီး null terminator ထွက်လာမယ်။

ဒီလိုမဖြစ်အောင် error checking ဒီလိုလုပ်လို့၇တယ်ပေါ့။
```
int main(int argc, string argv[])
{
  if (argc == 2) // cla မှာ words 2 ခုဘဲရှိမှ
  {
   printf("Hello %s \n",argv[1]);
  }
  else 
  {
  printf("hello world \n");
  }
}

```

ဒါဆိုရင်တော့ user က terminal မှာ words count ၂ ခုဘဲ မရိုက်တာနဲ့ hello worldပေါ့။ လျော့ရိုက်ရိုက် တိုးရိုက်ရိုက် hello world ဘဲ။ 

terminal ထဲထည့်လိုက်တာမှန်သမျှ ပြန်ပြဖို့
```
int main (int argc, string argv[])
{
 for (int i = 0; i < argc; i++)
 {
  printf("%s \n", argv[i]);
 }

}

```
ဒါဆိုရင်တော့ terminal ထဲ ရိုက်သမျှ command အကုန် တစ်ကြောင်းစီနဲ့ ပြန်ပြမယ်။ 

