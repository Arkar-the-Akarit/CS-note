
Stack ဆိုတာ data တွေကို ပန်းကန်ပြားချပ်တွေထပ်ထားသလို အပေါ်အောက် စီထားတာမျိုး

![[Images/stack_example.png]]

ဒီတော့ သူက သူ့ထဲကို အရင်ထည့်လိုက်တဲ့ data က အသစ်တွေထပ် ဝင်လာလေလေ အောက်ကို ရောက်လေ

data တွေပြန်ထုတ်မယ်ဆိုရင် အပေါ်ဆုံးက ကောင်ကို အရင်ပြန်ထုတ်ရတယ်။ ဒီတော့ နောက်ဆုံးဝင်တဲ့ကောင်က အရင် ထွက်ရမယ်
ဒါကြောင့် stack ကို ပြောကြတာက 

Last <span style=" color: cyan; ">in </span>First<span style=" color: red; "> out</span>

အရင်ဆုံးဝင်တဲ့ကောင်သည် **နောက်ဆုံးကျမှ** ထွက်မယ်

First <span style=" color: cyan; ">in </span>Last<span style=" color: red; "> out</span>

Stack data structure တည်ဆောက်ရင်

1. Array
2. Linked List
ကို သုံးပြီး တည်ဆောက်လို့ရတယ်။ အခုကတော့ Array ကို သုံးထားတယ်။


###### Basic Operations in Stack

Stack မှာ ပုံမှန်အားဖြင့် အသုံးပြုတဲ့ operations သုံးခုက

<span style=" color: cyan ; ">push</span> = data ထည့်
<span style=" color: cyan ; ">pop</span> = data ထုတ်
<span style=" color: cyan ; ">peek</span> = ထိပ်ဆုံး data ကို ထုတ်ကြည့်


###### Initialization of Stack

![[Images/stack_arr_initialization.png]]

###### Push Operation

![[stack_arr_push.png]]
```
int isFull(struct Stack *stack){  
  
    return(stack->top == MAX_SIZE-1);  
  
    /*  
     The max size is 10, the top is also used to check the current index of items array.     the indexes of items array are ranged from 0 to 9, total of 10 room.     if the top is 9, the current index of items array will be items[9], the last room.  
     writing return (..) is like, if it is true, return 1, else return 0;     */  
}  
  
void push(struct Stack *stack, int value){  
  
    if(isFull(stack)){  
        printf("Stack overflow\n");  
    } else {  
  
        stack->items[++stack->top] = value;  
  
        /*  
  
         writing only one sentence that is the same as  
         stack->top ++; cz current top is -1, after ++ it becomes zero;         stack->items[stack->top (which is zero)] == value.  
         ++stack->top means that before utilizing the top as the index of items array, we will first         increase the value of top,  
         if we write like stack->items[stack->top++] , then the we will first use the current value of         top for index of items, only then will increase the value of top.  
  
          */  
    }  
  
  
}


```


###### Pop Operation

![[Images/stack_arr_pop.png]]

stack သဘောတရားအရ data ထုတ်ရင် နောက်ဆုံး ဝင်တဲ့ကောင် အရင်ထွက်ရမှာ ဖြစ်လို့ ထုတ်မယ့် data  ကို ထည့်ရေးပေးစရာမလို။ ထုတ်မယ်ဆိုတာနဲ့ ထိပ်ဆုံးကကောင်ကို ထုတ်မယ်ဆိုတာ သိရမယ်

###### Peek Operation

![[Images/stack_arr_peek.png]]