#C #C-compiling

compiling လုပ်တယ်ဆိုတာက source code တစ်ခုကို machine code တစ်ခုအဖြစ်ပြောင်းပေးတာလို့ အလွယ်မှတ်လို့ရတယ်။

cs50 မှာ သုံးနေတဲ့ `make` command ဟာ တကယ်တေ့ာ source code ကနေ machine code ကို run ပေးတဲ့ compiler ကိုခေါ်ပြီး run ပေးတဲ့ command တစ်ခုသာဖြစ်တယ်။

သုံးတဲ့compiler အမျိုးအစားက <span style="color:rgb(146, 208, 80)">clang</span> လို့ခေါ်တဲ့ C Language အတွက် compiler တစ်မျိုးဖြစ်တယ်။ အခြားသော compiler တွေရှိသေးပေမယ့် clang က error message ပြတဲ့အခါမှာ ရှင်းလင်းလို့ အသုံးများတယ်။

helloworld.c program:
```
#include <cs50.h>
#inlcude <stdio.h>

int main(void){
	printf("Hello World\n");
}

```

အပေါ်က helloworld.c ကို compiler run ချင်ရင် command က
```
clang hello.c
```

ဆိုပြီးထွက်လာတယ်။ အဲ့မှာ ရလာမယ့် executable file က make နဲ့သုံးလိုက်သလို ကိုယ်ပေးထားတဲ့ file နာမည်အတိုင်းရလာမှာ<span style="color:rgb(220, 20, 60)">မဟုတ်ဘဲနဲ့</span> ပထမဆုံးလုပ်တာဆို `‌./a.output` ဆိုတာမျိုးဖြစ်မယ်။ run ချင်ရင် `./a`  အဲ့လိုခေါ််ပြီး run ရတာပေါ့။ အဲ့တာကိုမှာ ကိုယ်ပေးထားတဲ့ file name အတိုင်းရချင်တယ်ဆိုရင် 
<span style="color:rgb(0, 176, 240)">command line arguments (i.e. options)</span> ကိုသုံးရတယ်။
arguments က `-o`
```
clang -o hello hello.c
```
ဆိုပြီးဖြစ်မယ်။

hello.c program:
```
#include <cs50.h>
#include <stdio.h>

int main(void){
  
  string name = get_string("What's your name? : ");
  printf("Hello, %s\n", name);

}

```

အပေါ်က hello.c program ကို compiler သုံးမယ်ဆိုရင် error တက်မယ်။ 
![[clang error.png]]
get_string ဆိုတာကို မသိဘူး။ ဒီတော့ cs50 ဆိုတဲ့ external header file တစ်ခုကို သုံးထားတာသိအောင် argument `-l` (for link) နဲ့ header file နာမည်ကို တွဲသုံးရတယ်။
```
clang -o hello hello.c -lcs50
```


###### in header file

cs50.h , stdio.h ထဲမှာ ဘာတွေသလဲ။ သူတို့ထဲမှာ printf(), getstring()... စတဲ့ function တွေကို အသေးစိတ်ရေးထားတာ မပါဘဲနဲ့ <span style="color:rgb(146, 208, 80)">function prototype</span> တွေဘဲပါတယ်။ တကယ့် အသေးစိတ်က <span style="color:rgb(255, 105, 180)">cs50.c, stdio.c စတဲ့ file တွေထဲမှာရှိနေ</span>ပြီးတော့မှ local directory/server တစ်ခုထဲမှာရှိနေတယ်။ compile လုပ်တေ့ာမှ သူတို့ဆီကနေသွားယူသုံးတာမျိုးဖြစ်တယ်။

###### Process of turning source - machine code

source code ကနေ machine code ပြောင်းတာကို အလွယ်အနေနဲ့ compile လုပ်တယ်လို့ပြောပေမယ့် compiling က source to machine code process လေးခုထဲက တစ်ခုဘဲဖြစ်တယ်။

1. Preprocessing
2. Compiling
3. Assembling
4. Linking

1. Preprocessing
	\# နောက်မှာ ပါတဲ့ကောင်တွေကို C မှာ <span style="color:rgb(32, 178, 179)">preprocessor directive</span> လို့ခေါ်တယ်။
	preprocessing လုပ်တယ်ဆိုတာက \#include နောက်မှာပါတဲ့ header fileတွေကို ကိုယ့်ရဲ့ source code ထဲမှာ copy paste လာလုပ်တဲ့သဘောဘဲ၊ header ထဲမှပါပြီး ကိုယ်သုံးထားတဲ့ function တွေကို လာကြေညာတာပေ့ါ။ အပေါ်က hello.c program လိုမျိုးမှာဆိုရင်
	![[preprocessing.png]]ဆိုပြီး ဖြစ်သွားတယ်။ ဒါက နညး်လို့ သိသာတာ။ header ထဲမှာ ပါတဲ့ function အများကြီးကို သုံးမယ်ဆိုရင် အဲ့လို လိုက်ကြေညာနေတာထက် preprocessor directive နဲ့သုံးတာပိုကောငး်တာပေါ့။

2. Compiling
	source code ထဲမှာသုံးထားတဲ့ function တွေကိုလည်း အကုန်စုပြီးပြီဆိုရင် source code ကို assembly code အဖြစ် ပြောင်းပေးတယ်။
	hello.c in assembly language:
	![[hello.c in assembly.png]]

3. Assembling
	ဒီအဆင့်မှာ compiler က assembly code ကို machine code အဖြစ်ပြောင်းပေးတယ်။ hello.c as machine code:
	![[hello.c as machine code.png]]

4. Linking
	header နှစ်ခုဖြစ်တဲ့ cs50.h နဲ့ stdio.h ရဲ့ အခြေက cs50.c နဲ့ stdio.c ဆိုတာ အပေါ်မှာ mentioned, အဲ့ c file နှစ်ခုကလညး် ဒီအဆင့်မှာ machine code အဖြစ်ပြောင်းပြီးတော့မှ မူလ source code နဲ့ ပေါင်းလိုက်တာ ဒီတော့ machine code က file သုံးခုစာ - hello.c cs50.c stdio.c, and then linked together
	![[linking.png]]