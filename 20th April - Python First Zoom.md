
slope (symbol - <mark style="background: #FFB86CA6;">m</mark>)

1 2 3 4 5 6 -> x  <- input data, feature
2 4 6 8 10 12 -> y <- output data , predict

ဒီလိုဆတူတိုးတာကို graphလေးချကြည့် (x,y) နေရာတွေမှာ၊ အစက်တွေက မျဥ်းဖြောင့်ပုံစံဖြစ်နေမှာကို တွေ့မယ်

linear ပုံစံ ဆက်နွယ်နေတာကို မျဥ်းကိုကြည့်ပြီး ခန့်မှန်းလို့ရတယ်။
အဲ့လို graph နဲ့ model ပြတာကို linear regression လို့ခေါ်


y = 2x 

function, model, linear relations --> 'y = 2x'

ဆတူတိုး, ဆတူလျော့တဲ့ ဆက်နွယ်မှု  - linear relation

y = 2x ဆက်သွယ်ချက်ထဲမှာ ပါနေတဲ မြှောက်ဖော်ကိန်းကို (2) ကို correlation coefficient လို့ခေါ်တယ်။

e.g y = 3/x  # correlation coefficient - 3

ဒီလို ဆက်သွယ်မှု မြှောက်ဖော်ကိန်း(slope)ကို ရှာချင်ရင်
equation ရှိတယ်။

m = (y2 - y1 ) / (x2 - x1)

y  ကို (vertical) (rise) (height) 
x v ကို (horizonal) (run) (base) လို့လည်းခေါ်

y intercept (b) 
x တန်ဖိုး သုညဖြစ်တဲ့အချိန်မှာ y ရဲ့ တန်ဖိုးကို y intercept(b) လို့ခေါ်တယ်။

y = 2x  မှာဆိုရင် x တန်ဖိုး 0 ဆို y တန်ဖိုးသည်လညး် 0

m(slope)x + b(y-intercept)
mx + b


<mark style="background: #FFB86CA6;">dy</mark> = difference of y = y နှစ်ခုနှုတ်လဒ် (y2 - y1)
<mark style="background: #FFB86CA6;">dx</mark> = difference of x = x နှစ်ခုနှုတ်လဒ် (x2 - x1)

correlation coefficient = m (slope) = dy/dx 
y intercept = b
linear relations --> <mark style="background: #ADCCFFA6;">y = mx + b</mark>

regression - linear ပုံစံဆက်နွယ်ပြီး linear ပုံစံ ခန့်မှန်းတာ

linear ပုံစံခန့်မှန်းတာဆိုရင် python မှာ linregress(x,y) ဆိုတာရှိတယ်။ x & y values တွေထည့်ပေးလိုက်ရင် slope(m), y-intercept(b), rvalue, pvalue, stderr စတာတွေကို ရှာပေးတယ်
- slope (m)
- y-intercept (b)
- regression value ခန့်မှန်းရလဒ် (rvalue) (1 = 100%, 0.1 = 10%) (1 ဖြစ်ရင် equation သည် 100% မှန်)
- paired value (pvalue) 
- standard error (stderr) (rvalue နဲ့ ဆန့်ကျင်ဘက်)


mx + b ကို simple regression လို့ခေါ်
ရှူပ်ထွေးတာတွေအတွက်ကျ machine learning algorithms ကို သုံး


###### Machine Learning

သင်္ချာပုံစံ model တွေတည်ဆောက်တာကို machine learning လုိ့ခေါ်


တွက်လိုက်တဲ့ data မျိုးတွေက မတိကျတာမျုိး (ဥပမာ အိမ် စျေးကို predict လုပ်ရင် အိမ်ရှိနေတဲ့နေရာ factor plays an important role) - underfit (happens when model is too simple)

overfit - too many input features data

 