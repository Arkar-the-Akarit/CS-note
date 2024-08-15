
Data Point လေးတွေ တစ်ခုနဲ့ တစ်ခုကို <span style="color:red;">node</span> လို့သုံးနှုန်းတယ်

##### Single Linked List

![[Images/linked list tree.png]]
- **pointer တစ်ခုတည်းနဲ့** သူ့ရဲ့နောက်ကကောင်ကိုဘဲ ပြန်ထောက်လို့ **single linked list**
- pointer က နောက်က node တစ်ခုလုံးကို ထောက်ထားတာ
- ဒီတော့ နောက်  node ကို ထုတ်ချင်ရင်  ရှေ့ node ရဲ့  pointer ကိုထုတ်လိုက်တာနဲ့ ရ

##### **Declaration of Single Linked List Node**

```

 struct node{

  int data;
  struct node *pointer; / struct node* pointer;
 
 }

```
data နေရာမှာက ကြိုက်တဲ့ data တွေထည့်လို့ရ ၊ struct တစ်ခုလုံးထည့်ထားလို့ရ

node ဆိုတာ နာမည်သဘောပေါ့၊ struct  နဲ့တည်ဆောက်ပြီးရေးထားတာ၊

pointer ကကျ struct တစ်ခုလုံးကိုပြန်ထောက်တာပေါ့။ link လုပ်ဖို့

##### **SLL Initialize လုပ်မယ်**

```
int main(){

struct node *head;
struct node *one = NULL;
struct node *two = NULL;
struct node *three = NULL;

type ကို ကြေညာရုံဘဲ ကြေညာရသေးတာမလို့ memory ပေါ်မှာ နေရာယူပေးရမယ်

one = (struct node*)malloc(sizeof(struct node)) 
two = (struct node*)malloc(sizeof(struct node)) 
three = (struct node*)malloc(sizeof(struct node)) 


}

```

<span style="color:red;"> memory ပေါ်မှာ နေရာယူဖို့ မမေ့နဲ့ </span>

##### SLL Node ရဲ့ ရှေ့က node  မှာ data ထည့်ခြင်း

```
void insertAtBeginning(struct node **head, int newData) {  
  
    struct node *newNode = creatNode(newData);  
    newNode->next = *head;  

    *head = newNode;   <--- ဘာလို့ head ပြောင်းသလဲ
}  
  
int main(){  
  
    struct node* head = NULL;  
  
    insertAtBeginning(&head,100);  
    insertAtBeginning(&head,200);  
    insertAtBeginning(&head,300);  
  
  
  
return 0;  
}


```

- ##### ဘာလို့ insert at beginning မှာ double pointer သုံးတာလဲ

	၁. memory ကိုကိုင်ပြီး အလုပ်လုပ်နေတာမလို့

	double pointer သုံးခြင်းအားဖြင့် main ထဲကနေ 
	 insert_at_beginning(&head) ဆိုပြီး head ရဲ့ address ကြီးကိုထည့်ပေးလိုက်ရော။ အဲ့ insert function  ထဲမှာ ပြောင်းသမျှက main ထဲက head အစစ်အပေါ်သက်ရောက်မှုရှိသွားပြီ။ အဲ့တာ memory ကို ကိုင်ပြီး အလုပ်လုပ်တယ်လို့ ပြောတာ 

	 အကယ်လို့ double pointe မဟုတ်ဘဲ for example , viewAll(struct Node /* head) ဆိုပြီး ရိုးရိုးဘဲဆိုရင် main ကနေ အဲ့ function ကိုခေါ်လိုက်မယ်။ ပြီးရင် head ကိုထည့်ပေးလိုက်မယ်။ viewAll function ထဲမှာ head ကို ကြိုက်သလို ကိုင်တွယ် main ထဲက  head အပေါ်သက်ရောက်မှုမရှိ.. သာမန် pass by value လိုမျိုး copy head value တစ်ခု viewAll ထဲကို ထည့်ပေးလိုက်သလိုဘဲ

**ဘာလို့  head ကိုပြောင်းပေးတာလဲ**

![[Images/head_change.png]]

ss ထဲမှာဆိုရင် red rectangle နဲ့ပြထားတဲ့အပိုင်းက data 300 ရဲ့အပိုင်း
သူ့ရဲ့  next ထဲမှာ 200, 100 တွေရော ရောက်နေပြီ။
ဒါပေမယ့် head အဖြစ် main ထဲမှာ ကြေညာခဲ့တဲ့ node ကိုကြည့်၊ သူ့ထဲက value က 200 ထည့်ထားတုန်းက node အဖြစ်ဘဲရှိနေတုန်း။
ဒါကြောင့် **\*head** = newNode ဆိုပြီး  define လုပ်ပေးလိုက်တာ၊ အဲ့တာဆို ဒီလိုပြောင်းသွားမယ်

![[Images/after_head_change.png]]
ဒီမှာ ကြည့်မယ်ဆိုရင် ဒီ linked list တစ်ခုလုံးကို ထိန်းထားတဲ့ ဟာက **0x5ffe58** ဆိုတဲ့ head ဆိုတဲ့ အပေါ်ဆုံး node ၊ သူ့အောက်မှာမှ data 300, 200, 100 node အစရှိသ◌ဖြင့် အသီးသီး လာတယ်

##### SLL Delete Node

```
void deleteNode(struct node **head, int data) {  
  
    struct node *temp = *head, *prev = NULL;  
  
    if (temp != NULL && temp->data == data) {  
  
        *head = temp->next;  
        free(temp);  
  
        return; // return လုပ်လိုက်ရင် whole function ရပ်သွားပြီ  
    }  
  
    while (temp != NULL && temp->data != data) {  
  
        prev = temp;  
        temp = temp->next;  
    } // တူရင် ရပ်သွားမယ် null ဖြစ်ရင် ရပ်မယ်  
  
    if (temp == NULL)return;  
  
    prev->next = temp->next; // ဖျက်မယ့် node ရဲ့ ရှေ့ node ကို ဖျက်မယ့် node ရဲ့ နောက် node နဲ့ချိတ်  
    free(temp);  
}

```

