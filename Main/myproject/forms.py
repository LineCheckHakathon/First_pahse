from django import forms
from .models import User, ProcessGuideline, Stock, Order, Chat

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['email', 'password', 'name']

    def __str__(self):
        return self.instance.name

class ProcessGuidelineForm(forms.ModelForm):
    class Meta:
        model = ProcessGuideline
        fields = ['step_name', 'user', 'step_detail', 'step_number']

    def __str__(self):
        return self.instance.step_name

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['material_name', 'quantity', 'place', 'user']

    def __str__(self):
        return self.instance.material_name

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'phone_number', 'address', 'product_name', 'quantity', 'deadline', 'weight', 'status', 'user']

    def __str__(self):
        return self.instance.product_name

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['order', 'sender', 'content', 'created_at']

    def __str__(self):
        return f"Chat on order {self.instance.order.id} by {self.instance.sender}"
