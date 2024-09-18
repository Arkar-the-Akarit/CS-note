#C #Functions

main function() တစ်ခုထဲမှာဘဲ code တွေရေးနေတာက program ကြီးလာတဲ့အခါမှာ ပြဿနာရှိနိုင်တယ်။ ဒီတော့ အခြားသော function လေးတွေခွဲရေးတာပိုကောင်းတယ်။

functions တွေကို procedures, methods, subroutines စသည်ဖြင့်လည်းခေါ်ကြတယ်။

function -> ‌a black box with a set of 0+ input and one output

function ‌တွေကို ဘာလို့ blackbox လို့ခေါ်လဲဆိုရင် ကိုယ်တိုင်ရေးထားတဲ့ function မဟုတ်ရင် အထဲမှာ ဘယ်လိုအလုပ်လုပ်သွားတယ်ဆိုတာ သိစရာမလိုလို့ e.g. printf(), toupper();

###### Functions တွေကို ဘာလို့သုံးသင့်တာလဲ

- Organization: program/problem အကြီးကြီးတစ်ခုကို function တွေသုံးပြီး more manageable subparts တွေအဖြစ် ခွဲထုတ်ပစ်လို့ရတယ်။

- Simplification: function သေးသေးလေးတွေက design, implement, debug လုပ်ရတာ ပိုလွယ်ကူတယ်။

- Reusability: function တွေက တစ်ကြိမ်ဘဲ‌ရေးထားပြီးတော့ ထပ်ခါထပ်ခါပြန်သုံးလို့ရတယ်။

##### Creating Functions

C language မှာတော့ function တစ်ခုဖန်တီးတော့မယ်ဆိုရင် အရင် ကြေညာရတယ်။ အဲ့တာမှ compiler ကို အောက်မှာ user-written functions ‌တွေရှိတယ်ဆိုတာ ကြိုသိစေတယ်။ 

###### Function Declaration

function declaration လုပ်တာက main() function ရဲ့ ‌အပေါ်မှာ လုပ်ထားရတယ်။

standard form --> <span style="color:rgb(0, 176, 240)">return-type</span> <span style="color:rgb(255, 155, 0)">name</span>(<span style="color:rgb(146, 208, 80)">argument-list</span>)

e.g. int multiplication(int x, int y);

return-type - function က ပြန် output ထုတ်ပေးမယ့် variable ရဲ့ data-type

name - function ရဲ့ နာမည်

argument-lists - functions ထဲကို ထည့်ပေးလိုက်ချင်တဲ့ Inputs တွေ, တစ်ခုထက်ပိုတဲ့အခါ comma ခြားပြီးထည့်ရတယ်။ type ရယ် name ရယ် ပါတယ် e.g. (int a, string s\[])
\
###### Function Definition

declare လုပ်ပြီးသွား၇င် function ကို define လုပ်ရမယ်။ function အလုပ်လုပ်ဆောင့်မယ့် ပုံစံအတိုင်း function ထဲမှာ code တွေရေးတာ

--> return-type name(argument-lists)
	{
	  code-here;
	}

###### Function Call

declare & define လုပ်ပြီးသွားပြီဆိုရင် code ရေးတဲ့အချိန်မှာ လိုအပ်တဲ့အခါ function ကို ခေါ််သုံးလို့ရပြီ။

--> name(arguments)

e.g. multiplication(2,3);

##### Function miscellany

- input (arguement-lists) မှာ ဘာ data type မှ လက်မခံဘူးဆိုရင် 'void' argument list ကိုသုံးရတယ်။ e.g. int main(void)

- output မရှိတဲ့ function မျိုးဆိုရင်တော့ return-type နေရာမှာ void ကိုသုံးရတယ်။
