import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    # OpenAI API Configuration
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    
    # Application Settings
    APP_NAME = "AI Mermaid Diagram Editor"
    DEFAULT_WINDOW_WIDTH = 1200
    DEFAULT_WINDOW_HEIGHT = 800
    
    # Mermaid Rendering Settings
    MERMAID_CLI_PATH = os.getenv('MERMAID_CLI_PATH', '')