from django.shortcuts import render, redirect

from .forms import UserRegisterForm

from django.contrib import messages


def novo_usuario(request):

    if request.method == 'POST':

        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():

            formulario.save()

            usuario = formulario.cleaned_data.get('username')

            messages.success(request, f'usuario {usuario} criado com sucesso!')
        
            return redirect('pagina_login')
        
    else:

        formulario = UserRegisterForm()

    return render(request, 'usuarios/novo_usuario.html', {'formulario': formulario})


def pagina_login(request):

    return render(request, 'usuarios/login.html')


