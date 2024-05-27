from django.shortcuts import render,redirect
from django.contrib import messages
from category.models import CategoryModel
from django.views.generic import DetailView
from borrow.models import BorrowingModel
from books.models import BookModel
from accounts.models import UserLibraryAccount
from borrow.forms import ReviewForm
from django.contrib.auth.models import AnonymousUser,User
from django.utils.encoding import force_str
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_email(subject,template,user,amount):
    message=render_to_string(template,{
        "user":user,
        "amount":amount,
    })
    send_email=EmailMultiAlternatives(subject,"",to=[user.email])
    send_email.attach_alternative(message, "text/html")
    send_email.send()

def Home(request,category_slug=None):
    categorys=CategoryModel.objects.all()
    books=BookModel.objects.all()
    if category_slug is not None:
        category=CategoryModel.objects.get(slug=category_slug)
        books=BookModel.objects.filter(category=category)
    return render(request,"index.html",{"category":categorys,"books":books})

class BookDetailsView(DetailView):
    model = BookModel
    template_name = 'book_detail.html'
    context_object_name = 'book'

    def post(self, request, *args, **kwargs):
        book_object = self.get_object()
        user_review=UserLibraryAccount.objects.get(user=self.request.user)
        book_user=request.user
        if "book_borrow" in request.POST:
            if book_user.account.balance >= book_object.price:
                book_user.account.balance -= book_object.price
                book_user.save()
                BorrowingModel.objects.create(user=book_user, book=book_object)
                messages.success(request, 'Book borrowed successfully! ✅')
                send_email("Borrow Book","borrow_email.html",self.request.user,book_object.price)
                
            else:
                messages.warning(request, 'Insufficient balance to borrow this book.')

        if request.method=="POST":
            if "submit_review" in request.POST:
                form = ReviewForm(data=self.request.POST)
                if form.is_valid():
                    new_review = form.save(commit=False)
                    new_review.book = book_object
                    new_review.name=user_review.get_full_name()
                    new_review.email=user_review.email
                    new_review.save()
                    send_email("Review Book","review_email.html",self.request.user,0)
                    messages.success(request, 'Review Submitted successfully! ✅')
                else:
                    messages.error(request,"Wrong Submitted ❌")
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        book=self.get_object()
        context["book"] = book
        user=self.request.user
        user_str=force_str(user)
        if not isinstance(user,AnonymousUser):
            user_instance=User.objects.get(username=user_str)
            has_borrow_book=BorrowingModel.objects.filter(user=user_instance,book=self.get_object()).exists()
        else:
             has_borrow_book=False
             
        if has_borrow_book:
             context["review_form"]=ReviewForm()
        context["review_body"]=book.reviews.all()
        return context
    
def BookReturn(request,id):
    borrow_book=BorrowingModel.objects.get(pk=id)
    userProfile=request.user
    userProfile.account.balance+=borrow_book.book.price
    userProfile.save()
    borrow_book.delete()
    messages.success(request,"Your Borrow book return Successfully ✅")
    send_email("Return Book","return_email.html",request.user,0)
    return redirect("Profile")


