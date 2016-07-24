from django.db.models.query_utils import Q
from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response


# Create your views here.
from demo.forms import CommentForm
from demo.models import Post


def myview(request):
    args = {}
    args['pst'] = Post.objects.all()
    args['form'] = CommentForm()

    # args += {'pst': Post.objects.all()}
    return render_to_response('indeximiz.html', args)
