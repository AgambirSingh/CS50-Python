import emoji #importing emoji modules which has a lot of data on emoji conversion

text=input("Input: ")

#call emoji module then emojize function
#pass text and language function to use alias/nicknames
con_text= emoji.emojize(text , language="alias")

print(con_text)