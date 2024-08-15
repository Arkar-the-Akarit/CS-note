
Terminal ထဲမှာ "PATH" ဆိုတဲ့ variable တစ်ခုရှိတယ်။
- သူက environment variable တစ်ခုဖြစ်တယ်။
- သူ့ထဲမှာ executable programs တွေရှိနေတဲ့ directories တွေကို သိမ်းထားတယ်။ 
- command တစ်ခုကို terminal ထဲထည့်လိုက်ရင် shell က PATH variable ထဲမှာ list လုပ်ထားတဲ့ directories ထဲမှာ အဲ့ command program ကို လိုက်ရှာပြီး execute လုပ်ပေးတယ်

Default Directories: သူ့ထဲမှာ standard/default directories တွေဖြစ်တဲ့ '/bin' , 'usr/bin' စတာတွေပါတယ်။

custom directories: ကိုယ့်ဘာကိုယ်လည်း PATH ထဲကို directories တွေထည့်ပြီး custom cli program terminal ထဲက ဘယ်နေရာမှာဖြစ်ဖြစ် runလို့ရအောင်လုပ်လုိ့ရတယ်။

<span style="color:rgb(0, 176, 240)">Order Matters</span>: system က directories တွေကို လိုက်ရှာရင် PATH ထဲမှာ list ထားတဲ့ အစီအစဥ်အတိုင်း လိုက်ရှာမှာဖြစ်ပြီး command နဲ့ ကိုက်တဲ့ programကို အရင်ဆုံးတွေ့တာနဲ့ တွေ့တဲ့ကောင်ကို run လိုက်မှာဖြစ်ပါတယ်။ e.g. တူညီတဲ့ နာမည်နဲ့ command program တစ်ခုက directories နှစ်ခုထဲမှာ ရှိနေတယ်ဆိုရင် အ‌ရှေ့မှာ ရှိတဲ့ directories ထဲက ကောင်ကို အမြဲအရင် run မှာ

Viewing Path : "PATH" variable ကိုကြည့်ချင်ရင် 'echo $PATH' လို့ terminal ထဲထည့်ရိုက်ပြီး value ကိုကြည့်လို့ရတယ်။

