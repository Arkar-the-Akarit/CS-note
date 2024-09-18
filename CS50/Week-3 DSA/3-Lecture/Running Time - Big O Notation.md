#BigONotation

ပြဿနာကိုဖြေရှင်းတဲ့ algorithm တစ်ခုက efficient ဖြစ်မဖြစ်သိဖို့အတွက် big O notation လို့ခေါ်တဲ့ analysis နဲ့ running times (ပြဿနာဖြေရှင်းပြီးဖို့ run ရမယ့် အကြိမ်အရေအတွက်ကို) ဖော်ပြလေ့ရှိတယ်။

![[big O notation.png]]

Big O Notation မှာ O ဆိုတာက 'Order Of', ကို ပြောတာဖြစ်ပြီး input size ကြီးထွားလာတာနဲ့ running time or space requirements က ဘယ်လိုလိုက်ကြီးထွား(grow) လာတယ်ဆိုတာကို ဖော်ပြတာမျိုးဖြစ်တယ်။

**Meaning of 'O'**
- O = order of growth, constant factors & low-order terms တွေကို ထည့်မစဥ်းစားဘဲနဲ့ input size ကြီးထွားလာတာနဲ့ running time လိုက်တိုးလာတာကို ဖော်ပြတယ်။ (e.g. algorithm တစ်ခုက 3n + 5 steps ကြာမယ်ဆိုရင် O(n) လို့ဘဲ ဖော်ပြတယ်။ 3 & 5 ဆိုတဲ့ constant factors & lower order terms တွေက input size ကြီးလာတာနဲ့အမျှ သိပ်အရေးမပါလို့)
- O က <span style="color:rgb(0, 176, 240)">upper bound </span>လည်းဖြစ်တယ်။ running time / space တစ်ခုရဲ့ <span style="color:rgb(32, 178, 179)">upper limit (i.e. worst case scenario)</span>  ကိုဖော်ပြတယ်။ e.g. O(n<sup>2</sup>) ဆိုရင် input size (n) ဘယ်လောက်ကြီးလာလာ <mark style="background: #FFF3A3A6;">c * n<sup>2</sup></mark> (c is some constant) ထက်ကို running time က ကျော်သွားမှာ မဟုတ်ဘူး။

###### Examples of O

1. O(1) - <mark style="background: #FFF3A3A6;">Constant</mark> Time
	- 1 ကြိမ်တည်းလို့ ‌ဆိုလိုတာမဟုတ်ဘူး။ 100 ဖြစ်ရင် ဖြစ်မယ်၊ 1000 ဖြစ်ရင် ဖြစ်မယ်။ input size ဘယ်လောက်ဖြစ်ဖြစ် <span style="color:rgb(0, 176, 240)">တိကျသေချာတဲ့ ကိန်းသေ steps</span> နဲ့ ‌ေဖြရှင်းလို့ရတာ ကိုဆိုလိုတာဖြစ်တယ်။
	- input size ပေါ်လိုက်ပြီးတော့ running time မပြောင်း
	- e.g. array တစ်ခုထဲက element ကို index အတိအကျနဲ့ access

2. O(n) - Linear Time
	- input size နဲ့ linear (အညီ / မျဥ်းတစ်‌ဖြောင့်တည်း) လိုက်ပြီး running time လိုက်တိုး
	- e.g. size (n) ရှိတဲ့ array ကို loop ပတ်တာ

3. O(n<sup>2</sup>) - Quadratic Time
	- input size ရဲ့ နှစ်ဆစာ running time က အချိုးကျ လိုက်တိုး
	- e.g. input size(n) အတိုင်း outer loop ရော inner loop ပါ ပတ်တဲ့ nested loop တစ်ခု

4. O(log n) - Logarithmic Time
	- input size ရဲ့ logarithmic အလိုက် running time တိုး
	- e.g. binary search in sorted array
	
	--> များသောအားဖြင့်တေ့ာ log n ဆိုတာနဲ့ big o notation မှာ base 2 ကို ယူတာများတယ်။ binary search မှာဆိုရင်လည်း အခု ၁၀၀ ရှိတယ်ဆိုရင်, 50 - 25 - 14 - 8 - 4 - 2 - 1 (total ၇ ခါ) သွားရတာမျိုးပေါ့။ e.g. log 100 = 7 (rounded from float 6) 
	
	log n ဆိုရင် သူ့ value ကိုယူရတာဖြစ်တယ်။ 



5. O(n log n) - Linearithmic Time
	- running time grows proportional to <mark style="background: #ADCCFFA6;">n</mark> times logarithm of <mark style="background: #ADCCFFA6;">n</mark>
	- e.g. merge sort
###### Bound

1 - Upper Bound (Worst Case) - Big O (O):

- worst-case time complexity, i.e. <span style="color:rgb(255, 155, 0)">the maximum amount of time the algorithm will take as input size grows</span> ကို ဖော်ပြတယ်.
- ‌algorithm က ဒီ upper bound က time ထက် ဘယ်တော့မှ အချိန်ပိုမယူဘူးဆိုတာကို သေချ‌ာစေတယ်။

2 - Lower Bound (Best Case) - Big Omega (Ω)

- best-case time complexity, i.e. the <span style="color:rgb(255, 155, 0)">minimum </span>amount of time the algorithm will take as input size grows
- algorithm တစ်ခုက <span style="color:rgb(146, 208, 80)">အနည်းဆုံးတော</span>့ ဒီလောက် running time ကြာမယ်ဆိုတာ သေချာစေတယ်။  

3 - Tight Bound - Big Theta (Θ)

- upper bound & lower bound က same (တူညီ) နေတာမျိုး၊  best case & worst case scenario မှာ running time တူညီနေတာမျိုးကိုပြောတယ်။
- Θ(f(n)) ဆိုရင် algorithm တစ်ခုက best/worst/average case တွေအကုန်လုံးမှာ f(n) time ကြာမယ်လို့ ဆိုလိုတာဖြစ်တယ်။

**Example of Bounds - Binary Search**

- Worst Case (0) - binary search ရဲ့ O notation က O(log n), worst case တေွမှာ target element ကိုတွေ့ဖို့/ မရှိဘူးဆိုတာသိနိုင်ဖို့ log<sub>2</sub>(n) steps ကြာမယ်။
- Best Case (Ω) - Best Case မှာဆိုရင် target element ကို first try နဲ့တွေ့နိုင်တယ်။ ဒါကြောင့် Ω(1)
- Average Case (Θ) - Θ(log n) ဘဲ foot note





