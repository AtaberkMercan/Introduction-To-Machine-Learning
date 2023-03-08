#!/usr/bin/env python
# coding: utf-8

# In[3]:


var1 = 34
var2 = 36
day = "Monday"
var3 = 13.6


# In[4]:


list_int = [1,2,3,4,5]
type(list_int)


# In[5]:


value = list_int[3]
print(value)


# In[6]:


value


# In[7]:


list_int[-1]


# In[8]:


list_int[0:3]


# In[9]:


dir(list_int)


# In[10]:


list_int.append(7)
print(list_int)


# In[11]:


list_int.remove(7)
print(list_int)


# In[12]:


list_int.reverse()
print(list_int)


# In[13]:


list_int.sort()
print(list_int)


# In[14]:


for each in range(1,11):
    print(each)


# In[15]:


liste = [1,2,3,4,6,8,9,7]
sum(liste)
min(liste)


# In[16]:


minimum = 10000
for each in liste:
    if(each<minimum):
        minimum = each
    else:
        continue
print(minimum)


# In[17]:


i = 0

while (i < 4):
    print(i)
    i= i+1


# In[18]:


def cember_cevre(r,pi=3.14):
    
    
    """
    Çember Çevresi 
    
    """
    output = 2*pi*r
    
    return output

cember_cevre(6)


# In[19]:


def hesapla(x):
    output = x*x
    return output


# In[20]:


sonuc = lambda x: x*x
print(sonuc(4))


# In[21]:


dictionary = {"ATABERK":23, "MEHMET": 25,"MURAT":24}

dictionary["ATABERK"]


# In[22]:


dictionary.keys()


# In[23]:


def deneme():
    dictionary = {"ATABERK":23, "MEHMET": 25,"MURAT":24}
    
    return dictionary

dic = deneme()
print(dic)


# In[25]:


keys = dictionary.keys()

if "ATABERK" in keys:
    print("Yes")
else:
    print("No")


# In[ ]:




