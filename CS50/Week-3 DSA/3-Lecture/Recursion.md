#C #RecursiveFunction

A function that calls itself is recursive

function တစ်ခုက သူ့ထဲမှာ သူ့ကိုယ်သူ ပြန်ခေါ်သုံးတာမျိုးကို recursive function လို့ခေါ်တယ်။

##### Binary Search Example

 [[Binary Search]] ဆိုရင်လည်း သူ့ထဲမှာ left side ကိုရှာပါ။ right side ကိုရှာပါဆိုပြီး ပါတယ်။ အဲ့ရှာတဲ့အပိုင်းတွေက တကယ်တမ်းကျ recursive concept နဲ့သွားတာဘဲ။

#### Right-aligned Pyramid

```
   #include <cs50.h>
   #include <stdio.h>

   void draw(int n);

   int main(void)
   {
     int n = get_height("Height: ");
   
     draw(height);
   }

   void draw(height)
   {

	// if nothing left to print
    if(n <=0 )
    {
	 return;
	}

	// Print n-1
     draw(n-1);

	 for(int i =0 ; i < n; i++)
	 {
		 printf("#");
	 }

	printf("\n");
   }

```

nested for loop မသုံးဘဲ recursive နဲ့ right-aligned pyramid တစ်ခု လုပ်ထားတယ်။

သူ့အလုပ်လုပ်ပုံက 
- user က height တစ်ခုထည့်လိုက်မယ်။ let's say 4, draw(4)
- 0 ဟုတ်မဟုတ် စစ်မယ်။ မဟုတ်တဲ့အတွက် -1 လုပ်ပြီး recursive နဲ့ draw ကို ပြန်ခေါ်တယ်။ အခုက draw(3) ဖြစ်သွားပြီ
- အဲ့လိုနဲ့ draw(2) -->  draw(1) --> draw(0) ထိရောက်လာမယ်။
- 0 ရောက်ပြီဆိုတော့ function က return နဲ့ close လိုက်ပြီ 
- ဒီတော့ draw(1) ဆီကို ပြန်ရောက်လာတယ်။ recursive ခေါ်ထားတာကနေ ပြန်လာပြီး သူ့အောက်က for loop ကို run တယ်။ 
- အောက်ဆုံးထိ run ပြီးသွားတော့ draw(1) ကနေထွက် draw(2) ကို ပြန်ရောက်လာပြီး recursive ကထွက်လာပြီဖြစ်တဲ့အတွက် အောက်က for loop ကို ဆက် run တယ်။ အဲ့လိုနဲ့ နောက်ဆုံး draw(4) ထိပြန်ထွက်လာပြီးတော့မှာ # လေးခု print ထုတ်ပေးပြီး function ပြီးတယ်.

<mark style="background: #BBFABBA6;">draw(4)</mark> --> <mark style="background: #BBFABBA6;">draw(3)</mark> --> <mark style="background: #BBFABBA6;">draw(2)</mark> --> <mark style="background: #BBFABBA6;">draw(1)</mark> --> <mark style="background: #BBFABBA6;">draw(0)</mark>

at draw(0), it returns as n <= 0

<mark style="background: #BBFABBA6;">draw(0)</mark> - nothing --> <mark style="background: #BBFABBA6;">draw(1)</mark> - run code under recursive, print one hash, return --> <mark style="background: #BBFABBA6;">draw (2)</mark> - run code after recursive, print two hash, return --> <mark style="background: #BBFABBA6;">draw(3)</mark> - ... print 3 hash ... --> <mark style="background: #BBFABBA6;">draw(4)</mark> ... print 4 hash ... 