from django.shortcuts import render, HttpResponse
from django.http import FileResponse

def main_page(request):
    return render(request, "main.html")


def quiz01pdf(request):
    buffer = open("./templates/quiz01.pdf", "rb")
    response = FileResponse(buffer, filename="quiz01.pdf", as_attachment=True)
    response['Content-Type'] = 'application/pdf-stream'

    return response


def quiz02(request):
    buffer = open("./templates/quiz02.pdf", "rb")
    response = FileResponse(buffer, filename="quiz02.pdf", as_attachment=True)
    response['Content-Type'] = 'application/pdf-stream'

    return response

def test01(request):
    buffer = open("./templates/test01.pdf", "rb")
    response = FileResponse(buffer, filename="test01.pdf", as_attachment=True)
    response['Content-Type'] = 'application/pdf-stream'

    return response

def test01ans(request):
    buffer = open("./templates/test01ans.pdf", "rb")
    response = FileResponse(buffer, filename="test01ans.pdf", as_attachment=True)
    response['Content-Type'] = 'application/pdf-stream'

    return response

def quiz01ans(request):
    buffer = open("./templates/quiz01ans.pdf", "rb")
    response = FileResponse(buffer, filename="quiz01ans.pdf", as_attachment=True)
    response['Content-Type'] = 'application/pdf-stream'

    return response

def quiz02ans(request):
    buffer = open("./templates/quiz02ans.pdf", "rb")
    response = FileResponse(buffer, filename="quiz02ans.pdf", as_attachment=True)
    response['Content-Type'] = 'application/pdf-stream'

    return response



def tips01pdf(request):
    buffer = open("./templates/tips01.pdf", "rb")
    response = FileResponse(buffer, filename="tips01.pdf", as_attachment=True)
    response['Content-Type'] = 'application/pdf-stream'

    return response

def tips02(request):
    buffer = open("./templates/tips02.pdf", "rb")
    response = FileResponse(buffer, filename="tips02.pdf", as_attachment=True)
    response['Content-Type'] = 'application/pdf-stream'

    return response

def tips03(request):
    buffer = open("./templates/tips03.pdf", "rb")
    response = FileResponse(buffer, filename="tips03.pdf", as_attachment=True)
    response['Content-Type'] = 'application/pdf-stream'

    return response


def tips04(request):
    buffer = open("./templates/tips04.pdf", "rb")
    response = FileResponse(buffer, filename="tips04.pdf", as_attachment=True)
    response['Content-Type'] = 'application/pdf-stream'

    return response

def tips06(request):
    buffer = open("./templates/tips06.pdf", "rb")
    response = FileResponse(buffer, filename="tips06.pdf", as_attachment=True)
    response['Content-Type'] = 'application/pdf-stream'

    return response

def tips07(request):
    buffer = open("./templates/tips07.pdf", "rb")
    response = FileResponse(buffer, filename="tips07.pdf", as_attachment=True)
    response['Content-Type'] = 'application/pdf-stream'

    return response


def ans01pdf(request):
    buffer = open("./templates/ans01.pdf", "rb")
    response = FileResponse(buffer, filename="ans01.pdf", as_attachment=True)
    response['Content-Type'] = 'application/pdf-stream'

    return response

def ans02(request):
    buffer = open("./templates/ans02.pdf", "rb")
    response = FileResponse(buffer, filename="ans02.pdf", as_attachment=True)
    response['Content-Type'] = 'application/pdf-stream'

    return response


def ppt01(request):
    buffer = open("./templates/ppt01.pptx", "rb")
    response = FileResponse(buffer, filename="ppt01.pptx", as_attachment=True)
    response['Content-Type'] = 'application/pdf-stream'

    return response

def ppt02(request):
    buffer = open("./templates/ppt02.pptx", "rb")
    response = FileResponse(buffer, filename="ppt02.pptx", as_attachment=True)
    response['Content-Type'] = 'application/pdf-stream'

    return response

def ppt03(request):
    buffer = open("./templates/ppt03.pptx", "rb")
    response = FileResponse(buffer, filename="ppt03.pptx", as_attachment=True)
    response['Content-Type'] = 'application/pdf-stream'

    return response

def ppt04(request):
    buffer = open("./templates/ppt04.pptx", "rb")
    response = FileResponse(buffer, filename="ppt04.pptx", as_attachment=True)
    response['Content-Type'] = 'application/pdf-stream'

    return response

def ppt06(request):
    buffer = open("./templates/ppt06.pptx", "rb")
    response = FileResponse(buffer, filename="ppt06.pptx", as_attachment=True)
    response['Content-Type'] = 'application/pdf-stream'

    return response

def ppt07(request):
    buffer = open("./templates/ppt07.pptx", "rb")
    response = FileResponse(buffer, filename="ppt07.pptx", as_attachment=True)
    response['Content-Type'] = 'application/pdf-stream'

    return response

def ppt08(request):
    buffer = open("./templates/ppt08.pptx", "rb")
    response = FileResponse(buffer, filename="ppt08.pptx", as_attachment=True)
    response['Content-Type'] = 'application/pdf-stream'

    return response
