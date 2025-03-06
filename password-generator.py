import streamlit as st
import random
import string

# Function to generate password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

# Function to check password strength
def check_strength(length, use_digits, use_special):
    if length >= 12 and use_digits and use_special:
        return "🟢 Strong"
    elif length >= 8 and (use_digits or use_special):
        return "🟡 Medium"
    else:
        return "🔴 Weak"

# Streamlit App
st.set_page_config(page_title="Password Generator", page_icon="🔑", layout="centered")

st.markdown("## 🔐 **Secure Password Generator**")
st.write("Generate strong passwords to enhance your security.")

# UI Components
length = st.slider("🔢 Select password length", min_value=6, max_value=32, value=12)
use_digits = st.checkbox("🔢 Include Digits")
use_special = st.checkbox("🔣 Include Special Characters")

# Initialize session state
if "password" not in st.session_state:
    st.session_state.password = ""

# Buttons for actions
col1, col2 = st.columns(2)
generate_clicked = col1.button("🚀 Generate Password")
refresh_clicked = col2.button("🔄 Refresh")

# Generate password logic
if generate_clicked:
    st.session_state.password = generate_password(length, use_digits, use_special)
    st.session_state.strength = check_strength(length, use_digits, use_special)

# Refresh logic (clears everything)
if refresh_clicked:
    st.session_state.password = ""
    st.session_state.strength = ""

# Display password only if generated
if st.session_state.password:
    st.text_input("📝 Generated Password", st.session_state.password, key="password_display", type="default")
    st.markdown(f"**Strength:** {st.session_state.strength}")

    # Copy to Clipboard using JavaScript
    copy_script = f"""
    <script>
    function copyPassword() {{
        var password = document.getElementById("password_text").innerText;
        navigator.clipboard.writeText(password).then(() => {{
            alert("Copied to clipboard: " + password);
        }});
    }}
    </script>
    <button onclick="copyPassword()" style="padding: 8px 15px; background-color: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer;">📋 Copy to Clipboard</button>
    <p id="password_text" style="display:none;">{st.session_state.password}</p>
    """

    st.components.v1.html(copy_script, height=100)

st.write("---")

st.markdown("👨‍💻 **Built with ❤️ by ERSA RANI**, https://github.com/ersa-rani")
