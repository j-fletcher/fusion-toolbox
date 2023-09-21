import requests

class WolframAPI:
    """
        Object initializing WolframAlpha Short Answers API. Raises an exception 
        if a developer key is not given.
        Queries to the API are passed via the .query() classmethod.
        
        App ID Keys specific to the Short Answers API may be requested 
        via https://developer.wolframalpha.com
        
        Args:
            key (str): WolframAlpha App ID
    """
    _URL = 'http://api.wolframalpha.com/v2/result?appid={}&i={}%20of%20{}&units=metric'

    def __init__(self, key):
        if not isinstance(key,str):
            ermsg = 'API key (str) required for property lookup. '\
                    + 'Please generate a key at https://developer.wolframalpha.com'
            raise TypeError(ermsg)

        self.key = key
                        
    def query(self, compound, property):
        """
        Calls the Short Answers API and returns a string of text with the reply

        Args:
            compound (str): material of interest, e.g. "water"
            property (str): desired material property, e.g. "density"
        
        Returns:
            result (str): WolframAlpha Short Answer to the prompt. 
                          Given with metric units.
        """

        url = self._URL.format(self.key, property.lower(), compound.lower())
        r = requests.get(url)
        if r.text == 'No short answer available': 
            raise ValueError('No data found for specified property.')
        return r.text
