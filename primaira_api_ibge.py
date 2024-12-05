import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint
import requests

nome = "bernardo"

url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"

answer = requests.get(url)

try:
    answer.raise_for_status()
except requests.HTTPError as e:
    print(f'Erro no request: {e}')
    result = None
else:
    result = answer.json()




if result and isinstance(result, list) and len(result) > 0:  
    # Extract the first item from the list  
    data = result[0]  
    
    # Extract the 'res' data  
    res_data = data['res']  
    
    # Convert to DataFrame  
    df = pd.DataFrame(res_data)  
    
    # Rename columns for clarity  
    df.rename(columns={'periodo': 'Period', 'frequencia': 'Frequency'}, inplace=True)  

    # Print the DataFrame for debugging  
    #pprint(df)  

    # Create a plot  
    plt.figure(figsize=(10, 5))  
    plt.bar(df['Period'], df['Frequency'], color='skyblue')  
    plt.title(f'Frequency of the name {data["nome"]} over the periods')  
    plt.xlabel('Period')  
    plt.ylabel('Frequency')  
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability  
    plt.grid(axis='y')  # Add grid lines for the y-axis  
    plt.tight_layout()  # Adjust layout to prevent clipping of labels  
    plt.show()  
else:  
    print("No data available for the provided name.")  
