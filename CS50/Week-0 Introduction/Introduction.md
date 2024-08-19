###### What is Computer Science?

computer programming ဆိုတာမျိုးက input အချို့ထည့်သွင်းလိုက်ပြီး ထွက်လာတဲ့ output ကြောင့် ပြဿနာဖြေရှင်းနိုင်သွားတာမျိုးကို ဆိုလိုတယ်။

input & output ကြားထဲမှာ ဖြစ်ပျက်သွားတဲ့ အရာတွေကို black box လို့ ခေါ်ပြီး CS study က အဲ့ black box ကို အထူးပြုလေ့လာတာမျိုး။

![[computer-programming.png]]

သင်္ချာဂဏန်း 'တစ်' လုံးတည်း အသုံးပြုထားတဲ့ ကိန်းဂဏန်းတစ်ခု ကို တစ်လုံးကိန်း Unary Digit လို့ခေါ် 
သင်္ချာဂဏန်း 'နှစ်'  လုံးတည်းအသုံးပြုထားတဲ့ ကိန်းဂဏန်းကို  နှစ်လုံးကိန်း Binary Digit လို့ခေါ်  bit

- ကွန်ပြူတာ‌တွေက binary system (base 2 ) ကို အသုံးပြုတယ်။
- computer ရဲ့ binary system မှာပါတဲ့ ဂဏန်းနှစ်လုံးက zero & one 
- binary digit တွေကို bit လို့ခေါ်တယ်။ A bit can be zero or one / on or off
- eight bits = one byte , ကွန်ပြူတာတွေဟာ ပုံမှန်အားဖြင့် byte တွေကို သုံးပြီးတော့ သင်္ချာကိန်းဂဏန်း (base 10 system) တွေကို ဖော်ပြတယ်။ 8 bits (1 byte) နဲ့ base 10 number - 255 (from 0) ထိရေတွက်လို့ရတယ်။ binary 11111111 = 255 (base 10)

![[bit & byte.png]]

binary digit တစ်လုံးက one or zero ဘဲဖော်ပြနိုင်တယ်။ ဒါပေမယ့် binary digit တစ်လုံး ထက် ပိုလာမယ်ဆိုရင် ဖော်ပြနိုင်တဲ့ ကိန်းတွေ ပိုများလာမယ်

E.g. Binary Digits = Decimal Numbering System 
		0 0 0      =  0
		0 0 1      =  1
		0 1 0      =  2
		0 1 1      =  3
	    1 0 0      =  4
	    1 0 1      =  5 
	    1 1 0      =  6
	    1 1 1      =  7 .......

အလွယ်တွေးကြည့်မယ်ဆိုရင်
binary digit သုံးလုံးဆိုရင် ရှေ့ဆုံးက 4 ကို ရည်ညွှန်းပြီး၊ အလယ်က ကောင်ကကျ 2 ကို ရည်ညွှန်း၊ နောက်ဆုံးကကောင်က 1 ကို ရည်ညွှန်းတယ်
![[binary digits in herusitic ways.png]]

ကွန်ပြူတာက base-2 system ကို အသုံးပြုထားတယ်
![[base-2.png]]

###### ASCII 

American Standard Code for Information Interexchange

number ‌တွေကို one and zero ဘဲပါတဲ့ binary digit systems တွေနဲ့ ဖော်ပြသလိုဘဲ letters (A-Z, a-z, @, ! ..) တွေကိုလည်း computer က one and zero နဲ့ဘဲဖော်ပြတယ်။

one & zero နဲ့ နံပါတ်တွေ ကို သင်္ချာဂဏန်း 255 ထိဖော်ပြလိုက်သလိုဘဲ letters တွေကို ဖော်ပြတဲ့အခါ overlap (ထပ်)သွားတာမလို့ ASCII က တူညီတဲ့ 8 bits number ရှိတဲ့ base 10 numbers တွေနဲ့ alphabet letters ကိုတွဲပေးလိုက်တယ်။

![[ASCII table.png]]

ဥပမာကွာ 72 73 33 ဆိုရင် အဲ့နံပါတ်တွေကို ascii နဲ့  ချိတ်လိုက်တဲ့အခါမှာ HI! ဆိုပြီးရတယ်။
![[hi!.png]]

###### Unicode

binary (one & zero) system ကို အခြေခံထားတဲ့ ascii system က 0 - 255 (total 256) အထိဘဲ ရေတွက်လို့ရတာမလို့ ASCII နဲ့ ဖော်ပြလို့ရတဲ့ အက္ခရာစာလုံးတွေက Limit ရှိတယ်။ english characters တွေအတွက်က အဆင်ပြေပေမယ့် အခြားသော human language တွေအတွက်က binary system နဲ့ဖော်ပြဖို့ digits မလုံလောက်တော့တဲ့အခါ

hexadecimal (base 16) system ကိုအခြေခံထားတဲ့ **Unicode** standard ဆိုတာ ပေါ်ပေါက်လာတယ်။ သူနဲ့ဆိုရင် bit တစ်ခုကတောင် ဖော်ပြနိုင်တာ‌တွေအများ(from 0 - F) ကြီးမလို့ စာသားတွေအပြင်ကိုမှ emoji ‌တွေထိပါ ဖော်ပြနိုင်လာတယ်။

thumb up emoji = U+1F44D (U+ = represent Unicode)
အဲ့တာကိုမှ ကာလာတွေထပ်ထည့်ချင်တဲ့အခါ U+1F44D U+1F3FD အဲ့လိုမျိုးလေးတွေပြတယ်။ 
‌ကောင်လေးနဲ့ကောင်မလေး အလယ်မှာ အသည်းပုံနဲ့ emoji ဆိုရင်လည်း ကောင်လေး emoji ကောင်မလေး emoji နဲ့ အသည်းပုံ emoji ရဲ့ code တွေကို ပေါင်းထားတာ

###### Representation



