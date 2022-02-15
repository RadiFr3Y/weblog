from django.shortcuts import render, get_object_or_404
from .models import PostModel, WorkModel, Comment
from .forms import CommentForm

def indexView(request):
    context = {
        'post': PostModel.objects.all()
    }
    return render(request, 'index.html', context)

def contactView(request):
    return render(request, 'contact.html')

def singleView(request):
    return render(request, 'single.html')

def workView(request):
    context = {
        'work': WorkModel.objects.all()
    }
    return render(request, 'work.html', context)

def aboutView(request):
    return render(request, 'about.html')

# def slugView(request, slug):
#     context = {
#         'post': PostModel.objects.get(slug=slug)
#     }
#     return render(request, 'slug.html', context)



def SlugView(request, slug):
    template_name = 'slug.html'
    post = get_object_or_404(PostModel, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'postslg': PostModel.objects.get(slug=slug)})