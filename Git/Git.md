
Git ဆိုတာက files တွေမှာ အပြောင်းအလဲဖြစ်သွားတာတွေကို track လုပ်ပြီး အချိန်မ‌ရွေးပြန်ကြည့်ရှူနိုင်အောင် track လုပ်ပေးတဲ့ <span style="color:rgb(255, 155, 0)">distributed version control system (VCS)</span> ဖြစ်ပါတယ်။  
- project files တွေအပေါ် လုပ်လိုက်တဲ့ changes တွေကို record လုပ်ထားပေးတယ်။ version အ‌ဟောင်းတွေကို လိုသလိုပြန်ပြောငး်လို့ရ
- main codebase ကို မထိဘဲနဲ့ branches တွေကို ခွဲပြီး features အသစ်တွေ စမ်းသပ်ပြီး နောက်မှ main codebase ထဲ ပြန်ပေါင်းလို့ရ
- entire project history ကို local copy အဖြစ်သိမ်းထားပေးတဲ့အတွက် offline ဖြစ်နေရင်တောင် collaborate လုပ်လို့ရ

distributed version control system: store files in local as a copy, project ထဲမှာ ပြုပြင်ပြောင်းလဲတာတွေလုပ်ဖို့အတွက် online ဖြစ်ဖိုမလို

centralized version control system : ဖြစ်သမျှ changes/files တွေကို server တစ်ခုထဲမှာ သိမ်းထားတယ်။ အချင်းချင်းမျှဝေလို့ရပေမယ့် server နဲ့ connection ပြတ်သွားရင်ဖြစ်ဖြစ်, offline ဖြစ်သွားရင်ဖြစ်ဖြစ် ဘာ

###### GitHub

Github ဆိုတာက git ကို version control system အဖြစ်သုံးထားတဲ့ web-based platform တစ်ခု။ developers ‌တွေ project တွေကို ပိုပြီး ကောငး်ကောငး်စီမံခန့်ခွဲနိုင်ဖို့နဲ့ collaborate လုပ်နိုင်ဖို့ tools ‌တွေပါတယ်

###### Git Repositories

Repository (repo) ဆိုတာက project files တွေနဲ့ files တွေမှာ ဖြစ်ခဲ့တဲ့ အပြောင်းအလဲ (changes history) အကုန်လုံးကို track လုပ်ပြီး manage လုပ်တဲ့ storage location ကိုပြောတာ။ 

- <mark style="background: #CACFD9A6;">local repository </mark> : local machine (own pc, laptop) ထဲမှာရှိနေတဲ့ repo။ ကိုယ်ပိုင် laptop မှာ repository တစ်ခုဖန်တီးလိုက်ရင် အဲ့တာက local repo ဘဲ။ Git operation တွေဖြစ်တဲ့ adding files, committing changes, creating branches... စတာတွေကို local repo ထဲမှာ လုပ်ဆောင်တယ်။

- <mark style="background: #CACFD9A6;">Remote Repository </mark> : remote server တစ်ခု(such as Github, Gitlab, Bitbucket) မှာ ထည့်ထားတဲ့ repo။  project တွေကို အခြားသူတွေနဲ့ share လုပ်ပေးဖို့သုံးနိုင်ပြီး local repo က changes တွေကို remote repo ကို Push လုပ်တာ ၊ remote repo က  changes တွေကို local repo ထဲ Pull လုပ်တာ စတာတွေလုပ်လို့ရ

Repository တစ်ခုကို initialize လုပ်လိုက်တာနဲ့ ကိုယ်လုပ်လိုက်တဲ့ directory ထဲမှာ <mark style="background: #FFF3A3A6;">.git</mark> ဆိုပြီး <span style="color:rgb(255, 155, 0)">hidden directory</span> တစ်ခုကို git က ဖန်တီးပေးတယ်။ အဲ့ထဲမှာ လိုအပ်တဲ့ metadata နဲ့ history တွေပါတယ်။ hidden လုပ်ထားရတဲ့ အကြောင်းက အဲ့ထဲက file တွေ ပုံမှန်ဆို သွားထိပြီး ကလိစရာမလိုဘူး

hidden လုပ်ထားတာကိုမှ သွားကြည့်ချင်ပါတယ်ဆိုရင်
vsCode settings --> search "files.exc" --> delete .git



###### Committing in Git

commit လုပ်တယ်ဆိုတာက code ထဲမှာ အပြောင်းအလဲ (changes) တစ်ခုခု လုပ်လိုက်တာကို အချိန်တစ်ခုမှာ snapshot ရိုက်ပြီး သိမ်းလိုက်သလိုမျိုးဘဲ။ commit လုပ်ပြီဆိုရင် git က ကိုယ်လုပ်လိုက်တဲ့ changes တွေကို staging area ဆီသယ်သွားတယ်။ ပြီးမှ repository history ထဲမှာ သွားသိမ်းလိုက်တယ်။
commit တစ်ခုစီတိုင်းမှာ SHA-1 Hash လို့ခေါ်တဲ့ Unique identifier တစ်ခုဆီပါတယ်။ အဲ့ hash တွေနဲ့ commit တွေကို track လုပ်လို့ရသလို, Previous commit တွေဆီ ပြန်သွားလို့ရတယ်။ 

commit တစ်ခုမှာဆိုရင် ပုံမှန်အားဖြင့် message လေးပါတတ်တယ်။ လုပ်လိုက်တဲ့ ‌အပြောင်းအလဲနဲ့ ပတ်သတ်နဲ့ note လိုမျိုးဖြစ်ဖြစ်ပေါ့။ သူ့ကို <mark style="background: #BBFABBA6;">-m " " </mark> option နဲ့ထည့်ပေးရတယ်။

Committing မှာ အဆင့် (၂) ဆင့်နဲ့ ၊ နေရာ (၃) နေရာ အလုပ်လုပ်တယ်။
1. Working Directory / Working Tree / Work Space
2. Staging Area
3. Repository

Working Directory or Working Tree .. လို့ခေါ်တဲ့ လက်ရှိ directoryကနေ ပြီးမှာ git add command နဲ့ staging area/ index ကို ပို့တယ်။ staging area ကနေမှ တစ်ဆင့် git commit နဲ့ repository/comimt history ထဲကို လှမ်းထည့်လိုက်တာဖြစ်တယ်။
![[git commit.png]]


###### Staging area / index

working directory ထဲမှာ changes လုပ်လိုက်တာနဲ့ အဲ့တာတွေက automatic ကြီး repository ထဲကိုရောက်သွားတာမဟုတ်ဘူး။ user က နေပြီးတော့မှ အဲ့ကောင်တွေကို staging area ထဲအရင်ထည့်ရတာ။ အဲ့လိုထည့်တဲ့အချိန်မှာ ကိုယ်ထည့်ချင်တဲ့ file တစ်ခု/အများကို တစ်ခါထဲထည့်လို့ရတယ်။

staging area ဆိုတာက နောက် commit မှာ ကိုယ်ပါစေချင်တဲ့ changes တွေကို Git က သိမ်းဆည်းပေးတဲ့နေရာပေါ့။ တကယ့် commit မလုပ်ခင်မှာ changes လုပ်လိုက်တာတွေကို လိုသလိုပြင်ဆင်လို့ရသေးတဲ့ ကြားခံနေရာတစ်ခုလို့လည်းပြောလို့ရတယ်။

e.g.
- file1.txt , file2.txt, file3.txt ဆိုပြီး ဖိုင်သုံးခုမှာ အပြောင်းအလဲ changes နညး်နညး်လုပ်လိုက်တယ်။
- ဒါပေမယ့် file1 နဲ့ file2 ကိုဘဲ commit မှာ ပါစေချင်တယ်။
- ဒီတော့ git add file1.txt file2.txt ဆိုပြီးတော့ file ၂ ခုကိုဘဲ staging area ကိုပို့လိုက်တယ်။
- ပြီးတော့ commit လိုက်ရင် ပါစေချင်တဲ့ file1 နဲ့ file2 က changes တွေဘဲ ပါသွားမယ်။

##### Branch

DSA ကို သိထားရင်တော့ branch ဆိုတာက commit ကို ညွှန်ပြတဲ့ pointer တစ်ခုလို့ဘဲပြောရမှာဘဲ။ Linked list ပုံစံပေါ့။

default branch က‌တော့ ‌main / master ဆိုပြီး ခေါ်ကြတာများတယ်။
အဲ့ branch အောက်မှာ လက်ရှိ working directory, index , repo ရှိတယ်ပေါ့နော်။ 

development လုပ်တဲ့ အခါ deploy လုပ်ကြတာက များသောအားဖြင့် main ကိုလုပ်ကြတယ်။ functions & features တေ‌ွက main branch မှာက သေချာ test လုပ်ပြီးသားကိုး။ အဲ့ဒီမှာ functions/features အသစ်ထည့်ချင် ပြုပြင်ချင်တဲ့အခါကျတော့ main မှာ သွားလုပ်လု့ိ အဆင်မပြေဘူးလေ။ ဒီတေ့ာ branch အသစ်ဆောက်ရတယ်။ 
သက်ဆိုင်ရာ command နဲ့ branch အသစ်လုပ်လိုက်တဲ့ အခါကျတော့ branch အသစ်မှာ က လက်ရှိရောက်နေတဲ့ commit ကစပြီး wd, index အကုန်ပါမယ်။ ဒါပေမယ့်သူက pointer အသစ်နဲ့ ညွှန်တာမျိုး။ အဲ့မှာ ပြင်စရာရှိတာပြင်, အသစ်ထည့်စရာရှိတာထည့် staging ထဲ ပို့, commit လုပ် ကြိုက်တာလုပ်၊ main မှာ ဘာမှသွားမပတ်သက်သေးဘူး။ i.e. main branch ရဲ့ commit မှာက commit 3 ထိရှိတယ်ကွာ၊ new branch နဲ့ commit 5,6 ထိလုပ်လညး် main branch ကိုပြန်ပြောင်းကြည့်ရင် commit 3 ခုဘဲရှိဦးမှာပေါ့။ ကိုယ်က စိတ်ကြိုက်ဖြစ်ပြီဆိုမှ main branch ပြန်သွားပြီး အသစ်လုပ်လိုက်တဲ့ branch ကို လာ merge (ပေါင်း) ပေါ့။

<mark style="background: #BBFABBA6;">naming convention </mark> : နာမည်ကိုပေးချင်သလို ပေးလို့ရပေမယ့် categories or topics နဲ့ လိုက်ပြီး နာမည်ပေးတာက အသုံးများတယ်။ organize လည်းဖြစ်သွားသလို, branch တစ်ခုဆီရဲ့ purpose ကို လည်း နားလည်ရလွယ်စေတယ်။ e.g. 'feature/payment-integration' , 'feature/userLogin', 'bugfix/mailingError' 

##### Merge 

merge လုပ်တာက‌တော့ main branch ထဲကို အခြားသော branch တွေ လာပေါင်းတာပေါ့။
merge လုပ်တာ command က တစ်ခုထဲ ဆိုပေမယ့် အလုပ်လုပ်ပုံနှစ်မျိုးရှိတယ်။
1. fast forward
2. recursive three ways

Fast Forward
	သူက branch ခွဲလိုက်ပြီးနောက်မှာ main က ဘာcommit မှထပ်မလုပ်ထားဘူး။ new branch မှာဘဲ commit တွေ ထပ်ထည့်ထားတယ်။ ဒါဆိုရင် သွားပေါင်းလိုက်တဲ့ အချိန်မှာ ရိုးရိုးရှင်းရှင်‌းလေးဘဲ new branch က new commits တွေကို main commit ထဲမှာ လာ‌ထည့်ပေးတယ်။
	![[fast_forward_merge_1.png]] main က branch ခွဲထွက်ပြီးနောက် ဘာမှထပ်မဖြစ်။ still on c2 commit
	![[git_fast_forward_merge (2).png]]
	so after merging, သူက အေးဆေး c4 အထိ ပေါင်းလိုက်‌ရော

Recursive Three Ways
	main branch ကနေ branch အသစ်ခွဲထွက်ပြီးနောက်မှာ branch အသစ် တစ်ခု ထပ်လုပ်လိုက်တယ်။ new branch ထဲမှာ commit တွေထပ်ထည့်ပြီးတော့မှ main ကို လာပြီး commit အသစ်ထပ်ထည့်တယ်။ အဲ့တာပြီးမှ merge လုပ်မယ်ဆို git က recursive three ways ကို သုံးတယ်။ သူ့လုပ်ပုံက branch နှစ်ခုရဲ့ တူညီတဲ့ common ancestor commit ကိုရှာတယ်။ ပြီးတော့မှာ အဲ့common ancestor commit က စပြီး branch နှစ်ခုမှာ ဖြစ်လာတဲ့ အပြောင်းအလဲတွေနဲ့, branch နှစ်ခုရဲ့ လက်ရှိ head commits တွေကို ရှာတယ်။ ရှာပြီးတော့မှ commit အသစ်တစ်ခုနဲ့ branch နှစ်ခုရဲ့ head commit နှစ်ခုကို ညွှန်ပေးလိုက်တာပါ။
	![[recursive_three_ways_merge_1.png]]
	c2 မှာ branch ခွဲထွက်ပြီးနောက်မှာ main branch မှာက ထပ်ပြီးတော့ c5 ဆိုပြီး commit အသစ်တစ်ခုဝင်ထားတယ်။ ![[three_ways_recursive_merge_2.png]]
	ဒီမှာဆိုရင် merge လုပ်လိုက်တဲ့အချိန်မှာ c6 commit ဆိုပြီး gitက လုံးဝ commit အသစ်ထပ်လုပ်လိုက်တာ။
	![[recursive three ways eg in bash.png]]

Conflicts in merging
	recursive three ways မှာ common ancestor commit ပြီးလာတဲ့ commit တွေမှာ main branch မှာရော new branch မှာရော <span style="color:rgb(0, 128, 128)">တူညီတဲ့ file တစ်ခုကို edit</span> လုပ်ထားရင် bash က ဘယ် branch က file ကို အတည်ယူရမလဲ မသိဘူးဖြစ်သွားတယ်။ အဲ့တာကို conflicts ဖြစ်တယ်လို့ ခေါ်တယ်။ conflicts ဖြစ်ရင် vsCode မှာတော့ သူက ဘယ် file က ဟာကို သိမ်းမလဲ, နှစ်ခုစလုံးက ဟာကို သိမ်းမလားဆိုပြီ‌း ရွေးခိုင်းတယ်။ နှစ်ခုစလုံးကဟာကို သိမ်းမယ်ဆိုရင် sub-branch ဖြစ်တဲ့ကောင်ရဲ့ဟာက နောက်ကနေ လိုက်မယ်။