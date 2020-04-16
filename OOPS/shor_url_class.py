# OOP: Easier to design, reuse components and build large software
# OOP for ML & DS roles: Should know the basics to use various modules and extend them when needed.
'''
Q. How would you build a TinyURL service?

approach: 
Key = short-URL Value = Long-URL
Key: random variable length alphabetic suffix [tinyurl.com/tgwxyc]

'''

# Class variables shared by all objects

# Class: group all variables/attributes and functions/methods into a single logical unit

class ShortURL1:
    
    URLPrefix = "https://www.shortURL.com/"; # class variable 
    
    def __init__(self): # constructor
        self.d=dict();

    # given a long URL, get a short URL
    def getShortURL(self, longURL): 
        # length = random value in 6-10
        l = random.randint(6,10);
        

        # generate random characters into a string of length l
        chars = string.ascii_lowercase
        shortURL = ''.join(random.choice(chars) for i in range(l))
        

        # check if this string is already present in dict d
        if shortURL in self.d:
            return getShortURL(longURL);
        else:
            self.d[shortURL] = longURL;

        
        r = self.URLPrefix + shortURL
        return r;

    def getLongURL(self, shortURL):
        
        # extarct key from URL https://www.shortURL.com/mxzmuis ---> mxzmuis
        k = shortURL[25:];

        if k in self.d:
            return self.d[k];
        else:
            return None;

