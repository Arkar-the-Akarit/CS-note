
github နဲ့ connect လုပ်တော့မယ်ဆိုရင် repository link လိုတယ်
e.g. https://github.com/Arkar-the-Akarit/CS-note.git

အဲ့တာကို ကိုယ့် local repo ထဲမှာ သုံးဖို့ name ပေးရတယ် default = origin ပေါ့။

###### Git remote:

အဲ့လို အခြားserver တစ်ခုက repo တွေကို ကိုယ့် repo ထဲမှာ run တာမျိုးကို <mark style="background: #FFB8EBA6;">remote connection</mark> လုပ်ပြီးသုံးတယ်လို့ခေါ််တယ်။ remote connection ဆိုတာက a bookmark to remote repo။

command --> <mark style="background: #FFF3A3A6;">git remote </mark> 


full syntax --> <mark style="background: #FFF3A3A6;">git remote add repoName(default=origin) link</mark>
				<mark style="background: #FFF3A3A6;">git remote -v </mark>--> ကိုယ်ထည့်ထားတဲ့ remote တွေကို 

repoName က ကိုယ်ထားချင်တာ ထားလို့ရတယ်။ အဲ့ထားလိုက်တဲ့ နာမည်နဲ့ pull/push လုပ်ဖို့ သုံးရမှာပေါ့။ repo က အခြား branch တွေကို ကြည့်ချင်ရင် <mark style="background: #ADCCFFA6;">repoName/branchName </mark> နဲ့  ခေါ်ရတယ်။ 

###### Git push:

ဒီ command က ကိုယ့် repo က local commits တွေကို remote repository ကို ပို့ဖို့သုံး

syntax --> <mark style="background: #FFF3A3A6;">git push origin main</mark>

- origin - name of the remote repo
- main - branch on local to push

အကယ်လို ကိုယ်က main branch မဟုတ်တဲ့ local Branch ကို remote က main မဟုတ်တဲ့ အခြား branch တစ်ခုကို ပို့ချင်တယ်ဆိုရင်
```
git push orign localBranch:remoteBranch
```

အကယ်လို့ ကိုယ်ပို့ချင်တဲ့ local branch name နဲ့ remote branch name က တူတူဘဲဆိုရင်
```
git push origin bothSameNameBranch
```

###### Git clone:

remote repository တစ်ခုကို ကိုယ့် local machine ထဲကို copy ယူဖို့သုံးတယ်
ကိုယ်အဲ့ command ကိုခေါ်လိုက်တဲ့ directories ထဲမှာ အဲ့ repo ရောက်လာမယ်

syntax --> <mark style="background: #FFF3A3A6;">git clone link(https://..../..)</mark> 

Git pull:

remote repository မှာ အခြားသူတွေက တင်လိုက်တဲ့ commit changes တွေဖြစ်ဖြစ်/ကွကိုယ် remote server ထဲမှာ ဝင်ပြင်လိုက်တာဖြစ်ဖြစ် အဲ့ changes တွေကို local repo ထဲကို တစ်ခါတည်း <mark style="background: #D2B3FFA6;"> fetch & merge </mark> လုပ်ပေးတာ။ 
အလွယ်ပြောရရင် remote repo ရဲ့ current commit ပုံစံအတိုင်း local repo မှာ လုပ်ပေးတာဘဲ

syntax --> <mark style="background: #FFF3A3A6;">git pull origin main </mark>
- pull : fetch & merge changes from remote
- origin : specifies remote repo pulling from
- main : ဒီက main က ကိုယ် <span style="color:rgb(0, 255, 255)">pull လုပ်ချင်တဲ့ remote repo က</span> <span style="color:rgb(255, 105, 180)">branch name</span>

အကယ်လို ကိုယ်က local repo က အခြားသော branch ထဲကို pull လုပ်ချင်တယ်ဆိုရင် ကိုယ် <span style="color:rgb(0, 128, 128)">pull လုပ်ချင်တဲ့ branch ထဲ</span>ကို အရင်<span style="color:rgb(146, 208, 80)"> checkout</span> or<span style="color:rgb(146, 208, 80)"> switch</span> command နဲ့သွား 
ပြီးရင် --> git pull origin remoteBranchName

###### Git fetch:

remote repository က changes တွေကို download လုပ်ဖို့သုံးတယ်။ သူက local repo ထဲကို <span style="color:rgb(220, 20, 60)">merge မလုပ်</span>ပေးဘူး။ merge မလုပ်ခင် အခြားသူတွေက ဘာတွေ commit လုပ်ထားလဲ ကြည့်ဖို့သုံးတယ်

syntax --> <mark style="background: #FFF3A3A6;"> git fetch origin </mark>
- origin - specifies remote repo we'r fetching from

fetch လုပ်ပြီးပြီ ဘာတွေ changes ဖြစ်တာလဲကို ဘယ်လိုကြည့်မလဲ
	1. <mark style="background: #FFB86CA6;">git branch -r</mark> နဲ့ ကိုယ် fetch လုပ်လိုက်တဲ့ branches တွေကိုကြည့်
	2. <mark style="background: #FFB86CA6;">git diff origin/branch-name </mark>နဲ့ changes တွေကို compare လုပ်ထားတာ ပြခိုင်းလို့ရတယ်။ ကိုယ်က origin က main branch ကို fetch လုပ်ထားတယ်, ကြည့်ချင်တယ်ဆို origin/main ပေ့ါ
