from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from ..models import Category

### Não preciso dessa merda eu retirei a parte de likes, posso ver se posso dar outro nome caso
# precise para mostrar os livros

"""
@login_required
def like_category(request):
    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET['category_id']
        likes = 0
    if cat_id:
        cat = Category.objects.get(id=int(cat_id))
        if cat:
            likes = cat.likes + 1
            cat.likes = likes
            cat.save()
    return HttpResponse(likes)
"""