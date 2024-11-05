import streamlit as st

# Sidebar with index
st.sidebar.title("ABS Compass")
st.sidebar.write("Navigate through the modules:")
st.sidebar.markdown("- **Dashboard**")
st.sidebar.markdown("- **Help Guide**")
st.sidebar.markdown("- **System Administration**")
st.sidebar.markdown("- **Standard Documentation**")
st.sidebar.markdown("- **Developers**")
st.sidebar.markdown("- **Design Articles**")

# Main content area
st.title("ABS Compass Knowledge Base")

# Define modules with content for each section
modules = {
    "Help Guide": {
        "description": "The Help reference topics cover how the ABS Compass platform works. Learn about all the features you can incorporate into your Knowledgebase.",
        "content": "Detailed information about the Help Guide section goes here..."
    },
    "What's New": {
        "description": "Learn about the latest features and enhancements available by upgrading to the latest version of ABS Compass.",
        "content": "Information about the latest features and enhancements available in ABS Compass."
    },
    "System Administration": {
        "description": "Find installation instructions and other help topics for managing your ABS Compass server.",
        "content": "Installation and server management information for System Administration."
    },
    "Developers": {
        "description": "API reference docs for integrations. Learn how to sync with external systems.",
        "content": "API documentation, SDK usage, and integration methods for developers."
    },
    "Design Articles": {
        "description": "The design articles show how we solve more in-depth implementation challenges.",
        "content": "In-depth articles explaining implementation challenges and solutions."
    },
    "Standard System Documentation": {
        "description": "A reference guide to the key features of our standard knowledgebase.",
        "content": "A comprehensive guide to the core features and documentation standards."
    }
}

# Initialize session state for selected module
if "selected_module" not in st.session_state:
    st.session_state.selected_module = None

# Display tiles, making each clickable
if st.session_state.selected_module is None:
    cols = st.columns(3)
    for i, (title, module) in enumerate(modules.items()):
        with cols[i % 3]:
            # Render a markdown button-like tile with title and description
            if st.markdown(
                f'<a href="#" style="text-decoration: none;"><div style="background-color: #f0f0f5; padding: 20px; border-radius: 5px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1);">'
                f'<h4 style="color: #4c4c4c; margin: 0;">{title}</h4>'
                f'<p style="color: #7d7d7d; font-size: 0.9em;">{module["description"]}</p></div></a>',
                unsafe_allow_html=True,
            ):
                st.session_state.selected_module = title

else:
    # Show the selected module's content
    st.subheader(st.session_state.selected_module)
    st.write(modules[st.session_state.selected_module]["content"])
    if st.button("Back to Home"):
        st.session_state.selected_module = None
