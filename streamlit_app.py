st.set_page_config(page_title = "Generate Content",
                    layout='centered',
                    initial_sidebar_state = "collapsed")

st.header("Creative Writer✍️")

input_text = st.text_input("Enter the topic you want to write about")

col1,col2 = st.columns([5,5])

with col1:
    no_words = st.text_input('No of words')
with col2:
    category = st.selectbox("category",
                              ('Essays', 'Poem', 'Joke', 'Blog'),
                              index=0)
    
submit = st.button("Generate")

if submit:
    st.write(getLlamaResponse(input_text, no_words, category))
