
##### Strcut

ကိုယ်ပိုင် datatype ကြေညာဖို့အတွက် C မှာ <mark style="background: #FFF3A3A6;">struct</mark> ဆိုတဲ့ structure keywords လေးကိုသုံးလို့ရတယ်။ 

```
struct person{
	 string name;
	 string number;
}
```

ဒီလိုဆိုရင် custom data type တစ်ခုတည်ဆောက်ပြီးပြီ

custom data type ဖြစ်တဲ့အတွက် variable ကိုကြေညာချင်ရင် 
```
struct person p;
```
ဆိုပြီး အရှေ့က struct keyword ကိုပါ လိုက်ပြီး ကြေညာပြီးခေါ်သုံးရတယ်။

ကိုယ်ပိုင် custom datatype structure ကိုခေါ်သုံးချင်ရင် အရှေ့က struct ကို အမြဲသုံးနေရတယ်။ အဲ့လိုမဖြစ်အောင်

##### Typedef

<mark style="background: #FFF3A3A6;">typedef</mark> ဆိုတာက existing data type တစ်ခုကို new name (alias) ပေးဖို့သုံးတာဖြစ်တယ်။

```
typedef int height;
height h = 30;  // Equal to int h = 30

typedef int intArray[10];
intArray arr;  // Equalivent to int arr[10]

```

အသုံးများတာကတော့ array, pointers, function pointers တွေကို alias ပေးပြီး clean ဖြစ်ဖြစ်နဲ့ easily manage လုပ်လို့ရအောင်သုံးတာဖြစ်တယ်။

#### Typedef Struct

structure တစ်ခုကိုခေါ်သုံးတိုင် struct ဆိုတာကို‌ ကြေညာနေဖို့မလိုအောင်
```
typedef struct {

 string name;
 string number;
 
} person;

```
ဆိုပြီး တွဲသုံးကြတယ်။ အပေါ်က code မှာဆိုရင် typedef နဲ့ structure အတွက် alias တစ်ခုဖန်တီးလိုက်တာဖြစ်တဲ့အတွက် custom datatype variable တွေကို အလွယ်ဖန်တီးလို့ရသွားတယ်။

```
person p; // declare only one variable name 'p'

person p[3]; // array for custom data type
```

p ဆိုတာက person ဆိုတဲ့ custom data type အတွက် variable ဖြစ်ပြီး
person ထဲက data တွေကို access လုပ်မယ်ဆိုရင် <mark  style="background: #ABF7F7A6;">period (.)</mark> ကိုသုံးပြီး access လုပ်နိုင်တယ်။

```
p.name
p.number 

// If declare as array

p[0].name
p[0].number

p[1].name
p[1].number

```