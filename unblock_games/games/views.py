from django.shortcuts import render, get_object_or_404
from .models import Game, Category
from django.core.paginator import Paginator

def home(request):
    categories = Category.objects.all()
    games = Game.objects.all().order_by('-created_at')
    paginator = Paginator(games, 1)  # Show 6 games per page
    page_number = request.GET.get('page')  # Get the current page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the games for the current page
    query = request.GET.get('search')
    selected_category = request.GET.get('category')

    if query:
        games = games.filter(title__icontains=query)
    if selected_category:
        games = games.filter(category__name=selected_category)

    return render(request, 'games/shop.html', {
        'games': games,
        'categories': categories,
        'selected_category': selected_category,
        'query': query,
        'page_obj': page_obj
    })

def game_detail(request, slug):
    
    game = get_object_or_404(Game, slug=slug)
    related_games = Game.objects.filter(category=game.category).exclude(id=game.id).distinct()[:6]
    iframe_code = ""
    if game.website_url:
        iframe_code = f'<iframe src="{game.website_url}" width="100%" height="600px" frameborder="0" allowfullscreen></iframe>'
    return render(request, 'games/product-details.html', {
        'game': game,
        'iframe_code': iframe_code,
        'related_games': related_games,
    })