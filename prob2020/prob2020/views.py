from django.shortcuts import render, HttpResponse
from django.http import FileResponse

def main_page(request):
    return render(request, "main.html")


def quiz01pdf(request):
    buffer = open("./templates/quiz01.pdf", "rb")
    response = FileResponse(buffer, filename="quiz01.pdf", as_attachment=True)
    response['Content-Type'] = 'application/pdf-stream'

    return response

def quiz01anspdf(request):
    buffer = open("./templates/quiz01ans.pdf", "rb")
    response = FileResponse(buffer, filename="quiz01ans.pdf", as_attachment=True)
    response['Content-Type'] = 'application/pdf-stream'

    return response


def tips01pdf(request):
    buffer = open("./templates/tips01.pdf", "rb")
    response = FileResponse(buffer, filename="tips01.pdf", as_attachment=True)
    response['Content-Type'] = 'application/pdf-stream'

    return response

def ans01pdf(request):
    buffer = open("./templates/ans01.pdf", "rb")
    response = FileResponse(buffer, filename="ans01.pdf", as_attachment=True)
    response['Content-Type'] = 'application/pdf-stream'

    return response

def ppt01(request):
    buffer = open("./templates/ppt01.pptx", "rb")
    response = FileResponse(buffer, filename="ppt01.pptx", as_attachment=True)
    response['Content-Type'] = 'application/pdf-stream'

    return response
