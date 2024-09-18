
##### Scope

- scope ဆိုတာက variable တွေရဲ့ characteristic
- သူက variable တွေကို ဘယ်function ကနေ access လုပ်လို့ရတယ်ဆိုတာကို ပြောတဲ့ သဘောတရားမျိုး

- scope (၂) မျိုးရှိ
	- Local Variables
	- Global Variables

Local Variables: အဲ့ဒီ variable ကို create လုပ်လိုက်တဲ့ function ထဲကမှာဘဲ သူ့ကိုသုံးလို့ရတယ်။ အခြားသော function တွေကနေ လှမ်းခေါ်သုံးလို့ မရဘူး။

Global Variables: ဘယ် function ကနေမဆို‌ ခေါ်သုံးလို့ရတယ်။ C မှာတော့ main function ရဲ့ ‌အပေါ်မှာ များသောအားဖြင့် declare/initialize လုပ်ပြီးသုံးတယ်။

##### Why the distinction of scope matters?
#pass_by #value

C language က Variable တွေဟာဆိုရင် <mark style="background: #BBFABBA6;">pass by value</mark> ့သွားတယ်။ သဘောတရားက function တစ်ခုထဲကို arguments အနေနဲ့ variable တစ်ခုကို ထည့်လိုက်တာဖြစ်ဖြစ်၊ another variable တစ်ခုမှာ value ‌assign လုပ်တာဖြစ်ဖြစ် <mark style="background: #FF5582A6;">ပါသွားတာက မူလ variable မဟုတ်</mark>ဘူး။ သူ့<mark style="background: #BBFABBA6;">တန်ဖိုးကသာ copy အနေနဲ့ ပါသွား</mark>တာဖြစ်တယ်။ ဒါကြောင့်မလို arguments/assigned variable ကို ဘယ်လို manipulate လုပ်လုပ်, ပြောင်းလဲသွားတဲ့ value က value-passed လုပ်ပေးလိုက်တဲ့ variable အပေါ် မသက်ရောက်ဘူး။

ဒါကို CS50 မှာ ဒီလိုပြထားတယ်။

-- When a variable is passed by value, the <span style="color:rgb(255, 155, 0)">calle</span> (the function which is receiving the variable) receives a<span style="color:rgb(0, 176, 240)"> copy of the passed variable</span>, not the variable itself.

-- the variable in the <span style="color:rgb(255, 155, 0)">caller</span> (the function that is making the function call) is unchanged unless overwritten

```
int main(void)
{
int a = 10;  // variable in the caller

// Main() calls multiplication(), therefore main() is caller
multiplication(a);
}

int multiplicaiton(int x)   // calle
{
	 return x * 10;
}

```

pass by value အရ multiplication (calle) က သူ့ထဲကို ဝင်လာတဲ့ a value ကို 10 နဲ့မြှောက် ပြီး ရလဒ်ကို return ပြန်လိုက်လည်း main() ထဲက ‌a တန်ဖိုးက 10 ဘဲ, မပြောင်းလဲဘူး။ 

![[local variables.png]]
ဒီမှာကျတော့ variable name x ချင်းတူတာတောင် local variable တွေဘဲဖြစ်တဲ့အတွက် main() ထဲက x တန်ဖိုးက 1 ဘဲ, y ကသာ increment() ကနေပြန်လာတဲ့တန်ဖိုး 2 ဖြစ်သွားတယ်။ 

calle ထဲကို ထည့်ပေးလိုက်တဲ့ x အနီဆိုပေမယ့် calle ထဲကို‌ရောက်သွားတာက x ရဲ့ copy ဘဲ။ တကယ့် x မဟုတ်ဘူး။ ဒီတော့ calle ထဲမှာ ဘာလုပ်လုပ် main() ထဲက x တန်ဖိုးမပြောင်း