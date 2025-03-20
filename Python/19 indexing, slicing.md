
1. str
2. list
3. tuple
4. range
5. bytes
6. byte array
7. 2D, 3D data

from 1 - 6, အထိကို 2D data လို့ခေါ်တယ်။ row တွေ columns တွေနဲ့သိမ်းတာမျိုးဖြစ်လို့ နှစ်ဖက်မြင် 2D လို့ခေါ်။ data တွေကို ကိုင်တွယ်ဖို့ index နဲ့သုံး

##### Indexing

index ဆိုတာ <span style="color:rgb(0, 176, 240)">တည်နေရာနံပါတ်</span>ကို ပြောတာ။ အဲ့တာကိုသုံးပြီး data ထည့်ထုတ်လုပ်။

###### 1. Positive index, Negative Index

(first 1,3,5 , last 1,3,5)

တည်နေရာ နံပါတ်မှာ အပေါင်းတည်နေရာ နံပါတ်နဲ့ အနှုတ်တည်နေရာနံပါတ်ဆုိပြီး ရှိတယ်။

```
"abcdefg"

 a  b   c   d   e   f   g 
 0  1   2   3   4   5   6    (positive index)
-7 -6  -5  -4  -3  -2  -1   (negative index)

x = "abcdefg"
x[0]   # "a"
x[1]   # "b"

x[-1]  # "g"
x[-7]  # "a"


```

အပေါ်က string လေးမှာဆို a-g element 7 ခု

<mark style="background: #FFF3A3A6;">positive index</mark> သည် <span style="color:rgb(0, 176, 240)">zero-indexed</span> ဖြစ်ပြီး <span style="color:rgb(32, 178, 179)">ဘယ်ဘက်ရှေ့ဆုံး</span>ကp  index တပ်တယ်။

<mark style="background: #ABF7F7A6;">negative index</mark> သည် <span style="color:rgb(255, 155, 0)">ညာဘက်</span> က စရေတွက်ပြီး <mark style="background: #BBFABBA6;"> -1 </mark> ကနေ စရေတွက်တယ်။ 

##### 2. Difficult Index

အပေါ်မှာတွက်နည်းက လွယ်လွယ်ကူကူတွက်တာ, positive index ဆို လွယ်"ကူ" ပြောလို့ရပေမယ့် negative index ဆိုရင် data များလာရင် ရှာဖို့ ခက်တယ်။

negative index မှာဆိုရင် ဘယ်ဘက်ကစတွက်ရင် ပထမဆုံး element သည် total index ကို (-) တပ်ထားတာနဲ့တူတယ်။
data တစ်ခုရဲ့ length (total indexs)ကိုလိုချင်ရင် "<mark style="background: #FFF3A3A6;">len()</mark>" ကိုသုံးလို့ရတယ်။

```
x = "abcdefg"

total = len(x)

f1 = 0
f1n = - total

f2 = 1
f2n = - (total - 1)

```

<mark style="background: #FFF3A3A6;">wantedIndex = - (total - absolute value of easy index) </mark>

easy index ဆုိတာက ကိုယ်က 5 နေရာက element ကိုလိုချင်ရင် သူက positive index အနေနဲ့ဆို (4) , အမြဲတစ်လျော့ယုံဘဲ။ အဲ့တာကို အလွယ်ရှာလို့ရတဲ့ easy index ပေါ့ 

နောက်ဆုံးကရေတွက်ရင် (၅)နေရာမြောက်က index ကိုလိုချင်တယ်ဆိုပါတော့။ ဒါဆိုရင် နောက်ဆုံးကဖြစ်တဲ့အတွက် neg index က ရှာရလွယ်။ (-5) ဘဲလေ။ ဒီမှာလည်း positive index ကိုလိုချင်ရင် total ထဲက absolute easy index (- မပါတော့) (5) ကို နှုတ်ပေးလိုက်ရပြီ

##### 3. range

range ဆိုတာက အကန့်အသတ်ဘောင်တစ်ခုပေ့ါ။

```
x = "abcde"

```

အပေါ်က x မှာဆိုရင် total element က ငါးခု positive index ဆိုရင် (0 to 4) , negative index သည် (-1 to -5) ပေါ့။ အဲ့ range အတွင်းရှိတဲ့ index ကိုဘဲ access လုပ်လို့၇တယ်။ ကျော်ပြီး access လုပ်ရင် out of range error တက်မယ်။  total range (-total, (total-1) ) အနေနဲ့ဆို positive ရော index ရောတွက်ရင် (-5 to 4) အတွင်း သုံးလို့ရ ။ 
`e.g. x[5], x[-6] # out of range error`


##### 4. Middle index

အလယ်က index ကို တိုက်ရိုက်တွက်ထုတ်မယ်ဆိုရင်

total element က

<span style="color:rgb(255, 155, 0)">odd (မကိန်း)</span> ဖြစ်နေရင်  <mark style="background: #ABF7F7A6;">total // 2</mark> = middle index (or) index of middle element

<span style="color:rgb(255, 155, 0)">even (စုံကိန်း)</span> ဖြစ်နေရင်  <span style="color:rgb(0, 176, 240)">ညာဘက်-အလယ်</span>အတွက် (right middle index) = <mark style="background: #ADCCFFA6;">total // 2</mark> , <span style="color:rgb(255, 155, 0)">ဘယ်ဘက်-အလယ်</span>အတွက်က (left middle index) = <mark style="background: #ADCCFFA6;">right middle index - 1
</mark>

```
x = "abcdef"

total = len(x)                         # 6
right-middle = total // 2 = 3          # x[3] = d

left-middle = right-middle - 1 = 2     # x[2] = c

```


##### For fixed size memory 

ဒီနည်းနဲ့ပုံသေနည်းက memory size အသေရှိတဲ့ programming language မှာတော့ သေချာအလုပ်လုပ်ပေမယ့်။ python သည် dynamic memory size language ဖြစ်တာကြောင့် အလုပ်လုပ်ပုံသည် ကိုက်နေပမယ့် မကိုက်တာမျိုးလညး် ဖြစ်သွားနိုင်တယ်

နောက်ကွယ်မှာ ဘယ်လိုဖြစ်ပျက်နေသလဲပေါ့။ 2D, 3D data တွေမှာ တကယ်တမ်းတော့ index ဆိုပြီး မရှိဘူး။ ဒါပေမယ့် x\[index] ဆိုရင် ဘာလို့ value တွေထွက်လာသလဲပေါ့။

memory size တစ်ခု အသေရှိတယ်ဆိုပါတော့
`x = "abcdef"`
ဒီမှာဆိုရင် x\[0] ဆိုရင် a ဆိုပြီး ထွက်လာတာဘာလို့လဲဆိုတော့ ပုံသေနည်းကြောင့်

<mark style="background: #FFF3A3A6;">address = base_address + (i * memorySizeUsedByElement)</mark> (where "i" is the index of element)

သူက a ဆိုရင် store လုပ်ဖို့ 48 bytes ပမာဏယူတယ်ပေ့ါ။ အဲ့လိုဟာကိုသုံးပြီးတွက်တာ

base_address --> 1000 ဆိုပါတော့
first_element -> 1000 + (0 * 48) -> 1000   = (second_elemnt - base_address) 
second_element -> 1000 + (1 * 48) -> 1048 = (first_element + 48)
third_element -> 1000 + (2 * 48) -> 1096 = (second_element + 48)

ဆိုပြီး python က သူ့ဘာသာ တွက်ပြီး ပြန်ပေးတာ။ data အစုတွေ like string, list... တုိ့မှာဆိုရင် data တစ်ခုဆီ(a, b,c) စတာတွေကို အတွဲလိုက် အစဥ်တိုင်းသိမ်းတဲ့အတွက် ပုံသေနည်းကိုသုံးလို့ရတယ်။ 48 ဖြစ်နေတာက chr memory size = 48 bytes used





