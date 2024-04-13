import slugify
import datetime, re 

def slugify_decorator(cls):

    class slugWrapper(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.generate_slug()

        @staticmethod
        def slugify(s):
            return re.sub('[^\w]+', '-', s).lower()

        def generate_slug(self):
            self.slug = ''
           
            #if self.content:
                #self.slug = self.slugify(self.content)
                #self.repr_arg = self.content
            #elif self.public_content:
                #self.slug = self.slugify(self.public_content)
                #self.repr_arg = self.public_content
                
            return self.slug

        def __repr__(self):
            return f'<{self.__class__.__name__} {self.slug!r}>'
    
    return slugWrapper