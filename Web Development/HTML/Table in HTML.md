
table ဆွဲဖို့ဆိုရင် **< table > element** ကို သုံးရတယ် 

အဲ့ထဲမှာမှ <mark style="background: #FFB86CA6;">row တွေအတွက် < tr > element </mark>
အထဲမှာ data ထည့်ဖို့က <mark style="background: #FFF3A3A6;">heading ဆို < th ></mark> ၊ <mark style="background: #FFB86CA6;">ရိုးရိုးဆို < td > </mark>

< table > element ထဲမှာ ပါတဲ့ attribute တွေကတော့ လက်ရှိ

border = table တစ်ခုလုံးစာအတွက် မျဥ်းကြောင်းတွေကို ဘယ်လောက် pixel (px) သတ်မှတ်မယ် ဆိုတာ 
‌
cellpadding = border မျဥ်းနဲ့ cell ထဲက content ကြားက အကွာအဝေးသတ်မှတ်
cellspacing = cell ကွက် တစ်ခုချင်းဆီကြားက အကွာအဝေး

< tr > & < td > မှာ အခြေအနေလိုက် သုံးတဲ့ Attribute

rowspan = <mark style="background: #FFF3A3A6;">row ဘယ်နှစ်ခုစာယူမယ်</mark>ဆိုတာ သတ်မှတ်

colspan = အခု <mark style="background: #FFB86CA6;">cell က columnနေရာ ဘယ်နှစ်ခုယူမယ်</mark>ဆိုတာ သတ်မှတ်တာ


![[table content.png]]

နောက်တစ်နည်းက table head, table body, & table foot တွေပါထည့့််းပြီး ရေးတာ

```
< table >
	
	<thead> 
		<tr></tr>
	</thead>

	<tbody>
		<tr></tr>
	</tbody>

	<tfoot>
		<tr></tr>
	</tfoot>

</table>
```

table နဲ့ ဆိုင်တဲ့ CSS ကို [[CSS Table|ဒီမှာကြည့်ပါ]]။