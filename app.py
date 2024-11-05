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

# Define tiles for different modules
modules = [
    {
        "title": "Help Guide",
        "description": "The Help reference topics cover how the ABS Compass platform works. Learn about all the features you can incorporate into your Knowledgebase.",
        "icon": "💡"
    },
    {
        "title": "What's New",
        "description": "Learn about the latest features and enhancements available by upgrading to the latest version of ABS Compass.",
        "icon": "📢"
    },
    {
        "title": "System Administration",
        "description": "Find installation instructions and other help topics for managing your ABS Compass server.",
        "icon": "🖥️"
    },
    {
        "title": "Developers",
        "description": "API reference docs for integrations. Learn how to sync with external systems.",
        "icon": "👨‍💻"
    },
    {
        "title": "Design Articles",
        "description": "The design articles show how we solve more in-depth implementation challenges.",
        "icon": "🧩"
    },
    {
        "title": "Standard System Documentation",
        "description": "A reference guide to the key features of our standard knowledgebase.",
        "icon": "📚"
    }
]

# Display tiles
cols = st.columns(3)
for index, module in enumerate(modules):
    with cols[index % 3]:
        st.markdown(f"### {module['icon']} {module['title']}")
        st.write(module['description'])
        st.button("Learn More", key=module['title'])

