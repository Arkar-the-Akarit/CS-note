keyboard ကနေ command တွေကို လက်ခံပြီး operating system ဆီကို ပို့ပေးတဲ့ program ကို shell လို့ခေါ်တယ်။
terminal, console တွေဆိုတာ shell ကို launch လုပ်ပေးတဲ့ program တွေဘဲ။

shell - bash (bourne against shell), ksh,, zsh, tsch
bash - most linux defaults

command တွေအနောက်မှာ လိုက်တဲ့ စာတွေကို flags လို့ခေါ်တယ်။
`$ cd ../path1/file1`  cd က command, အနောက်ကဟာတွေက flags

###### Commands

echo
	သူက သာမန်အားဖြင့် သူ့နောက်က ရိုက်လိုက်တဲ့ စာတွေကို ပြန်ထုတ်ပေးတယ်
	`$ echo Hello World    # output - Hello World`

date
	`$ date`  output current date & time

whoami
	`$ whoami` output current user

pwd
	`$ pwd` လက်ရှိရောက်နေတဲ့ directory

cd
	`cd /path`
	flag မပါရင် မူလ user directory ကို ပြန်သွားမယ်။
	flags:
	. (current directory)
	.. (parent directory) လက်ရှိရောက်နေတဲ့ directory အပေါ်က တစ်ခုဆီကိုသါား
	~ (home directory) home ကိုပြန်ပို့ပေး
	- (previous directory) အရှေ့မှာရှိခဲ့တဲ့ directory ကို ပြန်ပို့ပေး

###### ls

list, လက်ရှိ directory or flag အနေနဲ့ ပါတဲ့ path အောက်မှာရှိနေတဲ့ directories or files တွေကိုပြ

flags:
`ls -a` a for all, ရှိသမျှ hidden files တွေကိုပါပြပေး

`ls -l` long, files တွေကို အသေးစိတ် permissions, number of links, owner name, owner group, file size နဲ့ နောက်ဆုံးပြင်ခဲ့တဲ့ အချိန်တွေထိပြပေး

`ls -R` recursively ပြပေး၊ parent directory အောက်က child directory အပြင် သူ့တို့ထဲမှာရှိတဲ့ content တွေကိုပါပြ

`ls -r` reverse order while sorting

`ls -t` sort by modification time, newest first

###### touch

file အသစ်တွေ create လုပ်ဖို့သုံးသလို
လက်ရှိ file or directories တွေရဲ့ timestamp ကိုလည်းပြင်ဖို့သုံးလို့ရ

##### file

linux မှာက file ထဲက contents (ပုံ, videos, photos) တွေကို ဖော်ပြဖို့ file type name ကိုမလိုဘူး။

touch hi.gif ဆိုပြီး gif မဟုတ်တဲ့ file တစ်ခုကို ဖန်တီးလို့ရတယ်။

file command ကိုသုံးပြီးတော့ file ထဲက content တွေရဲ့ descriptions တွေကို ကြည့်လို့ရ

![[command_file.png]]

###### cat

short for concatenate, files တွေကို ကြည့်ဖို့သုံးတယ်။ file နှစ်ခု၊ သုံးခုကို တွဲကြည့်ရင်လည်း file တွေကို ပေါင်းပြီး ဖတ်လို့ရအောင် output ထုတ်ပေးတယ်။
short content အတွက်ဘဲ ကောင်းပြိး long content တွေအတွက်ဆို အခြား tools & command တွေသုံးတာ ပိုကောင်းတယ်။

###### less

file content တွေက ရှည်လွန်းရင် paged manner နဲ့ ပြပေးဖို့သုံးတဲ့ command, 

less command ထဲရောက်သွားရင် အခြားသော command တွေကို သုံးလို့ရတယ်။

q - less ကနေ quit လုပ်, shell ဆီကိုပြန်
g - file အစကို ပြန်သွား
G - file အဆုံးကို သွား
/search_keyword - serach_keyword နေရာမှာ ထည့်ချင်တဲ့ စာလုံးကိုထည့်ပြီး file ထဲမှာရှာလို့ရ
h - help
page up, down, left, right arrows - ဘေးဘယ်ညာရွှေ့

###### history

လက်ရှိ terminal session မှာထည့်ခဲ့သမျှ commands တွေကို ပြန်ပြပေးတယ်။ up, down arrow 

နောက်ဆုံး run ခဲ့တဲ့ command တစ်ခုကို ပြန် run ချင်ရင် `$ !!`

`Ctrl + R` ဆိုရင် reverse search command ဖြစ်သွားပြီး အရင်က ထည့်ခဲ့တဲ့ command တွေကို စာလုံးပြန်ရိုက်ထည့်ပြီး ရှာလို့ရ
