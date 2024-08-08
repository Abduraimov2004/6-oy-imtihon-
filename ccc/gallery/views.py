from django.shortcuts import render
from .models import Photo, Author, Category


def photo_list(request):
    photos = Photo.objects.all()
    categories = Category.objects.all()
    authors = Author.objects.all()
    sort_option = request.GET.get('sort')
    selected_category = request.GET.get('category')
    selected_author = request.GET.get('author')



    if selected_category:
        photos = photos.filter(category_id=selected_category)
    if selected_author:
        photos = photos.filter(author_id=selected_author)
    if sort_option == 'new':
        photos = photos.order_by('-date_add')
    elif sort_option == 'last':
        photos = photos.order_by('date_add')
    elif sort_option == 'author':
        photos = photos.order_by('author__name')



    context = {
        'photos': photos,
        'categories': categories,
        'authors': authors,
        'selected_category': selected_category,
        'selected_author': selected_author,
        'sort_option': sort_option,
    }
    return render(request, 'home.html', context)


def photo_detail(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    if not request.session.get('gallery'):
        request.session['gallery'] = []
        request.session['gallery'].append(photo_id)
        photo.views += 1
    if photo_id not in request.session.get('gallery'):
        photo.views += 1
        request.session['gallery'].append(photo_id)
        request.session.save()
    photo.save()

    return render(request, 'detail.html', {'photo': photo})
