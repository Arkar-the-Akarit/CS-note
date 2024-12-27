color တွေရယ် computer memory အပိုင်းတွေမှာ binary or decimal တွေကိုသုံးတာထက် ပိုပြီးအဆင်ပြေတဲ့ <mark style="background: #BBFABBA6;">hexadecimal</mark> တွေကိုသုံးကြတယ်။ ဘာလို့လဲဆိုတော့ ဂဏန်းတစ်ခုကို binary တွေနဲ့ 8 bits (1 byte), 1 bit ရှစ်လုံးစာရေးရမယ့်အစား hexadecimal က ဂဏန်းနှစ်လုံးထဲနဲ့ဖော်ပြထားနိုင်လို့
`0 1 2 3 4 5 6 7 8 9 A B C D E F`

Hexadecimal မှာဆိုရင် two digit က စပြီးဖော်ပြနည်းက 
![[Hexadecimal_two_digit.png|400]] ဆိုပြီး ဖော်ပြတယ်။ အရှေ့ကိန်းက <mark style="background: #BBFABBA6;"> 16 </mark> /* # ဖြစ်ပြီး နောက်ကိန်းက <mark style="background: #BBFABBA6;"> 1 </mark> /* # ဖြစ်တယ်။ ဒီတော့ 16 & 1 ပေါ့

ထပ်ကိန်းတွေနဲ့တင်ထားတာဖြစ်တယ်။ 
ဥပမာ - 15 က F, 16 က `1 0 `ဖြစ်မယ်။ တွက်ကြည့်မယ်ဆိုရင် အနောက်က 16<sup>1</sup> = 0, အရှေ့ကိန်းက 1<sup>0</sup> =  ဆိုတော့ 16 + 0 = 16, 

F F ဆိုရင် 16 /* (15)F = 240, အနောက်က 1 /* (15)F = 15, ဒီတော့ 240 + 15 = 255

###### How hexadecimal is represented in computer memory

computer ပိုင်းမှာလည်း memory တွေကို address လုပ်ဖို့အတွက် hexadecimal တွေကို အသုံးပြုတယ်။
ဒါပေမယ့် hexa 10, 11 က decimal 16, 17 လို့ သာမန်လူတွေကြသိဖုိ့ခက်ပြီး hexadecimal တွေကို decimal ကိန်းလို့ထင်သွားနိုင်တယ်။ ဒီတော့ convention ဖြစ်အောင်

memory အခန်းတွေကို ညွှန်းဖို့အတွက် hexadecimal ကိန်းတွေရှေ့မှာ "<mark style="background: #FFF3A3A6;">0 x </mark>" ဆိုတာ ထည့်ထားပြီးဖော်ပြတယ်။ mathematically အတွက်မဟုတ်ဘဲ hexadecimal ဖြစ်တယ်ဆိုတာသိအောင်လို့သာ ထည့်သုံးခြင်းဖြစ်တယ်။
![[how_hexadecimal_is_reprsented_in_memory.png]]