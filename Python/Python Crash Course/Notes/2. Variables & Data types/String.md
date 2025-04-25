

###### changing case in string with methods (title())

syntax - <mark style="background: #FFF3A3A6;">title()</mark>
e.g. name.title()

သူက string ထဲမှာ ပါနေတဲ့ words (စကားလုံးတစ်လုံးချင်ဆီရဲ့) အစစာလုံးကို capital letter ပြောင်းပေးတယ်။


###### Tabs or Newlines

tab - \\t
newlines - \\n

e.g. `print("Languages: \n\tPython\n\tC\n\tJavaScript`

###### Stripping Whitespace

syntax - <mark style="background: #FFF3A3A6;">strip()</mark>, <mark style="background: #FFF3A3A6;">lstrip()</mark>, <mark style="background: #FFB86CA6;">rstrip()</mark>

ရိုးရိုးသည် ဘယ်ဘက် နဲ့ ညာဘက်က မှာရှိနေတဲ့ whitespaces ကိုဖြုတ်ပေး
lstrip သည် ဘယ်ဘက် whitespaces
rstrip သည် ညာဘက်။
စာလုံးတွေရဲ့ကြားက whitespacesကိုတော့ မဖြုတ်။

```
text = " i am "

text.strip() # "i am"
text.lstrip() # "i am "
text.rstipr() # " i am"

```

ဒီလို method တစ်ခုကို variable အပေါ်မှာသုံးလည်း original variable က သူရဲ့ မူလတန်ဖိုးအတိုငးဘဲ ကျန်မှာပါ။ သုံးလိုက်လို့ရလာမယ့်ဟာကို သိမ်းထားချင်ရင် variable အသစ် or အဟောင်းကိုဘဲ ပြန်  assign ထပ်လုပ်ပေးရတယ်။

###### Removing Prefixes

prefix (အရှေ့ကစာလုံးတွေ) ကိုဖြုတ်ချပစ်ချင်ရင်

syntax - removeprefix('prefixWords')

```
link = "https://hi.com"

link.removeprefix('https://")  # hi.com

```

Removing Suffixes

suffix (အနောက်က စာလုံးတွေ) ကိုဖြုတ်ချပစ်ချင်ရင်

syntax - removesuffix('suffixWords')

```
file_name = "python_notes.txt"

file_name = file_name.removesuffix('.txt')


```