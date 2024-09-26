#C #MergeSort

merge sort ဆိုတာက ‌randomly sorted စီထားတဲ့ array တစ်ခုကို နှစ်ခြမ်းခြမ်းပြီး ဘယ်ဘက်ကို စီမယ်။ ညာဘက်ကို စီမယ်။ ပြီးမှ နှစ်ခုကို ပြန်ပေါင်းတယ်။ အဲ့လို\

```
pseduocode

If only one number 
	Quit
Else
	Sort left-half of numbers
	Sort right-half of numbers
	Merge sorted halves

```

ဒီလို တစ်ဝက်ဆီခွဲတာက ဘယ်အထိခွဲလဲဆိုရင် ဘယ်ဘက်ခြမ်းကိုလည်း အသေးဆုံး sort လုပ်လို့ရမယ့်အထိ half လုပ်တာ။ e.g.
```
6  3   4  1   5  1  7  0
6  3   4  1 |  5  1  7  0
6  3 | 4  1
6  3 (before sorting)
3  6 (after sorted)
```

အပေါ်မှာ ပြထားသလိုမျိုး နှစ်ခုဘဲကျန်တဲ့အထိ recursive နဲ့ Half ချသွားပြီး နှစ်ခုကိုယှဥ် ပြီးရင် swap သင့်ရင် swap သွားတာ။

ပြန် merge လုပ်တဲ့အချိန်မှာလည်း သူက numbers တွေကို ဘယ်ဘက်ကကောင်နဲ့ ညာဘက်ကကောင် ယှဥ််ပြီးတော့မှ အရင်လာရမယ့်ကောင်ကိုထည့်တာ

အပေါ်က  `6 3 4 1` ကို မ merge ခင်မှာဆိုရင် ဒီလိုဖြစ်နေမှာ
`3 6 | 1 4` အဲ့မှာ သူက 3 နဲ့ 1 နဲ့ ယှဥ်မယ်။ 1 က ပိုကြီးတဲ့အတွက်

```
1 

3 6 | 4
```

အဲ့မှာပြီးရင် 3 နဲ့ 4 နဲ့ယှဥ်မယ်။ 3 က သေးတဲ့အတွက် 3 ကိုထား။ ပြီးရင် 6 နဲ့ 4 ကိုယှဥ် အဲ့လိုသွားတယ်။

Visualization:
![[visualization of merge sort.png]]

CS50 - finally algorithm will merge both sides. It will look at the <span style="color:rgb(0, 176, 240)">first number on the left</span> and the <span style="color:rgb(0, 176, 240)">first number on the right</span>. It will put t<span style="color:rgb(255, 155, 0)">he smaller number first</span>, <span style="color:rgb(146, 208, 80)">then the second smallest</span>. the algorithm will repeat this for all number.

bubble & selection sort က space တစ်ခုကိုဘဲ အဓိက ဦးတည်ထားပြီး အလုပ်လုပ်တယ်။ selection ဆိုရင် i & i + 1 ပေါ့။ ဒီအတွက် နည်းနည်းနှေးတယ်။ Computer Science မှာ factors တွေကို trade လုပ်လို့ရတယ်။ အချိန်ပိုမြန်စေဖို့အတွက် merge sort က space နှစ်ခု, left-side & right side array ယူပြီး အချိန်ကိုမြန်အောင် လုပ်ပေးတယ်။ trade space for time

##### Big O Notation for Merge Sort

![[merge sort Big O.png]]
yellow height light အရ merge sort ကို run ရတာ အကြိမ်ပေါင်း 24 times

တစ်ဝက်စီ divide လုပ်သွားရင် log<sub>2</sub> n ကိုသုံးတယ်။ merge sort ကလည်းအဲ့လိုဘဲ size 8 ရှိတဲ့ array တစ်ခုကို တစ်ဝက်စီ size 4 -> size 2 စသည်ဖြင့် half လုပ်သွားတယ်။

log<sub>2</sub> 8 -> log<sub>2</sub> 2<sup>3</sup> -> 3 (base & number cancel out each other)

ဒီတော့ size 8 ရှိတဲ့ problem တစ်ခုကို ‌half လုပ်သွားရင် 3 ခါထိလုပ်လို့ရတယ်။ 
yellow highlight လုပ်ထားတဲ့ကောင်လေးတေွက sort လုပ်ပြီးရင် ပြန် merge ရတယ်။ အကုန်လုံးကို ပြန် merge နိုင်ဖို့ n steps ပြန်ကြာတယ်။
ဂဏန်းရှစ်လုံး half လုပ်တာ 3 times (8 x 3) = 24

n height ရှိတဲ့အထိ half လုပ်လာပြီး n ကြိမ် width အထိအလုပ်လုပ်ရတဲ့အတွက်
<mark style="background: #FFF3A3A6;">O(n log n)
</mark> 

----- Another Explanation ---

1. **Recursive Sorting**: Each half is then sorted recursively. If the array has ( n ) elements, each recursive call deals with ( n/2 ) elements. This results in a logarithmic number of levels, specifically ( \log n ) levels.
    
2. **Merge Step**: Merging two sorted halves takes linear time, O(n), because you have to compare and combine all elements from both halves.
    

Combining these steps:
- The recursive sorting happens over ( \log n ) levels.
- The merging step is O(n) at each level.

So, the total time complexity is ( O(n \log n) ), because you perform the merge step (O(n)) at each level of recursion (O(\log n)).