
program တွေကအလုပ်လုပ်တဲ့အခါမှာ (e.g. hello.c ကို compile and runတာတို့လုပ်တဲ့အခါ) RAM လို့ခေါ်တဲ့ Random Access Memory chip ပြားလေးအပေါ်မှာ အလုပ်လုပ်သွားတယ်။ 
ဒီတော့ သူတို့ အလုပ်လုပ်နိုင်တဲ့ memory ပမာဏက finite/ဆံုးမှတ်ရှိနေတယ်။
16GB RAM ဆိုရင် အများကြီးလို့ထင်ပေမယ့် 16GB ပမာဏအထိဘဲ အလုပ်လုပ်လို့ရတယ်။ ဒါက infinite မဟုတ်ဘူး။ ဒီတော့ ဘာဖြစ်လာနိုင်လဲဆို အောက်က ဥပမာကိုကြည့်

e.g.
	![[integre-overflow-eg.png]] three bits(ဂဏန်းသုံးလံုး)ထိဘဲ access ရှိမယ့် memory လို့တွေးကြည့်ရအောင်။ ရှေ့ဆုံးက အရောင်မှိန်နေတဲ့ လေးလုံးမြောက်က သဘောတရားသိရအောင်ထည့်ထားတာ။ 
	အဲ့လို three bit နဲ့ဆို အများဆုံးရေတွက်လို့ရမယ့် နံပါတ်က `111` = 7 အထိဘဲရတယ်။ အကယ်လို့ နံပတ် '8' အထိရေတွက်ချင်ရင် ဘယ်လိုဖြစ်မလဲ 8 = `1000` ဖြစ်တဲ့အတွက် four bits လိုလာပြီ။
	![[integer-overflow-eg2.png]] ပုံအရတော့ 8 ဆိုတာသိနိုင်ပေမယ့် three bit အထိဘဲ တွက်လို့ရတဲ့အခါမှာ programက သုညသုံးလုံးလို့ သွားမှတ်ပြီး သူပြပေးမယ့် ဂဏန်းက <span style="color:rgb(0, 128, 128)">သုည</span> ဖြစ်သွားတယ်။ ဒါ integer overflow ဖြစ်တာဘဲ။

integer overflow ဆိုတာက computer မှာ လုံလောက်တဲ့ memory မရှိတော့ဘဲ နံပါတ်အမြင့်ကြီးတွေအထိရေတွက်ရတဲ့အခါ computer က နိုင်သလောက်ထိကိုဘဲ ချုံ့ပစ်လိုက်ပြီး သုည နဲ့ (အကယ်လို့ positive/negative number ကိုပါ support ရင် ) negative numbers တွေ မှားထွက်လာတာမျိုးကိုဆိုလိုတယ်

32 bits (4 bytes) - roughly around 2billions number (both positive and negative, if only positive ~4 billions)

64 bits (8 bytes) - crazy big numbers hehe

