from firecrawl import Firecrawl
import os

from dotenv import load_dotenv
load_dotenv()

firecrawl = os.getenv('FIRECRAWL_API_KEY') 

try:
    crawler= Firecrawl(api_key=firecrawl)
    print("Firecrawl client initialized successfully.")
except Exception as e:
    print(f"Error initializing Firecrawl client: {e}")




