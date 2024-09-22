#DSA #SelectionSort

0-7 ကို randomly စီထားတဲ့ array တစ်ခုရှိတယ်။
အဲ့တာကို selection sort နဲ့ပြန်စီမယ်ဆိုရင် ဒီလိုသွားတယ်။
- ပထမဆုံး array တစ်ခုလုံးကို loop ပတ်ပြီး အသေးဆုံးနံပါတ်ကို လိုက်ရှာတယ်။
- အဲ့ smallest number ကို အရှေ့ဆုံးကို ပို့လိုက်မယ်။
- ပြီးရင် အဲ့နောက်ကနေ loop ထပ်ပတ်ပြီး နောက်ထပ် second smallest number ကို လိုက်ရှာတယ်။ 
- ပြီးရင် အရှေ့ကို ပြန်ပို့တယ်။
- အစအဆုံး စီမပြီးမချင်း အဲ့လိုသွားတယ်။

```
pseudocode

for i from 0 to n-1
	Find smallest number between numbers[i] and numbers[n-1]
	Swap smallest number with numbers[i]

```

##### Selection sort with Big O Noatation

ဒီတော့ Selection Sort ရဲ့ efficiency ကို #BigONotation နဲ့ ကြည့်ရအောင်

ပထမဆုံး အသေးဆုံးနံပါတ်ကိုရှာဖို့ သူက array တစ်ခုလုံးကို ပတ်ပြီးရှာရမယ်။ 
- (n-1) times
ဒုတိယအသေးဆံုးနံပါတ်အတွက် (n-2) times ... စသည်ဖြင့်

(n-1) + (n-2) + (n-3).... +1 (1 for last comparison)
By formula of "**sum of the first k natural numbers**"

 $$ \frac{(n-1)n}{2}  $$

total steps အဲ့လောက်သွားရမယ်။
အဲ့ equation ကို ‌ဖြေရှင်းရင်

n(n-1)/2
(n<sup>2</sup> - n)/2
n<sup>2</sup>/2 - n/2

ဒီထဲမှာဆို အကြီးဆုံးနံပါတ်က n<sup>2</sup> , 2 နဲ့ စားသည်ဖြစ်စေ၊ n ကိုပြန်နှုတ်သည်ဖြစ်စေ n<sup>2</sup> က dominant, largest number ဖြစ်နေတဲ့အတွက်ကြောင့်မလို့ computer scientist တေ‌ွက wrap(ချုံ့ပြီး) selection sort ကို running time - order of n square
O(n<sup>2</sup>) လို့ သတ်မှတ်ကြတယ်။

###### higher & lower bound

အကယ်လို့ worst case မှာ O(n<sup>2</sup>) ဆိုရင် best case မှာရော selection sort က ဘယ်လိုဖြစ်နို်ငလဲ။
best case ဖြစ်နိုင်ချေက numbers တွေက အစဥ်လိုက်စီပြီးသား‌ဖြစ်နေတာဘဲ။ ဒါပေမယ့် algorithms က အဲ့လိုစီပြီးသားကို သိနိုင်မှာမဟုတ်တဲ့အတွက် သေချာအောင် loop တွေပတ်ပြီး အသေးဆုံးကိုပတ်ရှာပြီး ‌‌ေရှ့ကိုပို့တာ လုပ်ရဦးမှာဘဲ။ ဒီတော့ သူက best case မှာလည်း Ω(n<sup>2</sup>) ဘဲ 

upper bound နဲ့ lower bound တူတူဘဲ ဖြစ်တဲ့အတွက် selection sort ကို Θ(n<sup>2</sup>) အဖြစ်သတ်မှတ်လို့ရ။






