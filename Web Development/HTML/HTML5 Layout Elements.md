
Layout elements ဆိုတာက website တစ်ခုရဲ့ မတူညီတဲ့ အပိုင်းတွေကို <mark style="background: #FF5582A6;">structure ကျကျ ဖော်ပြဖို့</mark> သုံးတာ

< div > ကြီးဘဲ သုံးနေမယ့်အစား Layout elements တွေသုံးတော့ **clean code** ဖြစ်တယ်။

![[semantic html.png]]

< header > < / > = ခေါင်းစဥ်ပိုင်းတွေရေးလေ့ရှိပြီး သူ့ထဲမှာ

< nav > < / > = ဆိုတဲ့ လမ်းညွှန် element ပါတယ်။ navigation ကများသောအားဖြင့် ဘယ် page ၊ ဘယ် page ဆိုပြီး ညွှန်းထားတဲ့ anchor link တွေဘဲ

< footer > < / > = web page အောက်ခြေပိုင်း။ မျာ‌းသောအားဖြင့် contact info၊ phone၊ copyright ဘာညာပါတယ်

< aside > < / > = ဆက်စပ် content တွေပြဖို့၊ e.g. သတင်းဆိုရင် အလားတူ သတင်းတွေကို ဘေးမှာ ပြတာမျိုးပေါ့

< article > < / > = နာမည်အတိုင်းဘဲ article တွေရေးသားဖို့

< section > < / > = section တွေခွဲရေးလို့ရအောင်၊ e.g. သတင်းပေ့ချ် တစ်ခုမှာ ယနေ့သတင်း၊ popular သတင်း၊ သတင်းအ‌ဟောင်းဆိုပြီး section သုံးခု ခွဲရေးလို့ရ

< figure > < / > = သူက ပုံပါမယ်၊ caption လည်းပါမယ်ဆိုရင် သုံးဖို့ပေါ့။ ပုံကိုတော့ < img > element နဲ့ ရေးပြီး၊ caption ထိုးတာက < <mark style="background: #FFB8EBA6;">figcaption</mark> > နဲ့ ထိုးရတယ်။

```
<figure>
	<img src="filepath" title="imgTitle" alt="toShow" />
	
	<figcaption> On top of the mountain, with view of underneath </figcaption>

</figure> 

```

ဒါတွေအပြင် html5 မှာ 

< canvas > = ပုံဆွဲဖို့သုံးတာ
< audio > = audio တွေအတွက်
< video > = video တွေအတွက် စသည်ဖြင့် အခြားသော elements တွေရှိသေး