from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm
from .models import Usuario, Encontro


@login_required
def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    search_query = request.GET.get('search', '')
    filter_bairro = request.GET.get('bairro', '')
    filter_sexo = request.GET.get('sexo', '')
    filter_cidade = request.GET.get('cidade', '')

    usuarios = Usuario.objects.all()

    if search_query:
        usuarios = usuarios.filter(nome__icontains=search_query)
    if filter_bairro:
        usuarios = usuarios.filter(bairro__icontains=filter_bairro)
    if filter_sexo:
        usuarios = usuarios.filter(sexo__icontains=filter_sexo)
    if filter_cidade:
        usuarios = usuarios.filter(cidade__icontains=filter_cidade)

    context = {
        'usuarios': usuarios
    }
    return render(request, 'usuarios/usuarios.html', context)


def selecionar_usuario(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/selecionar_usuario.html', {'usuarios': usuarios})

def agendar_encontro(request, usuario_id):
    usuario = get_object_or_404(Usuario, id_usuario=usuario_id)
    
    if request.method == 'POST':
        data = request.POST.get('data')
        horario = request.POST.get('horario')
        descricao = request.POST.get('descricao')
        
        # Combine data e horário em um DateTimeField
        data_horario = f"{data}T{horario}"
        
        # Verificar se já existe um encontro no mesmo horário
        if Encontro.objects.filter(data=data_horario, usuario=usuario).exists():
            form_errors = ["Já existe um encontro agendado para esse horário."]
            return render(request, 'usuarios/agendar_encontro.html', {'usuario_id': usuario_id, 'form_errors': form_errors})
        
        # Criar o novo encontro
        Encontro.objects.create(
            usuario=usuario,
            data=data_horario,
            descricao=descricao
        )
        
        return redirect('listagem_agendamento')

    return render(request, 'usuarios/agendar_encontro.html', {'usuario_id': usuario_id})

def listagem_encontros(request):
    encontros = Encontro.objects.all()
    return render(request, 'usuarios/listagem_encontros.html', {'encontros': encontros})


def listagem_simples_encontros(request):
    encontros = Encontro.objects.all()
    return render(request, 'usuarios/listagem_agendamento.html', {'encontros': encontros})


def usuarios_com_encontros(request):
    usuarios = Usuario.objects.filter(encontro__isnull=False).distinct()
    return render(request, 'usuarios/usuarios_com_encontros.html', {'usuarios': usuarios})


def agendar_encontro_sem_usuario(request):
    return redirect('usuarios')



def acompanhamento(request, usuario_id):
    usuario = get_object_or_404(Usuario, id_usuario=usuario_id)
    encontros = usuario.encontros.all()
    
    if request.method == 'POST':
        encontro = Encontro()
        encontro.usuario = usuario
        encontro.data = request.POST.get('data')
        encontro.horario = request.POST.get('horario')
        encontro.descricao = request.POST.get('descricao')
        encontro.save()
        return redirect('acompanhamento', usuario_id=usuario_id)

    return render(request, 'usuarios/acompanhamento.html', {'usuario': usuario, 'encontros': encontros})



def acompanhamento_geral(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/usuarios.html', {'usuarios': usuarios})



def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o formulário
            return redirect('usuarios')  # Redireciona após salvar
    else:
        form = UsuarioForm()
    
    return render(request, 'usuarios/cadastrar_usuario.html', {'form': form})


def excluir_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id_usuario=usuario_id)
    usuario.delete()
    return redirect('usuarios')


def excluir_encontro(request, encontro_id):
    encontro = get_object_or_404(Encontro, id=encontro_id)
    encontro.delete()
    return redirect('listagem_agendamento')