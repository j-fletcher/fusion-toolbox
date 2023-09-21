import requests

class MissingKeyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class WolframAPI(object):
    def __init__(self, key = None):
        """
        Object initializing WolframAlpha Short Answers API. Raises an exception if a developer key is not given.
        Queries to the API are passed via the .query() classmethod.
        
        App ID Keys specific to the Short Answers API may be requested via https://developer.wolframalpha.com
        
        Args:
            key (str): WolframAlpha App ID
        """
        self.key = key
        
        if self.key is None:
            ermsg = 'API key required for property lookup. Please generate a key at https://developer.wolframalpha.com'
            raise MissingKeyError(ermsg)
              
                        
    def query(self, compound = None, property = None):
        """
        Calls the Short Answers API and returns a string of text with the reply

        Args:
            compound (str): material of interest, e.g. "water"
            property (str): desired material property, e.g. "density"
        
        Returns:
            result (str): WolframAlpha Short Answer to the prompt. Given with metric units.
        """
        key = self.key

        if compound is None:
            result = 'Incomplete query: no compound specified'
        elif property is None:
            result = 'Incomplete query: no property specified'
        else:
            prompt = property + "%20of%20" + compound
            url = 'http://api.wolframalpha.com/v2/result?appid=%s&i=%s&units=metric' % (
                key, prompt.lower()
                )
            r = requests.get(url)
            if r.text == 'No short answer available': 
                result = 'No data found for specified property.'
            else:
                result = r.text
            return result    
