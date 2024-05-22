from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class AdminUsuario(admin.ModelAdmin):
    list_display = ['id', 'nome', 'categoria']
    list_display_links = ('id', 'nome', 'categoria',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Usuario, AdminUsuario)


class AdminFormato1(admin.ModelAdmin):
    list_display = ['categoria']
    list_display_links = ('categoria',)
    search_fields = ('categoria',)
    list_per_page = 10

admin.site.register(Formato,AdminFormato1)

class AdminGenero(admin.ModelAdmin):
    list_display = ['nome']
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Genero,AdminGenero)


class AdminCategoriaLivro(admin.ModelAdmin):
    list_display = ['nome']
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(CategoriaLivro,AdminCategoriaLivro)


class AdminLivro(admin.ModelAdmin):
    list_display = ['nome', 'ano', 'qtd_paginas','numero_edicao', 'descricao', 'valor_emprestimo', 'qtd_estoque', 'status']
    list_display_links = ('nome','valor_emprestimo','qtd_estoque',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Livro,AdminLivro)


class AdminEmprestimo(admin.ModelAdmin):
    list_display = ['livroFK','data_emprestimo', 'data_devolucao_prevista', 'data_devolucao_realizada', 'valor_total_emprestimo', 'status']
    list_display_links = ('livroFK','valor_total_emprestimo', 'status',)
    search_fields = ('livroFK',)
    list_per_page = 10

admin.site.register(Emprestimo,AdminEmprestimo)


class AdminItemEmprestimo(admin.ModelAdmin):
    list_display = ['livroFK', 'emprestimoFK']
    list_display_links = ('livroFK', 'emprestimoFK',)
    search_fields = ('livroFK',)
    list_per_page = 10

admin.site.register(itemEmprestimo,AdminItemEmprestimo)