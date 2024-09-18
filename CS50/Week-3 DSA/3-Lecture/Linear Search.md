#DSA #LinearSearch

array လိုမျိုးထဲကနေ elements တစ်ခုကို ရှာချင်တဲ့အခါမျိုးမှာ elements တစ်ခုချင်းဆီကို လိုက်ကြည့်ပြီးတော့ တူသလား, မတူဘူးလား ရှာတာမျိုးကို linear search လို့ခေါ်တယ်။

![[locker array.png]]
ဒီလိုမျိုးထဲမှာဆို element value 50 ရှိသလားဆိုပြီး ရှာချင်တယ်။ index တစ်ခုဆီကို လိုက် check လုပ်ပြီးတော့ 
![[linear search black box.png]]
ရှိတယ် (yes), မရှိဘူး (no) ဆိုတဲ့ boolean value တစ်ခု return ပြန်ပေးမှာ။

```
pseudo code:

For i from 0 to n-1
	If 50 is behind doors[i]
		Return True
Return False


```