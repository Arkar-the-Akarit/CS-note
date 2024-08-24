###### program in cs50.dev

```
in terminal : 
$ code hello.c
$ make hello
$ ./hello
```

<mark style="background: #CACFD9A6;">code hello.c</mark> --> create hello.c file , ဒီ command က တကယ်တော့ vsCode ကိုဖွင့်တဲ့ code command, အနောက်က file လိုက်လိုက်တော့ ရှိရင် open, မရှိရင် create လုပ်တာမျိုး
<mark style="background: #CACFD9A6;">make hello</mark> --> create လုပ်လိုက်ပြီး text editor ထဲမှာ code ရေးမယ်။ အဲ့ code file ကို make fileName နဲ့ compile လုပ်ပြီး machine code ပြောင်းပြီး executable fileတစ်ခုထုတ်ပေးမယ်။  သတိထားရမှာက file ကို create လုပ်ရင်သာ file extension (.c) ထည့်ရပေမယ့် make နဲ့ compile လုပ်တဲ့ အချိန်မှာတော့ file name ဘဲပါရင် ရပြီ။
အကယ်လို့ file မှာ<span style="color:rgb(0, 176, 240)"> တစ်ခုခု changes</span> လုပ်လိုက်ရင် make နဲ့ ထပ်ပြီးတော <span style="color:rgb(146, 208, 80)">executable file အသစ်ထပ်ဆောက်</span>မှသာ file အသစ်အတိုင်း run နိုင်မှာဖြစ်တယ်။

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

###### Variables

variable ဆိုတာက ပြုပြင်ပြောင်းလဲလို့ရမယ့် တန်ဖိုးတစ်ခု။
သူ့ထဲမှာ user က input ထည့်လိုက်တဲ့ စာသား/တန်ဖိုးတွေဖြစ်ဖြစ်, program ကနေ ခဏသိမ်းချင်တဲ့ တန်ဖိုးတွေဖြစ်ဖြစ် ထည့်သိမ်းထားလို့ရတယ်။ i.e. special holding place

###### Input & Output in C

```
#include <stdio.h>

int main(void){
	string answer = get_string("What's your name?");
	printf("Hello, %s", answer);
}

```

get_string () ဆိုတာက user ဆီက string of text ကို ရယူတဲ့ function

string answer ဆိုတာက user ဆီက ရလာမယ့် input ကို answer လို့ခေါ်တဲ ့ variable ထဲထည့်သိမ်းမယ်လို့ပြောတာ။ user ဆီက လာမယ့် Input data က string ဖြစ်လို့ ‌‌answer ရှေ့မှာ သူ့ data type ကို တစ်ခါတည်းကြေညာပေးတာ။ data type can be int, bool, char...

ဒီ program ကို run လိုက်ရင် error တက်မယ်
![[error reading in C.png]]
hello.c --> file name 
သူ့နောက်က 5:5 ဆိုတာက အရှေ့က line number , အနောက်က column.. line number 5, column 5 မှာ error တက်နေတယ်ပေါ့။ 

ဘာဖြစ်တာလဲဆိုတော့ C language မှာက string ဆိုတဲ့ variable ကို originally support မပေးထားဘူး။ အဲ့လိုဘဲ သူ့နောက်က getstring() function ကလည်း cs50.h file ထဲမှာဘဲရှိတာ။ အဲ့တာကိုလည်း mention မလုပ်ထားဘူး။ ဒါကြောင့်မလို့ အပေါ််ဆုံးမှာ `#include <cs50.>` လို့ကြေညာပေးလိုက်ရင်ပြီ။

`printf("Hello, %s", answer);`
အခြားသော programming language တွေမှာက variable ကို output ထုတ်ချင်ရင် variable name ကို ခေါ်လိုက်ရင် ၇ပေမယ့် C မှာ အဲ့ variable format code ကို အရင် ခေါ်ရတယ်။ အပေါ်က စာကြောင်းမှာဆိုရင် %s ဆိုတာလေးပေါ့။ (%s --> string) အဲ့လိုလေးထည့်ရတယ်။ ပြီးတော့မှ <span style="color:rgb(0, 128, 128)">quotation mark ("") အနောက်မှာ coma လေးခြားပြီး</span> variable name ကို‌ခေါ်ရတယ်။ 

%s -> for string
%c -> for character
%f -> for float number
%i -> integer
%li -> long integer

###### Boolean Expression

if else, while ဘာညာ အနောက်မှာ () နဲ့ အထဲက နှိုင်းယှဥ်တဲ့ဟာကို boolean expression လို့ခေါ််တယ်။ 
သူက အထဲကဟာက မှန်တယ် (1), မှားတယ် (0) ဆိုတာကိုဘဲ ပြန်လာတာ။ အဲ့တာပေါ်မူတည်ပြီးမှ သက်ဆိုင်ရာ code block ကို run တာ။
ဒီတော့ variable နှစ်ခု မယှဥ်ဘဲနဲ့လည်း အလုပ်လုပ်သွားလို့ရတယ်။

e.g. if(x) --> x value က 1 ဖြစ်နေရင် အောက်က code block ကို run မယ်။ အခြား value ဆို else ပါရင် else ကိုဆက် run မယ်။

###### Equal (=\=) vs Assign (=)

သာမန်သင်္ချာမှာတော့ x = 10 ဆိုရင် x ဟာ 10 နဲ့ညီတယ်ပေါ့။

တကယ့်သဘောတရား (‌also in programming) x တန်ဖိုးအဖြစ် 10 ကိုထည့်သွင်း ‌(‌assign) လုပ်လိုက်တာ
e.g. x = y ဆိုရင် x တန်ဖိုးနေရာမှာ y တန်ဖိုး ထည့်သွင်းလိုက်တာ

x =\= y မှ x တန်ဖိုးဟာ y တန်ဖိုးနဲ့ ညီတယ်လို့ဆိုလိုတာဖြစ်ပြီး conditional တွေနဲ့စစ်ချင်ရင် အဲ့လိုစစ်ရတယ်။ 

###### Conditionals

if () else () , while () စတာတွေက အခြေအနေနဲ့ဆိုင်တဲ့ conditional code block


###### Increment & Decrement of Variable

x = 0 ;  x တန်ဖိုးထဲကို zero ဆိုတဲ့ value ထည့်

`x = x + 1 ;`
`x += 1 ;`
`x = x++`;
အပေါ်ကုတ် သုံးကြောင်းလုံးရဲ့ သဘောတရားက လက်ရှိ x တန်ဖိုးကို တစ်ပေါင်းပြီး variable x ထဲကို အဲ့တန်ဖိုး ပြန်ထည့်လိုက်တာဘဲဖြစ်ပါတယ်။

```
x = x - 1;
x -= 1;
x = 
x--;
```


###### Single character in C

single character တွေရေးရင် single quote '' နဲ့ရေးလို့ရတယ်။
e.g 'x' , 'y'

###### Expression 'OR'

ဒါမဟုတ်ရင် ဒါ ဆိုပြီး or ဆိုတဲ့ expression ကို programming မှာ --> || နဲ့ ဖော်ပြတယ်။

e.g. (if x =\= 'y' || x =\= 'Y' )
-> x ဟာ y (အသေး) နဲ့ ညီသည်ဖြစ်စေ ဒါမှမဟုတ် Y (အကြီးနဲ့) ညီသည်ဖြစ်စေ


###### Custom function in C

printf() တို့လိုမျိုး function တွေကို C မှာ ကိုယ်တိုင်ဖန်တီးလို့ရတယ်။

```
void meow(void){
	printf("meow\n");
}
```

<span style="color:rgb(0, 176, 240)">void</span> meow(<span style="color:rgb(255, 155, 0)">void</span>)
<span style="color:rgb(0, 176, 240)">void</span> -> ပထမဆုံး void က ဒီ function က ဘာ return value မှ မပြန်လာဘူး။ ဘာတန်ဖိုးမှ ပြန်မထုတ်ပေးဘူး။ သူ့ထဲက code ကိုဘဲ run ပေးမယ်။
meow -> function ရဲ့ နာမည်။ အဆင်ပြေသလိုပေးလို့ရ
<span style="color:rgb(255, 155, 0)">void</span> -> ဒုတိယ void က ဒီ function ထဲမှာ arguments မပါဘူးလို့ပြောတာ။ arguments ဆိုတာက function ကိုခေါ်တဲ့အချိန် value တစ်ခုထည့်ပေးလိုက်ပြီး function အထဲက code တစ်နေရာမှာ အဲ့ value ကို ပြန်သုံးနိုင်တာမျိုး

C မှာဆိုရင် function တစ်ခုကို main function ရဲ့ အောက်မှာ သွားရေးပြီး main ထဲကနေ လှမ်းခေါ််သုံးရင် အလုပ်မလုပ်ဘူး။ main function ရဲ့ အပေါ်မှာ ကြေညာပေးရတယ်။ ဒါပေမယ့် အဲ့လိုကြေညာတာက function တွေများလာရင် code တွေပွထလာတယ်။ ဒီတော့ အတိုကြေညာဖို့က prototype of function / function prototype ဆိုတာကို သုံးတယ်။

function တစ်ခုရဲ့ တွန့်ကွင်း curly braclet {} အောက်ကဟာမပါဘဲ ရှေ့ကအပိုင်းလေးတွေဘဲကို function prototype လို့ခေါ််တယ်။
e.g. void meow (void);
အဲ့လိုလေး။ အဲ့ကောင်လေးကို main function အပေါ်မှာ ကြေညာပေးလိုက်ရင် တိုတိုနဲ့ ခေါ်သုံးလို့ရသွားတယ်။ သူ့အလုပ်လုပ်ပုံက compiler ကို ဒီ function လေးတော့ အောက်မှာရှိတယ်။ အခုအကျယ်မပါသေးပေမယ့် ခေါ်သုံးတဲ့အချိန်ရှိနေမှန်းသိစေတယ်။

```
void meow (int n)
{
	for (int i = 0; i < n; i ++)
	{
	  printf("meow\n");
	}
}

```

ဒီမှာဆိုရင် no argument - void မဟုတ်တော့ဘဲ int n ဆိုပြီးဝင်လာတယ်။ အဲ့ ‌argument - n ရဲ့ တန်ဖိုးက အောက်က for loop condition နေရာမှာထည့်ထားတယ်။ ခေါ််သုံးတဲ့အချိန် function အနောက်မှာ argument value ပါတစ်ခါတည်းထည့်ပေးရမယ်။

int n ဆိုပြီး data type ကို ပါတစ်ခါတည်းကြေညာပေးရတယ်။ argument က လက်ခံတဲ့အခါမှာလည်း integer data type ကိုဘဲ လက်ခံမယ်လို့ ကြေညာတာ။

```
#include <stdio.h>
#include <cs50.h>

void mewo(int n);

int main(void){
	meow(3);
}

void meow(int n){
	for (int i=0; i<n; i++){
	printf("mewo\n");
	}
}

```

```
int add(int a, int b){
	return a+b;
}
```

ဒီ function မှာဆိုရင် ‌‌‌‌ရှေ့ဆုံးက void မဟုတ်တော့ဘဲ int ဆိုတဲ့ data type ဖြစ်သွားတယ်။ ဒီ function ရဲ့ return value က integer data type ဖြစ်မယ်။ ဒီ function ကို ခေါ်သုံးလို့ရှိရင် integer ဖြစ်တဲ့ ဂဏန်းတစ်ခုပြန်လာမယ်လို့ပြောတာ။

function တွေကို function ထဲမှာ ထပ်ခေါ်လို့ရတယ်။
e.g. printf("output is %i", add(x,y));

###### Scope 

scope = context where variable exists 

variable တည်ရှိနေတဲ့ နေရာပေါ့။ 

```
int a = 0;

int main(void){
	int b = 0;
}

void test(void){
	 int c = 1;
}

```

variable တည်ရှိနေတဲ့ နေရာကို ခြားနားပေးတာက curly bracket {} တွေ။ 

int b ဆိုရင် main function() ထဲမှာတည်ရှ‌ိနေတယ်။ သူ့ scope က main function ဘဲ။
int c ဆိုရင် test() ထဲမှာ တည်ရှိနေတယ်။ သူ့ scope က test

အဲ့ကောင်လေးတွေကို local scope လို့ခေါ်တယ်။ b ကို test ထဲမှာ သွားသုံးလို့မရသလို, int c ကိုလည်း main ထဲကနေ ဒီတိုင်းသုံးလို့မရဘူး။

int a ကျတော့ ကွာသွားပြီ။ သူက function တွေရဲ့အပြင်မှာ လာကြေညာထားတာ။ သူ့ကိုကျ global scope လို့ခေါ်တယ်။ သူ့အောက်က ကြိုက်တဲ့ function တွေကနေ ‌ယူသုံးလို့ရတယ်။