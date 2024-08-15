
file type : <span style="color:red;">နှစ်မျိုး</span>
1. .txt (text file)
2. .bin (binary file)

###### File handle လုပ်ဖို့ 

```
FILE *fptr;
```
file တွေကို ကိုင်တွယ်ရင် pointer ကို သုံးရတယ်

###### File open 
C မှာ file ဖွင့်ဖို့အတွက်

```
fptr = fopen("file_name.txt", mode)
```

##### Mode in file Handling

###### Basic အနေနဲ့ **သုံးခု** ရှိ

- **r** (Read mode)

		- သူကကျ file ကို read  ဖို့အတွက်ဖွင့်တာ 
		- file က ရှိနေရမယ် ။ မဟုတ်ရင် fopen() fail & return ==**NULL**==
		- ဒီ mode နဲ့ file ဖွင့်လိုက်ရင် file pointer က **==file အစမှာ==** ရှိနေမယ်။

- **"w"** (Write Mode)
		- file ကို write ဖို့ ဖွင့် i.e. file ထဲကို data ထည့်ဖို့
		- File ရှိမနေရင် create auto လုပ် ၊ ရှိနေရင် အထဲက data တွေကို **overwrite** လုပ်
		- ဒီ mode နဲ့ file ဖွင့်လိုက်ရင် file pointer က **==file အစမှာ==** ရှိနေမယ်။

- **"a"** (Append Mode)
		- သူကကျ file ထဲက data  တွေကို overwrite မလုပ်ဘဲ လက်ရှိ data အနောက်ကနေ ဆက်ထည့်တာ။
		- File ရှိမနေရင် create auto လုပ်
		-  file pointer က **==file အဆုံးမှာ==** ရှိနေမယ်။

- For Binary File
	     - rb, wb, ab



###### Mode Combination

- **" r+ "** (Read/Write Mode)
		- file ကို read or write လုပ်ဖို့ ဖွင့်။
		- normal r လို့ဘဲ file ရှိနေရမယ်။ မရှိရင် fopen fail & return NULL
		- file pointer က file <span style="color:chartreuse;"> အစမှာ</span> (at the <span style="color:chartreuse;"> beginning </span> of the file)
		- read & write operations တွေကို file ရဲ့ ==ဘယ်နေရာမှာ ဖြစ်ဖြစ်== လုပ်လို့ရ

- **" w+ "** (Read/Write Mode, Overwrite)
		- for both read & write
		- file ရှိနေရင် data တွေကို truncate, i.e ဖျက်ပစ် ၊ မရှိရင် create လုပ်
		- file pointer က <span style="color:chartreuse;"> အစမှာ</span> (at the <span style="color:chartreuse;"> beginning </span> of the file)
		- read & write operations တွေကို file ရဲ့ ==ဘယ်နေရာမှာ ဖြစ်ဖြစ်== လုပ်လို့ရ

- " a+ " (Read/Append Mode)]
		- for both reading and appending
		- file မရှိရင် create လုပ်
		- Read တာကတော့ file ရဲ့ ==ဘယ်နေရာကို ဖတ်ဖတ်== ရ ။ ဒါပေမယ့် Write လုပ်မယ်ဆိုရင် ==file အဆုံးကနေဘဲ လုပ်လို့ရတယ်==
		- file pointer ဟာ <span style="color:chartreuse;"> ကနဥ◌ီး</span> အနေနဲ့ ==file <span style="color:red;">အဆုံးမှာ</span>==ရှိတယ်။ ဒါပေမယ့် read လုပ်ဖို့ **အတွက်** ဆို ဘယ်ကို ရွှေ့ရွှေ့ ရ။

  **Brief Comparison**
    - "r+" vs "w+"
		    နှစ်ခုလုံးက read & write ဖို့ဆိုပေမယ့်  w+ က ရှိပြီးသား data/content တွေကို  erase လုပ်ပစ်။
		    
	- "r+" vs "a+"
			"r+" က file pointer ကို file ==အစမှာ== ထားပေမယ့် "a+" ကတော့ ==ကနဥ◌ီး== အနေနဲ့ file ==အဆုံးမှာ== ထားပါတယ်။ i.e r+ နဲ့ဆို အသစ်ထည့်တဲ့ data တွေက file အစကနေ **ဝင်** အရင်ရှိပြီးသားတွေက နောက်ရောက်သွား၊ a+ ကျ နောက်ဆုံးက စဝင်


##### full syntax of file opening

```
FILE *fptr;

fptr = fopen("example.txt", r);

if(fptr == NULL) or if(!fptr) {

perror(); 

} 

// write operations

fclose(fptr) <== important


```

file ဖွင့်ပြီးရင် <span style="color:red">ပိတ်ဖို့မမေ့ရ</span>


##### feof()

feof(file stream) ဆိုတဲ့ function က file အဆုံး ရောက်ပြီလား မရောက်သေးဘူးလား ကြည့်ဖို့သုံးတယ်။ ဒီ function က file ဆုံး မဆုံး သိဖို့အတွက် file pointer ကို ကြည့်ပြီး ဆုံးဖြတ်သွားတာ။ file ကို read ပြီဆိုရင် file pointer လေးက read လုပ်တဲ့ data တွေပေါ် လိုက် ထောက်နေတာ။ အကယ်လို့ data အကုန်ဖတ်ပြီးသွားရင် သူက end-of-file indicator လေးကို set  လုပ်လိုက်တယ်။ ဒီတော့ အဲ့ eof indicator လေးကို တွေ့ရင် feof() က return **true** ၊ မတွေ့ရင် return false ပေါ့။ 

ဒါဆို feof ကို သုံးပြီး file empty ဖြစ် မဖြစ် ဘယ်လို စစ်လဲ?

တကယ်တော့ စစ်နညး်မှန်တယ်လို့  ပြောလို့မရပါဘူး။ feof က လက်ရှိ file pointer ရောက်နေတဲ့ နေရာကို ကြည့်တာပါ။ အဲ့မှာ file တစ်ခုကို read mode နဲ့ဖွင့်လိုက်ရင် file pointer လေးက beginning of the file မှာပါ။ file အထဲမှာ ဘာ data မှရှိမနေတဲ့အခါ eof indicator ရှိမယ်။ အဲ့မှာ feof() သုံးလိုက်ရင် file pointer က လညး် file အစမှာ အဲ့တော့ eof လည်းရှိနေတော့ return true ရော။ အကယ်လို့  file ထဲမှာ data ရှိနေရင် file pointer က file အစမှာဆိုတော့ eof က file pointer ရှိနေတဲ့ နေရာမှာ မဟုတ်ဘူးလေ။ ဒီတော့ return false

the better way to check file is empty of not is 

```
char ch = getc(file stream); file ကိုဖွင့်ရင် file pointer က file အစမှာမလို့ ထိပ်ဆုံးက char ကို ယူပေးတာ

if( ch == EOF ) {

printf("File is empty"); 

} else {

printf("file is not empty");

}

```

##### Input functions