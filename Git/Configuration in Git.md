
##### Configuration Setting in Git

config settings ဆိုတာက local (individual) repositories / globally git က ဘယ်လို လုပ်ဆောင်မယ်ဆိုတာ သတ်မှတ်ပေးတာ -- git က user infos, line endings, diff algorithms စတဲ့ version control ရဲ့ အစိတ်အပိုင်းအမျိုးမျိုးကို ဘယ်လိုကိုင်တွယ်မလဲဆိုတာ သတ်မှတ်တာ။

1. System Level Config 
	system ထဲမှာရှိသမျှ system user အားလုံးအပေါ်သက်‌ရောက်တယ်
2. Global Config
    လက်ရှိ user ရဲ့ repositories အားလုံးအပေါ်သက်ရောက်တယ်။ 
3. Local Config
	command ကို run လိုက်တဲ့ repositories တစ်ခုထဲအပေါ်ဘဲ သက်ရောက်


**အသုံးများတဲ့ Git Config Settings တွေ**

###### user information

commits တွေနဲ့ ဆိုင်တဲ့ user information (‌name, email) တွေ

```
global:
git config --global user.name "name"
git config --global user.email "email"

local:
git config --local user.name "name"
git config --local user.email "email"

```

###### Text Editor

default text editor သတ်မှတ်ခြင်
```
git config --global core.editor "code --wait"

```

code : ဆိုတာက vsCode ကို ဖွင့်ဖို့ ပြောတာ 
/-- wait : ဆိုတာက ပုံမှန်ဆို git က editor တစ်ခုကို <span style="color:rgb(255, 155, 0)">terminal </span>မှာ  ဖွင့်ပြီးတာနဲ့ editor က file ကိုဖွင့်ပေးမှာ။ ဒါပေမယ့် git က အဲ့ file ကို ငါတု့ိ edit ပြီးအောင် စောင့်မှာ မဟုတ်ဘူး။ vsCode ကိုဖွင့်လိုက်တာနဲ့ git က editing လုပ်တာပြီးပြီထင်ပြီး ဆက် run နေမှာ။ wait command နဲ့ဆို သူက vsCode ကိုဖွင့်ပြီးရင်  ဘာမှ ဆက်မrun ဘဲ pause လုပ်ထားမယ်။ ငါတို့ file ကိုပိတ်လိုကတော့မှ <span style="color:rgb(255, 155, 0)">terminal</span>   မှာ ဆက်ပြီး proceed လုပ်မယ်။ <mark style="background: #FF5582A6;">အရေးကြီး </mark> 

###### Line Ending Conversions

operating systems တွေကကွာ စာကြောင်းတစ်ကြောင်းဆုံးသွားပုံကို ဖော်ပြတာချင်း မတူကြဘူး။

windows မှာဆိုရင် carriage return (\\r) နဲ့ line feed (\\n) ကိုသုံးတယ်။ CRLF ဆိုပြီး line တစ်ကြောင်းဆုံးတာကို represent လုပ်တယ်။ carriage return ဆိုတာက အကြမ်းဖျင်းအားဖြင့် cursor ကို ‌‌ရှေ့ဆံုးကို ပြန်သယ်သွားပေးတာမျိုး

macs / linus မှာကျတော့ line feed (\\n) တစ်ခုတည်းနဲ့ end of the line ကို ညွှန်ပြတယ်။

project တစ်ခုကို မတူညီတဲ့ Operating systems တွေမှာ လုပ်ပြီဆိုရင် line endings မတူတာတွေက issues/ပြဿနာဖြစ်စေတယ်။

ဒါကြောင့် git မှာ line endings မတူတာကို handle လုပ်ဖို့အတွက် <mark style="background: #D2B3FFA6;">core.autocrlf </mark> ဆိုတဲ့ config settign လေးပါတယ်။

```
windows:
git config --global core.autocrlf true

mac / Linus
git config --global core.autocrlf input 

```

<span style="color:rgb(255, 155, 0)">core.autocrlf true </span>
	- git က <span style="color:rgb(0, 176, 240)">LF</span> line endings တွေကို <span style="color:rgb(0, 176, 240)">CRLF </span>အဖြစ် repo က files တွေကို checkout လုပ်တဲ့အချိန်မှာ ပြောင်းပေးတယ်။
	- files တွေကို repository အထဲသို့ commit လုပ်တဲ့အချိန်မှာ <span style="color:rgb(0, 176, 240)">CRLF အဖြစ်ပြန်ပြောင်‌း</span>ပေးတယ်။
	- ဒီ settings က local system က ဘယ်လို line ending ရှိရှိ Git Repo ထဲမှာ အမြဲ LF line endings ဘဲရှိမယ်။

<span style="color:rgb(255, 155, 0)">core.autocrlf input </span> 
	- files checking out လုပ်ရင် line endings တွေကို ဘာမှမပြောင်းဘူး
	- files တွေကို Repo ထဲ commit လုပ်ရင် <span style="color:rgb(0, 176, 240)">CRLF line endings</span> တွေကို <span style="color:rgb(0, 176, 240)">LF ending</span> အဖြစ်ပြောင်းပေးတယ်။
	- LF ending ကို native အဖြစ်သုံးတဲ့ Linus/MacOS တို့မှာဆိုရင် LF endings အဖြစ်အမြဲရှိစေတယ်။

###### Aliases နာမည်တိုများပေးခြင်း

အသုံးများတဲ့ / ရှည်တဲ့ command တွေအတွက် နာမည်တိုလေးတွေပေးလို့ရတဲ့ config

<mark style="background: #FFF3A3A6;">syntax</mark>: git config --global alias.< alias-name > "full command"

e.g.
```
git config --global alias.st "status"

git config --global alias.co "checkout"

git config --global alias.rh "reset --hard HEAD"
```

ပေးထားတဲ့ alias တွေကိုကြည့်မယ်ဆိုရင်
```
git config --get-regexp alias
```

alias ပေးထားတာကို ဖျက်မယ်
```
git config --global --unset alias.<alias-name>
```

##### Default Branch Name Change

```
git config --gloabl init.defaultBranch name
```

###### Viewing & Editing Configuration

လက်ရှိ config setting ကိုကြည့်
```
git config --list
```

config setting တစ်ခုကိုကြည့်
```
git config <setting>
```

config file ကို directly edit လုပ်
```
git config --global --edit
```