
###### git init 

repository အသစ်တစ်ခု / ရှိပြီးသားအဟောင်းကို working directory ထဲမှာ initialize လုပ်လိုက်တာ။ 

syntax: <mark style="background: #FFF3A3A6;">git init</mark> 

###### git add

WDထဲက files တွေကို staging area ထဲထည့်

syntax: <mark style="background: #FFF3A3A6;"> git add </mark> 
		<mark style="background: #FFF3A3A6;">git add file1.txt file2.txt</mark> --> file တစ်ခုဆီထည့်
		<mark style="background: #FFF3A3A6;">git add . </mark> --> ရှိသမျှ file အကုန်ထည့် (working on current directories & its sub directories)
		<mark style="background: #FFF3A3A6;">git add -A </mark>--> sub directories ‌ထဲကနေရိုက်လိုက်ရင်တောင် the whole working directories က changes ‌တွေကို staging area ထဲ add

###### git commit

staging area / index ထဲမှာရှိတာ‌တွေကို repository/commit history ထဲထည့်သိမ်းဖို့သုံးတယ်။ -m option နဲ့ message လေးထည့်ပေးရတယ်။ -‌am option နဲ့ add & commit တစ်ခါတည်းလုပ်လည်းရ

syntax: <mark style="background: #FFF3A3A6;">git commit -m "message here"</mark>
		<mark style="background: #FFF3A3A6;">git commit -am "message"</mark> --> git add + commit (cannot use for first commit, add all the file first to staging area)

###### git status

working directories မှာဘာဖြစ်နေတယ်။ ဘယ် files တွေကို change ထားတယ်။ staging area ထဲမှာ ဘာတွေဖြစ်နေတယ်ဆိုတာကို ကြည့်လို့ရတယ်။

syntax: <mark style="background: #FFF3A3A6;"> git status </mark> 


###### git log

commit ဘယ်နှစ်ခါလုပ်ထားတယ်ဆိုတာ ပြန်ကြည့်လို့ရ

syntax: <mark style="background: #FFF3A3A6;"> git log </mark> 
		<mark style="background: #FFF3A3A6;">git log --oneline </mark> --> commit တစ်ခုဆီကို စာတစ်ကြောင်းဆီနဲ့ဘဲ ပြ\
		<mark style="background: #FFF3A3A6;">git log commit ID/hash</mark> --> အဲ့ commit နဲ့ဆိုင်တဲ့အချက်တွေ details ပြ
		<mark style="background: #FFF3A3A6;">git log fileName.type  </mark>--> အဲ့ file နဲ့ဆိုင်တဲ့ commit history ကိုပြ
		<mark style="background: #FFF3A3A6;">git log -n number --oneline</mark> --> ‌နောက်ဆုံး လုပ်ခဲ့တဲ့ commit ဘယ်နှစ်ခုစာကိုဘဲ ပြပါ ဆိုပြီး ![[git log -n.png]]
		<mark style="background: #FFF3A3A6;">git log "from commit id" .. "to commit id"</mark> --> ဒီ commit id နဲ့ ဒီ commit id ကြားက commit တွေကိုဘဲ ပြပါဆိုပြီး 
	

###### git checkout 

 commit history ကို ဘာမှမပြောင်းဘဲ ဒီတိုင်‌‌းလေး ရှေ့ commit မှာရှိခဲ့တဲ့ code ပုံစံကို ပြန်သွားချင်ရင် git log မှာပြတဲ့ သက်ဆိုင်ရာ commit နဲ့ဆိုင်တဲ့ hash code နဲ့တွဲသုံးတဲ့ command

syntax: <mark style="background: #FFF3A3A6;"> git checkout hashCode </mark> 

###### git restore

working directories ထဲက files တွေကို staging area (index) ကဖြစ်စေ၊ commit history (repo) ထဲကနေဖြစ်စေ အရင် state ကို ပြန် restore လုပ်ဖို့သုံးတယ်။

syntax:
- <mark style="background: #FFF3A3A6;">git restore (file)</mark> --> file ကို changes တွေတော့လုပ်ပြီးပြီ ။ ဒါပေမယ့် <span style="color:rgb(255, 155, 0)">stage မလုပ်ရသေး</span>ဘူးဆိုရင် ဒီ syntax ကိုသုံးပြီး changes တွေကို discard/ဖျက် လိုက်လို့ရ။ ဘယ်ထိဖျက်ပေးမှာလဲဆိုရင် ‌ရှေ့က commit လုပ်လိုက်တဲ့ file ပုံစံအထိရောက်အောင်ဖျက်ပေးမှာ           ![[git restore.png|300]]                            ဒီမှာဆိုရင် four.txt 2nd line က staged မလုပ်ရသေး, i.e. staging area(index) ကိုမပို့ရသေး။ အောက်ကပုံမှာ restore လုပ်လိုက်တော့ 2nd line ပျောက်သွားရော                                 ![[git restore 2.png|300]]
- <mark style="background: #FFF3A3A6;">git restore --staged (file) </mark> --> သူကကျ staged လုပ်ပြီးပြီ၊ git status နဲ့ စစ်လိုက်ရင်                                     ![[restore --staged.png|300]] changes to be committed လို့ပြနေပြီ။ i.e. file က staged area/index ထဲကို‌ ရောက်နေပြီ။ အဲ့file ကို staging area ထဲကနေပြန်ဆွဲထုတ်ဖို့ --staged ဆိုတဲ့ option ထည့်ပြီး သုံးရတယ်။                                                     ![[restore --staged 2.png|400]] ဒီမှာဆိုရင် --staged option ကိုသုံးပြီး four.txt ကို staging area/index ထဲကနေပြန်ဆွဲထုတ်လိုက်ပြီ။ git status လိုက်လို့ရ

###### git reset

commit history ထဲက commit တစ်ခုခုကို အကြောင်းအမျိုးမျိုးကြောင့် ဖျက်မယ်ဆိုရင်သုံးလို့ရတယ်။

သူ့အလုပ်လုပ်ပုံ HEAD pointer ကို လက်ရှိ commit ကနေ အခြား commit တစ်ခုကို ပြောင်းပေးလိုက်တာ။ သုံးလိုက်တဲ့ options ကို လိုက်ပြိး staging area နဲ့ working directories အပေါ််သက်ရောက်မှုတွေရှိနိုင်တယ်။

syntax မှာက <span style="color:rgb(255, 155, 0)">commit HASH</span> နဲ့ သွားချင်တဲ့ commit ကို ပြန်သွားလို့ရသလို။ <span style="color:rgb(255, 155, 0)">HEAD ~ num</span> (1 / 2 /3 ) 1 ဆို တစ်ခု, 2 ဆို နှစ်ခုအဲ့လိုပြန်သွားလည်းရ 

syntax

<mark style="background: #FFF3A3A6;">git reset --soft hash/HEAD </mark> : ရွေးလိုက်တဲ့ commit ဆီကို ပြောင်းပြီး သူ့ရှေ့က ဟာတွေကို ဖျက်ပေးမယ်။ ဒါပေမယ့် working directory နဲ့ staging area မှာတော့ ဘာမှ ပျက်ခြင်းပြုခြင်းမရှိဘဲ reset မလုပ်ခင်က ပုံအတိုင်းရှိနေမယ်။ staging area မှာဆိုရင်လည်း files တွေက staged & ready to be committed ဖြစ်နေမယ်။

<mark style="background: #FFF3A3A6;">git reset --mixed hash/HEAD </mark> : <span style="color:rgb(255, 155, 0)">default value</span> ဖြစ်ပြီး ‌ရွေးလိုက်တဲ့ commit ဆီကိုသွား၊ ‌ရှေ့ကဟာတွေကို ဖျက်ပေးမယ်။ staging area ကတော့ အဲ့ commit တုန်းကအတိုင်းဖြစ်သွားပြီး (ရှေ့ commit မှာမှ modified လုပ်ခဲ့တာတွေက un-staged ) working directory ကိုတော့ ဘာမှ သက်ရောက်မှုမရှိဘူး။ 

<mark style="background: #FFF3A3A6;">git reset --hard hash/HEAD </mark> : ပြောင်းလိုက်တဲ့ commit အတိုင်း staging area အပြင် working directory ကိုပါလိုက် change မှာဖြစ်လို့ အကုန်ပျက်မယ်။ 
ဒါပေမယ့် --hard ကို မသုံးခင် staging area ထဲမှာ <span style="color:rgb(220, 20, 60)">stage မလုပ်ရသေး</span>တဲ့ <span style="color:rgb(0, 176, 240)">files</span> တွေရှိရင်တော့ အဲ့တာတွေက ကျန်ခဲ့မယ်။<span style="color:rgb(255, 155, 0)"> Untracked files တွေ</span>ကိုပြောတာ
files တွေကို ‌ပြောတာနော်။ <span style="color:rgb(0, 128, 128)">staging area ထဲ add ပြီး modified </span>လို့ ပြတဲ့ ဟာတွေတော့ <span style="color:rgb(255, 155, 0)">မရဘူး</span>

![[--hard reset untracked file.png]]
ဒီမှာဆို second.txt ကို create လုပ်ပြီး စာတွေထည့်ထားပေမယ့် git add နဲ့ staging area ထဲမထည့်ရသေးဘူး။ အဲ့လိုမထည့်သေးဘဲ reset --hard နဲ့ ပထမဆုံး commit ကိုပြန်သွားတာ‌တောင် အဲ့ file က ကျန်သေးတယ်။

chat gpt က ရှင်းပြထားတဲ့ ဥပမာကို [[git reset example by GPT]] မှာကြည့်ပါ
 
![[git reset.png]]

###### git branch

လက်ရှိ ရှိနေတဲ့ branch တွေကိုကြည့်တာ, branch အသစ်လုပ်ဖို့, အဟောင်းဖျက်ဖို့ သုံးလို့ရပါတယ်။

syntax
<mark style="background: #FFF3A3A6;">git branch </mark> : လက်ရှိရှိနေသမျှ branch တွေကို ပြပေးမယ်
<mark style="background: #FFF3A3A6;">git branch Name </mark> : branch အသစ်တစ်ခု create လုပ်မယ်
<mark style="background: #FFF3A3A6;">git branch -d Name  </mark> : branch တစ်ခုကို delete လုပ်မယ် 

###### main branch နာမည်ပြောင်း

```
git config --global init.defaultBranch defaultBranchNameHere

```


###### git switch

branch တစ်ခုကနေ တစ်ခုကူးပြောင်းဖို့ သုံးတယ်။

syntax: <mark style="background: #FFF3A3A6;"> git switch branchName   </mark>
		<mark style="background: #FFF3A3A6;"> git switch -c branchName </mark> --> branch အသစ်တစ်ခုကို create လည်းလုပ်၊ အဲ့ branch ကိုလည်းပြောင်းပေး

###### git rm filename.type --cached

ဒါက file တစ်ခုကို staging area ထဲကနေ ထုတ်/ Unstage လုပ်ဖို့သုံးတယ်။ working directory ထဲမှာတော့ ကျန်နေဦးမှာဆိုပေမယ့် staging area ထဲမှာ မရှိတော့ဘဲ untracked file ဖြစ်သွားမယ်။

<mark style="background: #FFF3A3A6;">git rm filename.type --cached </mark>   
or 
git rm --cached filenam.type

for folder --> <mark style="background: #FFF3A3A6;">git rm -r --cached folderName/</mark>
folder ထဲက files တွေကပါ recursive remove ချင်တာကြောင့်မလို့ -r options ထည့်ပေးရပါတယ်။

<mark style="background: #D2B3FFA6;">--> </mark> ဒီလို remove လုပ်လိုက်ရင် git ls-files ဆိုပြီး စစ်ရင် အဲ့ file ကို မပြဘူး။ system ထဲမှာတော့ကျန်နေသေး‌တဲ့အတွက် ရိုးရိုး system command ls နဲ့ဘဲကြည့်ရင်တော့ ပြသေးတယ်။

များသောအားဖြင့်တော့ <mark style="background: #FFF3A3A6;">.gitignore</mark> နဲ့ တွဲပြီး အဲ့ file ကို ဆက်ပြီး track မလုပ်တော့အောင်လည်း သုံးတယ်။ <span style="color:rgb(0, 128, 128)">အဓိကကတော</span>့ configurations or environment files တွေပေါ်မှာသုံးတယ်။
<mark style="background: #FFF3A3A6;">echo "filename.type" >> .gitignore </mark>

###### .gitignore

git က သာမန်အားဖြင့် file တစ်ခု သုံးမျိုးမြင်တယ်
1. tracked
2. untrack
3. ignore

track နဲ့ untrack ကတော့ staging area ထဲမှာ file ရှိနေလား/မရှိနေလားပေါ့။ ignore ကတော့ အဲ့ file ဘယ်လိုရှိနေလဲဆိုတာကို လုံးဝလိုက်မကြည့်‌တော့ဘဲ ignore လုပ်လိုက်တာ။ အဲ့လို လုပ်ဖို့ အတွက် <mark style="background: #FFB86CA6;">.gitignore</mark> ဆိုတဲ့ files (files <span style="color:rgb(220, 20, 60)">not folder</span>)

တစ်ခါတည်းတော့ .git folder ထဲမှာ ပါမလာဘူး။ ကိုယ့်ဘာသာ create လုပ်ရတယ်။

<mark style="background: #FFF3A3A6;">touch .gitignore </mark>  \
ဒါဆိုရင် ignore လုပ်ဖို့ file ရပြီ အဲ့ file ထဲမှာ ကိုယ် ignore လုပ်စေချင်တဲ့ file နာမည် or all file type အနေနဲ့ သတ်မှတ်လို့ရတယ်။

![[.gitignore.png]]
![[.gitignore folder.png]]
ဒီလို folder လိုက် ignore လုပ်လို့လည်းရတယ်။

<mark style="background: #FF5582A6;">caution: </mark>
.gitignore ထဲကို ထည့်လို့ရတာက untracked files တွေကိုဘဲ။ staging area/index ထဲကို ရောက်နေပြီဖြစ်တဲ့ tracked files တွေကိုတော့ သွားထည့်လို့မရ။ ဒီတော့ အရှေ့က commit တွေထဲ ပါပြီး index ထဲ ‌ရောက်နေတဲ့ files/folder ကို ignore လုပ်ချင်တယ်ဆိုရင် 
- အဲ့ files/foldered ကို git rm --cached (-r) နဲ့ index က အရင်ထုတ်ပါ
- ပြီးမှ .gitignore ထဲထည့်ပါ။
- ဒီလိုလုပ်လိုက်ရင် ‌ရှေ့လျှောက်အတွက် ignore လုပ်ပြီးသားဖြစ်မှာပါ။
- ဒါပေမယ့် ရှေ့ commit တွေကို ပြန်သွားရင်တော့ အဲ့ files/folder က index ထဲမှာရှိနေပါလိမ့်မယ်


###### git diff

command line မှာလိုဘဲ git diff file1 file2 ဆိုရင်တော့ သာမန်ဘဲပြမှာဖြစ်ပါတယ်

<mark style="background: #FFF3A3A6;">git diff --staged </mark> --> လက်ရှိ staging area/index ထဲမှာ ရှိနေတဲ့ files တွေနဲ့ သူ့ရှေ့က commit မှာရှိနေတဲ့ files တွေကို ယှဥ်ပြ
<mark style="background: #FFF3A3A6;">git diff commit1 commit2 </mark>  --> commit နှစ်ခုကြားက changes တွေကို ယှဥ်
<mark style="background: #FFF3A3A6;">git diff branch1 branch2 -- filename  </mark>--> branches နှစ်ခုကြားက ကိုယ်သိချင်တဲ့ files ရဲ့ အပြောင်းအလဲကို ပြ

git diff --staged
	သူ့ကိုက status နဲ့ staged လုပ်ထားတဲ့ files တွေကို ကြည့်ပြီး diff နဲ့ files တွေကြားက အပြောင်းအလဲကိုကြည့်လို့ရ
	![[diff.png]]
	- diff --git a/file.txt .. က compare လုပ်တဲ့ files‌ တွေကို ပြတာ
	- index hash1 hash2 က commit hashes before and after the change
	- --- a/file.txt နဲ့ +++ b/file.txt ဆိုတာက ပြောင်းလဲသွားတဲ့ file path တွေကိုပြတာ
	- @@ -1,4 +1,4 @@ က line numbers & context
	- - Old line က ဖျက်ခံလိုက်ရတဲ့ lines တွေ
	- + New lines က အသစ်ထည့်လိုက်တဲ့ linesတွေ
	![[git diff --staged-1.png]]
	


###### git merge:

branch တစ်ခုမှာ လုပ်စရာရှိတာလုပ်ပြီးသွားတဲ့အခါ အဲ့ branch ကို အခြားသော branch (e.g. main branch) ထဲ သွားပေါင်းဖို့လုပ်တဲ့ အခါသုံးတယ်

အရင်ဆုံး ကိုယ် <span style="color:rgb(146, 208, 80)">သွားပေါင်းမယ့် branch ဆီ</span>ကို switch/checkout command နဲ့ သွား။ အဲ့ branch ထဲရောက်ပြီဆိုမှ  

syntax --> <mark style="background: #FFF3A3A6;">git merge feature-branchName</mark>
