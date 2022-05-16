from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader

from app_coder.models import Course


def template_using_context(self, name: str = "name", last_name: str = "last_name"):

    my_html = open(
        "/home/jere/Projects/Coder_Python/project_Coder_18/project_18/project_18/templates/template.html"
    )

    my_template = Template(my_html.read())
    # Se carga en memoria nuestro documento, template
    ##Import template & contex, with: "from django.template import Template, Context"

    my_html.close()  # Close file

    context_dict = {
        "name": name,
        "last_name": last_name,
        "now": datetime.now(),
        "class_grades": [4, 5, 8, 7, 9],
    }

    my_context = Context(
        context_dict
    )  # Por mas que no haya parametros para pasarle, se crea igual.

    document = my_template.render(
        my_context
    )  # Aca se renderiza el "template" en  el "document"

    return HttpResponse(document)


def template_using_loader(self, name: str = "name", last_name: str = "last_name"):

    my_template = loader.get_template("template_loader.html")

    context_dict = {
        "name": name,
        "last_name": last_name,
        "now": datetime.now(),
        "class_grades": [4, 5, 8, 7, 9],
    }
    document = my_template.render(
        context_dict
    )  # Aca se renderiza el "template" en  el "document"

    return HttpResponse(document)


def new_course(self, name: str = "course", code: int = 0):

    template = loader.get_template("template_course.html")

    course = Course(name=name, code=code)
    course.save()  # save into the DB

    context_dict = {"course": course}

    render = template.render(context_dict)
    return HttpResponse(render)


def list_course(self, name: str = "course", code: int = 0):

    template = loader.get_template("template_course.html")

    course = Course(name=name, code=code)
    course.save()  # save into the DB

    context_dict = {"course": course}

    render = template.render(context_dict)
    return HttpResponse(render)
