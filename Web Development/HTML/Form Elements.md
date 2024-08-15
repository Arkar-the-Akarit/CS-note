
```
<form> </form>
```
html မှာ form ကို wrap အုပ် ပြီးရေးရတယ်။ form element က အခြားသော form control inputs တွေကို wrap လုပ်ထားတာကို ပြောတာ။

form element မှာ **‌action** ဆိုတဲ့ attribute ပါရတယ်။ ဘယ်ဖောင်ကိုဖြည့်နေတာလဲ၊ ဒီဖောင်က ဘာအတွက်လဲဆိုတဲ့ ရည်ရွယ်ချက်မျိုး။ action attribute မပါရင် form ကို submit လိုက်ရင် လက်ရှိ page ကိုဘဲ ပြန်ခေါ်သွားမယ်

###### Attribute of form element

action = သူက ဒီဖောင်က ဘာအတွက်၊ ဘယ်ကိုသွားရမယ်ဆိုတဲ့ url or server side script ိကို ဦးတည်ရာ အနေနဲ့ ထည့်ပေးရတယ်

method = valueတွေက အများအားဖြင့် 'get' method နဲ့ 'post' method။ server ဆီက 
<mark style="background: #ADCCFFA6;">data လှမ်းယူရင် get</mark>၊ 

data ပြန်ပို့ပြီး <mark style="background: #ABF7F7A6;">တစ်ခုခုလုပ်စေချင်ရင် post</mark>
( e.g. login from ဖြည့်, submit လုပ်လိုက်တယ်ဆိုရင် serverဘက်ကနေ login ဝင်ဖို့ ခွင့်ပေးစေချင်တာမျိုး ..... post method)

###### Form အလုပ်လုပ်ပုံများ

![[how form works.png]]

form ထဲမှာ name က **အရေးကြီး**တယ်။ submit လုပ်လိုက်ပြီဆိုရင် element တွေရဲ့ name နဲ့ user input လုပ်လိုက်တဲ့ data ကိုသယ်ပြီး serverဘက်ကို ပို့ပေးတာ။  
e.g. username ကို input type="text" name="userName" နဲ့ ယူထားပြီး user ဖြည့်လိုက်တဲ့ နာမည်က Arkar Phyo ဆိုရင် server ဆီကို ပို့တဲ့အချိန်မှာ userName: ArkarPhyo လို့ပို့တာ


#### form controls elements များ

##### Text Input

< input   / > element က <mark style="background: #FFB8EBA6;">self-closing tag</mark> ပါ

user တွေက keyboard ကနေ စာတစ်ကြောင်း ရိုက်ထည့်လို့ရမယ်။ < input > element ကိုသုံး။ 

attribute "type" နဲ့ user ရိုက်ထည့်လို့ရမယ့် အခြေအနေကို သတ်မှတ်ပေးလို့ရတယ်။

< label > element ကို input ကို focus လုပ်ဖို့၊ Label ကို ခေါင်းစဥ်ပေးဖို့ သုံးတယ်
< label > ရဲ့  attribute "for" က input element ရဲ့ ==**id**== ကို ညွှန်းပေးရတယ်။ အဲ့ for 
ကိုသုံးထားရင် user က label ကို click လိုက်ရင် သက်ဆိုင်ရာ input field ကို ညွှန်းပေးတယ်။ enhance user experience

input ရဲ့ attribute "type" ရဲ့  valueများ
- text
- password
- email
- number
- tel
- date

attribute "name" = server ကို action process ပို့ဖို့
attribute "id" = label ကိုညွှန်းတာတို့ ၊ JS နဲ့ element manipulate လုပ်တာတို့အတွက်။ must be unique

attribute "required" = မထည့်မနေရမထည့်မနေရ

attribute "placeholder" = input field ထဲမှာ စာကို grey နဲ့ပြပြီး user ကို ဘာထည့်ရမယ်သိအောင် ကူညီပေးတာ

attribute "value" = ကြိုပြီး input field ထဲမှာ စာတစ်ခုခုထည့်တာမျိုး၊ submit တို့ reset တို့လို button တွေဆိုရင် ပြမယ့် စာကို လိုသလိုထား


![[label and input element.png]]

input attribute "type" ရဲ့ button ပုံစံ valueများ
- submit = form submit
- reset = for clearing the form


input attribute "type" ရဲ့ selector form control value များ

- checkbox = <mark style="background: #ADCCFFA6;">တစ်ခုထက်ပိုပြီး</mark>‌ေရွးချယ်လို့ရတာတွေ အတွက်
- radio = <mark style="background: #FFF3A3A6;">တစ်ခုပဲ</mark> ‌ရွေးချယ်တဲ့အခါမှာသုံး

##### Radio Button

တစ်ခုပဲ ‌ေရွးချယ်ရတဲ့အခါမှာသုံးတယ်

type="radio" ဆိုရင် ကိုယ်‌ေရွးချယ်မှုပေးချင်တဲ့ အရာတွေအကုန်လုံးရဲ့ <mark style="background: #FF5582A6;">attribute "name" မှာ value</mark> တွေက တူနေရမယ်။

<mark style="background: #FF5582A6;">attribute "value" လည်း ကြိုတင်သတ်မှတ်</mark>ပေးရမယ်။

form ကို server ဆီကို ပို့ပြီဆိုရင် value တစ်ခုကတော့ ပါရစမြဲ။ ဟုတ်တယ်ဟုတ်။
ဒါပေမယ့် radio ကျ group သဘောမျိုး။ user ဆီမှာ ပြတဲ့ စာက value ကိုသတ်မှတ်ပေးတာမဟုတ်သေးဘူး။ user ကြည့်လို့ရအောင် ထည့်ထားတဲ့သဘောမျိုးဘဲ။ ဒီတော့ server ကို လှမ်းပို့တဲ့အချိန်ကျရင် value ကို သိနေအောင် < input >မှာကတည်းက <mark style="background: #FFB86CA6;">radio သုံးရင်</mark> <mark style="background: #ADCCFFA6;">value တစ်ခါတည်း ထည့်ပေး</mark>ဖို့လိုတယ်။


radio & checkboxမှာ user မ‌ရွေးခင် value တစ်ခုကို ကြို‌‌ရွေးပေးထားချင်တယ်ဆိုရင် <mark style="background: #FFF3A3A6;">‌attribute checked
</mark> ကို ကိုယ်‌ရွေးပေးထားစေချင်တဲ့ content မှာ ထည့်ထားပေးလို့ရတယ်။

dropdownမှာတော့ child element - option ထဲမှာ <mark style="background: #FFF3A3A6;">attribute selected </mark>နဲ့ ရွေးထားပေးလို့ရတယ်
```
<input type="radio" name="gender" value="male" id="male"/>
<label for="male"> Male </label>

<input type="radio" name="gender" value="female" id="female"/>
<label for"female"> Female </label>

```

##### Checkbox 

<mark style="background: #FFF3A3A6;">တစ်ခုထက်ပိုပြီး</mark> ‌ရွေးချယ်စေချင်ရင်သုံး

<mark style="background: #FFB8EBA6;">attribute "name"</mark> တွေရဲ့ value က <mark style="background: #BBFABBA6;">တူ</mark>ရမယ်

<mark style="background: #FFB8EBA6;">attribute "value"</mark> တွေ <mark style="background: #BBFABBA6;">ကြိုတင်သတ်မှတ်</mark> ပေးထားရမယ်

```
<input type="checkbox" name="language" value="en" id="en" />
<label for="en"> English </label>

<input type="checkbox" name="language" value="cn" id="cn" />
<lable for="cn"> Chinese </label>

<input type="checkbox" name="language" value="my" id="my" />
<label for="my"> Myanmar </label>



```
radio & checkboxမှာ user မ‌ရွေးခင် value တစ်ခုကို ကြို‌‌ရွေးပေးထားချင်တယ်ဆိုရင် <mark style="background: #FFF3A3A6;">‌attribute checked
</mark> ကို ကိုယ်‌ရွေးပေးထားစေချင်တဲ့ content မှာ ထည့်ထားပေးလို့ရတယ်။

dropdownမှာတော့ child element - option ထဲမှာ <mark style="background: #FFF3A3A6;">attribute selected </mark>နဲ့ ရွေးထားပေးလို့ရတယ်
##### Dropdown selector

Checkbox နဲ့ Radio က input element ရဲ့ attribute "type" နဲ့ သွားပေမယ့် dropdown selector ကတော့ <mark style="background: #BBFABBA6;"> element ( select ) ရယ် သူ့ရဲ့ child element ( option )  </mark> ရယ်နဲ့ သုံးရတယ်။

element < select > မှာ form control တွေရဲ့ သဘောတရားအတိုင်း <mark style="background: #FF5582A6;">‌‌attribute name</mark> ပါမယ်။ child element < option > မှာက<mark style="background: #FF5582A6;"> ‌attribute value</mark> ပါမယ်။

user တွေက <mark style="background: #FF5582A6;">option မှာ ပြထားတဲ့ content </mark>တွေကို မြင်ရမယ်

```

<select name="favColor">

<option value="red" > Red </option>
<option value="green"> Green </option>
<option value="violet"> Violet </option>


</select>

```
radio & checkboxမှာ user မ‌ရွေးခင် value တစ်ခုကို ကြို‌‌ရွေးပေးထားချင်တယ်ဆိုရင် <mark style="background: #FFF3A3A6;">‌attribute checked
</mark> ကို ကိုယ်‌ရွေးပေးထားစေချင်တဲ့ content မှာ ထည့်ထားပေးလို့ရတယ်။

dropdownမှာတော့ child element - option ထဲမှာ <mark style="background: #FFF3A3A6;">attribute selected </mark>နဲ့ ရွေးထားပေးလို့ရတယ်
##### Multiline input

< textarea > element ကတော့ user ကို multi-line text တွေ ရိုက်ထည့်စေချင်ရင်သုံး။

< textarea> </ textarea> သူက <mark style="background: #FF5582A6;">closing tag </mark>ပါပါတယ်။

##### Form submit element

form ကို submit လုပ်တဲ့ < input > element

type = submit နဲ့ သုံးတယ်
user ဘက်မှာ submit နဲ့ မပေါ်စေချင်ရင် attribute value နဲ့ ပေါ်စေချင်တာကို ရေးပေးလိုက်လို့ရတယ်။

```
<input type="submit" value="Submit Here" />
```

submit အတွက် element  button ကို သုံးပြီး ဒီလိုရေးလို့လည်းရတယ်

```
<button type="submit"> Submit </button>

mostly used ---> < button type="button"> ... </button>

```

ဒါပေမယ့် element button ရဲ့ type မှာ submit ထက် <mark style="background: #FF5582A6;">button ကို ပိုအသုံးများ</mark>တယ်။ 

##### Form Upload Element

file တွေကို upload လုပ်လို့ရတဲ့ form controls element

element < input > ကိုသုံးပြီး <mark style="background: #FFF3A3A6;">attribute type ရဲ့ value ကို file</mark> လို့ပေးရင်ရပြီ။

ဒါပေမယ့် form ကို <mark style="background: #ADCCFFA6;">encoding system ပြောင်</mark>းပေးရမယ်။ ဒါ‌ကြောင့် <mark style="background: #FF5582A6;">element form </mark>မှာ <mark style="background: #ABF7F7A6;">attribute enctype = "multipart/form-data"</mark> ဆိုတဲ့ attribute & value ထည့်ပေးရမယ်။

![[accepting file in form.png]]

file input မှာ ဘယ်လို file မျိုးဘဲ upload လုပ်လို့ရမယ်ဆိုတာ သတ်မှတ်ပေးဖို့အတွက်က 
element input မှာ 

```
<input type="file" accept="image/*"
```

ဆိုပြီး ထည့်ပေးလို့ရတယ်။ image ကတော့ ပုံဘဲ လက်ခံမယ်ပြောတာ။ Asterisk ( * ) ကြယ်လေးကတော့ Image file type အကုန်လက်ခံမယ်လို့ပြောတာ