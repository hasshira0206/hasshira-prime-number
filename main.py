import streamlit as st
import time
st.sidebar.title("はっしら数学同好会")
st.sidebar.write("好きな制作物を選択してください")
if st.sidebar.checkbox("自然数を2つの素数の和で表す君"):
  st.title("自然数(偶数)を2つの素数の和で表す君")
  n=st.slider("お好きな自然数を入力（偶数で）",5,10000)
  if n%2!=0:
    n+=1
    st.write("あなたが入力したのは奇数です！！失望しました！偶数にしますよ！")
  def prime(n):
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
              return "[{}]＋[{}]ですねぇ".format(x,y)
  if st.checkbox("結果を本当に見ちゃう？"):
      st.write(prime(n))
if st.sidebar.checkbox("人生を一日にすると今何時？"):
  st.write("〜製作中〜")
  time.sleep(0.5)
  st.write("ね")
  time.sleep(0.5)
  st.write("む")
  time.sleep(0.5)
  st.write("い")
  time.sleep(0.5)
  st.write("ので")
  time.sleep(0.5)
  st.write("ね")
  time.sleep(0.5)
  st.write("ます")
if st.sidebar.checkbox("時計の長針と短針でできる扇形の面積を求めます"):
  st.write("〜製作中〜")
  time.sleep(0.5)
  st.write("ね")
  time.sleep(0.5)
  st.write("む")
  time.sleep(0.5)
  st.write("い")
  time.sleep(0.5)
  st.write("ので")
  time.sleep(0.5)
  st.write("ね")
  time.sleep(0.5)
  st.write("ます")
