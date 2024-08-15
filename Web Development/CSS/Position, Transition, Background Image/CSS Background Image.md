
background ကို အရောင်ထားသလိုဘဲ ပုံတွေထားလို့ရတယ်

property: <span style="color:rgb(255, 155, 0)">background-image</span>
value: <mark style="background: #FFF3A3A6;">url("file path")</mark>

```
.container{
	background-image: url("path/image.jpg");
}
```

![[background-image property.png]]

အခြား သူနဲ့ သက်ဆိုင်တဲ့ property တွေက

- <span style="color:rgb(255, 155, 0)">background-repeat</span>
- <span style="color:rgb(255, 155, 0)">background-size</span>
- <span style="color:rgb(255, 155, 0)">background-position</span> 

##### Background-repeat

ပုံကိုထပ်ခါတလဲလဲ ပြန်သုံးမလား၊ မသုံးဘူးလားသတ်မှတ်တာ

background-repeat: <mark style="background: #FFF3A3A6;">no-repeat</mark>; ဆိုရင် ပုံကို <span style="color:rgb(220, 20, 60)">ပြန်မသုံးဘဲနဲ့</span> ၊ ပုံရဲ့ <span style="color:rgb(0, 176, 240)">size ရှိသလောက်ဘဲ ယူ</span>သွားမယ်

: <mark style="background: #FFF3A3A6;">repeat</mark> ; ဆိုရင် ပုံကို ထပ်ခါထပ်ခါ မပြည့်မချင်းယူသွားမယ်

: <mark style="background: #FFF3A3A6;">repeat-x</mark> ; ဆိုရင် ပုံကို အလျားလိုက် x-ဝင်ရိုးမှာ ထပ်ခါထပ်ခါယူသွားမယ်

: <mark style="background: #FFF3A3A6;">repeat-y</mark> ; ဆိုရင် ပုံကို ဒေါင်လိုက် y-ဝင်ရိုးမှာ ထပ်ခါထပ်ခါယူသွားမယ်

![[property background-repeat.png]]

##### Background Size

background မှာထားမယ့် image ရဲ့ size ကို သတ်မှတ်ပေးတာ

သတိထားရမှာက background-repeat property က ပုံရဲ့ size ကို မူတည်အလုပ်လုပ်တာဖြစ်လို့ background-size property က သက်ရောက်မှုရှိ

background-size: <mark style="background: #FFF3A3A6;">cover</mark>; ဆိုရင် နောက်က container ရဲ့ size အပြည့်ကိုယူတယ်

value တွေကို  "<mark style="background: #FFF3A3A6;">x-တန်ဖိုး y-တန်ဖိုး</mark>" နဲ့ သတ်မှတ်လို့ရသလို၊ "<mark style="background: #FFF3A3A6;">percentage</mark>" နဲ့လည်းသတ်မှတ်လို့ရ၊ ပြီးတော့ "<mark style="background: #FFF3A3A6;">top right/ left right</mark>" အစရှိသဖြင့်လည်း သတ်မှတ်လို့ရ

![[background-size property.png]]

![[css background-size.png]]