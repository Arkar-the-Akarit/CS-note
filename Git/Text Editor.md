
MS word, Google doc တို့လို GUI text editor တွေရှိသလိုဘဲ, terminal ထဲမှာ ရေးလို့ရတဲ့ screen-based text editor တွေ (e.g. vim, nano) တို့ရှိကြတယ်။

ဒီမှာတော့ vim အကြောင်းကို နည်းနည်းပါးပါးပြောထားတယ်

Git Bash Shell ထဲမှာ Vim ကိုဖွင့်ချင်ရင် 

<mark style="background: #CACFD9A6;">$ vim </mark> လို့ရိုက်လိုက်တာနဲ့ ရတယ်။ ဒါက new file တစ်ခုကိုဖွင့်ပေးမှာ။
<mark style="background: #CACFD9A6;">$ vim fileName.type</mark> ဆိုရင် ရှိပြီးသား file တစ်ခုကိုသွားဖွင့်လို့ရတယ်။

ပထမဆုံး vim ထဲကို ရောက်ရောက်ချင်းဆိုရင် သူက default mode အနေနဲ့ <span style="color:rgb(146, 208, 80)">Read only</span> ဘဲဖြစ်နေမယ် no matter file is empty or not 
![[command vim.png]]
ဒီလိုမြင်ရမယ်။ file အသစ်မလို့ အောက်ဆုံးမှာ နာမည်ပြမနေ

<mark style="background: #ABF7F7A6;">  i  </mark> ကို နှိပ်လိုက်ရင် insert mode ကို ပြောင်းသွားမယ်။ အဲ့မှာ စာရိုက်လို့ရမယ်။ 
normal / default mode ကို ပြန်သွားချင်ရင် <mark style="background: #ABF7F7A6;">ESC </mark> escape နဲ့သွားလို့ရတယ်။
![[insert in vim.png]]
ဘယ်ဘက်အောက်ဆုံးမှာ insert လို့ပြောင်းသွားပြီ။ စာတွေရိုက်လို့ရ

<mark style="background: #FFF3A3A6;">Normal / Default Read only mode</mark> ထဲမှာက cursor ကို ရွှေ့ချင်ရင် arrow နဲ့ မရဘူး။

j -- 1 line down
k -- 1 line up
l -- beside (->)
h -- front (<-) 

အကယ်လို့ moving keys တွေရဲ့ ရှေ့မှာ နံပါ‌တ်တွေ (e.g. 2k, 3k, 4l) နှိပ်လိုက်ရင် သူက cursor ကို နံပါတ်အတိုင်း အကြိမ်ရေလိုက်‌‌ရွှေ့ ။ 2k ဆို 2 line အပေါ်တက်, 4l ဆို စာလုံး လေးလုံးစာ ‌cursor ကို‌ရွှေ့

$ -- to last character of current line
ESC -- to first character of current line

dG -- delete all 
![[delete command in Vim.png]]

###### Command Mode

<mark style="background: #ABF7F7A6;">: </mark>  full colon ကို နှိပ်လိုက်ရင် သူက command ရိုက်လို့ရမယ့် command mode ထဲကိုသွားမယ်။

<mark style="background: #ABF7F7A6;">:set number </mark> -- စာကြောင်းတွေရှေ့မှာ line number ထည့်
<mark style="background: #ABF7F7A6;">:set nonumber</mark>  -- line number ဖြုတ်

<mark style="background: #ABF7F7A6;">:wq </mark> (<span style="color:rgb(0, 255, 255)">if new file, file name.type</span>) -- write & quit လက်ရှိရေးထားတာ‌တွေကို save / file ထဲကို write လုပ်ပြီး quit, file က အသစ် create ထားတာဆို fileName.type ထည့်ပေးရတယ်။ မဟုတ်ရင် error 

<mark style="background: #ABF7F7A6;">:q </mark> : vim ထဲကနေ ဒီတိုင်းပြန်ထွက်တာ၊ စာတွေ‌ရေးပြီး မ save ရသေးရင်တော့ ရိုးရိုး q နဲ့ဘဲထွက်ရင် error တက်

<mark style="background: #ABF7F7A6;">:q! </mark> -- quit & override.

<mark style="background: #ADCCFFA6;">:syntax on </mark> -- code ရေးရင် အချို့ syntax တွေကို hightlight လုပ်ပေး

