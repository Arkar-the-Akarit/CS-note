#c
```
int x = 1;
int y = 3;

printf("%i\n", x/y); //output Zero only

```

ဆိုရင် output က zero တစ်လုံးထဲထွက်လာမယ်။ 
ဒါဆို format code ကို %i ကနေ decimal point ကို လက်ခံမယ့် %f (for float & double) ကို ဒီု

```
int x = 1;
int y = 3;

float z = x / y;

printf("%f", z);

```
ဆိုပြီး ချိန်းလိုက်မယ်။
ထွက်လာမယ့် output က 0.00000 ဘဲဖြစ်နေဦးမယ်။ ဘာလို့လဲ? Truncation ဖြစ်တာ။

<mark style="background: #FFB8EBA6;">Truncation</mark> : <span style="color:rgb(32, 178, 179)">integer</span> value တစ်ခုကို အခြား <span style="color:rgb(32, 178, 179)">integer</span> value တစ်ခုနဲ့ divide (စား) လိုက်တဲ့အခါမှာ အကယ်လို့ fraction value i.e. decimal value တွေ ရလာခဲ့ရင်တောင် အဲ့ decimal (ဒသမ)/ fraction (အပိုင်းကိန်း) တန်ဖိုးတွေက truncate(လျှော့ချ) i.e. discard (ဖယ်ထုတ်)ခံလိုက်ရတယ်။ ဒါကို programming မှာ truncation ဖြစ်တယ်လို့ဆိုလိုတယ်။

ဒီလိုမဖြစ်အောင် C language မှာ data type ကို ယာယီ ‌convert (ပြောင်း)လို့ရတဲ့နည်းရှိတယ်။ <span style="color:rgb(255, 155, 0)">type-casting</span> လုပ်တယ်လို့ခေါ်တယ်။ 

<mark style="background: #FFB8EBA6;">Typecasting</mark> : ကိုယ်ပြောင်းလိုက်ချင်တဲ့ datatype ကို variable name အရှေ့မှာ parenthesis () လက်သည်းကွင်းနဲ့ ထည့်ပေးရုံဘဲ။

e.g (float) x
သဘောတရားက ဒီ variable က integer data type မှန်း သိပါတယ်။ ဒါပေမယ့် အခုတော့ ခဏလေးသူ့တန်ဖိုးကို float အဖြစ်ယူဆပြီး operations လုပ်ပေးပါ။ ဒီလိုtype-casting နဲ့ဆိုရင် division operation မှာ အဖြေက အပြည့်ကိန်းထွက်ရင်တောင် ဒသမနဲ့ပြပေးမယ်။

```
int a = 2;
int b = 3;
int c = 6;

float y = (float) a / (float) b;
float z = (float) c / (float) c;

printf("%f \n", y); //output will now be 0.666666
printf("%f \n", z); //output will be 2.00000
```

float format code (%f) မှာ percent symbol နောက်က <mark style="background: #D2B3FFA6;">".n" </mark>(ဒသမနဲ့ ဂဏန်းတစ်ခုလိုက်ပေးချင်း)ဖြင့် လိုသလောက် ဒသမအရေအတွက်ထိ ထုတ်လို့ရတယ်။
e.g. %.2f -> ဒသမနှစ်နေရာ
	 %.5f -> ဒသမငါးနေရာ

ဒါပေမယ့် အဲ့လိုကြည့်တဲ့အခါမှာ %.30f တို့ %.40f တို့ဆိုရင် ထွက်လာတဲ့ ဒသမဂဏန်းတွေက နညး်နညး်လွဲလာတယ်။

e.g. code & output
```
float x = 1;
float y = 3;

printf("%.30f \n", x/y);

```

output : ![[float-point-imprecision.png]]
ဒီလိုကြီးထွက်လာတယ်။ တကယ်က 0.3333 အဆုံးမရှိဖြစ်ရမယ်။
float မဟုတ်ဘဲ double သုံးလိုက်ရင်လည်း (format code of double is also %f) output က ![[double imprecision.png]]
0.3 ဆိုပြီး ပိုတိကျတဲ့နေရာများလာပေမယ့် နောက်ပိုငး်နံပါတ်တွေက rounding ဖြစ်နေတုန်းဘဲ။

ဒီလိုဖြစ်သွားတာကို <mark style="background: #FFB8EBA6;">floating-point imprecision</mark> ဖြစ်သွားတယ်လို့ခေါ်တယ်။ သဘောတရားကတော့ computer မှာ finite amount of memory (တိကျသတ်မှတ်ထားတဲ့ memory ပမာဏ) တစ်ခုဘဲရှိနေတဲ့အခါ infinite number of real numbers (တကယ့်ကိန်းတန်ဖိုးအစစ်ကို အဆုံးမရှိတဲ့အထိ) ဖော်ပြဖို့ရာမဖြစ်နိုင်တော့လို့ computer က auto rounding လုပ်ချလိုက်တာဖြစ်တယ်။