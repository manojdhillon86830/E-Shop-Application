# from django.shortcuts import render
# from .models.product import Product
# from .models.category import Category



# # Create your views here.
# def index(request):
#     products = None
#     categories = Category.get_all_categories();
#     categoryID = request.GET.get('category')
#     if categoryID:
#         products = Product.get_all_products_by_categoryid(categoryID)
#     else:
#         products = Product.get_all_products();
#     data = {}
#     data['products'] = products
#     data['categories'] = categories
    
#     return render(request, 'index.html', data)
    # return render(request, 'orders/order.html')



# def registerUser(request):
#     postData = request.POST
#     first_name = postData.get('firstname')
#     last_name = postData.get('lastname')
#     phone = postData.get('phone')
#     email = postData.get('email')
#     password = postData.get('password')
    
#     value = {
#         'first_name': first_name,
#         'last_name': last_name,
#         'phone': phone,
#         'email': email
#     }
#     error_message = None

#     customer = Customer(first_name=first_name,
#                         last_name=last_name,
#                         phone=phone,
#                         email=email,
#                         password=password)
    
#     error_message = validateCustomer(customer)
    
#     if not error_message:
#         print(first_name, last_name, phone, email, password)
#         customer.password = make_password(customer.password)
#         customer.register()
#         return redirect('homepage')
#     else:
#         data = {
#             'error': error_message,
#             'values': value
#         }
#         return render(request, 'signup.html', data)

# class Signup(View):
#     def get(self, request):
#         return render(request,'signup.html')
#     def post(self, request):
#         postData = request.POST
#         first_name = postData.get('firstname')
#         last_name = postData.get('lastname')
#         phone = postData.get('phone')
#         email = postData.get('email')
#         password = postData.get('password')
    
#         value = {
#             'first_name': first_name,
#             'last_name': last_name,
#             'phone': phone,
#             'email': email
#         }
#         error_message = None

#         customer=Customer(first_name=first_name,
#                         last_name=last_name,
#                         phone=phone,
#                         email=email,
#                         password=password)
    
#         error_message = self.validateCustomer(customer)
    
#         if not error_message:
#             print(first_name, last_name, phone, email, password)
#             customer.password = make_password(customer.password)
#             customer.register()
#             return redirect('homepage')
#         else:
#             data = {
#                 'error': error_message,
#                 'values': value
#             }
#             return render(request, 'signup.html', data) 

#     def validateCustomer(self, customer):
#         error_message = None;
#         if(not customer.first_name):
#             error_message = 'First Name Required !'
#         elif len(customer.first_name) < 4:
#             error_message = 'First Name must be 4 char long'
#         elif len(customer.phone) < 10:
#             error_message = 'Phone must be 10 char long'
#         elif len(customer.password) < 7:
#             error_message = 'Password must be 7 char long'
#         elif customer.isExists():
#             error_message = 'Email Already Registered !'

#         return error_message    

# def signup(request):
#     if request.method == 'GET':
#         return render(request,'signup.html')
#     else:
#         return registerUser(request)

# class Login(View):
#     def get(self, request):
#         return render(request, 'login.html')
#     def post(self, request):
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         customer = Customer.get_customer_by_email(email)
#         if customer:
#             flag = check_password(password, customer.password)
#             if flag:
#                 return redirect('homepage')
#             else:
#                 error_message = 'Email and Password invalid !'
#         else:
#             error_message = 'Email and Password invalid'
#         return render(request, 'login.html', {'error': error_message})       

# def login(request):
#     if request.method == 'GET':
#         return render(request, 'login.html')
#     else:
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         customer = Customer.get_customer_by_email(email)
#         if customer:
#             flag = check_password(password, customer.password)
#             if flag:
#                 return redirect('homepage')
#             else:
#                 error_message = 'Email and Password invalid'
#         else:
#             error_message = 'Email and Password invalid'
#         return render(request, 'login.html', {'error': error_message})