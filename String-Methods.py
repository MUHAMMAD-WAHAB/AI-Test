#!/usr/bin/env python
# coding: utf-8

# In[7]:


txt = "this is my first assignment"
a= txt.capitalize()
print (a)



# In[9]:


txt = "This is my first Assignment"
a= txt.casefold()
print (a)


# In[12]:


txt = "Assignment"
a= txt.center(40)
print (a)



# In[16]:


txt = "I love AI course, AI course is my most favourite course"
a=txt.count("AI")
print (a)


# In[34]:


txt = "My name is wahab "
a=txt.encode()
print (a)


# In[24]:


txt = "What is the AI assignemnt for batch 3 islamabad?"

a= txt.endswith("?")
print (a)

txt = "What is the AI assignemnt for batch 3 islamabad?"

b= txt.endswith(".")
print (b)


# In[33]:


txt = "w\ta\th\ta\tb"

a =  txt.expandtabs(4)

print(a)


# In[28]:


txt = "What is the AI assignemnt for batch 3 islamabad?"
a= txt.find ("batch")
print (a)


# In[32]:


txt = "AI course is only for  {price:} rupees"
print(txt.format(price = 12000))


# In[1]:


txt = "This is my first Assignment"

a = txt.index("Assignment")

print(a)


# In[2]:


txt = "AI Batch 3 Islamabad"

a = txt.isalnum()

print(a)


# In[3]:


txt = "A1 for everyone"

a = txt.isalpha()

print(a)


# In[1]:


txt = "\u1234"

x = txt.isdecimal()

print(x)


# In[2]:


txt = "123456"

x = txt.isdigit()

print(x)


# In[35]:


txt = "My Name is WAHAB!"

x = txt.islower()

print(x)


# In[4]:


txt = "123A!"

x = txt.isnumeric()

print(x)


# In[8]:


txt = "What is the first assignment of AI?"

x = txt.isprintable()

print(x)


# In[10]:


txt = "   "

x = txt.isspace()

print(x)

txt = ""

a = txt.isspace()

print(a)


# In[36]:


txt = "My name is wahab arshad"

x = txt.istitle()

print(x)


# In[12]:


txt = "This is My First Assignment"

x = txt.isupper()

print(x)


# In[14]:


txt = "AI is the best course i have ever enrolled"

x = txt.partition("course")

print(x)


# In[15]:


txt = "I like AI course"

x = txt.replace("course", "classes")

print(x)


# In[37]:


txt = "My name is wahab arshad"

x = txt.rfind("hab")

print(x)


# In[23]:


txt = "welcome to the PIAIC BATCH 3"

x = txt.split()

print(x)


# In[25]:


txt = "welcome to the\n PIAIC BATCH 3"

x = txt.splitlines()

print(x)


# In[38]:


txt = "My Name is wahab arshad"

x = txt.startswith("wahab")

print(x)


# In[29]:


txt = "     AI     "

x = txt.strip()

print(x, "is my best course", "i have ever enrolled")


# In[39]:


txt = "Hello My Name Is wahab arshad"

x = txt.swapcase()

print(x)


# In[31]:


txt = "Welcome to PIAIC Batch 3 class"

x = txt.title()

print(x)


# In[40]:


txt = "My name is Wahab"

x = txt.upper()

print(x)


# In[ ]:




