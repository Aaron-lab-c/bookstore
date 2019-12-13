from django.shortcuts import render, redirect
from article.models import Article, Comment
from article.forms import ArticleForm
from django.contrib import messages




def article(request):
    '''
    Render the article page
    '''
    
    articles = {article:Comment.objects.filter(article=article) for article in Article.objects.all()}
    context = {'articles':articles}
    return render(request, 'article/article.html', context)



def articleCreate(request):
    '''
    Create a new article instance
        1. If method is GET, render an empty form
        2. If method is POST,
           * validate the form and display error messages if the form is invalid
           * else, save it to the model and redirect to the article page
    '''
    template = 'article/articleCreate.html'
    if request.method == 'GET':
        
        return render(request, template, {'articleForm':ArticleForm()})
    
    
    
    # POST
    articleForm = ArticleForm(request.POST)
    if not articleForm.is_valid():
        return render(request, template, {'articleForm':articleForm})

    articleForm.save()
    messages.success(request, '文章已新增')

    return redirect('article:article')