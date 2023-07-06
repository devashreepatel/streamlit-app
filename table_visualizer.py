import streamlit as st
import pandas as pd
import openai

# Set up OpenAI API credentials
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Streamlit app
def main():
    st.title("Table Visualization Code Generator")

    # File upload
    file = st.file_uploader("Upload a CSV file", type=["csv"])

    if file is not None:
        # Read the uploaded file
        table = pd.read_csv(file)

        # Show the table
        st.write("Uploaded Table:")
        st.dataframe(table)

        # Generate visualization code using OpenAI
        code = generate_code(table)

        # Show the generated code
        st.write("Generated Visualization Code:")
        st.code(code)

# Generate visualization code using OpenAI
def generate_code(table):
    # Convert the table to a Markdown string
    markdown_table = table.to_markdown()

    # Prepare the prompt for OpenAI
    prompt = f"```python\nimport pandas as pd\n\ndf = pd.read_markdown('''{markdown_table}''')\n\n# Generate visualization code here\n```"

    # Generate code using OpenAI
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        temperature=0.5,
        n=1,
        stop=None,
        timeout=10
    )

    # Extract the generated code from OpenAI's response
    code = response.choices[0].text.strip()

    return code

if __name__ == '__main__':
    main()