#C #String

##### String

```
int main(void)
{
	string s = "HI!";
}

```

<mark style="background: #FF5582A6;">caution</mark> -> char တွေဆိုရင် single quote (' ') နဲ့ရေးပြီး string ဆိုရင် double quote(" ") နဲ့ရေးရပါတယ်။

string ဆိုပြီး ဒီလိုကြေညာလိုက်ရင် memory ထဲမှာ သူက char တွေကို အစဥ်လိုက်လေးသွားပြီး ဒီလို store လုပ်တယ်။

![[hi as string array.png]]

ဘာနဲ့တူလည်းဆိုတော့ အရှေ့က [[Memory & Array#Array|Array]] လိုဘဲတူတူဘဲ။

ဒီတော့ string is an array of characters.
array ဖြစ်တဲ့အတွက် C language မှာ string ကို ဒီလိုလေး ‌manipulate လုပ်လို့ရတယ်

```
printf("%c %c %c \n", s[0],s[1],s[2]);

printf("%i %i %i \n", s[0],s[1], s[2]); // 72 73 66
```
သဘောတရားကတော့ string variable ကို <span style="color:rgb(0, 176, 240)">array လိုဘဲ</span> indexခန်းတွေသုံးပြီး treat လုပ်လို့ရတယ်။

###### Null Terminator

memory ထဲမှာ အစဥ်တိုင်း store လုပ်တယ်ဆိုရင် array/ string တစ်ခု အဆုံးသတ်သွားကြောင်း ကွန်ပြူတာက ဘယ်လိုသိနိုင်မလဲ။

တကယ်တမ်းတော့ string ရဲ့ နောက်ဆုံးနေရာ, input ထည့်ထားတဲ့ character အဆုံးရဲ့ အနောက် index မှာ
<mark style="background: #CACFD9A6;">00000000 </mark> = သုည ရှစ်လုံးပါတယ်။ အဲ့အခန်းကို ကွန်ပြူတာကရောက်သွားတာနဲ့ သုညရှစ်လုံးကို တွေ့ပြီး ဒီstringဟာ ဆုံးသွားပြီဆိုတာကို သိနိုင်တယ်။

![[null terminator in string.png]]

ဒါကို string s = HI! ဆိုရင် s\[2] မှာ \! ကိုရောက်ပေမယ့် s\[3] ဆိုပြီးထုတ်ကြည့်လို့ရတာကို သိနိင်တယ်။ format မှာတော့ %i ထား

```
printf("%i %i %i %i\n", s[0], s[1], s[2], s[3]); 

// 72 73 66 0
```

သုညရှစ်လုံးလုံးပြရင် ရှည်မှာဖြစ်လို့ <span style="color:rgb(146, 208, 80)">0 တစ်လုံးတည်း</span>နဲ့ဖော်ပြတယ်။ program မှာ ဒီလို string/array တစ်ခုဆုံးကြောင်းပြချင်တာကို ထည့်သုံးချင်တယ်ဆိုရင် တကယ့် zero/0 နဲ့ မမှားစေဖို့ <mark style="background: #D2B3FFA6;">\0 </mark> or <mark style="background: #D2B3FFA6;">\000</mark> ဆိုပြီး back slash နဲ့တွဲသုံးတယ်။

\\0 မပါရင် string ဆုံးပြီဖြစ်ကြောင်း computer က မသိတဲ့အတွက် အနောက်က memory ခန်းက ကောင်တွေကိုပါဆက်ပြီး ဖတ်သွားနိုင်တယ်။

အဲ့လို \\000 တွေကို null terminator/null character လို့လည်းခေါ်ကြပြီး <mark style="background: #CACFD9A6;">NUL</mark> လို့လည်း ခေါ်ကြတယ်။ output မှာကတော့ integer format  နဲ့ %i သုံးပြီးတော့ဘဲ 0 ရှိတာကို ထုတ်ကြည့်လို့ရမယ်။

<mark style="background: #BBFABBA6;">null terminator / null character</mark> -> <mark style="background: #CACFD9A6;">\0</mark> or <mark style="background: #CACFD9A6;">NUL</mark>

<mark style="background: #FF5582A6;">Caution</mark> --->  null terminator ကို များသောအားဖြင့် <span style="color:rgb(0, 176, 240)">strings</span> (char arrays meant to treated as text) မှာဘဲ အသုံးများတယ်။ ပြီးတော့ ကိုယ်က <span style="color:rgb(255, 155, 0)">double quote</span> နဲ့ ("Hello") ဆိုပြီး ကြေညာလိုက်မှ <span style="color:rgb(255, 155, 0)">null terminator က auto </span>ပါလာတယ်။ 
အကယ်လို သာမန် fixed size array တစ်ခုကြေညာတယ်ဆိုရင် (e.g. char array) မျိုးဆိုရင် <span style="color:rgb(32, 178, 179)">ကိုယ်တိုင် '\0' ဆိုပြီး index တစ်ခန်းယူမထည့်ပေးသေးသရွေ့ </span>မပါဘူး။ အကယ်လို့ ကိုယ်က char array ကို <span style="color:rgb(255, 155, 0)">typecast </span>လုပ်တာဖြစ်ဖြစ်, <span style="color:rgb(255, 155, 0)">printf တို့ strlen တို့</span> သုံးမယ်ဆိုရင်တော့ <mark style="background: #BBFABBA6;">ပါဖို့လိုတယ်။</mark> မပါလဲအလုပ်လုပ်ကောင်းလုပ်နိုင်ပေမယ့် အနောက်က မဆိုင်တဲ့ memory တွကိုပါ program က ဖတ်နိုင်ချေတအားများ 

###### String Array / Two dimensional Array

```
int main(void)
{
	string words[2];

	words[1] = "HI!";
	words[2] = "BYE!";
}
```

ဒီလို ‌words ဆိုပြီး string array တစ်ခုကြေညာလိုက်မယ်ဆိုရင် ဒီလိုထည့်လိုက်ပြီဆိုတာနဲ့ computer မှာ store လုပ်တဲ့ပုံစံက ဒီလို

![[string array.png]]
words\[0] = HI! , words\[1] = BYE! ဆိုတော့ ဒီလိုမျိုးလေး တစ်လုံးစီ ယူလိုက်လို့လည်းရတယ်။

![[string array 2.png|800]]

ပုံစံက two dimensional array လိုမျိုးဖြစ်သွားတာပေါ့။
```
printf("%c %c %c %i\n" words[0][0], words[0][1], words[0][2], words[0][3] ) 

// output  H I ! 0

printf("%c %c %c %i\n" words[1][0], words[1][1], words[1][2], words[1][3] )

// output B Y E ! 0

```

<mark style="background: #FF5582A6;">Important</mark> - အကယ်လို့ words\[0]\[4] ဆိုပြီး %i နဲ့ထုတ်ချကြည့်လိုက်ရင် B value ဖြစ်တဲ့ 66 ထွက်လာတယ်။ အဲ့လိုက ရလာတာမှန်ပေမယ့် ဂဏန်းများလာရင်/တစ်ခါတလေကျရင် error တက်နိုင်တယ်။ မလုပ်ပါနဲ့ သူ့ index နဲ့ သူသုံး

##### string.h
string တစ်ခုရဲ့ length ကိုသိရဖို့ C မှာ built-in feature မပါပေမယ့် ကိုယ်တိုင်function တစ်ခု‌ရေးလို့ရတယ်။

```
int main(void)
{

}

int string_length (string s)
{
  int n = 0;   // lenght count ဖု့ိရယ်, index အတွက်ရယ် 

  while (s[n] != '\0')  
  {
	 n++ 
  }

 /* 
string = char array , အဲ့တာကြောင့် sရဲ့ index s[n] က NUL  character, '\0' နဲ့ မညီမချင်း while loop နဲ့ n ကို increment လုပ်, တူသွားရင် ရပ်ပြီ ဆက်မတိုးတေ့ာဘူး n value ကို၊ အဲ့တော့ n က တစ်ဆင့် string length ရ 
  */

  return n;
}


``` 

ဒါပေမယ့် C မှာ အဲ့လိုတကူးတကကြီးရေးနေစရာမလိုသလို string အတွက် ဖန်တီးပေးထားတဲ့ "string.h" ဆိုတဲ့ header file ရှိတယ်။

အဲ့ထဲမှာ string length ကို return ပြန်ပေးတဲ့ <mark style="background: #FFF3A3A6;">strlen()</mark> ဆိုတဲ့ function တစ်ခုပါတယ်။ int return ပြန်ပေးတယ်။

```
string name = "David";
int length = strlen(name);

```

C မှာ string နှစ်ခု <span style="color:rgb(0, 176, 240)">တူမတူ နှိုင်းယှဥ်ချင်ရင်</span> Equality operator (=\=) <span style="color:rgb(220, 20, 60)">သုံးလို့ မရ</span>။

<mark style="background: #FFF3A3A6;">strcmp(string1, string2)</mark> function ကို သုံးရတယ်။
- တူရင် Zero(0) return;
- string 1 က string 2 ထက် ငယ်နေရင် negative value return
- string 1 က string 2 ထက် ကြီးနေရင် positive value return

#C #C-loop 
<mark style="background: #BBFABBA6;">trick</mark> --> for loop မှာ initialization လုပ်ရင်လေ နှစ်ခုနဲ့အထက်လုပ်လည်း ရတယ်။ 
```
for (int i = 0, n = strlen(name); i < n; n++ )

```

int i initialization နဲ့ n ကြားမှာ ခြားထားတာ <mark style="background: #ABF7F7A6;">coma (,)</mark> ပါ။ ဒီလိုမျိုး <span style="color:rgb(0, 176, 240)">initialization part မှာ တစ်ခါတည်းကြေညာလိုက်တာမျိုး</span> or '<span style="color:rgb(0, 176, 240)">for' loop အပြင်မှာ variable အနေနဲ့ ကြေညာတာ</span>မျိုးက 
`for (int i =0; i < strlen(name); i++)` လို့ကြေညာတာထက် ပိုကောင်းတယ်။ ဘာလို့ဆို for loop ပတ်တိုင်း boolean အခြေအနေဖြစ်တဲ့ i က strlen() ထက် ငယ်သေးလားဆိုတာကို လာစစ်ဖို့ strlen() ကို ထပ်ခါထပ်ခါ ပြန်ပြန် run နေရမှာမလို့။
