#C #C-loop

loop ဆိုတာက code တွေကို ထပ်ခါထပ်ခါ ပြန် run နေနိုင်အောင်လုပ်ပေးတဲ့ဟာတွေ

###### while loop

```
while (true)
{
  ;
}
```

(true) လို့ထည့်ထားလိုက်ရင် အမြဲ မရပ်တော့ဘဲ run နေမှာဖြစ်လို့ infinity loop လို့လည်းခေါ်

```
while (boolean-expression)
{
 ;
}
```
boolean-expression က မှန်နေသမျှ code ကို run နေမယ်

###### do-while loop

```
do
{

} 
while (boolean-expr);

```

{ } curly brackets ထဲက code တွေကို အရင်ဆုံး တစ်ခါ run မယ်။ ပြီးမှ boolean-expr ကို စစ်။ မှန်ရင် ထပ် run, မှားရင် ကျော်။
အနည်းဆုံး တစ်ခေါက်တော့ run ဖြစ်တာပေါ့။


###### for loop

```
for(initialization, condition, increment){

}

for(int i = 0; i < 10 ; i ++)
{

}
```

variable တစ်ခုကြေညာ, ဘယ်မှာဆိုရပ်မယ်ဆိုတဲ့ အခြေအနေတစ်ခု, ပြီးရင် variable တန်ဖိုး အတိုးအလျော့

<mark style="background: #BBFABBA6;">trick</mark> --> for loop မှာ initialization လုပ်ရင်လေ နှစ်ခုနဲ့အထက်လုပ်လည်း ရတယ်။ 
```
for (int i = 0, n = strlen(name); i < n; n++ )

```

int i initialization နဲ့ n ကြားမှာ ခြားထားတာ <mark style="background: #ABF7F7A6;">coma (,)</mark> ပါ။ ဒီလိုမျိုး <span style="color:rgb(0, 176, 240)">initialization part မှာ တစ်ခါတည်းကြေညာလိုက်တာမျိုး</span> or '<span style="color:rgb(0, 176, 240)">for' loop အပြင်မှာ variable အနေနဲ့ ကြေညာတာ</span>မျိုးက 
`for (int i =0; i < strlen(name); i++)` လို့ကြေညာတာထက် ပိုကောင်းတယ်။ ဘာလို့ဆို for loop ပတ်တိုင်း boolean အခြေအနေဖြစ်တဲ့ i က strlen() ထက် ငယ်သေးလားဆိုတာကို လာစစ်ဖို့ strlen() ကို ထပ်ခါထပ်ခါ ပြန်ပြန် run နေရမှာမလို့။

###### Loop use-case recommendation

![[loop recommedation.png]]