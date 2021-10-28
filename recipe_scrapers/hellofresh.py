import extruct
import requests
from ._abstract import AbstractScraper
from ._utils import normalize_string

class HelloFresh(AbstractScraper):
    @classmethod
    def host(self, domain="com"):
        return f"hellofresh.{domain}"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def image(self):
        return self.schema.image()

    def nutrients(self):
        return self.schema.nutrients()
    
    def description(self):
        return self.schema.description()
        
    def cuisine(self):
        return self.schema.cuisine()
    
    def category(self):
        return self.schema.category()
        
    def author(self):
        return self.schema.author()
    
    def date_published(self):
        return self.schema.datePublished()
    
    def difficulty(self):
        d = self.soup.find("span", {"data-translation-id": "recipe-detail.cooking-difficulty"}).parent.next_sibling.get_text()
        return normalize_string(d)

