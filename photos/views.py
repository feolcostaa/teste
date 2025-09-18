# photos/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.db.models import Q 
from .models import Photo
from .forms import ContatoForm # Certifique-se de criar este arquivo forms.py no app 'photos'

def photo_list(request):
    """
    Lista todas as fotos ou filtra com base em uma consulta de pesquisa.
    """
    search_query = request.GET.get('search_query', '')

    if search_query:
        photos = Photo.objects.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(location__icontains=search_query)
        ).order_by('-published_at')
    else:
        photos = Photo.objects.all().order_by('-published_at')

    context = {
        'photos': photos,
        'search_query': search_query
    }
    return render(request, 'photos/photo_list.html', context)

def photo_detail(request, pk):
    """
    Exibe os detalhes de uma foto específica.
    """
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'photos/photo_detail.html', {'photo': photo})

def photo_sobre_nos(request):
    """
    Renderiza a página 'Sobre Nós' da galeria de fotos.
    """
    return render(request, 'photos/photo_sobre_nos.html')

def photo_contato(request):
    """
    Processa o formulário de contato.
    """
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']

            # Lógica para enviar o e-mail
            send_mail(
                subject=f'Contato da Galeria de Fotos - {nome}',
                message=f'Nome: {nome}\nEmail: {email}\n\nMensagem:\n{mensagem}',
                from_email=email, # E-mail do remetente
                recipient_list=['seu_email_para_receber@exemplo.com'], # E-mail que receberá a mensagem
                fail_silently=False,
            )
            return redirect(reverse('photo_sucesso'))
    else:
        form = ContatoForm()

    return render(request, 'photos/photo_contato.html', {'form': form})

def photo_sucesso(request):
    """
    Renderiza a página de sucesso após o envio do formulário.
    """
    return render(request, 'photos/photo_sucesso.html')