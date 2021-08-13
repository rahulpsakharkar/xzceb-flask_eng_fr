''' Language Translation '''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv() # Load .env file

apikey = os.environ['apikey'] # Get apikey
url = os.environ['url'] # Get url of translator service

# Create tranalator instance
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator = authenticator
)
language_translator.set_service_url(url)

# Function for English to French Translation
def english_to_french(english_text):
    ''' This function translates text from English to French. '''
    translation = language_translator.translate(
                  text = english_text,
                  model_id ='en-fr').get_result()

    # Extract actual tranalated text
    french_text = translation.get('translations')[0].get('translation')
    return french_text

# Function for French to English Translation
def french_to_english(french_text):
    ''' This function translates text from French to English. '''
    translation = language_translator.translate(
                  text = french_text,
                  model_id ='fr-en').get_result()

    # Extract actual tranalated text
    english_text = translation.get('translations')[0].get('translation')
    return english_text
