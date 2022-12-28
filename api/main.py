import streamlit as st
from utils import *

st.set_page_config(page_title="COVID", page_icon=":ghost:", layout="wide")


def search_engine():

    txt = f'<p style="font-size: 60px" align="left"> Article search engine </p>'
    st.markdown(txt, unsafe_allow_html=True)
    query = st.text_input("Search for an article")
    # milvus search limit - 16384
    no_of_results = st.slider(
        "number of search results", min_value=1, max_value=16384, value=50
    )
    if query:
        txt = f'<p style="font-style:italic;color:gray;">Showing top {no_of_results} related articles</p>'
        st.markdown(txt, unsafe_allow_html=True)
        search_param = {
            "query": query,
            "no_of_results": no_of_results,
        }
        with st.spinner("Searching..."):
            articles = get_articles(search_param=search_param)

            for i in articles:
                title, summary, authors, link = i
                if not title:
                    st.write("Title Not Available")
                else:
                    st.title(title)
                if not authors:
                    st.write("Author Information Not Available")
                else:
                    st.write(authors)
                if not summary:
                    st.write("Abstract Not Available")
                else:
                    st.write(summary)
                if not link:
                    st.write("URL Not Available")
                else:
                    st.markdown("[View Paper](%s)" % link)


page_names_to_funcs = {
    "Search Engine": search_engine,
}

pages = st.sidebar.selectbox("What would you like to do?", page_names_to_funcs.keys())
page_names_to_funcs[pages]()
