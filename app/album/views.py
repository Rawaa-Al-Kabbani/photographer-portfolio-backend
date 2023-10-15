from django.shortcuts import render
from django.http import JsonResponse
from album.models import Image, Category, Contact, About, Website
from .forms import CategoryForm

# Create your views here.


def get_album_categories(album):
    album_categories = album.categories.all()
    result = []
    for item in album_categories:
        result.append(
            {
                "id": item.id,
                "name": item.name,
                "link": item.link,
            }
        )
    return result


def album(request):
    form = CategoryForm(request.GET)
    if not form.is_valid():
        return JsonResponse({"error": "Invalid request"}, status=400)
    slug = form.cleaned_data["slug"]
    if slug != "":
        images = Image.objects.filter(categories__link=slug)
    else:
        images = Image.objects.all()
    result = []
    for item in images:
        result.append(
            {
                "id": item.id,
                "title": item.title,
                "description": item.description,
                "photo": item.get_absolute_uri(request),
                "categories": get_album_categories(item),
            }
        )
    return JsonResponse({"album": result})


def categories(request):
    categories = Category.objects.all()
    result = []
    for item in categories:
        result.append(
            {
                "id": item.id,
                "name": item.name,
                "link": item.link,
            }
        )
    return JsonResponse({"categories": result})


def about(request):
    about = About.objects.first()
    return JsonResponse(
        {
            "about": {
                "text": about.text,
                "photo": about.get_absolute_uri(request),
            }
        }
    )


def contact(request):
    contact = Contact.objects.first()
    return JsonResponse(
        {
            "contact": {
                "title": contact.title,
                "name": contact.name,
                "email": contact.email,
                "tel": contact.tel,
            }
        }
    )


def website(request):
    website = Website.objects.first()
    return JsonResponse({"website": {"name": website.name}})
