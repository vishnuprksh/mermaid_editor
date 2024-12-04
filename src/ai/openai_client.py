from openai import OpenAI
from src.config.settings import Settings

class OpenAIClient:
    def __init__(self):
        self.client = OpenAI(api_key=Settings.OPENAI_API_KEY)
    
    def generate_mermaid_diagram(self, prompt: str) -> str:
        """
        Generate a Mermaid diagram based on a text prompt using OpenAI API
        
        Args:
            prompt (str): Natural language description of the diagram
        
        Returns:
            str: Mermaid diagram code
        """
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert at creating Mermaid diagrams. Generate precise Mermaid syntax based on the user's description."
                    },
                    {
                        "role": "user",
                        "content": f"Create a Mermaid diagram for: {prompt}"
                    }
                ],
                response_format={
                    "type": "text"
                },
                temperature=1,
                max_tokens=2048,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            # Extract the Mermaid code and remove any surrounding '```mermaid' or '```' markers
            mermaid_code = response.choices[0].message.content.strip('```mermaid\n').strip('```')
            return mermaid_code
        except Exception as e:
            print(f"Error generating diagram: {e}")
            return ""

# Test function
def test_api():
    client = OpenAIClient()
    prompt = "Create a flowchart for a login process."
    diagram = client.generate_mermaid_diagram(prompt)
    print("Generated Mermaid Diagram:\n", diagram)

# Run the test
if __name__ == "__main__":
    test_api()