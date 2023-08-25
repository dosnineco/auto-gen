import pandas as pd
import openai

# Define the data with headings Keyword, Heading, Search Intent, and Outline
data = {
    'Keyword': ['Keyword1', 'Keyword2'],
    'Heading': ['Heading1', 'Heading2'],
    'Search Intent': ['Intent1', 'Intent2'],
    'Outline': ['Outline1', 'Outline2']
}

# Create a pandas DataFrame from the data
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel('content.xlsx', index=False)

# You can then use the OpenAI API to generate content for each keyword
for keyword in data['Keyword']:
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=f"Write content for keyword: {keyword}",
      max_tokens=150
    )
    
    print(response.choices[0].text) # Print the generated content
