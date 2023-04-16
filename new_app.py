import streamlit as st
import spacy
from spacy import displacy

# Load your custom trained model in spaCy
nlp = spacy.load("model-best")


def annotate_text(text):
    doc = nlp(text)
    return doc


# Define the Streamlit app with custom styles
def main():
    st.set_page_config(page_title="Text Annotation App", page_icon=":memo:", layout="wide")
    st.title("Text Annotation App")
    st.sidebar.markdown("Testing dataset")
    example_texts = ["The proportion of the crop cycle that takes place in one year The average actual annual yield ",
                     "taking into account the Energy or number of chews necessary to chew the banana to make it ready ",
                     "to be swallowed Aroma of fresh grass Elemental flavor caused by dilute aqueous solutions of "
                     "various substances such as sucrose or aspartame ",
                     "Emergence time is when the cotyledon appears above the soil surface.",
                     "Uniformity of color of the surface of the sample ",
                     "The visual aspect of boiled potatoes: potatoes turn gray or dark after boiling",
                     "Causative agent: Liriomyza cicerina. The leaflets are mined have a reduced photosynthetic "
                     "capacity and senesce prematurely.",
                     "The tolerance to drought of the plant"]
    example = st.sidebar.selectbox("Or select an example:", example_texts)
    st.sidebar.markdown("---")

    # Define the main panel with the annotation interface
    st.write("### Enter some text to annotate:")
    text = st.text_area("", example, height=200)
    if st.button("Annotate"):
        doc = annotate_text(text)
        for ent in doc.ents:
            if ent.start > 0:
                st.write(doc[:ent.start].text)
            st.markdown(
                f"<span style='background-color: #ddd; padding: 0.25em 0.5em; margin: 0.25em; border-radius: 0.25em;'>{ent.text} ({ent.label_})</span>",
                unsafe_allow_html=True)
            if ent.end < len(doc):
                st.write(doc[ent.end:].text)
            st.write("\n")


if __name__ == "__main__":
    main()

