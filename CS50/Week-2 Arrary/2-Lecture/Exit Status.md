#C #exit-status

ရေးလိုက်တဲ့ program တိုင်းမှာ (infinite loop ပတ်ထားတာ မဟုတ်သ‌ရွေ့) program ဘယ်လိုပြီးဆုံး/ထွက်သွားတယ်ဆိုတာကို ပြတဲ့ exit status ဆိုတာရှိတယ်။ ကိုယ်တိုင် သတ်မှတ်ပေးလိုက်လို့ရသလို, program က သူ့ဘာသာ auto ပြန်တဲ့ exit status code လည်းရှိတယ်။

program က အောင်'မြင်' execute လုပ်ပြီး exit သွားတယ်ဆိုရင် --> <mark style="background: #BBFABBA6;">exit status - 0</mark>

error တစ်ခုခုနဲ့ တစ်နေရာရာမှာ မှားလို့ ထွက်သွားရတယ်ဆိုရင် --> <mark style="background: #BBFABBA6;">သုည မဟုတ်တဲ့ ကျန်တဲ့ဂဏန်းအကုန်</mark> (- နဲ့စတဲ့ negative နံပတ်ပါဖြစ်နိုင် )

ဒါကြောင့်မလို့ Cရဲ့ main() ဟာလည်း exit code ကို ပေးနိုင်ဖို့ int return type ရှိနေတာဖြစ်တယ်။

exit status တွေက program က သူ့ဘာသာ secretly exit ထွက်ပြီး မပြပေမယ့် 
<mark style="background: #ADCCFFA6;">echo $?</mark> command နဲ့ program က ဘယ် exit status နဲ့ထွက်သွားတယ်ဆိုတာကို ကြည့်နိုင်တယ်။

```
int main(int argc, string argv[])
{
 if (argc != 2)
 {
  printf("Missing command-line argument");
  return 1;
 }

 printf("Hello %s", argv[1]);
 return 0;
}

```

ဒီလိုဆိုရင် argc မှာ 2 ဖြစ်အောင် command က 2 words ဘဲရှိရမယ်။ မဟုတ်ရင် error message ကိုပြပြီး code 1 နဲ့ exit သွားမယ်။

ဒါကို echo $? command နဲ့ ကြည့်မယ်ဆိုရင် ဒီလိုပြမယ်။
![[Pasted image 20240831211330.png]]

testing (unit-test) ဘာညာလုပ်ပေးတဲ့ software တွေကလည်း ဒီ exit status ကို သိနိုင်တယ်။