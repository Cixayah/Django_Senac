from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contato (request):
    context = {
        'nome':'MotorWeb',
        'fone':'17-123456789',
        'email':'email@teste.com',
    }
    return render(request, 'contato.html', context)
