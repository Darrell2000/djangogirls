from Django.Contrib import Admin 
from .models import Post

Admin.site.register(Post) 
