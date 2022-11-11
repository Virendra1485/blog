from django.shortcuts import render

# Create your views here.
posts = [
    {
        "author": "Virendra Singh Rawat",
        "title": "blog1",
        "content": "First content",
        "date_posted": "August 27, 2022"
    },
    {
        "author": "Bhavya",
        "title": "blog2",
        "content": "Second content",
        "date_posted": "August 28, 2022"
    }
]


def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "Blog"})
