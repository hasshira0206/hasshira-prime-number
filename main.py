import streamlit as st
st.title("自然数を2つの素数の和で表す君")
while True:
  n=st.slider("お好きな自然数を入力",5,10000)
  n1=n
  n2=n
  n//=2
  y=0
  a=0
  while y<n:
    y+=1
    x=n1-y
    flag=True #Trueなら素数である
    for i in range(2,y):
      if y%i==0:
        flag=False #素数である
        break
    if flag==True:
      flag=True #Trueなら素数である
      for i in range(2,x):
        if x%i==0:
          flag=False #素数である
          a+=1
          break
    if x!=1:
      if y!=1:
        if flag:
            kotae=("[{}]＋[{}]ですねぇ".format(x,y))
  if st.checkbox("結果を本当に見ちゃう？？？？"):
      st.write(kotae)
