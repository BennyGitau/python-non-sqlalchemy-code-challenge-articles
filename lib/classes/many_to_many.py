from collections import Counter

class Article:
    all = [] # list of all articles
    
    #Initializing an Article instance.
    def __init__(self, author, magazine, title):
        
        if not isinstance(title, str):
            raise TypeError("Title must be of type str")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters")
        self._title = title

        self.author = author
        self.magazine = magazine
        Article.all.append(self)

    @property
    def title(self):
        #Title getter that returns the title of the article.
        
        return self._title
    
    @property
    def author(self):
        #Author getter that returns the author of the article.
        
        return self._author

    @property
    def magazine(self):
        #Magazine getter that returns the magazine of the article.
        
        return self._magazine

    @author.setter
    def author(self, value):
        #Sets the author of the article.
        #vaue must be of type Author
    
        if not isinstance(value, Author):
            raise TypeError("Author must be of type Author")
        self._author = value
    
    @magazine.setter
    def magazine(self, value):
        #Sets the magazine of the article.
        #value must be of type Magazine
    
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be of type Magazine")
        self._magazine = value

class Author:
    #author of articles.
    
    #Initializes an Author instance.
    def __init__(self, name):
        #name musta non-empty string
        if not isinstance(name,str):
            raise TypeError("Name must be of type str")
        if len(name) == 0:
            raise ValueError('Name must be longer than 0 characters')
        self._name = name

    @property
    def name(self):
        # name getter that returns the name of the author.
        
        return self._name
    
    def articles(self):
        #Returns a list of all the articles written by the author.
        
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        #Returns a list of all the magazines the author has contributed to.
        
        return list(set(article.magazine for article in self.articles()))
        
    def add_article(self, magazine, title):
        #Creates and returns a new article given a magazine and title.
        
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be of type Magazine.")
        return Article(self, magazine, title)
        
    def topic_areas(self):
        #Returns a list of topic areas for all articles written by the author.
        
        mag_categories = [article.magazine.category for article in self.articles()]
        if mag_categories:
            return list(set(mag_categories))
        return None

class Magazine:
    magazines = [] # list of all magazines
    #Initializes a Magazine instance.
    def __init__(self, name, category):        
        self.name = name
        self._category = category
        Magazine.magazines.append(self) # appends the magazine to the list of magazines

    @property
    def name(self):
        # name getter that returns the name of the magazine.
        
        return self._name
    
    @name.setter
    def name(self, value):

        #name setter that sets the name of the magazine.
        #name must be a non-empty string and between 2 and 16 characters
        
        if isinstance(value,str) and (2 <= len(value) <=16):
            self._name = value
        else:
            raise ValueError('Name must be of type string and between 2 and 16 characters')
        
    @property
    def category(self):
        # category getter that returns the category of the magazine.
        
        return self._category
    
    @category.setter
    def category(self, value):
        #category setter that sets the category of the magazine.
        
        if isinstance(value, str) and len(value) != 0:
            self._category = value
        else:
            raise ValueError("Category must be type string with more than 0 characters")

    def articles(self):
        #Returns a list of all articles published in the magazine.
        
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        #Returns a list of authors who have contributed articles to the magazine.
        
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        #Returns a list of titles of all articles published in the magazine.
        
        titles = [article.title for article in self.articles()]
        if titles:
            return titles
        return None

    def contributing_authors(self):
        #Returns a list of authors who have contributed more than two articles to the magazine.
        
        authors = Counter(article.author for article in self.articles())
        result = [author for author, count in authors.items() if count > 2]
        return result if result else None
    
    @classmethod
    def top_publisher(cls):
        #Returns the magazine with the most articles.
    
        if not cls.magazines:
            return None
        top_magazine = max(cls.magazines, key=lambda mag: len(mag.articles()))
        return top_magazine if top_magazine.articles() else None
    
        
