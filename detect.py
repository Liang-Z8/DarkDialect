import sys
from dark_cookies import CDA
from dark_cookies.CDA_Options import Options

# Function to explore a single website.
def explore_website(domain):
    '''
    param domain: string
        specifies the base domain of the webpage that we are analysing.
    '''
    options = Options()
    CDA(domain, options=options)