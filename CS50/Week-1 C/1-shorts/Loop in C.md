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

###### Loop use-case recommendation

![[loop recommedation.png]]