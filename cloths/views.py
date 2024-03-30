from django.shortcuts import get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from datetime import datetime, timedelta

from .models import Cloth,Comment
from .forms import CommentForm
from cart.forms import AddToCartForm

class HighestSellingView(generic.ListView):
    model = Cloth
    template_name = 'cloths/highest_selling.html'
    context_object_name = 'cloths'
    paginate_by = 5

    def get_queryset(self):
        queryset = self.model.objects.filter(active=True,datetime_created__month=timezone.now().month).order_by('-sales')
        return queryset

class FemaleView(generic.ListView):
    queryset = Cloth.objects.filter(active=True,gender='female').order_by('-datetime_created')
    template_name = 'cloths/female_list.html'
    context_object_name = 'cloths'
    paginate_by = 10


class maleView(generic.ListView):
    queryset = Cloth.objects.filter(active=True,gender='male').order_by('-datetime_created')
    template_name = 'cloths/male_list.html'
    context_object_name = 'cloths'
    paginate_by = 10


class IndexView(generic.ListView):
    queryset = Cloth.objects.filter(active=True).order_by('-datetime_created')
    template_name = "index.html"
    context_object_name = 'cloths'


class ClothsListView(generic.ListView):
    queryset = Cloth.objects.filter(active=True).order_by('-datetime_created')
    template_name = 'cloths/cloths_list.html'
    context_object_name = 'cloths'
    paginate_by = 10


class ClothDetailView(generic.DetailView):
    model = Cloth
    template_name = 'cloths/cloth_detail.html'
    context_object_name = 'cloth'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['add_to_cart_form'] = AddToCartForm()
        return context


class CommentCreateView(LoginRequiredMixin,generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        cloth_id = int(self.kwargs['cloth_id'])
        cloth = get_object_or_404(Cloth, id=cloth_id)
        obj.cloth = cloth
        
        return super().form_valid(form)