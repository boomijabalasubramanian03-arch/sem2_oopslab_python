class st:
   count = 0
   def __init__(self):
      st.count = st.count+1
   @staticmethod
   def display():
      print("NO OF OBJECTS CREATED:",st.count)
a1 = st()
a2 = st()
st.display()
a3 = st()
a4 = st()
st.display()
