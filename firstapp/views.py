from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse



"""
MVT - Model View Template
    model - data base
    View - Business Logic
    Template - html page


MVC - Model View Controller
    Model - database
    View - html page
    Contoller - Business logic

"""


# Create your views here.

def home(request):
    return HttpResponse("hello world")

def jsonOutput(request):
    return JsonResponse({
                    "postId": 1,
                    "id": 2,
                    "name": "quo vero reiciendis velit similique earum",
                    "email": "Jayne_Kuhic@sydney.com",
                    "body": "est natus enim nihil est dolore omnis voluptatem numquam\net omnis occaecati quod ullam at\nvoluptatem error expedita pariatur\nnihil sint nostrum voluptatem reiciendis et"
                })


studentsData =  [
    {
        "name": "Alice Smith",
        "age": 20,
        "contact": "123-456-7890",
        "email": "alice.smith@example.com"
    },
    {
        "name": "Bob Johnson",
        "age": 11,
        "contact": "234-567-8901",
        "email": "bob.johnson@example.com"
    },
    {
        "name": "Charlie Brown",
        "age": 21,
        "contact": "345-678-9012",
        "email": "charlie.brown@example.com"
    },
    {
        "name": "Diana Prince",
        "age": 19,
        "contact": "456-789-0123",
        "email": "diana.prince@example.com"
    },
    {
        "name": "Edward Davis",
        "age": 17,
        "contact": "567-890-1234",
        "email": "edward.davis@example.com"
    },
    {
        "name": "Fiona Green",
        "age": 20,
        "contact": "678-901-2345",
        "email": "fiona.green@example.com"
    },
    {
        "name": "George Wilson",
        "age": 18,
        "contact": "789-012-3456",
        "email": "george.wilson@example.com"
    },
    {
        "name": "Hannah Lee",
        "age": 21,
        "contact": "890-123-4567",
        "email": "hannah.lee@example.com"
    },
    {
        "name": "Ian Martinez",
        "age": 20,
        "contact": "901-234-5678",
        "email": "ian.martinez@example.com" 
    },
    {
        "name": "Jessica Taylor",
        "age": 15,
        "contact": "012-345-6789",
        "email": "jessica.taylor@example.com"
    },
    {
        "name": "Kevin Thompson",
        "age": 19,
        "contact": "123-456-7890",
        "email": "kevin.thompson@example.com"
    },
    {
        "name": "Lisa Wilson",
        "age": 20,
        "contact": "234-567-8901",
        "email": "lisa.wilson@example.com"
    },
    {
        "name": "Michael Johnson",
        "age": 22,
        "contact": "345-678-9012",
        "email": "michael.johnson@example.com"
    }
]



def index(request):
    return render(request, "index.html", { "studentsData": studentsData})


def main(request):
    return render(request, "firstapp/main.html")


def home(request):
    return render(request, "firstapp/home.html",{ "studentsData": studentsData})

def about(request):
    return render(request, "firstapp/about.html")



def formView(request):
    if request.method == "POST":
        print(request.POST)
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        contact = request.POST["contact"]

        context = {
            "email" : email,
            "username" : username,
            "password" : password,
            "contact" : contact,
        }

        return render(request, "firstapp/form.html", context)
        
    return render(request, "firstapp/form.html")



def calculator(request):
    if request.method == "POST":
        value1 = int(request.POST["num1"])
        value2 = int(request.POST["num2"])

        # value1 = int(value1)
        # value2 = int(value2)

        sumValue = value1 + value2
        subValue = abs(value1 - value2)
        productValue = value1 * value2
        divValue = value1 / value2

        context = {
            "value1": value1,
            "value2" : value2,
            "sumValue":sumValue,
            "subValue": subValue,
            "productValue" : productValue,
            "divValue" : divValue
        }

        return render(request, "firstapp/calculator.html", context)


        ...
    return render(request, "firstapp/calculator.html")

