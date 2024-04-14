from flask import render_template, request 
from ..database import conn, db



def object_list(template_name, query, paginate_by=20, **kwargs): 
    page = request.args.get('page') 
    if page and page.isdigit(): 
        page = int(page) 
    else: 
        page = 1 
    object_list = query.paginate(page, paginate_by) 
    return render_template(template_name, object_list=object_list, 
**kwargs)

def content(template, query, **kwargs): 
    search = request.args.get('q') 
    if search: 
        query = query.filter( 
            (db.Content.body.contains(search)))
    return object_list(template, query, **kwargs)