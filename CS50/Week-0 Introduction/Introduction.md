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

Zeros & Ones (Binary)တွေဟာ အရောင်တွေကိုဖော်ပြဖို့လည်းသုံးလို့ရတယ်။

RGB coloring မှာဆိုရင် R/ G/ B တစ်‌ရောင်စီကို (၀-၂၅၅) ပေးချင်းအားဖြင့် အရောင်စပ်လိုက်လို့ရတယ်။
![[rgb-color.png]] = ![[rgb_result.png]]

ASCII မှာဆိုရင်ကျ 72, 73, 33 က "HI!" ဆိုတဲ့ textကို ကိုယ်စားပြုတာ။
ဒီတော့ ဘာကိုသိထားရမလဲဆိုရင် <mark style="background: #ADCCFFA6;">"Context Matters"</mark> -  binary digits တွေကို သုံးလိုက်တဲ့ အခန်းကဏ္ဍက အရေးပါတယ်။ 
	စာပို့တဲ့ application တွေမှာဆိုရင် 72,73,33 ဆိုတဲ့ numbers ‌တွေက hi! လို့ပြမှာဆိုပေမယ့် ပန်းချီဆွဲတာတို့၊ ps တို့မှာဆိုရင်တော့ အရောင်ကို ကိုယ်စားပြုသလိုမျိုးပေါ့

- ဓာတ်ပုံတွေဆိုတာ RGB values တွစုထားတဲ့ a collection of RGB values
- Zeros & Ones တွက ပုံတွေ, ဗီဒီယို, နဲ့ သီချင်းတွေကိုကအစ ဖော်ပြနိုင်တယ်။
- ‌ဗီဒီယိုတွေဆိုတာ ဓာတ်ပုံအတွဲလိုက်အများကြီးစုထားတဲ့ဟာတွေ 
- သီချင်းတွေကို MIDI data နဲ့ဖော်ပြလို့ရ

###### Algorithms

ပြဿနာကို ဘယ်လိုဖြေရှင်းမယ်ဆိုပြီး ချဥ်းကပ်တဲ့ နည်းတွေကို ‌‌algorithms လို့ခေါ််တယ်။ problem-solving က computer science မှာရော computer programming မှာရော အခြေခံကျတယ်။

e.g. ပြဿနာတစ်ခုရှိမယ်။ ဖုန်းစာအုပ်ထဲက နာမည်တစ်ခုကိုရှာဖို့
```
alogrithm - 1: 
တစ်မျက်နှာချင်းဆီမတွေ့မချင်းရှာသွားမယ်။

algorithm - 2:
တစ်ခါလှန် နှစ်မျက်နှာဆီ လှန်သွားမယ်။

algorithm - 3:
စာအုပ်ရဲ့ အလယ်ကိုသွားမယ်။ ရှာချင်တဲ့နာမည်က ဘယ်ဘက်မှာရှိလား၊ ညာဘက်မှာရှိလား ကြည့်မယ်။ ညာဘက်မှာရှိရင် ညာဘက်ခြမ်းကို နှစ်ပိုင်းပိုင်း အလယ်ကိုသွားမယ်။ အဲ့လိုနဲ့ ရှာချင်တဲ့ နာမည်ကိုမတွေ့မချင်း တစ်ဝက်စီ ပိုင်းသွားမယ်။

```

ဒီ algorithms တွေ ဘယ်လောက်မြန်တယ်ဆိုတာကို big-0 notation နဲ့ ဒီလိုကြည့်လို့ရတယ်။

![[big-O notation for name searching.png]]
1. မျဥ်းအနီနဲ့က algorithm-1 ကို ကိုယ်စားပြုတယ်။ problem ကြီးလာလေလေ time to solve က ပိုမြင့်လာ‌လေလေဘဲ။ အချိန်ပိုကြာတာပေါ့။ တစ်မျက်နှာချင်းဆီရှာရမှာဆိုတော့ အခါတစ်ရာရှာရမှာ

2. နှစ်မျက်နှာဆီသွားရင်ကျ နှစ်ဆပိုမြန်တယ်။ ဒီတော့ n by 2 

3. algorithm - 3 ကျက line အစိမ်းလေး။ တစ်ဝက်ဆီခွဲသွားတာဖြစ်တဲ့အတွက် log<sub>2</sub>n ပေါ့။ ဒီလို နည်းက အမြန်ဆုံးဘဲ။ သူက problem ကို တစ်က်ဆီပိုင်းသွားတာဖြစ်လို့။ အခု တစ်ရာကနေ နှစ်ရာအဖြစ် နှစ်ဆ တိုးသွားရင်တောင် တစ်ဝက် တစ်ခါထပ်ပိုင်းရုံနဲ့ ရတဲ့အတွက် - problem size နှစ်ဆဖြစ်သွားရင်တောင် တစ်ခါဘဲထပ်တိုးပြီး ‌‌ဖြေရှင်းစရာလိုတယ်။ extra efficient

###### Pseudocode

- pseudocode တစ်ခုဖန်တီးနိုင်တာက computer programming မှာ အလုပ်ပြီး‌မြောက်ဖို့ အရေးပါတယ်

- pseudocode ဆိုတာက program code ကိုမှ ဘယ်သူဖြစ်ဖြစ်ဖတ်လို့ရမယ့်ပုံစံမျိုး
- pseudocode က အရေးကြီးရတဲ့အဓိကနှစ်ချက်
	1. problem/ပြဿာနာ ဖြေရှင်းဖို့နည်းကို ကြိုတင်ပြီး logic (အချက်ကျကျ) တွေးတောထားရလို့
	2. pseudocode ရေးထားလိုက်ရင် ကိုယ်ဘာlanguage နဲ့ program ကိုရေးရေး၊ ကိုယ့်ရဲ့ coding decision နဲ့ program ဘယ်လိုအလုပ်လုပ်သွားတယ်ဆိုတာ သိချင်တဲ့ သူတိုင်းကို pseudocode လေးပေး‌လိုက်ရင်ရပြီရပြီ

Pseudocode for Algorithm-3
```
1  Pick up phone book
2  Open to middle of phone book
3  Look at page
4  If person is on page
5      Call person
6  Else if person is earlier in book
7      Open to middle of left half of book
8      Go back to line 3
9  Else if person is later in book
10     Open to middle of right half of book
11     Go back to line 3
12 Else
13     Quit

```

Pseudocode ထဲမှာ ရှိတဲ့ unique features လေးတွေ
	- pseudocode ထဲမှာ စာကြောင်းအချို့က 'pick up', 'open', 'look at' တို့နဲ့ စထားတာကိုတွေ့ရမယ်။ အဲ့တာတွေကို --> function လို့ခေါ်
	- အချို့လိုင်းတွေမှာက 'if' / 'else if ' စတဲ့ statements တွေနဲ့စထားတယ်။ --> conditionals လို့ခေါ်
	- စာသားအချို့ကကျ မှန်/မှား (true or false) ဆိုပြီး ဆုံးဖြတ်ရတာမျိုး e.g. "person is earlier in the book" ဆိုတာမျိုးတွေ, ရှိလား မရှိဘူးလားပေါ့ --> boolean expression လို့ခေါ်
	- 'go back to line 3' ဆိုပြီး တစ်နေရာရာကို ပြန်သွားခိုင်းတာမျိုးကျ    --> loop 
	- အပေါ်က အခေါ််အဝေါ်/အယူအဆလေးတွေက programming မှာ အခြေခံဘဲ

###### Artificial Intelligence

<mark style="background: #CACFD9A6;">Large Language Models (LLMs)</mark> တွေကို သုံးပြီး AI တွေကို ဖန်တီးလို့ရတယ်။ သူတို့ code blocks အကြီးကြီးတွေထဲကနေမှ patternsတွေနဲ့ ဘယ်စာလုံးပြီးရင် ဘယ်စာလုံးသွားမယ်ဆိုတာကို ခန့်မှန်းပြီး users တွေနဲ့ Interact လုပ််နိုင်တယ်။

###### Scratch

block ‌လေးတွေကို ချိတ်ပြီး program ရေးနိုင်အောင်လုပ်ထားတဲ့ visual programming language
MIT (မြန်မာက မဟုတ်ပါ) က develop လုပ်ထားတယ်။

scratch ရဲ့ coordinate system က ဒီလိုသွားတယ်

![[scratch-coordination.png]]

###### Abstraction

pseudocoding လိုဘဲ abstraction ကလည်း Programming အပိုင်းမှာ အရေးကြီးတဲ့ concept တစ်ခုဘဲ။

abstraction ဆိုတာက ပြဿနာကြီးတစ်ခုကို သေးသေးလေးတွေဖြစ်အောင် ပိုင်းပိုင်းသွားတာကိုပြောတာ။ 


6600 + 5200 - rate 2100