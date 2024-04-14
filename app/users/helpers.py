from flask import render_template, request 
#from ..database import db




class ContentHelpers:

    def __init__(self):
        pass
    
    @staticmethod
    def object_list(template_name, query, paginate_by=20, **kwargs): 
        page = request.args.get('page') 
        if page and page.isdigit(): 
            page = int(page) 
        else: 
            page = 1 
        object_list = query.paginate(page, paginate_by) 
        return render_template(template_name, object_list=object_list, 
    **kwargs)

   
    def content(self, template, query, **kwargs): 
        search = request.args.get('q') 
        if search: 
            query = query.filter()
                #(db.Content.body.contains(search)))
        return self.object_list(template, query, **kwargs)



class Families:

    def __init__(self):
        pass

    @staticmethod
    def get_families() -> list:
        
        all_families = [
            ('Apidae', 'Bees'),
            ('Accipitridae', 'Hawks, Eagles'),
            ('Ambystomatidae', 'Mole Salamanders'),
            ('Anatidae', 'Ducks, Geese, Swans'),
            ('Bufonidae', 'Toads'),
            ('Bovidae', 'Cattle, Goats, Sheep'),
            ('Canidae', 'Dogs'),
            ('Cheloniidae', 'Sea Turtles'),
            ('Cervidae', 'Deer'),
            ('Cichlidae', 'Cichlids'),
            ('Columbidae', 'Pigeons, Doves'),
            ('Crocodylidae', 'Crocodiles'),
            ('Cyprinidae', 'Carps, Minnows'),
            ('Drosophilidae', 'Fruit Flies'),
            ('Elephantidae', 'Elephants'),
            ('Falconidae', 'Falcons'),
            ('Felidae', 'Cats'),
            ('Formicidae', 'Ants'),
            ('Gobiidae', 'Gobies'),
            ('Haemulidae', 'Grunts, Sweetlips'),
            ('Hominidae', 'Great Apes, including Humans'),
            ('Hylidae', 'Tree Frogs'),
            ('Lepidoptera', 'Butterflies, Moths'),
            ('Passeridae', 'Sparrows'),
            ('Psittacidae', 'Parrots'),
            ('Pythonidae', 'Pythons'),
            ('Ranidae', 'True Frogs'),
            ('Salmonidae', 'Salmons, Trouts'),
            ('Scarabaeidae', 'Scarab Beetles'),
            ('Scombridae', 'Mackerels, Tunas'),
            ('Strigidae', 'Owls'),
            ('Tetraodontidae', 'Pufferfishes'),
            ('Testudinidae', 'Tortoises'),
            ('Tettigoniidae', 'Katydids'),
            ('Ursidae', 'Bears'),
            ('Viperidae', 'Vipers')
        ]
    
        all_families_sorted = sorted(all_families)
        print(all_families_sorted)

        return all_families_sorted
            
        
