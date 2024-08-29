#C #C-operators

###### Assignment Operators

<mark style="background: #FFF3A3A6;"> = </mark>

variable တစ်ခုထဲကို value assign လုပ်တဲ့ operator

e.g. x = 5; -> variable x ထဲကို တန်ဖိုး 5 ထည့်လိုက်တယ်။ သူ့တန်ဖိုးက 5 ဖြစ်သွားပြီ

e.g. x = y; -> var x ထဲကို var y တန်ဖိုးထည့်လိုက်တယ်။ x တန်ဖိုးက လက်ရှိ var y ရဲ့ တန်ဖိုးဖြစ်သွားပြီ။

###### Arithmetic Operators

ပေါင်းနှုတ်မြှောက်စား + အကြွင်း ပြန်ရတဲ့ operators 

<mark style="background: #FFF3A3A6;"> + </mark> = အပေါင်း

<mark style="background: #FFF3A3A6;"> - </mark> = အနှုတ်

<mark style="background: #FFF3A3A6;"> * </mark> = အမြှောက်

<mark style="background: #FFF3A3A6;"> / </mark> = အစား

<mark style="background: #FFF3A3A6;"> % </mark> = အကြွင်းပြန်
e.g. x = 10 % 3; ဆို x တန်ဖိုးက အကြွင်းဖြစ်တဲ့ 1

#math ဂဏန်းအကြီးကြီးတစ်ခုထုတ်ပြီးတော့ အဲ့ကောင်ကို ကိုယ်လိုချင်တဲ့ ဂဏန်း range ထက် ကြီးတဲ့ကောင်တဲ့စားလိုက်ရင် အကြွင်းက 0 - ကိုယ်လိုချင်တဲ့ဂဏန်းဘဲ
e.g. ကိုယ်က 0-19 အတွင်းလိုချင်တယ်ဆို အဲ့ဂဏန်းကို 20 နဲ့စားလိုက် အကြွင်းက 0 - 19 ဘဲ

 shorthand (sugaric syntax)

```
x *= 5 -> x = x * 5;
x /= 5 -> x = x / 5;
x += 5 -> x = x + 5;
x -= 5 -> x = x - 5;
x %= 5 -> x = x % 5;

x++ -> x = x + 1;
x-- -> x = x - 1;
```

###### Boolean Expression

value တွေကို နှိုင်းယှဥ်ဖို့သုံးတယ်။ boolean expression တိုင်းက true or false နှစ်ခုထဲက တစ်ခုကိုဘဲညွှန်ပြတယ်။

if, while, စတာတွေနောက်မှာ boolean expression () လိုက်တယ်။ true ဆို အောက်က ကုဒ်ကို run, မဟုတ်ရင် ကျော်ပေါ့။

- <mark style="background: #FFF3A3A6;">every nonzero value</mark> = <mark style="background: #FFF3A3A6;">true</mark>
- <mark style="background: #ABF7F7A6;">zero</mark> = <mark style="background: #ABF7F7A6;">false </mark>

two main types of boolean expression
	1. logical operators
	2. relational operators

###### Logical Operators

AND (&&)
	is true only when both operand is true
	e.g (x && y) ဆို x ရော, y ရော true မှ မှန်မယ်။ otherwise false
	![[logical AND.png]]

OR (||)
	is true when one of operand or both are true
	e.g (x || y) ဆို x true ဖြစ်ဖြစ်၊ y true ဖြစ်ဖြစ်၊ နှစ်ခုလုံး true ဖြစ်ဖြစ် true
	![[logical OR.png]]

NOT (!)
	သူက value နှစ်ခုယှဥ်တာမဟုတ်ဘဲ သူ့ကိုသုံးလိုက်တဲ့ operand တန်ဖိုးကို ပြောင်းပြန်လှန်ပစ်တာ
	e.g. x = true , x !\= false
	![[logcial NOT.png]]


###### Relational Operators

ကြီးရင် ငယ်ရင် တူရင် စသည်ဖြင်နှိုင်းယှဥ်တာ

less than (<)
x < y , x သည် y ထက်ငယ်

less than equal to (<\=)
x <\= y , x က y ထက် ငယ်တာလည်းဖြစ်မယ်၊ y နဲ့ တန်ဖိုးတူညီတာလညး်ဖြစ်မယ်။ 

greater than (>)
x > y , x သည် y ထက်ကြီး 

greater than equal to (>\=)
x >\= y , x က y ထက် ကြီးတာလည်းဖြစ်မယ်၊ y နဲ့ တန်ဖိုးတူညီတာလညး်ဖြစ်မယ်။ 

equality (=\=)
x =\= y ဆိုရင် x နဲ့ y တန်ဖိုးက ညီမျှမှုရှိတယ်။ တန်ဖိုးတူတူဘဲ, 

inequality (!\=)
x !\= y ဆိုရင် x နဲ့ y တန်ဖိုး မတူညီဘူး

