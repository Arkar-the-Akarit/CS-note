#cryptography

cryptography ဆိုတာက message တစ်ခုကို cipher (ဝှက်စာလုပ်ခြင်း) & decipher (ဝှက်စာဖော်ခြင်း) အနုပညာတစ်ခု

![[Cryptography.png]]

plain text နဲ့ key တစ်ခုကို ထည့်ပြီး cipher လုပ်လိုက်တဲ့အခါမှာ ciphertext ကိုရရှိလာတယ်။ cipher က ထည့်သွင်းလိုက်တဲ့ key အပေါ်မူတည်ပြီး cipher algorithm ကို ဘယ်လို implement လုပ်ရမလဲ ဆုံးဖြတ်တယ်။
အဲ့တာကို တစ်ဖက်က key ရှိတဲ့လူကဘဲ ပြန်ပြီး decrypt လုပ်နိုင်မယ်။

e.g. 
text - HI!, key - 1 (စာလုံးတွေကိုရှေ့တစ်လုံးစီရွှေ့မယ်) --> IJ! (cipher text)

key to decrypt - (-1) (cipher text ကို နောက်တစ်လုံး)