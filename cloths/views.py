from django.shortcuts import get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.contrib import messages
from django.utils.translation import gettext as _

from .models import Cloth,Comment
from .forms import CommentForm
from cart.forms import AddToCartForm


class HighestSellingView(generic.ListView):
    model = Cloth
    template_name = 'cloths/highest_selling.html'
    context_object_name = 'cloths'
    paginate_by = 10

    def get_queryset(self):
        queryset = self.model.objects.filter(datetime_created__month=timezone.now().month).order_by('-sales')
        return queryset


class FemaleView(generic.ListView):
    queryset = Cloth.objects.filter(gender='female').order_by('-datetime_created')
    template_name = 'cloths/female_list.html'
    context_object_name = 'cloths'
    paginate_by = 10


class MaleView(generic.ListView):
    queryset = Cloth.objects.filter(gender='male').order_by('-datetime_created')
    template_name = 'cloths/male_list.html'
    context_object_name = 'cloths'
    paginate_by = 10


class ClothsListView(generic.ListView):
    queryset = Cloth.objects.all().order_by('-datetime_created')
    template_name = 'cloths/cloths_list.html'
    context_object_name = 'cloths'
    paginate_by = 10


class ClothDetailView(generic.DetailView):
    model = Cloth
    template_name = 'cloths/cloth_detail.html'
    context_object_name = 'cloth'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['add_to_cart_form'] = AddToCartForm()
        return context


class CommentCreateView(LoginRequiredMixin,generic.CreateView):
    model = Comment
    form_class = CommentForm
    redirect_field_name = ""

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        cloth_slug = self.kwargs.get("slug")
        cloth = get_object_or_404(Cloth, slug=cloth_slug)
        obj.cloth = cloth

        if obj.author.is_superuser and obj.author.is_staff:
            obj.active = True
        else :
            messages.success(self.request, _("Your comment has been sent and it will show after we've checked it"))
        
        return super().form_valid(form)