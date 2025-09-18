# photos/forms.py

from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(
        label='Nome',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'mt-1 block w-full p-2 bg-gray-50 border border-gray-300 rounded-md text-gray-800 focus:ring-blue-500 focus:border-blue-500 shadow-sm', 
            'placeholder': 'Seu Nome'
        })
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'mt-1 block w-full p-2 bg-gray-50 border border-gray-300 rounded-md text-gray-800 focus:ring-blue-500 focus:border-blue-500 shadow-sm', 
            'placeholder': 'seu.email@exemplo.com'
        })
    )
    mensagem = forms.CharField(
        label='Mensagem',
        # Usamos Textarea aqui, que é mais apropriado para mensagens longas
        widget=forms.Textarea(attrs={
            'class': 'mt-1 block w-full p-2 bg-gray-50 border border-gray-300 rounded-md text-gray-800 focus:ring-blue-500 focus:border-blue-500 shadow-sm', 
            'rows': 4, 
            'placeholder': 'Sua mensagem...'
        })
    )