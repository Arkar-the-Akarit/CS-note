
The shell is Git Bash

<mark style="background: #ABF7F7A6;">ls </mark> : ဒါက လက်ရှိရောက်နေတဲ့ directory အောက်က files/directories တွေကိုပြပေး
	<mark style="background: #FFF3A3A6;">-a</mark> option က hidden files/directories တွေပါ အကုန်ပြပေး

<mark style="background: #ABF7F7A6;">pwd </mark> : print working directory, လက်ရှိကိုယ်ရောက်နေတဲ့ directory ကိုပြပေး

<mark style="background: #ABF7F7A6;">mkdir </mark>  : make directory, လက်ရှိရောက်နေတဲ့ directory အောက်မှာ directory တစ်ခုထပ်ဆောက်

<mark style="background: #ABF7F7A6;">clear </mark> : သူက လက်ရှိ terminal ထဲမှာ စာတွေရှူပ်နေတယ်ဆို သုံး၊ နောက်ရိုက်မယ့် command line က screen ‌အပေါ််ဆုံးကို ရောက်လာမယ်။ အရင် ဟာတွေက အပေါ်မှာရှိသေးတယ်။ ရှင်းသွားအောင် command line အသစ်ကို screen အပေါ်ဆုံးမှာ ပြတာ

<mark style="background: #ABF7F7A6;">cd </mark> : change directory, directory တွေပြောင်းဖို့
- လက်ရှိရောက်နေတဲ့ directory ရဲ့ အပေါ်က parent directory ကိုသွားချင်တယ်ဆိုရင် <mark style="background: #ABF7F7A6;">cd ..</mark> ဆိုပြီး '..' နှစ်ခုကိုသုံးတယ်။ သူက ".." တစ်ခါကို အပေါ် directory တစ်ခါတက်တယ်။ အကယ်လို နှစ်ခု,သုံးခု ထိတက်ချင်တယ်ဆိုရင် cd ../../../ ဆိုပြိးသွားလို့ရတယ်။![[cd ...png|1000]] ပုံမှာဆိုရင် first command မှာ ရောက်နေတဲ့ directory က "1_font_family", အဲ့မှာ ".." နှစ်ခါနဲ့ အပေါ်တက်လိုက်တော့ second command မှာ "VS Code" directory ကိုရောက်သွားရော
- ပုံထဲကလိုမှ "VS Code" directory ကနေ 1_font_family directory ထိကို ပြန်သွားချင်တယ်ဆိုရင် <mark style="background: #FFB86CA6;">cd နဲ့ tab ကိုသုံးတဲ့</mark> trick ကိုသုံးလို့ရတယ်။
	- cd ရိုက်ပြီး ကိုယ်သွားချင်တဲ့ directory ရဲ့ နာမည်အစလေးကို ရိုက်ပြီး <span style="color:rgb(0, 128, 128)">tab ခေါက်</span>လိုက်ရင် terminal က ကျန်တဲ့ နာမည်ကို<span style="color:rgb(0, 128, 128)"> auto fill ပေး</span>တယ်။ အကယ်လို နာမည်အစ တူနေတဲ့ directory နှစ်ခုနဲ့အထက်ရှိနေတယ်ဆိုရင် သူက ပြပေးတယ်။ ဒီအောက်မှာ ဒီ directories တွေရှိတယ်ပေါ့။ e.g. cd HTM ဆိုပြီး tab ခေါက်လိုက်ရင် auto ဒီလိုဖြစ် "$ cd HTML\ \&\ CSS/" အဲ့တာကို မှ <span style="color:rgb(0, 128, 128)">tab ထပ်ခေါက်</span>လိုက်ရင် ![[cd and tab.png|900]]သူ့အောက်က directories တွေကိုပြပြီး အောက်မှာ ကိုယ်သွားချင်တာကို ရိုက်ထည့်လို့ရအောင် auto ထပ်ရိုက်ပေးထားတယ်။ အဲ့မှာလည်း နာမည်အစရိုက် tab ခေါက် auto fill, နောက် tab က directories ပြနဲ့ ကိုယ်သွားချင်တဲ့ directories အထိသွားလို့ရတယ်။

<mark style="background: #ABF7F7A6;">&&  </mark> : command နှစ်ခုနဲ့ အထက်ကို တစ်ခါတည်း‌ ပေါင်းရေးဖို့ (e.g. $ cd ../another dir/ <span style="color:rgb(0, 176, 240)">&&</span> mkdir NewDir )

<mark style="background: #ABF7F7A6;">touch </mark> : file create လုပ်ဖို့သုံးတယ်။ director တစ်ခုအောက်မှာ create လုပ်ချင်တာဆိုရင် <mark style="background: #D2B3FFA6;">file name.file type </mark> နဲ့ တစ်ခါတည်းရေးလို့ရပြီး ၊ <mark style="background: #D2B3FFA6;">child directory / file name. file type</mark> နဲ့လည်း လက်ရှိ ရောက်နေတဲ့ directory အောက်က directory တွေထဲမှာ create လုပ်လို့ရ

<mark style="background: #ABF7F7A6;">cat </mark> : file တွေကို ဖတ်ဖို့သုံးတယ်။ ခေါ်လိုက်တဲ့ file ကို ပြပေးတာပေါ့။ --> $ cat file path (file name 'or +' directory) ![[cat command.png]]

<mark style="background: #ABF7F7A6;">mv </mark> : သူက file တွေကို <span style="color:rgb(255, 155, 0)">move</span> လုပ်ဖို့ နဲ့ <span style="color:rgb(255, 155, 0)">rename</span> လုပ်ဖို့ သုံးတယ်။
	- <span style="color:rgb(255, 105, 180)">move</span> : <span style="color:rgb(0, 255, 255)">file path (file name 'or' child directory/file name) target Directory</span> (ပြောင်းချင်တဲ့ directory). --> e.g. $ mv test1/test.txt test2
	- <span style="color:rgb(255, 105, 180)">rename</span> : <span style="color:rgb(0, 255, 255)">file path (file name 'or' child directory/file name) target directory/new Name</span> --> e.g. $ mv test1/test.txt test1/nameChangetest.txt 
	  ဒီနေရာမှာ file name change ပြီဆိုရင် ကိုယ်change မယ့် file က parent directory ထဲမှာ မဟုတ်ဘူးဆိုရင် change လိုက်တဲ့ file ကို ဘယ်မှာ ထားမယ်ဆိုတာ သတ်မှတ်ပေး၇တယ်။ သူရှိနေတဲ့ child directory ကိုပြန်ထည့်ပြီး new name ထည့်မှ name change ပြီးရင် အဲ့ရှိနေတဲ့ directory ထဲကို ပြန်ရောက်တာ။ ဘာမှမထည့်ဘဲ e.g. $ mv test1/test.txt nameChangeTest.txt ဆိုရင် parent directory ထဲ အဲ့ file က ရောက်သွားလိမ့်မယ်။

<mark style="background: #ABF7F7A6;">cp </mark> : file တစ်ခုကို <span style="color:rgb(0, 176, 240)">copy</span> ယူဖို့သုံးတယ်
	- cp file.txt file/path/
	- cp file.txt file/path/newName.txt
	- <mark style="background: #FFF3A3A6;">cp -r folder/path another/folder/path</mark> --> directory တစ်ခုလုံးကို copy ဖို့သုံးတယ်


<mark style="background: #ABF7F7A6;">rm </mark> :  
	- <span style="color:rgb(0, 176, 240)">file</span> ကို ဖျက်ဖို့သုံးတယ်။ file path (file name 'or' child directory/fileName) --> $ rm test1/test.txt
	- <span style="color:rgb(255, 155, 0)">directory</span> ကို ဖျက်ချင်ရင် rm command အနောက်မှာ option "-r" လေးကို space ခြားပြီး လိုက်ပေးရတယ်။ အဲ့နောက်မှာမှ ကိုယ်ဖျက်ချင်တဲ့ directory. --> $ rm -r directory . <mark style="background: #D2B3FFA6;">-r</mark> ဆိုတဲ့ option က <span style="color:rgb(255, 105, 180)">recursive </span> ကို ပြောတာ။ အဲ့တာနဲ့ ဖျက်ရင် အဲ့ directory အေ‌ာက်မှာ ရှိမယ့် files / directories တွေရော <span style="color:rgb(220, 20, 60)">အကုန်ပျက်</span>။ အကယ်လို့ directory ထဲမှာ ဘာfileမှ ရှိမနေဘဲ အလွတ်ကြီးဆိုရင် <mark style="background: #FFF3A3A6;">rmdir</mark> command 
	- rm \*fileType ဆိုရင် အဲ့ file type ရှိသမျှ အကုန်ကို တစ်ခါတည်းဖျက်တာ
	- <mark style="background: #FFF3A3A6;">rm -f</mark> -f option သုံးလိုက်ရင် nonexistent files ‌တွေကို ignore လုပ်ပြီး ဖျက်ဖို့ confirmation မတောင်းတော့ဘူး။ files or directories က not exist (မရှိ) နေ‌ရင်ဖြစ်ဖြစ်၊ write-protected (read only) ဘဲဖြစ်နေရင်တောင်ဖြစ်ဖြစ် ဖျက်ပစ်မှာ
	- <mark style="background: #FFF3A3A6;">rm -rf</mark> recursive & force ကို တွဲသုံးတာ။ အေအောက်က ရှိသမျှ sub-directories/files တွရော အကုန်ဖျက်။ e.g. <mark style="background: #BBFABBA6;">git rm -rf .git/</mark>


<mark style="background: #ABF7F7A6;">which </mark> : 
	- အခုသုံးနေ‌တဲ့ ls, pwd, mkdir... အစရှိတဲ့ command တွေအားလုံးက program လေးတွေ၊ သူတို့ကို terminal ထဲမှာ run ခိုင်းလိုက်ရင် terminal --> shell ကိုပို့၊ shell ကမှ တကယ် run ပေးတာပေါ့့နော်။ အဲ့မှာ ကိုယ် run တဲ့<span style="color:rgb(0, 128, 128)"> command program file က ဘယ်နားမှာ ရှိနေလဲ</span> သိချင်ရင် which command ကို သုံးရတယ်။ --> $ which ls / $ which pwd . အဲ့လိုဆိုရင် command program file ရှိတဲ့နေရာကိုပြပေးတယ်။

<mark style="background: #ABF7F7A6;">echo  </mark> : terminal ထဲမှာ text / <span style="color:rgb(146, 208, 80)">စာကြောင်းတစ်ကြောင်းကို display ပြဖို့</span>သုံးလို့ရသလို, <span style="color:rgb(0, 255, 255)">variable တစ်ခုရဲ့ value ကိုကြည့်ဖို့</span>လည်းသုံလို့ရ။ e.g. echo "Hello, World!" , echo $PATH


<mark style="background: #ABF7F7A6;">sudo </mark> : task တစ်ခုကို administrator privilege နဲ့ run ဖို့သုံး, ဒါနဲ့ ‌ဒေါင်းရင် User ရဲ့ password ထည့်ပေးရတယ်.. <mark style="background: #FFF3A3A6;">only for</mark> unix-operating system such as Linux, macOS

<mark style="background: #ABF7F7A6;">curl </mark> : link တစ်ခုခုကို download လုပ်ဖို့သုံးတယ်။ <mark style="background: #FFF3A3A6;">only for</mark> unix like operating system
- <mark style="background: #ADCCFFA6;">-L </mark> : အကယ်လို့ download link က အခြားသော link တစ်ခုကို ပြောင်းသွားရင် အဲ့ link ကိုပါ လိုက်သွားဖို့သုံးတဲ့ option
- <mark style="background: #ADCCFFA6;">-o </mark> : ‌ဒေါင်းလို့ရလာတာကို ဒီ path မှာ သိမ်းပေးပါဆိုပြီး နေနောက်က directories ပါ လိုက်ရတဲ့ option
e.g. $ sudo curl -L blahblah.com -o usr/bin/blah

<mark style="background: #ABF7F7A6;">chmod </mark> : change mode, download လုပ်လိုက်တဲ့ file တွေကို system က virus တွေကို ကာကွယ်ဖို့အတွက် ပိတ်ထား၊ အဲ့တာကို ဖွင့်လို့၇အောင် mode ပြောင်းဖို့။ only for unix-like operating system

- <mark style="background: #ADCCFFA6;">a+ </mark> : for all user in this system
- <mark style="background: #ADCCFFA6;">r </mark> : allowed for reading
- <mark style="background: #ADCCFFA6;">x </mark> : allowed to execute
e.g. sudo chmode a+rx /usr/bin/blah

<mark style="background: #ABF7F7A6;">diff </mark> : 
- file နှစ်ခုကြားမှာဖြစ်သွားတဲ့ အပြောင်းအလဲတွေကို ပြပေးတယ်
- <mark style="background: #CACFD9A6;">diff \[ options \] file1 file2 </mark> --> syntax
- output မှာ Less than sign '<' နဲ့က file1 မှာဘဲပါပြီး file2 မှာ မပါတဲ့ lines တွေကို ပြပေး
- greater than sign '>' နဲ့က file2 မှာ ပါပြီး file1 မှာ မပါတာတေတွေကို ပြ
- ဒီ မတူညီတာတွေ မပါတာတွေက files တွေရဲ့ ဘယ် line number မှာဖြစ်တယ်ဆိုတာကို lines numbers က ပြတယ်
- ![[diff command in CLI.png]] 
	- 2,4 c 2,4 ဆိုတာက ဘယ်ဘက်က 2,4 က diff1.txt က line number 2 & 4 ကိုဆိုလိုတာ
	- ညာဘက်က 2,4 က diff2.txt က line number 2,4 ကိုဆိုလိုတာ
	- c ဆိုတဲ့ စကားလုံးက 'change' လို့ပြောတာ, သဘောက ဒီလိုင်းတွေမှာ file ၂ ခုက မတူညီကြပါဘူးပေါ့
	- < for content of diff1.txt
	- > for content of diff2.txt
	- \\ no newline at end of file ဆိုတာက file က text file တစ်ခုမှာ ရှိရမယ့် newline character (/n) ဆိုတာမျိုးမပါဘူးလို့ဆိုု

Terms:

- <span style="color:rgb(0, 176, 240)">directory</span> : a location in the file system that contains references to other files or directories