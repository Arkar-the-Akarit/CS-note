
1.  website name **(domain name)** ကို user က browser မှာ input ထည့်လိုက်တယ်

	 e.g: google.com/ blah blah ==> / နောက်ကစာတွေကို **path** လို့ခေါ်တယ်
		domain name နဲ့ path နှစ်ခုပေါင်းကို ==> uniform resource locater (URL) လို့ခေါ်

2. when browser call google.com, it uses **IP Address (internet protocol)** to call
	firstly it goes to **DNS Server**, which stores Domain Name and IP address **of the websites. 
	
3. So when browser request with **Domain name of the website , DNS sever sends back  **IP address**. 

4. then the browser uses that **IP address** to call the server where the website is hosted, by using HTTP ( Hyper Text Transfer Protocol ).  We can say that is **requesting** to the browser

5. When the server knows our request, it **response back** with data. In the data includes like "**Content = "HTML/text**", meaning the response comes as text in html form. The browser translate that and show the browser content.
![[how browsing works.png]]

ဒီတော့ browser တစ်ခု အကြမ်းဖျင်းဘယ်လို အလုပ်လုပ်လဲ သိပြီဆိုရင် 

[[Beginning of HTML]] အစလေးအနည်းငယ်နဲ့ [[Html Elements]] တွေကို ကြည့်လို့ရပါပြီ