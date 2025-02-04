from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()  
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logado com sucesso!")
            return redirect('home')
        else:
            messages.success(request, "Ocorreu algum erro no Login. Tente novamente.")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})



def logout_user(request):
    logout(request)
    messages.success(request, 'Você foi deslogado!')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Você foi registrado com sucesso!')
            return redirect('home')                       
    else:
        form = SignUpForm()
        
    return render(request, 'register.html', {'form': form})


def custumer_record(request, pk):
    if request.user.is_authenticated:
        custumer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'custumer_record':custumer_record})
    else:    
        messages.success(request, 'Você precisa estar logado para ver esta página.')
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk) 
        delete_it.delete() 
        messages.success(request, 'Registro apagado!')
        return redirect('home')
    else:    
        messages.success(request, 'Você precisa estar logado para apagar este cadastro.')
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, 'Cadastrado!')
                return redirect('home')
                
        return render(request, 'add_record.html', {'form':form})
    else:    
        messages.success(request, 'Você precisa estar logado para cadastrar.')
        return redirect('home')

def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Cadastro atualizado!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "Você precisa estar logado para atualizar um cadastro.")
		return redirect('home')