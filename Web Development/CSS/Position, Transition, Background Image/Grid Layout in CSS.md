
modern ခေတ်မှာ <span style="color:rgb(255, 155, 0)">အသုံးအများဆုံး</span> layout CSS

###### Grid Structure မှာ ဘာတွေပါလဲ

grid မှာ <span style="color:rgb(0, 255, 255)">vertical</span> line နဲ့ <span style="color:rgb(0, 255, 255)">horizontal</span> line တွေပါပါတယ်။

![[grid strucutre.png]]

ဒါကြောင့်မလို two dimensional အတွက် <span style="color:rgb(255, 105, 180)">layout ကို လိုသလို ထိန်းချုပ်</span>လို့ရ

grid ရဲ့ <span style="color:rgb(0, 255, 255)">vertical</span> line ကြားက နေရာတွေကို <span style="color:rgb(255, 155, 0)">column</span> လို့ခေါ်ပြီး
grid ရဲ့ <span style="color:rgb(0, 255, 255)">horizontal</span> line ကြားက နေရာတွေကို <span style="color:rgb(255, 155, 0)">row</span> လို့ခေါ်ပါတယ်။
![[grid row & column.png]]

column နဲ့ row ကြားက <span style="color:rgb(0, 176, 240)">cell ကွက် တစ်ကွက်</span>ဆီကို <span style="color:rgb(0, 176, 240)">grid items</span> တွေလို ခေါ််တယ်။ row တစ်<span style="color:rgb(255, 155, 0)"> row ဆီတိုင်း</span>ကို <span style="color:rgb(255, 155, 0)">grid container</span> လို့ခေါ််တယ်။ သူ့အထဲမှာ ရှိတာတွေက <span style="color:rgb(0, 176, 240)">grid items</span> တွေပေါ့။
![[grid container & grid item.png]]

##### Grid Column

output:
![[output of grid column test.png]]

html:
```
<div class="grid">
	<div class="box"></div>
	<div class="box"></div>
	<div class="box"></div>
	<div class="box"></div>........
</div>
```

css:
```
.grid{

	display: gird;

	grid-template-columns: 20% 30% 50%; 
						   1fr 1fr 1fr;
						   repeat(3, 1fr);
	
}

.box{
	padding: 3rem; /* root em, relative meassurement unit, start measuring from root, i.e. < html > element
	background-color: #74b9ff;
}

.box:nth-child(even){
	background-color: #a29bfe
}

```

<mark style="background: #FFF3A3A6;">display : grid</mark>   ဆိုတာက target container element ရဲ့ display ကို ဘယ်လိုထားမလဲလို့ သတ်မှတ်လိုက်တာ။ အဲ့ container ထဲမှာ ရှိသမျှ direct child elements တွေ (<span style="color:rgb(255, 155, 0)">whether inline or block</span>) , (not include grand-child elements) အကုန်လုံးက grid items တွေဖြစ်လာတယ်။ container ကို သတ်မှတ်ပေးလိုက်မယ့် grid context အတိုင်းဘဲ grid items တွေက အစီအစဥ်ချခံရမယ်

###### Grid-template-column

<mark style="background: #FFF3A3A6;">grid-template-column: 20% 30% 50%;</mark>

ဒီ property က <span style="color:rgb(255, 155, 0)">column အ‌ရေအတွက်</span>နဲ့ <span style="color:rgb(0, 255, 255)">column တစ်ခုဆီရဲ့အကျယ်</span>ကို သတ်မှတ်ဖို့ သုံးတာ

အပေါ်က percentage value နဲ့ဆိုရင် <span style="color:rgb(0, 176, 240)">screen width</span> ရဲ့ ဘယ်လောက် percent ကို ယူမယ်ဆိုပြီး သတ်မှတ်တာ
![[grid-tempalte-column-percentage.png]]

grid-template-column: <mark style="background: #FFF3A3A6;">1fr 1fr 1fr / (3,1fr);</mark> 
ဘယ်လိုရေးရေး တူတူဘဲ။ 1fr သုံးခါရေးရေး/ (3,1fr)ဆိုပြီး ရေး‌ရေး နဲ့ 1fr ဆီရှိတဲ့ column သုံးခုရမယ်။

<mark style="background: #ADCCFFA6;">fractional unit (fr)</mark> : သူက grid container ရဲ့ space ကို အပိုင်းပိုင်းပြီး သတ်မှတ်လိုက်တဲ့ fr အလျောက်ခွဲပေးမှာ။
```
gird-column-template: 1fr 2fr 1fr;
```
ဆိုရင် လေးပိုင်းပိုင်းပြီး အလယ် column က 2fr နေရာရမယ်။
```
grid-column-template: 100px 1fr 2fr;
```
ဆိုရင် ပထမဆုံး column အတွက် 100pixel နေရာယူပြီးမှ ကျန်တဲ့အကျယ်ကို သုံးပိုင်းပိုင်း ဒုတိယcolumnက 1fr, တတိယcolumn က 2fr ရမယ်။

![[fractional unit - fr.png]]
![[fr - usage.png]]

##### Grid Row

CSS:
```
.grid{
	display: grid;
	grid-template-columns: repeat(3,200px);

	grid-auto-rows: 200px;
				    minmax(200px,auto);
				    
				    
	grid-tmeplate-rows:   100px 200px 300px;
					    repeat(3, minmax(50px,auto));
}
```

ဒီမှာက grid-template-column က column သုံးတန်းကို 200px အညီအမျှယူမယ်လို့ပြောတာ

###### Grid-auto-rows

property: <span style="color:rgb(255, 155, 0)">grid-auto-rows</span>

သူကကျ grid items တွေက သတ်မှတ်ထားတဲ့ defined grid ကိုကျော််ပြီး row အသစ်ဖြစ်လာရင်လည်း အဲ့ကောင်တွေ အတွက်ပါ row သတ်မှတ်ပေးတယ်။

when to use: number of rows is dynamic or unknown, & to ensure additional rows have consistent height

value: 200px ကကျတော့ row တွေကို automatic 200px height (အမြင့်) ပေးမှာ 
![[grid-auto-rows.png]]

အကယ်လို့ 65px လို့ value ပေးလိုက်မယ်ဆိုရင် ဒီလိုဖြစ်သွားမယ်
![[grid-auto-rows-2.png]]

ပုံထဲမှာဆိုရင် grid-auto-rows: 65px; လို့သတ်မှတ်လိုက်တော့ content တွေက cell နဲ့ မဆံ့တော့ဘဲ ပျောက်သွားတယ်။ ဒီလိုပျောက်မသွားအောင်

<span style="color:rgb(255, 155, 0)">grid-auto-rows</span>: <mark style="background: #FFF3A3A6;">minmax(65px,auto)</mark>
ဒီလိုဆိုရင် သူက minimum အနည်းဆုံး height 65px ထားမယ်။ maximum အနေနဲ့ကတော့ auto ဖြစ်တဲ့အတွက် <span style="color:rgb(0, 176, 240)">content အမြင့်အလိုက်</span> cell ကို လိုက်မြင့်ပေးမယ်။ 

![[grid-auto-rows minmax().png]]

![[minmax() output.png]]

###### Grid-template-rows

သူက rows တစ်ခုစီရဲ့ အမြင့်ကို သူတို့ရဲ့ အစီအစဥ်အလိုက် သတ်မှတ်ပေးရတာ။
အကယ်လို့ grid items တွေက အကြောင်းကြောင်းကြောင့် defined grid အပြင်ကိုထွက်ပြီး row အသစ်ယူသွားမယ်ဆိုရင်တော့ သူက အမြင့်သတ်မှတ်ပေးမှာ <span style="color:rgb(220, 20, 60)">မဟုတ်</span>

when to use: when we know the exact number of rows & their heights

```
.grid{
	display: grid;
	grid-template-columns: repeat(3,200px);
	grid-template-rows: 300px 200px 100px;
}
```
<span style="color:rgb(255, 155, 0)">grid-template-rows</span> ကလည်းဘဲ column လိုမျိုးဘဲ <span style="color:rgb(146, 208, 80)">row တစ်တန်းဆီရဲ့ အမြင့်နဲ့ </span><span style="color:rgb(0, 255, 255)">row အရေအတွက်ကို</span> သတ်မှတ်ဖု့ိသုံးတယ်

![[grid-template-rows.png]]

<span style="color:rgb(255, 155, 0)">grid-template-rows</span>: repeat(3,minmax(50px,auto));

ဒီလိုဆိုရင်ကျ row သုံးတန်း၊ တစ်တန်းဆီရဲ့ min အမြင့်က 50px၊ လိုသလောက် auto ထပ်ကျယ်ပေးမယ်

![[grid-template-rows 2.png]]

##### Grid Gaps

CSS:
```
.grid{
	display: grid;
	grid-template-columns: repeate(3,200px);
	grid-template-rows: repeate(3,minmax(50px,auto));

	grid-row-gap:10px;
	grid-column-gap: 10px;

	/* grid-gap: 10px; */
	/* grid-gap: 20px 30px */
	
}
```

<span style="color:rgb(255, 155, 0)">grid-row-gap</span>: က row တစ်တန်းနဲ့ တစ်တန်းကြားက အကွာအဝေး
<span style="color:rgb(255, 155, 0)">grid-column-gap</span>: က column တစ်ခုနဲ့ တစ်ခုကြားက အကွာအဝေး
![[grid-gap.png]]

<span style="color:rgb(255, 155, 0)">grid-gap</span>: ဆိုရင်တော့ သူက row & column နှစ်ခုလုံးအတွက် ခြားပေးမှာ
value တစ်ခုဘဲ ဆိုရင် row & column ညီတူညီမျှ
value <span style="color:rgb(146, 208, 80)">နှစ်ခု</span>ဆိုရင် <span style="color:rgb(0, 255, 255)">ပထမတစ်ခုက row</span> , <span style="color:rgb(255, 105, 180)">ဒုတိယတစ်ခုက column</span>
![[gird-gap two value.png]]



##### Grid Column Position နေရာချခြင်း

HTML:
```
<div class='grid">
	<div class="box take-2"> </div>
	<div class="box take-4"> </div>
	<div class="box"> </div>
	<div class="box"> </div>
	<div class="box"> </div>
	<div class="box"> </div>
	<div class="box take-3-auto"> </div>
</div>
```

CSS:
```
.grid{
	display: grid;
	grid-template-columns: repeate(6,1fr);
	grid-template-rows: repeat(7,minmax(50px,auto));
	grid-gap: 10px;
}

.take-2{
	grid-column: 1 / 3;
}

.take-4{
	grid-column: 3 / 7;
}

.take-3-auto{
	grid-column: auto / span 3;
}

.box{
	background-color: #74b0ff;
}

.box:nth-child(even){
	background-color: #a20bfe;
}

```

Output:
![[grid_column_position.png]]

<span style="color:rgb(255, 155, 0)">grid-template-columns</span>: <mark style="background: #FFF3A3A6;">repeat(6,1fr)</mark>; ဆိုတဲ့ အတွက် screen ကို 1 fraction unit စီနဲ့ အပိုင်း‌ခြောက်ပိုင်း ပိုင်းလိုက်တယ်။
![[repeat(6,1fr);.png]]

အဲ့လို အပိုင်း‌‌ခြောက်ပိုင်း ရဖို့အတွက် <span style="color:rgb(146, 208, 80)">grid column line</span> <span style="color:rgb(0, 255, 255)">၇ လိုင်း</span> တိတိဆွဲမှ အပိုင်းခြောက်ပိုင်း/အကွက်ခြော ရလာမှာ, ပုံတွင်ကြည့်

လက်ရှိက သူက <span style="color:rgb(255, 105, 180)">div class="box"</span> တစ်ခုစီက grid column ဖြစ်လာတာဖြစ်တဲ့အတွက် အကွက်‌ခြောက်ကွက်မှာ အဲ့ box class တစ်ခုစီကို နေရာချပေးထားတာ

အဲ့လိုမဟုတ်ဘဲ ကိုယ်က box တစ်ခုဆီကို နှစ်ကွက် ဒါမှမဟုတ် ‌ပိုပြီးနေရာယူစေချင်တယ်။ e.g. class="box take-2" & class="box take-4" တို့လိုပေါ့

အဲ့လိုနေရာချချင်ရင် <span style="color:rgb(146, 208, 80)">grid column line</span> တွေကို သုံးပြီး အကွက်ချရတယ်။ column line number <span style="color:rgb(0, 255, 255)">အစ / အဆုံးကို slash ( / ) </span>ခံပြီးရေး

property: <span style="color:rgb(255, 155, 0)">grid-column</span>
value: <mark style="background: #FFF3A3A6;">starting line point / ending line point</mark>
```
.take-2{
	grid-column: 1 / 3;
}
```

![[grid-column.png]]
ဒီပုံမှာဆို class take 2 ကို column <span style="color:rgb(255, 105, 180)">နှစ်ခု</span>စာယူချင်တယ်။ ဒါကြောင့် စမှတ်ကို 1 ဆုံးမှတ်ကို 3 ဆိုပြီး နှစ်ကွက်ပေးလိုက်တယ်။

class take 4 အတွက်က စမှတ် 3 ဆုံးမှတ် 7, total 4 ကွက်ရသွားတယ်။

အဲ့မှာ ပထမ တစ် row စာ column အကွက် ၆ ကွက်ပြည့်သွားပြီ။ ဒီတော့ နောက်က <span style="color:rgb(255, 105, 180)">ဆက်ရေးတာတွေက ဒုတိယလိုင်းကစ</span>တယ်။ <span style="color:rgb(0, 176, 240)">စမှတ် ၁ ‌ကနေဘဲ ပြန်စ</span>တယ်။

![[grid-column-1.png]]
ဒီပုံကဆိုရင် ဒုတိယ row မှာပေ့ါ။ class take-3-‌‌auto ရဲ့ ရှေ့မှာ box သုံးခုရှိတယ်။ အဲ့တာတွေက grid item တစ်ခုဆီအနေနဲ့ တစ်ကွက်ဆီဘဲယူတယ်။ 

<span style="color:rgb(255, 155, 0)">grid-column</span>: <mark style="background: #FFF3A3A6;">auto / span 3</mark>; ဆိုတာက <span style="color:rgb(0, 176, 240)">auto ကကျ</span> စမှတ်ကို တိတိကျကျ မထားဘဲ gird column line ကို နောက်ဆုံး element/box ပြီးတဲ့ နေရာကစမယ်။ <span style="color:rgb(0, 176, 240)">span 3</span> ဆိုတာကကျ <span style="color:rgb(0, 128, 128)">အကွက် ၃ ကွက်စာ</span> နေရာယူမယ်လို့ပြောတာ။ (i.e. span 2 ဆိုရင် column line 6 မှာ ရပ်သွားမယ်။)

##### Grid Alignment Items ချိန်ညှိခြင်း

![[grid container & grid item.png]]
<span style="color:rgb(0, 176, 240)">gird container ဖြစ်တဲ့ ‌parent element </span>အပေါ်မှာ alignment (property <span style="color:rgb(146, 208, 80)">justify-items, align-items</span>) စတာတွေ သုံးလိုက်တာနဲ့ <span style="color:rgb(255, 105, 180)">grid items တွေအားလုံးအပေါ်သက်‌ရောက်</span>မှုရှိ

HTML:
```
<h3>Grid Container Alignments</h3>
<div class="grid grid-1">
  <div class="box">Box-1</div>
  <div class="box">Box-2</div>
  <div class="box">Box-3</div>
  <div class="box">Box-4</div>
</div>

<h3>Self Items</h3>
<div class="grid">
  <div class="box box-1">Box-1</div>
  <div class="box box-2">Box-2</div>
  <div class="box box-3">Box-3</div>
  <div class="box box-4">Box-4</div>
</div>
```

CSS:
```
.grid{
	display: grid;
	grid-template-columns: repeat(4,1fr);
	grid-auto-rows: minmax(200px,auto);
	grid-gap: 10px;
	margin-bottom: 1rem;
}

.grid-1 {
  /* justify-items: start; */
  /* align-items: start; */
}

.box {
  padding: 1rem;
  background-color: #74b9ff;
}

.box:nth-child(even) {
  background-color: #a29bfe;
}

.box-1 {
  /* justify-self: center; */
  /* align-self: center; */
}
.box-2 {
  /* justify-self: center; */
}

.box-3 {
  /* justify-self: end; */
  /* align-self: start; */
}

.box-4 {
  /* justify-self: stretch; */
  /* align-self: stretch; */
}

```

###### Justify-items

property: <span style="color:rgb(255, 155, 0)">justify-items</span> (သူက grid container ရဲ့ <span style="color:rgb(146, 208, 80)">အလယ်က </span><span style="color:rgb(0, 255, 255)">horizontal မျဥ်း</span>အပေါ် အခြေခံပြီး အလုပ်လုပ်)
value: 
- <mark style="background: #FFF3A3A6;">start</mark> (horizontal မျဥ်းရဲ့ <span style="color:rgb(146, 208, 80)">အစ</span>)
- <mark style="background: #FFF3A3A6;">center</mark> (horizontal မျဥ်းရဲ့ <span style="color:rgb(146, 208, 80)">အလယ်</span>)
- <mark style="background: #FFF3A3A6;">end</mark> (horizontal မျဥ်းရဲ့ <span style="color:rgb(146, 208, 80)">အဆုံး</span>)
- <mark style="background: #FFF3A3A6;">stretch</mark> (ဆန့်လိုက်ပြီး grid item တစ်ခုစာ <span style="color:rgb(146, 208, 80)">နေရာအပြည့်ယူ</span>)
![[justify-items.png]]

<hr> 

###### Align-items

property: <span style="color:rgb(255, 155, 0)">align-items</span> (သူက grid container ရဲ့ <span style="color:rgb(146, 208, 80)">အလယ်က </span><span style="color:rgb(0, 255, 255)">vertical မျဥ်း</span>အပေါ် အခြေခံပြီး အလုပ်လုပ်)
value: 
- <mark style="background: #FFF3A3A6;">start</mark> (vertical မျဥ်းရဲ့ <span style="color:rgb(146, 208, 80)">အစ / အပေါ်ဆုံး</span>)
- <mark style="background: #FFF3A3A6;">center</mark> (vertical မျဥ်းရဲ့ <span style="color:rgb(146, 208, 80)">အလယ်</span>)
- <mark style="background: #FFF3A3A6;">end</mark> (vertical မျဥ်းရဲ့ <span style="color:rgb(146, 208, 80)">အဆုံး / အောက်ဆုံး</span>)
- <mark style="background: #FFF3A3A6;">stretch</mark> (ဆန့်လိုက်ပြီး grid item တစ်ခုစာ <span style="color:rgb(146, 208, 80)">နေရာအပြည့်ယူ</span>)
![[photos/align-items.png]]

<hr>

###### Justify-items + Align-items

justify-items ရော align-items ရော နှစ်ခုလုံးတွဲသုံးမယ်ဆိုရင် value အလိုက် horizontal မျဥ်းနဲ့ vertical <span style="color:rgb(0, 255, 255)">မျဥ်းနှစ်ကြောင်</span>း <span style="color:rgb(255, 105, 180)">စုံတဲ့နေရာလေးဘဲ</span> ကွက်ပြီး ပေါ်မယ်။

![[justify & align.png]]
![[justify & align 2.png]]

<hr>

###### Items တစ်ခုစီကို သီးသန့် align လုပ်ခြင်း

justify-items , align-items ဆိုရင် သူက parent container (where we put display : gird) ထဲမှာ သွားရေးပြီးတော့ 
grid<span style="color:rgb(255, 105, 180)"> items တစ်ခုဆီအတွက်</span>ရေးမယ်ဆိုရင် <span style="color:rgb(255, 155, 0)">justify-self </span>နဲ့<span style="color:rgb(255, 155, 0)"> align-self </span>တို့ကို သုံးရတယ်။

![[justify-self & align-self.png]]

