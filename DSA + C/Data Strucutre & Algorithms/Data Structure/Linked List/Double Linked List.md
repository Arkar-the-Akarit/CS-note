
Check [[Single Linked List Tree]] first


![[Images/doubleLinkedList.png]]

##### Node Create လုပ်ခြင်း

```
struct Node *createNode(int newData) {  
  
    struct Node *newNode = (struct Node *) malloc(sizeof(struct Node));  
    newNode->data = newData;  
    newNode->prev = NULL;  
    newNode->next = NULL;  
  
    return newNode;  
}


```

##### ရှေ့ဆုံး node ရှေ့ မှာ Data ထည့်

```
void insertAtBeginning(struct Node **head, int data) {  
  
    struct Node *newNode = createNode(data);  
    newNode->next = *head;  
    newNode->data = data;  
  
    if (*head != NULL) {  
  
        (*head)->prev = newNode; // အပြန်အလှန် ချိတ်ဆက်  
  
    }  
  
    *head = newNode; // <---- မမေ့နဲ့ 
}


```
##### နောက်ဆုံးမှာ data ထည့်

```
void append(struct Node** head,int data){  
  
    struct Node* last = *head;  
  
    struct Node* newNode = createNode(data);  
  
   if ( *head == NULL){  
       *head = newNode;  
       return;  
   }  
  
    while(last->next != NULL){  
       last = last->next;  
    }  
  
    last->next = newNode;   // အပြန်အလှန်ချိတ်ဆက်  
    newNode->prev = last;  
      
}


```
