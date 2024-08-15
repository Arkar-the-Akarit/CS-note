
unit: <mark style="background: #FFF3A3A6;">‌"auto"</mark>, <mark style="background: #FFF3A3A6;">"px"</mark>, <mark style="background: #FFF3A3A6;">"%"</mark> 

###### True Width of Element

html မှာ element တစ်ခုရဲ့ total/true width က

<mark style="background: #FFF3A3A6;">total width = width + padding (left + right) + border (left + right )</mark>

ရှင်းရှင်းလေးပါ။

width ကို 100px ထားလိုက်တယ်, padding-left: 10px, padding-right: 10px, border-left: 10px, border-right: 20px ဆိုရင်

အဲ့ element ဖြစ်လာမယ့် width က

total width = 100px + (10px + 10px) + (10px + 20px) = 150px ပေါ့။

အဲ့လို မဖြစ်စေချင်ရင်<span style="color:rgb(0, 176, 240)"> property box-sizing</span>: <span style="color:rgb(0, 128, 128)">border-box value</span> ကိုသုံးလို့ရတယ်။ ကိုယ်ထားလိုက်တဲ့ width က 100 px ဆိုရင် အဲ့ထဲမှာဘဲ padding တွေ border တွေရဲ့ width ကိုထည့်ယူသွားတယ်။ content ကတော့ <span style="color:rgb(255, 155, 0)">သေးသွားနိုင်</span>တာပေါ့



height ဆိုရင်တော့ padding, border က top + bottom ပေ့

```
<!DOCTYPE html>
<html>
<head>
    <style>
        .box-content-box {
            width: 200px;
            padding: 20px;
            border: 10px solid black;
            background-color: lightblue;
            margin-bottom: 20px;
        }
        
        .box-border-box {
            width: 200px;
            padding: 20px;
            border: 10px solid black;
            background-color: lightgreen;
            box-sizing: border-box;
        }
    </style>
</head>
<body>
    <div class="box-content-box">
        This box uses the default box-sizing: content-box.
    </div>
    <div class="box-border-box">
        This box uses box-sizing: border-box.
    </div>
</body>
</html>

```

![[css_box-sizing property.png]]

###### Min-Width & Max-width

 property: "<span style="color:rgb(255, 155, 0)">min-width</span>" , "<span style="color:rgb(255, 155, 0)">max-width</span>"
 value: <mark style="background: #BBFABBA6;">px</mark>, <mark style="background: #BBFABBA6;">auto</mark>, <mark style="background: #BBFABBA6;">%</mark>

 min-width: 200px ဆိုရင် ကိုယ် selected လုပ်ထားတဲ့ element ရဲ့ အကျယ်ကို <span style="color:rgb(0, 255, 255)">အနည်းဆုံး</span> 200px ထားမယ်လို့ပြောတာ

 m‌‌ax-width: 200px ဆိုရင် ကိုယ် selected လုပ်ထားတဲ့ element ရဲ့ အကျယ်ကို <span style="color:rgb(0, 255, 255)">အများဆ</span>ုံး 200px ထားမယ်လို့ပြောတာ။ ပုံတစ်ပုံ ထည့်လို့ သူ့width က 1000px ရှိနေတယ်ဆိုရင် 200px ထိလျော့ပေးမယ်

###### <span style="color:rgb(255, 155, 0)">auto</span> :

element တစ်ခုရဲ့ width ကို <span style="color:rgb(146, 208, 80)">auto</span> နဲ့ သုံးမယ်ဆိုရင် browser က အဲ့ element အတွက် width ကို သူ့ရဲ့ <span style="color:rgb(146, 208, 80)">child element / content အကုန် ဆံ့</span>အောင် / <span style="color:rgb(146, 208, 80)">overflow မဖြစ်အောင်</span> သတ်မှတ်ပေးမှာ
i.e. <span style="color:rgb(0, 255, 255)">automatically adjusted to fit</span> all of the content

<span style="color:rgb(220, 20, 60)">Block element</span> ဆို <span style="color:rgb(0, 176, 240)">parent</span> element <span style="color:rgb(0, 176, 240)">အကျယ်ကို အပြည့်ယူ</span>

<span style="color:rgb(220, 20, 60)">inline element</span> ဆို <span style="color:rgb(0, 176, 240)">ကိုယ်ပိုင် content</span> ရှိသလောက်ယူ

အကယ်လို့ child element ရဲ့ width ကို 'auto' နဲ့သုံးမယ်ဆိုရင် ဖြစ်လာနိုင်တဲ့ အခြေအနေတွေက child element ရဲ့ content/context ပေါ်မူတည်တယ်

1. child element <span style="color:rgb(0, 255, 255)">with </span>defined parent element width
		parent element အတွက် တိကျတဲ့ width ကို defined <span style="color:rgb(220, 20, 60)">လုပ်</span>ထားတယ်ဆိုရင် child element က သူ့ width ကို parent element အထဲမှာ ဝင်ဆံ့နိုင်အောင် auto adjust လုပ်မယ်၊
		
2. child element <span style="color:rgb(0, 255, 255)">without</span> defined parent width
		parent element က undefined width နဲ့ဆိုရင် child element ကို auto လည်းထားထားမယ်, သူ့ content တွေက <span style="color:rgb(0, 255, 255)">parent element width ထက်ပိုကြီးနေ‌မယ်ဆိုရင်</span> [[CSS Overflowing Content|Overflow]]ဖြစ်လာပြီး
		ကိုယ်က ဒါကို <mark style="background: #FFF3A3A6;">overflow property</mark> နဲ့ ဘယ်လိုကိုင်တွယ်မယ်ဆိုတာပေါ်မူတည်ပြီး ပြောင်းသွားမယ်

###### <span style="color:rgb(255, 155, 0)">px</span> :

fixed height သတ်မှတ်ပေးဖို့သုံးတယ်။ <span style="color:rgb(146, 208, 80)">absolute unit</span> ဖြစ်တာကြောင့် screen size ဘယ်လိုရှိရှိ သတ်မှတ်လိုက်တဲ့ အတိုင်း element height က  အတိအကျထွက်လာမယ်။

###### <span style="color:rgb(255, 155, 0)">
%</span> :

သူက<span style="color:rgb(255, 155, 0)"> parent element ရဲ့ height အပေါ်မူတည်</span>ပြီး သုံးလိုက်တဲ့ element ရဲ့  height ကို သတ်မှတ်ပေးတာ။ <span style="color:rgb(146, 208, 80)">relative unit</span>,
ဒီတော့ သူ့ရဲ့ height က parent container/element ရဲ့ height အပေါ်မူတည်တယ်။

###### <span style="color:rgb(255, 155, 0)">vw (viewport width)</span>

viewport ဆိုတာ user သုံးနေတဲ့ device ထဲက browser ရဲ့ web page ကိုပြပေးတဲ့ အကျယ် (i.e. <span style="color:rgb(255, 105, 180)">visible area of webpage in browser</span>) ၊ browser ရဲ့ toolbars, menus, scrollbars တွေမပါဘူး။ web page design ကို user မြင်ရတဲ့ အပိုင်းကို viewport လို့ခေါ််တယ်။

viewport width က <span style="color:rgb(146, 208, 80)">relative unit</span>, viewport ရဲ့ အကျယ် (width) ကို percentage နဲ့ ကိုယ်စားပြုတယ်။ <span style="color:rgb(255, 105, 180)">measurement unit</span> က <mark style="background: #FFB8EBA6;">" vw "</mark> 

1vw ဆိုရင် သူက viewport's width ရဲ့ 1% ကို ကိုယ်စားပြုတယ်။ အကယ်လို့ <span style="color:rgb(255, 105, 180)">viewport</span> က <span style="color:rgb(255, 105, 180)">1000 pixels</span> အကျယ်ရှိတယ်ဆိုရင်၊ <span style="color:rgb(0, 128, 128)">1vw</span> က <span style="color:rgb(0, 128, 128)">10 pixels</span> ပေါ့

100vw ဆိုရင်တော့ 100% ပေါ့။ selected element က viewport နေရာ အပြည့်ယူသွားလိမ့်မယ်။

သူက elements တွေကို viewport size ပေါ်မူတည်ပြီး အချိုးကျကျ scale လုပ်ပေးနိုင်တာကြောင့် <span style="color:rgb(146, 208, 80)">responsive design</span> အတွက်ကောင်းတယ်။
ပြီတော့ viewport size ပြောင်းတာနဲ့ vw သံုးထားတဲ့ elements တွေကပါ လိုက်ပြောင်းတာကြောင့် <span style="color:rgb(146, 208, 80)">consistent layout</span> ဖြစ်စေတယ်။

###### Container 1 - Width Auto

```
html:

<div class= " width-auto "> Container 1 - Width Auto </div>

```

```
css:

div {
	margin-bottom: 10px;
	border-radius: 3px;
}

.width-auto {
	width: auto;
}

```

![[element-height_width-auto.png]]

container 1 က width auto ကို သုံးလိုက်တယ်။ div က block element, ဒီတော့ သူ့ parent element ဖြစ်တဲ့ < body > element အကျယ်အတိုင်း အပြည့်ယူ

###### Container 2 - Width Px

```
<div class=" width-250px bg-pink>
	Conatiner 2 -- Width 250 px with Background Color Pink
</div>

```

```
.width-250px {
	width: 250px;
}

```

![[css width - 250px.png]]
250 px ပေးလိုက်တဲ့ အတွက် အဲ့ အတိုင်း အတိအကျယူ

###### Container 3 - Width %

```
<div class="widht-50-percent bg-lightblue>
	Contianer 3 -- Width 50% and Background color lightBlue
</div>
```

```
.width-50-percent{
	width: 50%;
}
```
![[css width - 50 percent.png]]
parent element < body > ရဲ့ 50% အကျယ်ကို ယူ

###### Container 4 - width 100%, padding 50px

```
<div class="width-250px container">
	<div class="width-100-percent bg-lightblue padding-left-50px>
		Container 4 -- Width 100%, 
		Padding left 50px;
	</div>
</div>
```

```
.width-250px {
	width: 250px;
}

.width-100-percent {
	width: 100%;
}

.padding-left-50px {
	padding-left: 50px;
}

```

![[css_width - container 4.png]]

parent element ရဲ့ width သည် 250px, child element ရဲ့ width သည် <mark style="background: #FFF3A3A6;">100% (in this case - 250px)</mark> ။ ဒါပေမယ့် <mark style="background: #FFB86CA6;">padding-left : 50 px </mark>ဆိုတာပါ ပါလာတယ်။ ဒီတော့ [[Width of HTML box in CSS#True Width of Element|True width of element]] အရ width နဲ့ padding နဲ့ပေါင်းပြီး total width က 300px ဖြစ်ပြီး parent element ကနေ overflow ဖြစ်သွားတယ်။

padding သုံးလို့ child element ရဲ့ content က သူ့ box နဲ့ ခြားတာ၊ margin သုံးရင်‌တော့ bg-lightblue နဲ့ စာတွေနဲ့က ကပ်နေပြီး နောက်က bg-black ကိုမြင်ရပြီး overflow ဖြစ်မယ်။
![[css_width -- width 100, margin left.png]]

###### Container 5 - Width Auto, Padding-left 50px

```
<div class="width-250px container">
	<div class="width-auto bg-lightblue padding-left-50px">
		Contianer 5 -- Width Auto, Padding Left 50px
	</div>
</div>

```

```
.width-250px {
	width: 250px;
}

.width-auto {
	width: auto;
}

.padding-left-50px {
	padding-left: 50px;
}
```
![[css_width - container 5.png]]

ဒီမှာဆို auto width ထားလိုက်တယ်၊ parent element ကလည်း defined width နဲ့၊ ဒီတော့ browser ကနေပြီးတော့ child element ဟာ padding, border ဘာညာစတာတွေပါပြီးတာတောင်မှ parent element အတွင်းမှာ fit ဖြစ်အောင် automatically adjust လုပ်ပေးတယ်။