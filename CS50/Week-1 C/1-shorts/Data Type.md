#C

variable name တစ်ခုပေးပြီး variable တစ်ခုမဖန်တီးခင်မှာ ဒီ variable က ဘာ data အမျိုးအစားလဲဆိုတာ ကြေညာပေးတာ

###### int 

- integer‌ တွကို သုံးဖို့ သိမ်းတဲ့ variable
- take <mark style="background: #ABF7F7A6;">4 bytes</mark> (32 bits) of memory
- 32 bits ပမာဏရှိတဲ့ information တွေကို store လုပ်နိုင်
- 32 bits range ကို positive integer နဲ့ negative integer သိမ်းဖို့ တစ်ဝက်ဆီပိုင်းလိုက်တယ်။ (each get roughly 2 billion numbers)
- ![[integer range.png]] positive int ဘက်မှာ -1 နှုတ်ထားတာက သုညအတွက် နေရာယူလို့

32 bits range ကို တစ်ဝက်စီပိုင်းပေမယ့် 16 bits ဘာလို့မဖြစ်လဲဆို‌တော့   --> split (ပိုင်း) လိုက်တာက sign bit ကို အခြေခံပြီးပိုင်းလိုက်တာ။ sign bits ဆိုတာက binary number မှာ number တစ်ခုရဲ့ အပေါင်းအနှုတ် sign ကို ဖော်ပြဖို့သုံးတဲ့ most significant bit (msb)  
![[two complement system.png]]

Unsigned Integer
	သူက data type အသစ်တစ်မျိုးမဟုတ်ဘဲနဲ့ integer ကိုဘဲ negative value လက်မခံတော့ဘဲ positive value သီးသန့်ယူလိုက်ဖို့ သတ်မှတ်ပေးတဲ့ <mark style="background: #FFB86CA6;">qualifier</mark> ဒါအတွက်ကြောင့် သူလက်ခံနိုင်တဲ့ တန်ဖိုးက double positive range (roughly 4billion) 
	- အကယ်လို့ ကိုယ့် value က negative မဖြစ်နိုင်ဘူးဆိုတာကို သေချာသိရင် unsigned integer ကို သုံးလို့ရ
	![[unsigned integer.png]]

အခြားသော long, short, const အစရှိသဖြင့် qualifier တွေရှိသေးတယ်

###### char

- single character ကို store ဖို့သုံး
- <mark style="background: #ABF7F7A6;">1 byte</mark> (8bits) worth of memory 
- ![[char range.png]]

###### float

- floating point value i.e. real numbers တွေကို store
- <mark style="background: #ABF7F7A6;">4 bytes</mark> (32bits) of memory
- due to complication in describing the total length float, there is floating point imprecision

###### double

- double precision in storing float point 
- <mark style="background: #ABF7F7A6;">8 bytes</mark> (64 bits) of memory

###### void

- <mark style="background: #FFF3A3A6;">type</mark> but <mark style="background: #ABF7F7A6;">not data type</mark> 
- void return type -> function doesn't return value
- void in function parameter -> function takes no parameter
- bit of white lies = void is a placeholder for nothing

printf() has void return type. printf ထဲထည့်လိုက်လို့ terminal မှာ display လုပ်တယ်ဆိုတာက just a side effect of function, printf() က ဘာကိုမှ return မပြန်ပေး

-------------------------------

###### bool

- <mark style="background: #ABF7F7A6;">1 byte</mark> (4 bits) of memory
- not include in five built-in data type of C
- include in cs50.h
- can store only two values: <mark style="background: #BBFABBA6;">true</mark> , <mark style="background: #ABF7F7A6;">false</mark> 
- <span style="color:rgb(0, 176, 240)">Zero (0)</span> represents <span style="color:rgb(0, 176, 240)">false</span>, other <span style="color:rgb(255, 155, 0)">non-zero digits</span> represents <span style="color:rgb(255, 155, 0)">true</span>

###### string

- store a series of characters (words, sentences, paragraphs...)


###### Variable အသုံးပြုခြင်းအခေါ်အ‌ဝေါ်များ

![[variable.png|600]]
