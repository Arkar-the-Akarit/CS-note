##### <span style="color:rgb(0, 255, 255)">Font Weight</span>

စာသားတွေကို <mark style="background: #FF5582A6;">Thickness / Bold အထူ၊ အပါး</mark> လုပ်ဖို့

property : <span style="color:rgb(255, 255, 0)">font-weight
</span>
value : ပုံမှန်ကတော့ <mark style="background: #FFF3A3A6;">normal, bold</mark> ကိုအသုံးများ
		![[values of font-weight property.png]]
		ပြထားတဲ့ typeface ရဲ့ value တွေက <mark style="background: #D2B3FFA6;">font ကိုယ်တိုင်က</mark> type-face font styleတွေကို <mark style="background: #ADCCFFA6;">supportပေးမှ</mark> အဲ့တန်ဖိုးတွေက <mark style="background: #ADCCFFA6;">အလုပ်လုပ်မှာ</mark> <mark style="background: #FFF3A3A6;">မဟုတ်ရင် "bold" ဘဲ</mark> အလုပ်လုပ်မယ်

<hr> 
##### <span style="color:rgb(0, 255, 255)">Font Style</span>

စာလုံးတွေကို အစောင်းနဲ့ဖော်ပြဖို့

property: <span style="color:rgb(255, 255, 0)">font-style</span>
value : <mark style="background: #FFF3A3A6;">normal, italic, oblique</mark>

"Italic" ရော "oblique" ‌ရော နှစ်ခုစလုံးက စာလုံးကို‌ <mark style="background: #BBFABBA6;">စောင်းအောင်လုပ်တာဘဲ</mark>

**ကွာခြားချက်**
- italic က font ဖန်တီးသူက version ကွဲ variant အနေနဲ့ <mark style="background: #ADCCFFA6;">italic အတွက် သီးသန့်ဖောင့်</mark>ကို လုပ်ပေးထားရင်သုံး
- oblique ကတော့ italic အတွက် သီးသန့်စောင်းဖောင့် မပါရင်သုံး။ သူက လက်ရှိဖောင့်အမျိုးအစားကိုဘဲ စောင်းပြိး စကားလုံးစောင်းပုံစံ (italic appearance) ဖြစ်အောင်လုပ်ပေးလိုက်တာ။ 
ပုံမှန်ကတော့ အတူတူပါဘဲ။ web ‌လောကမှာတော့ oblique ကို အသုံးများ

<hr> 
##### <span style="color:rgb(0, 255, 255)">Text အတွက် Units များ</span>

<mark style="background: #D2B3FFA6;">Default</mark> အနေနဲ့က <mark style="background: #D2B3FFA6;">< p > element</mark> ထဲက စာသားတွေက <mark style="background: #D2B3FFA6;">16px</mark> / 16 pixel scale ရှိတယ်

property : <span style="color:rgb(255, 255, 0)">font-size</span>
value unit : <mark style="background: #FFF3A3A6;">"px", "em", "%"</mark>

"em" နဲ့ "%" တို့က default body text size နဲ့သွားတာ

ပုံမှန်ဆို browser ရဲ့ <span style="color:rgb(0, 112, 192)">default body text size</span> က <span style="color:rgb(0, 176, 240)">16px</span>. ဒီမှာဆိုရင် <mark style="background: #ADCCFFA6;">16px = 1em = 100%</mark> ဖြစ်သွားပြီ။ <mark style="background: #ADCCFFA6;">32px = 2em = 200%</mark> ပေါ့။

	![[text unit equavilent.png|500]]

<mark style="background: #FF5582A6;">မှတ်ချက်</mark> : <span style="color:rgb(0, 176, 240)">1em</span> က အမြဲတမ်း 16px မဟုတ်။<mark style="background: #FFF3A3A6;"> body{ font-size: 16px}</mark>  
ဆိုတာက browserက သတ်မှတ်ပေးထားတာ။ အကယ်လို့ <span style="color:rgb(0, 176, 240)">body{font-size: 12px}</span> လို့ သွားပြောင်းလိုက်ရင် <mark style="background: #FFF3A3A6;">12px</mark> = 1em = 100% ဖြစ်သွားမယ်။

<hr> 
##### <span style="color:rgb(0, 255, 255)">Text Transform
</span>

စကားလုံးတွေကို စာလုံးအကြီးပြောင်း၊ အသေးပြောင်း၊ ရှေ့စာလုံးအကြီးပြောင်း စတာတွေအတွက်

property: <span style="color:rgb(255, 255, 0)">text-transform</span>
value: <mark style="background: #FFF3A3A6;">"uppercase", "lowercase", "capitalize"</mark> 
	   ![[text transform example.png]]

<hr>

##### <span style="color:rgb(0, 255, 255)">Text Decoration</span> 

<mark style="background: #ADCCFFA6;">မျဥ်းလိုင်း</mark>တွေကိုသုံးပြီး <mark style="background: #ADCCFFA6;">အောက်မှာ မျဥ်းတား</mark>တာ (သို့) <mark style="background: #ADCCFFA6;">အလယ်ကနေ ကန့်လန့်ဖြတ်</mark>တာမျိုးအတွက်

property: "<span style="color:rgb(255, 255, 0)">text-decoration-line</span>",
          "<span style="color:rgb(255, 255, 0)">text-decoration-color</span>", (line ရဲ့ အရောင်)
          "<span style="color:rgb(255, 255, 0)">text-decoration-style</span>", (တစ်ဖြောင့်တည်း၊ dot-dat..)
          "<span style="color:rgb(255, 255, 0)">text-decoration-thickness</span>", (line ရဲ့ အထူ)

value of text-decoration-line: <mark style="background: #FFF3A3A6;">"none", "underline", "overline", "line-through"</mark>
![[value of text-decoration-line.png|500]]

value of text-decoration-style: <mark style="background: #FFF3A3A6;">"solid", "double", "dotted", "dashed", "wavy"</mark>
![[value of text-decoration-style.png|500]]

<mark style="background: #FF5582A6;">အတိုကောက်ရေးသားပုံ: </mark>

```
p{
	text-decoration: line color style thickness;
}
```

![[short-form of text-decoration.png | 500]]

<hr>

##### <span style="color:rgb(0, 255, 255)">Text Line-Height</span>

စာကြောင်း <mark style="background: #FFF3A3A6;">တစ်ကြောင်းနဲ့ တစ်ကြောင်းကြား အကွာအဝေး</mark>သတ်မှတ်တာ

property: <span style="color:rgb(255, 255, 0)">line-height</span>
value: <mark style="background: #FFF3A3A6;">no / %</mark>

browserတွေရဲ့ default line-height က 110% ~ 120% 
"line-height: 1" ဆိုရင်<mark style="background: #ABF7F7A6;"> 100%</mark>, <mark style="background: #FF5582A6;">လက်ရှိ ဖောင့်ဆိုဒ်</mark> ရဲ့ <mark style="background: #ADCCFFA6;">တစ်ဆ </mark>

![[line-height example.png | 450]]

<hr>

##### <span style="color:rgb(0, 255, 255)">letter spacing & word spacing</span> 

<mark style="background: #D2B3FFA6;">letter (စာလုံး)</mark> တစ်လုံး ဆီကြားက အကွာအဝေး နဲ့ <mark style="background: #ABF7F7A6;">word (စကားစု)</mark> တစ်လုံးဆီကြားက အကွာအဝေး

property: <span style="color:rgb(255, 255, 0)">letter-spacing</span> / <span style="color:rgb(255, 255, 0)">word-spacing</span>
value: <mark style="background: #FFF3A3A6;">px</mark> 
	   ![[letter spacing & word spacing example.png]]
	   
<hr>

##### <span style="color:rgb(0, 255, 255)">Text Alignment ချိန်ခြင်း</span>

စာသားတွေရဲ့ တည်နေရာကို ပြောင်းလဲသတ်မှတ်

property: <span style="color:rgb(255, 255, 0)">text-alignment</span>
value: <mark style="background: #FFF3A3A6;">"left", "right", "center", "justify"</mark> 

- left : <span style="color:rgb(146, 208, 80)">Default</span>, ဘယ်ဘက်ကို ကပ်နေစေတာ
- right : ညာဘက်ကပ်
- center : အလယ်မှာပေါ်
- justify : ‌<span style="color:rgb(146, 208, 80)">နောက်တစ်လိုင်းဆင်းခါနီးမှာ</span> ကြားလိုအပ်တဲ့ <span style="color:rgb(255, 105, 180)">space‌ တွေကို ဖြည့်ပေး</span>
- ![[text-align example.png | 450]]

<hr>

##### <span style="color:rgb(0, 255, 255)">Text တွင် အရိပ်ထည့်ခြင်း</span>

စာသားတွေရဲ့ အနောက်မှာ Shadow <span style="color:rgb(255, 105, 180)">အရိပ်ကိုဖော်ပြ</span> ချင်ရင်သုံး

property: <span style="color:rgb(255, 255, 0)">text-shadow</span>
value: <mark style="background: #FFF3A3A6;">"X-offset" "Y-offset" "Blur Radius" "Color of shadow"</mark>

value <span style="color:rgb(220, 20, 60)">လေးခုလုံးထည့်</span>ပေးရမယ်။ 

![[text-shadow property example.png]]

![[text-shadow with output.png]]

- X-offset: horizontal line မှာရှိတဲ့ X တန်ဖိုး၊ <span style="color:rgb(0, 176, 240)">များလေလေ အရိပ်က ညာဘက်ကို ထွက်လေလေ</span>၊ <mark style="background: #FFF3A3A6;">ဘယ်ဘက်</mark> ကို တိုးချင်ရင် <span style="color:rgb(255, 155, 0)">(-) minus တန်ဖိုး </span>    ![[x-offset value in text-shadow.png | 450]]

- Y-offset: vertical line မှာရှိတဲ့ Y တန်ဖိုး၊ <span style="color:rgb(0, 176, 240)">များလေလေ အရိပ်က အောက်ကို ကျလေလေ</span>၊ <mark style="background: #FFF3A3A6;">အပေါ်တက်</mark> ချင်ရင် <span style="color:rgb(255, 155, 0)">(-) minus တန်ဖိုး</span>             ![[y-offset value in text-shadow.png | 450]]

- Blur Radius: အရိပ်ရဲ့ မှုန်ဝါးမှုစက်ဝန်းရဲ့ အကျယ် <mark style="background: #FFF3A3A6;">(px)</mark> နဲ့ ထည့် 

  ![[blur radius value in text-shadow.png | 500]]

- Color: အရိပ်ရဲ့ အရောင်ပေါ့

<hr> 
