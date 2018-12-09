from django.contrib.auth.decorators import login_required
from django.shortcuts import render

#### Página do restrição de acesso
#### Trocar depois para erro 404

@login_required
def restricted(request):
    return render(request, 'rango/restricted.html', {})