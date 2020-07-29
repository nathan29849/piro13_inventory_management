from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Item, Account
from .forms import ItemForm, AccountForm


def item_list(request):
    item__list = Item.objects.all()

    context = {'item_list': item__list}  # 왼쪽이 내가 쓸 변수 이름, 오른쪽이 불러올 객체
    return render(request, 'item/item_list.html', context)

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item/item_detail.html', {
        'item': item,
    })

def item_register(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)  # ModelForm에서 제공하는 기능
            item.save()
            pk = item.id
            url = reverse('item:item_detail', kwargs={'pk': pk})
            return redirect(to=url)
    else:
        form = ItemForm
    return render(request, 'item/item_register.html', {
        'form': form,
    })

def item_update(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            pk = item.id
            url = reverse('item:item_detail', kwargs={'pk': pk})
            return redirect(to=url)
    else:
        form = ItemForm(instance=item)
    context = {'form': form}
    return render(request, 'item/item_register.html', context)


def item_delete(request, pk):
    item = Item.objects.get(id=pk)
    item.delete()

    url = reverse('item:item_list')
    return redirect(to=url)

def account_list(request):
    account__list = Account.objects.all()

    context = {'account_list': account__list}
    return render(request, 'item/account_list.html', context)

def account_detail(request, pk):
    account = get_object_or_404(Account, pk=pk)
    # my_account = Item.get.objects.get(Account__name)
    return render(request, 'item/account_detail.html', {
        'account': account
    })

# def account_register(request, account=None):
#     if request.method == "POST":
#         form = AccountForm(request.POST, instance=account)
#         if form.is_valid():
#             account = form.save()  # ModelForm에서 제공하는 기능
#             return redirect(account)
#     else:
#         form = AccountForm(instance=account)
#     return render(request, 'item/account_register.html', {
#         'form': form,
#     })
#
# def account_update(request, pk):
#     account = get_object_or_404(Account, pk=pk)
#     return account_register(request, account)

def account_register(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.save()
            pk = account.id
            url = reverse('item:account_detail', kwargs={'pk': pk})
            return redirect(to=url)
    else:
        form = AccountForm
    context = {'form': form}
    return render(request, 'item/account_register.html', context)

def account_update(request, pk):
    account = Account.objects.get(id=pk)
    if request.method == 'POST':
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            account = form.save(commit=False)
            account.save()
            pk = account.id
            url = reverse('item:account_detail', kwargs={'pk': pk})
            return redirect(to=url)
    else:
        form = AccountForm(instance=account)
    context = {'form': form}
    return render(request, 'item/account_register.html', context)

def account_delete(request, pk):
    account = Account.objects.get(id=pk)
    account.delete()

    url = reverse('item:account_list')
    return redirect(to=url)