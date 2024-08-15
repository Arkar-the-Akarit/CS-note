
HSL ရဲ့ Hue, Saturation, & Lightness ပါ။
နားလည်လွယ်စေပေမယ့် အသုံးနည်းပါတယ်။

![[Color Wheel.png]]
color စက်ဝန်း

###### Hue 

သူက traditional color wheel ( အရောင်စက်ဝန်း ) ရဲ့ အရောင်တစ်ခုကို ကိုယ်စားပြုပါတယ်။
CSS မှာ hue ကို <mark style="background: #FFF3A3A6;">color စက်ဝန်းရဲ့ </mark> 0 degree ( ဒီဂရီ) ကနေ 360 degree အတွင်းမှာရှိတဲ့ <mark style="background: #ADCCFFA6;">ထောင့်တစ်ထောင့်</mark> တန်ဖိုးကို ယူပြီး သတ်မှတ်ပေးရတယ်။

- အနီ‌ရောင်က 0 degree စမှတ်
- အစိမ်းရောင်က 120 degree
- အပြာ‌ရောင်က 240 degree အသီးသီးမှာ ရှိ

###### Saturation

ရာခိုင်နှုန်း Percentage အနေနဲ့ ‌ရေးရပြီး
<mark style="background: #ABF7F7A6;">0 % ( မီးခိုး‌ရောင်စကေး )</mark> ကနေ <mark style="background: #ABF7F7A6;">100 % (ထင်ရှားသော အရောင်)</mark> အဖြစ် သတ်မှတ်ပေးရတယ်။

ရာခိုင်နှုန်း <span style="color:rgb(0, 176, 240)">နည်း</span> ရင် <span style="color:rgb(0, 176, 240)">နည်းနည်းဖျော့တေ့</span> ပြီး
ရာခိုင်နှုန်း <span style="color:rgb(255, 255, 0)">များ</span>  ရင် <span style="color:rgb(255, 255, 0)">ထင်ထင်ရှားရှား</span> 

###### Lightness


အလင်းကို ကိုယ်စားပြုပြီး အရောင်ကို <mark style="background: #FFF3A3A6;">ပိုတောက်၊ပိုလင်း</mark> (သို့) <mark style="background: #ADCCFFA6;">ပိုမှောင်</mark> သွားစေဖို့ သုံး။ သူလည်း ရာခိုင်နှုန်းအနေနဲ့ ဘဲ‌ရေးရတယ်။

<mark style="background: #ABF7F7A6;">0 % ( လုံးဝအနက်ရောင် )</mark> ကနေ <mark style="background: #ABF7F7A6;">100 % (လုံးဝအဖြူရောင်)</mark>

<mark style="background: #FFB86CA6;">0 - 50 %</mark> ကြားက တန်ဖိုးတွေက <mark style="background: #FFB86CA6;">ပိုမိုနက်နဲတဲ့ အမှောင်</mark> ကိုဖြစ်စေပြီး
<mark style="background: #D2B3FFA6;">50 - 100 %</mark> ကြားက တော့ <mark style="background: #D2B3FFA6;">ပိုလင်းတဲ့ အရောင်</mark>ကို ဖြစ်စေတယ်။


###### CSS မှာရေးမယ်ဆိုရင်
```
hsl(0,100%,50%)
```

h = 0, hue က 0 degree က အရောင်ဆိုတော့ အနီ
s = 100%, Saturation က အထင်ရှားဆုံး 100%
l = 50%, lightness က တော့ အလင်းရဲ့ အစ 50%

အရောင် အတွက် hue ( color ထောင့်နံပါတ်ကို ) ရပြီ ဆိုတာနဲ့ အလင်း၊ အမှောင် s, l တို့ကို လိုသလို အလျော့အတင်းလုပ်ပြီး အရောင်ကို ပြောင်းလဲလို့ရလို့ Designer တွေကတော့ HSL အရောင် စနစ်ကို အသုံးများတယ်။