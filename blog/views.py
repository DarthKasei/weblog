from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse

from dbe.blog.models import *

# Create your views here.

def main(request):
	posts = Post.objects.all().order_by("-created")
	paginator = Paginator(posts, 2)

	try: 
	    page = int(request.GET.get("page",'1'))
	except ValueError: page = 1

	try:
	    posts = paginator.page(page)
	except (InvalidPage, EmptyPage):
	    posts = paginator.page(paginator.num_pages)

	return render_to_reponse("list.html", dict(posts=posts, user=request.user))
