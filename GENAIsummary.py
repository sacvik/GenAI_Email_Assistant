### Class for summarizing emails using GENAI Languagge Model

## import necessary libraries

from langchain_core.runnables import Runnable
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import StateGraph, END
from langchain_community.chat_models import ChatOllama
from IPython.display import display, Markdown
from openai import OpenAI

class GenAISummarizer(Runnable):
    """
    A class to summarize emails using a GENAI Language Model.
    Attributes:
        model (ChatOllama): The language model used for summarization.
    """

    def __init__(self, model, role_message):
        
        self.model = "mistral" if model is None else model
        self.messages = role_message

    def chat_compilation_using_ollama(self):
        """
        This function initializes the chatollama model with ChatGPT chat compliation.
        and helps defines role of the model and other parameters.
        """

        try:
            client = OpenAI(
                base_url = 'http://localhost:11434/v1',
                api_key='ollama', # required, but unused
            )

            response = client.chat.completions.create(
                model=self.model,
                messages= self.messages,
                temperature=0.1,
                max_tokens=1000
            )

            return response.choices[0].message.content

        except Exception as e:
            print(f"Error in function chat_compilation_using_ollama: {e}")

    def _call(self, emails: list) -> str:
        """
        Summarizes the provided emails using the GENAI Language Model.
        
        Args:
            emails (list): List of email content to summarize.
        
        Returns:
            str: Summary of the emails.
        """
        messages = [HumanMessage(content="\n".join(emails))]
        response = self.model.invoke(messages)
        return response.content
    
    def preprocess_email(self, state):
        """
        """
        # Here you can add any preprocessing logic if needed
        return emails
    
    def _display(self, summary: str) -> None:
        """
        Displays the summary in a Markdown format.
        
        Args:
            summary (str): The summary to display.
        """
        display(Markdown(f"### Summary:\n{summary}"))
    
    def run(self, emails: list) -> str:
        """
        Runs the summarization process and displays the summary.
        
        Args:
            emails (list): List of email content to summarize.
        
        Returns:
            str: Summary of the emails.
        """
        summary = self._call(emails)
        self._display(summary)
        return summary
