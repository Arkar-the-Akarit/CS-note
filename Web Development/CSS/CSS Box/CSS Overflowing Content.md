
overflow ဖြစ်လာတယ်ဆိုတာ content/element တွေက သူ့ container/ parent element ထဲမှာ မဆံ့တော့တဲ့ အခြေအနေကို ပြောတာ၊ သတ်မှတ်ထားတဲ့ area ထက် content/child element တွေက ပိုကြီးနေမယ်ဆိုရင် ဖြစ်တယ်။ ဒါကို control လုပ်ဖု့ိ

property: <span style="color:rgb(255, 155, 0)">overflow</span>
value : "<mark style="background: #FFF3A3A6;">visible</mark>", "<mark style="background: #FFF3A3A6;">hidden</mark>", "<mark style="background: #FFF3A3A6;">scroll</mark>", "<mark style="background: #FFF3A3A6;">auto</mark>", "<mark style="background: #FFF3A3A6;">clip</mark>"

- <mark style="background: #FFF3A3A6;">visible</mark> : default value, overflow ဖြစ်သွားတဲ့ content/element တွေက သူတို့ container ရဲ့အပြင်ဘက်ကို ထွက်ပြီး ပြမှာ
  ![[overflow_visible.png|450]]

- <mark style="background: #FFF3A3A6;">hidden</mark> : overflow ဖြစ်တဲ့အပိုင်းက မပြဘဲ hide လုပ်ထား။ ဒါပေ‌မယ့် hidden ဖြစ်တဲ့ content တေွွကို scroll-snap property တို့, js event handling တို့နဲ့ interact လုပ်လို့ရ။ 
  ![[Overflow_hidden.png|450]]

- <mark style="background: #FFF3A3A6;">scroll</mark> : overflow ဖြစ်သွားတဲ့ content တွေကို scroll bar နဲ့ ဆွဲကြည့်လို့ရမယ်။
  ![[overflow_scroll.png|450]]

- <mark style="background: #FFF3A3A6;">‌auto</mark> : browser က scroll bar ထည့်သင့် မထည့်သင့် ဆုံးဖြတ်မယ်။ overflow ဖြစ်ရင် ထည့်မယ်၊ မဖြစ်ရင် မထည့်ဘူး
  ![[overflow_auto.png|450]]

- <mark style="background: #FFF3A3A6;">clip</mark> : သူကလည်း hidden လုပ်ပေး, မတူတာက သူက overflow ဖြစ်သွားတဲ့ ကောင်ကို clip လုပ်ပလိုက်တာ, make overflow content invisible and unscrollable

property: <span style="color:rgb(255, 155, 0)">overflow-x</span> , <span style="color:rgb(255, 155, 0)">overflow-y</span>

အလျားလိုက် ကျော်လွန်သွားတဲ့ content ကိုဘဲ ထိန်းချုပ်တာတို့၊ ဒေါင်လိုက် ကျော်လွန်သွားတဲ့ content ကိုဘဲ ထိန်းချုပ်တာတို့အတွက် သုံးတာ

![[overflow_x & overflow_y.png]]n
