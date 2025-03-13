
##### Creating data type with names - Type Casting

**Type Casting** - ထည့်လိုက်တဲ့တန်ဖိုးပေါ်မူတည်ပြီး data type အမျိုးအစားပြောင်းပေးတာ

1. str 
	`str('apple')`
	`str()` <-- function call for empty string
	

2. int
	`int()` <- empty, function call, return value 0
	`int(10)`
	စာတန်ဖိုးတွေထည့်ပြီး value in string (e.g. '1000') or ဒသမကိန်း တွေကိုလည်း int() ထဲထည့်ပြီး typecast လုပ်လို့ရ
	
	<mark style="background: #ABF7F7A6;">int(x,base)</mark>
	convert x to integer, base specifics the base if <mark style="background: #FFB86CA6;">x is string</mark>
 
 3. float
	`float()` <- return value 0.0
	`float("1000")` <- 1000.0

4. complex
	`complex()` <- empty complex, function call, return 0j
	`complex(3)` <- 3j
	
	complex ကိန်းတွဲဖန်တီးချင်ရင် real part နဲ့ imaginary part ဆိုပြီး နှစ်ခုထည့်ရတယ်
	`complex(3, 2)` <- (3 + 2j)

5. list
	`list()` <- return \[] ,i.e. empty list
	`list(["apple", "banana"])` <- \["apples", "banan"]
	
	typecast `list((1,2,3))` <- inside () is "tuple", type-casted to list

6. tuple
	`tuple()` <- return ()
	`tuple((1,2,3))` <- (1,2,3)

7. range
	`range(2,5)` <- output is range(2,5), if want num, loop
	
	`list(range(1,100)` ဆိုရင် 1 - 99 ရှိတဲ့ list တစ်ခုထုတ်ပေးမယ်

8. dict
	`dict()` <- return {}
	`dict({key:value, key2:value2})` -> {key:value, key2:value2}
	
	`dict(name="abc")` -> {'name' : 'abc' }
	
	<mark style="background: #FFF3A3A6;">တန်ဖိုးနှစ်ခုတွဲရှိတဲ့</mark> nested list or nested tuple တို့ကို<mark style="background: #FFB86CA6;"> dict အဖြစ်ပြောင်းလို့ရ</mark>
	`dict([['name','Arkar'], ['age',22],['sex','male'])`
	output -> {'name' : 'Arkar', 'age' : 22, 'sex' : 'male' }

9. set
	`set()` -> output set(), dict နဲ့မရောအောင် empty set ကို တွန့်ကွင်းသီးသန့် မပြ
	
	`set({1,2,3})` -> {1,2,3}
	`set([1,2,3])` -> {1,2,3} tuple to list, typecast
	
	`set({'name':'mg mg', 'age': 22})` -> {22,"mg mg"} not in input order
	

10. frozenset
	 `frozenset()` -> frozenset()
	
	`frozenset({1,2,3})` -> frozenset({1,2,3})
	
	`frozenset([1,2,3])` -> frozentset({1,2,3})
	
	dict ကို frozen set ထဲထည့်လိုက်ရင် key တွေကိုဘဲ set အဖြစ်ပြန်ထုတ်ပေးတယ်
	`dict({"name":"mg mg", "age" : 22, "height" : 5.5})` -> frozenset({"name", "age", "height"})

11. bool
	`bool()` -> default value : <mark style="background: #FFF3A3A6;">False</mark>
	`bool(0)` -> false
	
	empty string, empty list, empty set တန်ဖိုးအလွတ်တွေဆို false အဖြစ်ပြောင်းပေးတယ်
	
	empty or 0 မဟုတ်တဲ့ value မှန်သမျှကို typecast လုပ်ရင် ထွက်လာမှာက true

12. bytes
	`bytes()` -> output b''
	`bytes(5)` -> b'\x00\x00\x00\x00' bytes 5 ခုဖန်တီးပေး

13. bytearray
	`bytearray()` -> bytearray(b'')

14. memoryview()
	ထည့်ပေးလိုက်တဲ့ data ရဲ့ memory address ကို ကြည့်လို့ရအောင်လုပ်ပေးတယ်။ အလွတ်သုံးမရ၊ data တစ်ခုခုထည့်ပေးရတယ်

##### typecasting

type casting (2) မျိုးရှိ - explicit type casting, implicit type casting

###### 1. Explicit type casting

programmer က ကိုယ်တိုင် ဒါကို ဒါပြောင်းဆိုပြီး type cast လုပ်တာမျိုး။ Direct typecasting

အခြား string တွေကတော့ ပြဿနာမရှိပေမယ့် ဂဏန်းတွေကို ပြောင်းပြီဆိုရင် 

	1. truncate, int
	       -> 1 + int(1.6) ---> 1 + 1 = 2
	       
	2. round
		 -> 1 + round(1.6) --> 1 + 2 = 3
		 
	3. float to int
		 -> float (1) + 1.6 = 1.0 + 1.6 = 2.6

\2. Implicit typeCasting 

indirect type casting

python က သူ့ဘာသာ type cast လုပ်ပေးတာမျိုးဖြစ်တယ်။ အပေါ်က explicit type casting မှာဆိုရင် လိုချင်တဲ့ အဖြေအတိအကျရဖို့ int ကို float အဖြစ်သတ်မှတ်ပြီး ပေါင်းမှ အတိအကျရတယ်။ 

ဒါပေမယ့် python မှာက implicit type casting နဲ့ အလိုအလျောက်ပြောင်းပြီး ပေါင်းပေးတဲ့အတွက်
`1 + 1.6` 
ဆိုရင် data type မတူတောင် ပြောငး်ပြီး ပေါင်းပေးတယ်
အဲ့တာက float အတွက်

implicit type casting for <mark style="background: #FFF3A3A6;">boolean</mark>

<mark style="background: #BBFABBA6;">True Result</mark>
int, float --> not zero
group --> str, list, tuple, dict, set.. -> not empty

<mark style="background: #FF5582A6;">False Result</mark>
zero, empty


##### Check Datatype - type()

data type အမျိုးအစားကိုစစ်ချင်ရင် type() ဆိုတဲ့ function ကိုသုံးလို့ရ

`type(0j)` -> \< class complex >

