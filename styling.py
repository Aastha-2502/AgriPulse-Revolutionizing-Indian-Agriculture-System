def custom_css():
    return """
<style>
/* General resets */
.css-18e3th9 {
    padding: 0!important;
}

/* Main content styling */
/* General styles for the body */
body {
    background-color: #0E1117; /* Dark background for content */
    color: #FFF; /* Light text for contrast */
}

/* Target the main block for content */
div.main.block.container {
    max-width: 800px; /* Set a max width for the main content if desired */
}

/* Specific targeting for Streamlit widgets */
div.stTextInput > div > div > input {
    background-color: #2C2F36; /* Background color for text input */
}

div.stSelectbox > select {
    background-color: #2C2F36; /* Background color for select input */
}

/* Increase specificity for sidebar styles */
section.main.css-1d391kg {
    background-color: #111; /* Lighter background for the sidebar */
}

/* Sidebar header styling with increased specificity */
section.main.css-1d391kg > header {
    background: #000; /* Darker background for header */
}

/* Specific button styling */
button.css-2trqyj {
    background-color: #2086ee; /* Button background color */
    border: none;
}

button.css-2trqyj:hover {
    background-color: #106ba3; /* Darker background on hover */
}

/* Footer styling */
footer {
    background-color: #2b2b2b; /* Footer background color */
    color: white; /* Footer text color */
}

/* Replace .css-2trqyj with the correct class from your app */
</style>
"""


def custom_footer():
    return """
    <footer style="position: fixed; bottom: 0; width: 100%; height: 60px; line-height: 60px; background-color: #2b2b2b; color: white; text-align: center;">
        Developed by Punters &copy; 2023
    </footer>
    """
