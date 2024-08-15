Class Attribute က element အကုန်လုံးမှာ သုံးလို့ရတဲ့ <span style="color:rgb(0, 112, 192)">Global Attribute</span> 
သူ့ကို elements တွေမှာ <span style="color:rgb(255, 255, 0)">တစ်ခု (သို့ ) တစ်ခုထက်ပိုတဲ့</span> <span style="color:rgb(112, 48, 160)">Class Names </span> တွေ Assign လုပ်ဖို့သုံးတယ်။
Class Name တွေကို သုံးပြီး CSS နဲ့ Style လုပ်တာ၊ JS နဲ့ manipulate လုပ်တာတွေအတွက် သုံးလို့ရတယ်
```
<p class= "class1 class2 class3"> This is class test </p>

<h1 class= "class3 classTest"> Hello World! </h1>

CSS:
 .class3{
	 background-color: blue;  // appliable to both h1 and p bcz of class3 
 }
```