
< a > element ဟာ link ချိတ်ဖို့သုံးတယ်။ link တွေကို browserက အောက်က underline ရယ်၊ မျဥ်းအပြာရယ်နဲ့ ပြတယ်။ link ကို ဝင်ပြီးသွားရင် အချို့ browser တွေမှာဆို ခရမ်းရောင်ပြောင်းသွားတယ်။ ဒါဟာ ဒီလို ဖြစ်ရမယ်လို့ Html Structureထဲမှာ ထည့်‌ရေးထားတာလည်း မဟုတ်ဘူး။ Browser က ဝင်ပြီးသား link တွေကို track လုပ်ပြီး <mark style="background: #FFB86CA6;">":visited"</mark> ဆိုတဲ့ pseudo-class ကို apply လုပ်ပေးလို့သာဖြစ်သွားတာ။

<mark style="background: #FFB86CA6;">:link</mark> : သူက user က link မဝင်ရသေးခင်ပြမယ့် ပုံစံကို modify လုပ်ဖို့။ 

<mark style="background: #FFB86CA6;">:visited</mark> : သူက link တစ်ခုကို click/ ဝင်ကြည့်ပြီးရင် ပြဖို့။

```
a:link {
    color:white;
    background-color: #de1767;
    padding: 10px;
    border-radius: 8px;
}

a:visited {
    color: white;
    background-color: blue;
    padding: 10px;
    border-radius: 8px;
}

```

![[link pseudo class example.png]]
![[visted pseudo class example.png]]

ဟာ <mark style="background: #ADCCFFA6;">:link</mark> pseudo class အစား <span style="color:rgb(0, 176, 240)">a element</span> ကို <span style="color:rgb(0, 176, 240)">direct style ‌apply</span> လုပ်လို့မရဘူးလားဆို၊ ရတယ်။ ဒါပေမယ့် url linkတွေရဲ့ stateက အမျိုးမျိုး (:link, :visited, :hover, :active) ရှိနိုင်တယ်။ ဒီတော့ အခြေအနေတစ်မျိုးချင်းဆီကို မတူညီတဲ့ ပုံစံနဲ့ styles apply လုပ်လို့ရတာပေါ့။ 

[[Action အ‌‌ခြေအနေကို ဖမ်းသော Pseudo-classes]] တွေကို < a > element မှာလည်း သုံးလို့ရတယ်။