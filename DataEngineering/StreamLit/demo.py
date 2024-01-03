import streamlit as st

st.title("Hello StreamLit") #Title that looks big
st.header("Header")         #Headding 
st.subheader("Sub Headder") #Sub Headding
st.text("Hello this is Miss Craftivity. Hope you liked the tutorial :D")    #general paragraph text
st.markdown(""" # h1 tag    
## h2 tag
### h3 tag
:moon:<br>
:sunglasses:
**bold**
_italic_
            
""",True)                   # markdown by default treats everything as text. if used html tags inside, use ',True' at end
                            #h1,h2 and h3 are tags   #words used inbetween :: are to represent emojies # ** for bold and _ for italic text

st.latex(r''' a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right) ''')           # this represents this in form of an equation

st.write("Chinmai","Jyothy","Murali")                  # Printing all arguements
st.write(st)                                           # prints documentation of StreamLit
