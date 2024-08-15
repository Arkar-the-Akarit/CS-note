```
h1{
    font-family: "Palatino Linotype", "Book Anqiqua", Palatino, serif;
}

h2{
    font-family: Arial, Arial, Helvetica, sans-serif;
}
```

h1 element အတွက် ပထမဆုံး Palatino Linotype ဆိုတဲ့ font ကိုပေးထားတယ်။ သူ့နောက်က ကျန်တာတွေက fallback fonts တွေ။ အကယ်လို့ ပထမဆုံးဖောင့်က user စက်ထဲမှာ မရှိရင် နောက်ကဟာတွေကို ပြပေးဖို့ သတ်မှတ်ထားတာ။ 

အကယ်လို့ သုံးမယ့်ဖောင်နာမည်မှာ <span style="color:rgb(192, 0, 0)">space bar</span> ခြားနေခဲ့ရင် <span style="color:rgb(192, 0, 0)">double quote ("")</span> နဲ့ရေးပေးတာ ကောင်းတယ်။

Some Default System Font:                                              
![[DefaultSystemFonts.png|350]]

###### CDN Fonts များအသုံးပြုခြင်း

CDNဆိုတာက Content Delivery Network ကိုပြောတာ။
အကယ်လို့ user စက်ထဲမှာ ရှိမနေတဲ့ ဖောင့်တွေကို ပြမှာ။

နမူနာ‌အနေနဲ့ Google Font Api Service ကနေ font တွေကို ယူပြီးပြမယ်

နည်း (၂) နည်း
1. [[Applying fonts in CSS#Link element နဲ့ ချိတ်ဆက်ပြီး ပြနည်း|Link element နဲ့ ပြနည်း]]
2. [[Applying fonts in CSS#CSS file ထဲမှာ တိုက်ရိုက် import လုပ်ပြီးပြနည်း| CSS file ထဲမှာ တိုက်ရိုက်ပြနည်း]]

###### Link element နဲ့ ချိတ်ဆက်ပြီး ပြနည်း

Google api font service : https://fonts.google.com

အဲ့မှာ ကိုယ်သုံးချင်တဲ့ ဖောင့်ကိုရွေး၊ ပြီးရင် **Get Embedded Code** ကိုနှိပ်
ဒါဆိုရင်<mark style="background: #FFF3A3A6;"> < link ></mark> နဲ့ချိတ်သုံးမလား၊ <mark style="background: #FFF3A3A6;">@import method</mark> နဲ့ သုံးမလားရွေးလို့ရပြီ 

- < link > နဲ့ သုံးမယ်ဆိုရင် < link rel="..." > ကနေ စ copy ကူးပြီး <mark style="background: #BBFABBA6;"> head  element </mark> အထဲမှာ ထည့်ပေးရမယ်
- @import နဲ့ သုံးမယ်ဆိုရင် သူ့ကို copy ယူပြီး <mark style="background: #BBFABBA6;">CSS file</mark> ထဲမှာ ထည့်သံုး

```
<title>Document</title>

    <link rel="preconnect" href="https://fonts.googleapis.com">

<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<link href="https://fonts.googleapis.com/css2?family=Playwrite+FR+Moderne:wght@100..400&display=swap" rel="stylesheet">

</head>

<body>
  <h1> H1 Title - Tag </h1>
    <p>
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Facere, illo!
    </p>
</body>
```

CSS:
```
p {

    font-family:"Playwrite FR Moderne",san-serif;

}
```


###### CSS file ထဲမှာ တိုက်ရိုက် import လုပ်ပြီးပြနည်း

@ import method ကို သုံးမှာ။
google font api မှာ @import ဆိုတာကို ရွေးပြီး သူ့ကို CSS ထဲမှာထည့်၊ ပြီးရင် အပေါ်လိုဘဲ element အတွက် font-family ဆိုပြီး‌ ရေးလို့ရပြီ

<mark style="background: #BBFABBA6;">@import </mark>ဆိုတာက တကယ်တော့<mark style="background: #ABF7F7A6;"> ပြင်ပ Resource filesတွေ၊ ပြင်ပ CSS ဖိုင်</mark>တွေကို ချိတ်ဖို့ သုံးတာ။ ဒါပေမယ့် <span style="color:rgb(255, 255, 0)">performance & compatibility ပိုကောင်းဖို့</span> <mark style="background: #FFF3A3A6;">< link > element</mark> ကို သုံးသင့်

##### Custom Fonts များအသုံးပြုခြင်း

font တွေရဲ့ format (or) file extensions ဖိုင်အမျိုးအစားတွေက 
- .tff (အသုံးပြုရအလွယ်ဆုံး)
- .otf
- .woff
- .woff2
- .svg .... အစရှိသဖြင့်ရှိကြတယ်။

Broswerတွေကလညး် မတူညီတဲ့ formatတွေကို supportလုပ်ပုံကွာတယ်
![[font_format_support_browser.png | 500]]

font file format တွေပြောင်းချင်ရင် : https://transfonter.org

Custom font တွေကို CSS မှာသုံးမယ်ဆိုရင် ကိုယ့် <mark style="background: #FFF3A3A6;">web project ဆောက်ထားတဲ့ folder/directory ထဲမှာ</mark> အဲ့ custom fontကိုထည့်ထားရမယ်။ များသောအားဖြင့် fonts folder ဆောက်ပြီးထားတယ်။

![[font_folder_in_vsCode.png]]

syntax in CSS
```
@font-face {
	font-family: "font name";
	src: url("file path to font"); 
	src: url("file path to font") format("");
		 url("file path to font") format("");

	font-weight: normal;
	font-style: normal;
}
```

<mark style="background: #ABF7F7A6;">at-rules</mark> ထဲက font-family မှာပေးရမယ့် nameက <mark style="background: #BBFABBA6;">ဖောင့်နာမည်အစစ်</mark>ဖြစ်စရာ<mark style="background: #FFB8EBA6;">မလိုဘူး</mark>။ ကိုယ် css ထဲမှာ သုံးမယ့် ‌alias (နာမည်တု/နာမည်ပွား)တစ်ခုဘဲ။ custom font ကို at-rules ထဲက font-family မှာ ပေးခဲ့တဲ့ alias အတိုင်းတော့ selector ထဲမှာ ပြန်ခေါ်ပေးရမယ်။ ဥပမာ:
```
@font-face {
	font-family: "abcdefg";
	src: url("file path");
}

h1{
	font-family: "abcdefg", san-serif;
}

```

format ထည့်လည်းရတယ်။ မထည့်လည်းရတယ်။ file format ဖြစ်တဲ့ svgဆို "svg", tff ဆို "tff" ဆိုပြိးထည့်ပေးရတာ။
<mark style="background: #FFB86CA6;">format() ထည့်တာက</mark> browser တွေကို ဘယ်file type ကို loading လုပ်ရမယ်ဆိုတာပြောတာ။ older browser တွေမှာဆို ဒါမပါရင် ဘယ်fontကို စာရင်းသွင်းမယ်ဆိုတာ မသိဘူး။ modern browserတွေမှာတော့ မလိုပေမယ့် <mark style="background: #FFF3A3A6;">compatibility ကောင်းအောင်</mark> ထည့်ပေးသင့်တယ်။

format မပါတာအတွက်၊ ပါတာအတွက် တစ်ခါကြေညာပြီးရင် ကျန်တဲ့ format တွေအတွက်က url(") နဲ့ ဆက်တိုက်ရေးသွားလို့ရတယ်။

example code:
```
@font-face {

    font-family: "Zombie Holocaust";

    src: url("../fonts/ZombieHolocaust/ZombieHolocaust.eot");

    src:  url("../fonts/ZombieHolocaust/ZombieHolocaust.eot?#iefix") format("embedded-opentype"),

        url("../fonts/ZombieHolocaust/ZombieHolocaust.woff2") format("woff2"),

        url("../fonts/ZombieHolocaust/ZombieHolocaust.woff") format("woff"),

        url("../fonts/ZombieHolocaust/ZombieHolocaust.ttf") format("truetype"),

        url("../fonts/ZombieHolocaust/ZombieHolocaust.svg#ZombieHolocaust") format("svg");

  
    font-weight: normal;
    font-style: normal;
}
h1{
   font-family: "Zombie Holocaust";
}
```

ဒီမှာဆို အချို့ url တွေမှာ (" .eot?#iefix") , (".svg#Zombieholocaust) ဆိုပြီး ပါနေတာတွေ့ရမယ်။

.eot?#iefix = internet explorer IE 6-8 versionတွေက eot file type တွေနဲ့ issueရှိလို့ ကောင်းကောင်းအလုပ်လုပ်နိုင်အောင် ထည့်ပေးထားတာ။

.svg#ZombieHolocaust = svg font filesတွေက fontsတွေအများကြီးပါင်တယ်။ ဒါကြောင့် font ID ကို svg font file ထဲမှာကြေညာပေးတာ။ id နဲ့ကြည့်ပြီး ဘယ် fontသုံးရလဲ သိအောင်လို့။



































































































































