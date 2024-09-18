
- arrays hold <span style="color:rgb(0, 255, 255)">values</span> of <span style="color:rgb(146, 208, 80)">same data type</span> at <span style="color:rgb(146, 208, 80)">contiguous(တစ်ဆက်တည်း) memory location</span>
- a fundamental data structure & extremely useful

C မှာဆိုရင် arrays တွေက zero-indexed (zero က စပြီး ရေတွက်တယ်)။ 

arrays တစ်ခုက<span style="color:rgb(0, 255, 255)"> n<sup>th</sup> element</span> ရှိတယ်ဆိုရင်။ ပထမဆုံး element က index 0 မှာ ရှိတာဖြစ်ပြီး နောက်ဆုံး element က index (n-1) မှာရှိတာဖြစ်တယ်။

C မှာ arrays တွေက လက်ရှိ index အခန်းထက်ကျော်ပြီး ရေးမိရင်တောင် error ပြမှာ မဟုတ်ဘဲ အနောက်က မဆိုင်တဲ့ memory တွေကို သွားဖတ်မှာဖြစ်တယ်။ (Java မှာဆိုရင် index out of bonds ဆိုပြီး error တက်)
	index 5 ခန်းရှိတဲ့ကောင်မှာ array\[7] ဘာညာထုတ်ကြည့်လည်း Cက အနောက်က memory တွေကို လျှောက်ဖတ်မှာ။ 

###### Array Declaration

--> <span style="color:rgb(255, 155, 0)">type</span> <span style="color:rgb(146, 208, 80)">name</span>\[ <span style="color:rgb(0, 255, 255)">size</span>]

type - array ရဲ့ elements ‌ဖြစ်လာမယ့် variables တွေရဲ့ data type

name - array ရဲ့ name

size - ထည့်သိမ်းချင်တဲ့ elements အရေအတွက်

###### Array Initialization

e.g. 

Instantiation Syntax :
bool truthtable\[3] = {false, true, true}

Individual element syntax :
bool truthtable\[3];
truthtable\[0] = false;
truthtable\[1] = true;
truthtable\[2] = true;

###### Two dimensional arrays

array တွေက single dimension ဘဲရှိနေတာမဟုတ်ဘူး။
size specifiers တွေ လိုသလောက်ရှိလို့ရတယ်။

  e.g. bool battleship\[10]\[10]

ဒီလိုမျိုးဆို သူက 10 x 10 gird တစ်ခု ပုံစံမျိုးဖြစ်လာပြီး cells တေွကို လိုသလို access လုပ်လို့ရ။ 
e.g. battleship\[1]\[5], battleship\[3]\[0], battleship\[3]\[9]

- 10 x 10 two dimensional array က <span style="color:rgb(0, 255, 255)">memory</span> ထဲမှာတေ့ာ <span style="color:rgb(255, 105, 180)">just 100-element-one-dimensional array </span>. same for three, four, five dimensional array, all are one dimensional in memory

- multi dimensional array ‌တွေက game boards / other complex representations ‌တွေကို visualize လုပ်လို့ကောင်းတဲ့ great abstractions

###### Things to be careful with arrays

- Array ရဲ့ <span style="color:rgb(255, 105, 180)">individual elements</span> (e.g. arr\[3]) တွေကို variables အနေနဲ့ <span style="color:rgb(255, 105, 180)">သုံးနိုင်</span>ပေမယ့် ‌<span style="color:rgb(220, 20, 60)">array တစ်ခုလုံးကြီး </span>(e.g. arr) ကိုတော့ variable တစ်ခုအနေနဲ့ <span style="color:rgb(220, 20, 60)">သုံးလို့မရ</span>ဘူး။

- ‌Array တစ်ခုကို နောက် array တစ်ခုထဲ assignment operator (=) သုံးပြီး value assign လုပ်လို့ <span style="color:rgb(220, 20, 60)">လုံးဝမရ </span>။ လုပ်ချင်ရင် for loop ပတ်ပြီး တစ်ခုစီ လုပ်ရတယ်။

```
int arr1 [3] = {0,1,2};

int arr2[3];

for(int i=0; i<3; i++)
{
  arr2[i] = arr1[i];
  
}


```

##### Pass by reference
#pass_by #reference

In C, arrays တွေက <mark style="background: #BBFABBA6;">pass by reference</mark> ပါ

<span style="color:rgb(255, 155, 0)">Calle</span> (function which is receiving the variable) က copy value ကိုရသွားမှာ မဟုတ်ဘဲ <span style="color:rgb(146, 208, 80)">တကယ့် array အစစ်ကြီးကိုရ</span>သွားမှာပါ။ ဒီတေ့ာ calle ထဲမှာ array ကို manipulate လုပ်ရင် တကယ့် array value တွေလည်းပြောင်းပါတယ်။ 

```
int main(void)
{
    int num[5] = {0, 1, 2, 3, 4};
    pbr_test(num);
    
    for(int i = 0; i < 5; i++)
    {
        printf("%i \n", num[i]);
    }
}

void pbr_test(int arr[])
{
 arr[3] = 33;
}

```

အပေါ်က program ထဲမှာဆိုရင် သူ့ဘာသာ test function ထဲမှာ index ခန်းတစ်ခုကို value အသစ်ပေးလိုက်တယ်။ ဘာမှလည်း return မပြန်ထားဘူး။ ဒါ‌ပေမယ့် num array ကို print ထုတ်ကြည့်တဲ့အခါမှာ သူ့ထဲက index 3 ခန်းက value က 33 ဖြစ်သွားပြီ။ 
ဒါ pass by reference ဘဲ။ 
calle ထဲမှာ manipulate လုပ်သမျှ original array မှာလည်း value တွေပြောင်းကုန်တာ

**Different of Pass by reference & value** 

```
int main(void)
{
	int a = 10;
	int b[4] = {0, 1, 2, 3};

	set_int(a);
	set_array(b);

	printf("%d %d\n", a, b[0]);

}

void set_array(int array[])
{
 array[0] = 22;
}

void set_int(intx)
{
 x = 22;
}
```

ဒီ program မှာဆိုရင် int variable အတွက် set_int function ကို ခေါ်ပြီးထည့်လိုက်တယ်။ ဒါပေမယ့် variable တွေက ‌pass by value ပြီးတော့ overwrite လုပ်လိုက်တာလည်း မဟုတ်တဲ့အတွက်ကြောင့် main() ထဲက int a သည် value 10 ဘဲ မပြောင်းဘူး။

array တွေကျ pass by reference လုပ်တာဖြစ်တဲ့အတွက် set_array() ကို ခေါ်လိုက်ပြီးတာနဲ့ main() ထဲမှာ b\[0] value သည် 22 ဖြစ်သွားပြီ။
