import google.generativeai as genai

import gepetto.config
from gepetto.models.openai import GPT


class Gemini(GPT):
    def __init__(self, model):
        try:
            super().__init__(model)
        except ValueError:
            pass  # May throw if the OpenAI API key isn't given, but we don't need any to use Gemini.

        self.model = model
        api_key = gepetto.config.get_config("Gemini", "API_KEY", "GEMINI_API_KEY")
        if not api_key:
            print(_("Please edit the configuration file to insert your {api_provider} API key!")
                  .format(api_provider="Gemini"))
            raise ValueError("No valid Gemini API key found")

        genai.configure(api_key=api_key)
        self.client = genai.GenerativeModel('gemini-1.5-flash')

