#DSA #BinarySearch

array တစ်ခုထဲကနေ value 50 ကိုရှာတာမျိုးမှာ linear search လို တစ်ခုဆီလိုက်မကြည့်တော့ဘဲနဲ့, array ထဲက value တွေက smallest to largest စီထားတယ်လို့ ယူဆပြီးတော့ array ရဲ့ အလယ် Index ကို သွားကြည့်တယ်။ အဲ့ index မှာ value 50 ရှိရင် true, မရှိဘူးဆိုရင် smallest to largest စီထားတာဖြစ်တဲ့အတွက် သူ့ရဲ့ ဘယ်ဘက် or ညာဘက်, value 50 ရှိနိုင်မယ့်ဘက်ကိုသွားပြီး အပေါ်ကလိုဘဲ တစ်ဝက် ထပ်ဝက်ပြီးရှာတယ်။

အနီးစပ်ဆုံးတူမယ့် pseudo code က

```
pseudocode 

If no index left
	Return false
If 50 is behind index[middle]
	Return True
Else if 50 < index[middle]
	Search  index[0] through index[middle-1]
Else if 50 > index[middle]
	Search index[middle+1] through index[n-1]

```



