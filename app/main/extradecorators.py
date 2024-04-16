import slugify
import datetime, re 

def slugify_decorator(cls):

    class slug_Wrapper(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.generate_slug()

        @staticmethod
        def slugify(s):
            return re.sub('[^\\w]+', '-', s).lower()
        def generate_slug(self): 
            self.slug = '' 
            #if self.title: 
                #self.slug = slugify.slugify(self.title) 
            print('Slug:', self.slug)
  
        def __repr__(self): 
            return '<Entry: %s>' % self.title
            
    return slug_Wrapper