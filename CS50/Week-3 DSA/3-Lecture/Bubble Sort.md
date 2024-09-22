bubble sort ဆိုတာက
{1,2,3,4,5,6,7} ဆိုတဲ့ array တစ်ခုကို အထဲက နံပါ‌တ်တွေက randomly စီထားတယ်ဆိုရင် 
- ပထမဆုံး နံပါတ်နှစ်ခုကို ကြည့်မယ်
- ကြီး/ငယ် အစဥ်တိုင်းဖြစ်မနေရင် အဲ့နှစ်ခုကို swap မယ်
- second & third num ကိုကြည့်မယ်
- အဲ့လိုနဲ့ swap သွားမယ်။

```
psudocode

Repeat n-1 times
	For i from 0 to n-2
		If number[i] and number [i+1] out of order
			Swap them
		If no swaps
			Quit


```

BigONotation နဲ့ဆိုရင် worst case က selection sort လိုဘဲ most influential factor ဖြစ်တဲ့ n<sup>2</sub> ကိုယူပြီး O(n<sup>2</sup>) အဖြစ်သတ်မှတ်တယ်။ 

ဒါပေမယ့် best case scenario မှာဆိုရင်တော့ သူက အကုန် order ကျနေတာကို တစ်ခေါက်စီလိုက်ကြည့်ရုံဘဲဖြစ်တဲ့အတွက် n times, size အပေါ်မူတည်ပြီး အကြိမ်ကွာသွားမှာဖြစ်တဲ့အတွက် 1   Omega(n) အဖြစ်သတ်မှတ်တယ်။