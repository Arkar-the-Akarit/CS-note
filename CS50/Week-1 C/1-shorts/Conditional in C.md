#C #C-conditional

###### if statement

if (boolean-expression)
{
 statement;
}

အကယ်လို့ boolean-expression က true ဆို အောက်က code ကို run,

if - else ကျ if ထဲက boolean expression က false ဆို else ထဲကိုသွား

if - else if - else if ဆိုပြီး အများကြီးသုံးလို့ရ


###### switch statement

```
int x = get_int(); 

switch(x)
{
 case 1:
    ....
    break;

 case 2:
	 ....
	 break;

 case 3: 
	 ....
	 break;

 default:
	 ....

}

```

switch statement ဆိုတာက boolean expression အပေါ်နဲ့ မဟုတ်ဘဲ ဂဏန်းတွေနဲ့ မတူညီတဲ့ case တွေကို လုပ်ဆောင်ပေးနိုင်တဲ့ statement as shown above code

case တစ်ခုနဲ့ တစ်ခုကြားမှာ <span style="color:rgb(0, 176, 240)">break လုပ်ထား</span>ပေးဖို့ လိုတယ်။ 

မလုပ်ထားဘူးဆိုရင် အပေါ်က code လိုပုံစံမျိုးမှာဆိုရင် ကိုယ်က 1 ‌ထည့်လိုက်လညး် အောက်က 2,3,4 default အထိ အကုန် run
2 ထည့်လိုက်ရင် 3,4 default ထိ run

အဲ့လို ကိုယ်ရွေးလိုက်တဲ့ case ကနေ အောက်ထိ fall off ဖြစ်သလို run သွားမှာ။ အဲ့လိုဖြစ်စေချင်ရင်တော့ မထည့်ဘဲ သုံးလို့ရ