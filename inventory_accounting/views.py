from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from .models import Section, Employee, Premises, Supplier, Computer
# from django.db.models import Sum
import xlwt


def index(request):
    return render(request, 'index.html')


def add(request):
    return render(request, 'add.html')


def report(request):
    employees = Employee.objects.all()
    sections = Section.objects.all()
    premises = Premises.objects.all()
    computers = Computer.objects.all()
    context= {
        "employees": employees,
        "sections": sections,
        "premises": premises,
        "computers": computers,
    }
    return render(request, 'report.html', context)


def form_add_section(request):
    return render(request, 'form_add_section.html')


def form_add_employee(request):
    return render(request, 'form_add_employee.html')


def form_add_supplier(request):
    return render(request, 'form_add_supplier.html')


def form_add_premises(request):
    sections = Section.objects.all()
    return render(request, 'form_add_premises.html', {"sections": sections})


def form_add_computer(request):
    employees = Employee.objects.all()
    premises = Premises.objects.all()
    suppliers = Supplier.objects.all()
    return render(request, 'form_add_computer.html', {"employees": employees, "premises": premises,
                                                      "suppliers": suppliers})


def edit(request):
    return render(request, 'edit.html')


def edit_computer(request):
    computers = Computer.objects.all()
    return render(request, 'edit_computer.html', {"computers": computers})


def edit_employee(request):
    employees = Employee.objects.all()
    context = {"employees": employees}
    return render(request, 'edit_employee.html', context)


def edit_premises(request):
    premises = Premises.objects.all()
    return render(request, 'edit_premises.html', {"premises": premises})


def edit_section(request):
    sections = Section.objects.all()
    return render(request, 'edit_section.html', {"sections": sections})


def edit_supplier(request):
    suppliers = Supplier.objects.all()
    return render(request, 'edit_supplier.html', {"suppliers": suppliers})


def add_section(request):
    if request.method == 'POST':
        section_id = request.POST.get('section_id')
        section_name = request.POST.get('section_name')
        data = Section(section_id=section_id, section_name=section_name)
        data.save()
    return HttpResponseRedirect("/")


def add_employee(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        birth_date = request.POST.get('birth_date')

        data = Employee(employee_id=employee_id, name=name,
                        gender=gender,birth_date=birth_date)
        data.save()
    return HttpResponseRedirect("/")


def add_premises(request):
    if request.method == 'POST':
        premises_id = request.POST.get('premises_id')
        p_section_name = request.POST.get('p_section_name')
        data = Premises(premises_id=premises_id, p_section_name=p_section_name)
        data.save()
    return HttpResponseRedirect("/")


def add_supplier(request):
    if request.method == 'POST':
        supplier_id = request.POST.get('supplier_id')
        company_name = request.POST.get('company_name')
        City = request.POST.get('City')
        inn = request.POST.get('inn')
        data = Supplier(supplier_id=supplier_id, company_name=company_name, City=City, inn=inn)
        data.save()
    return HttpResponseRedirect("/")


def add_computer(request):
    if request.method == 'POST':
        computer_id = request.POST.get('computer_id')

        c_employee_name = request.POST.get('c_employee_name')
        c_premises_id = request.POST.get('c_premises_id')
        c_supplier_company_name = request.POST.get('c_supplier_company_name')

        start_date = request.POST.get('start_date')
        amortisation_period = request.POST.get('amortisation_period')

        accounting_date = request.POST.get('accounting_date')
        status = request.POST.get('status')

        cpu = request.POST.get('cpu')
        gpu = request.POST.get('gpu')
        ram = request.POST.get('ram')

        manufacturer = request.POST.get('manufacturer')

        rom = request.POST.get('rom')
        data = Computer(computer_id=computer_id, c_employee_name=c_employee_name, c_premises_id=c_premises_id,
                        c_supplier_company_name=c_supplier_company_name,start_date=start_date,accounting_date=accounting_date, amortisation_period=amortisation_period,
                        manufacturer=manufacturer, cpu=cpu, gpu=gpu, ram=ram, rom=rom, status=status)
        data.save()
    return HttpResponseRedirect("/")


def delete_employee(request, id):
    try:
        row = Employee.objects.get(id=id)
        row.delete()
        return HttpResponseRedirect("/edit")
    except Employee.DoesNotExist:
        return HttpResponseNotFound("<h2>Employee not found</h2>")


def delete_supplier(request, id):
    try:
        row = Supplier.objects.get(id=id)
        row.delete()
        return HttpResponseRedirect("/edit")
    except Supplier.DoesNotExist:
        return HttpResponseNotFound("<h2>Supplier not found</h2>")


def delete_computer(request, id):
    try:
        row = Computer.objects.get(id=id)
        row.delete()
        return HttpResponseRedirect("/edit")
    except Computer.DoesNotExist:
        return HttpResponseNotFound("<h2>Computer not found</h2>")


def delete_section(request, id):
    try:
        row = Section.objects.get(id=id)
        row.delete()
        return HttpResponseRedirect("/edit")
    except Section.DoesNotExist:
        return HttpResponseNotFound("<h2>Section not found</h2>")


def form_edit_employee(request, id):
    try:
        employee = Employee.objects.get(id=id)
        if request.method == "POST":
            employee.employee_id = request.POST.get("employee_id")
            employee.name = request.POST.get("name")
            employee.gender = request.POST.get("gender")
            employee.birth_date = request.POST.get("birth_date")
            employee.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "form_edit_employee.html", {"employee": employee})
    except employee.DoesNotExist:
        return HttpResponseNotFound("<h2>Employee not found</h2>")


def form_edit_supplier(request, id):
    try:
        supplier = Supplier.objects.get(id=id)
        if request.method == "POST":
            supplier.supplier_id = request.POST.get("supplier_id")
            supplier.company_name = request.POST.get("company_name")
            supplier.City = request.POST.get("City")
            supplier.inn = request.POST.get("inn")
            supplier.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "form_edit_supplier.html", {"supplier": supplier})
    except supplier.DoesNotExist:
        return HttpResponseNotFound("<h2>Supplier not found</h2>")


def form_edit_premises(request, id):
    try:
        premises = Premises.objects.get(id=id)
        sections = Section.objects.all()
        if request.method == "POST":
            premises.premises_id = request.POST.get("premises_id")
            premises.p_section_id = request.POST.get("p_section_name")
            premises.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "form_edit_premises.html", {"premises": premises, "sections": sections})
    except premises.DoesNotExist:
        return HttpResponseNotFound("<h2>Premises not found</h2>")


def form_edit_section(request, id):
    try:
        section = Section.objects.get(id=id)
        if request.method == "POST":
            section.section_id = request.POST.get("section_id")
            section.section_name = request.POST.get("section_name")
            section.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "form_edit_section.html", {"section": section})
    except section.DoesNotExist:
        return HttpResponseNotFound("<h2>Section not found</h2>")


def form_edit_computer(request, id):
    try:
        computer = Computer.objects.get(id=id)
        employees = Employee.objects.all()
        premises = Premises.objects.all()
        suppliers = Supplier.objects.all()
        if request.method == "POST":
            computer.computer_id = request.POST.get("computer_id")
            computer.c_employee_name = request.POST.get("c_employee_name")
            computer.c_premises_id = request.POST.get("c_premises_id")
            computer.c_supplier_company_name = request.POST.get("c_supplier_company_name")
            computer.start_date = request.POST.get("start_date")
            computer.accounting_date = request.POST.get("accounting_date")
            computer.amortisation_period = request.POST.get("amortisation_period")
            computer.manufacturer = request.POST.get("manufacturer")
            computer.cpu = request.POST.get("cpu")
            computer.gpu = request.POST.get("gpu")
            computer.ram = request.POST.get("ram")
            computer.rom = request.POST.get("rom")
            computer.status = request.POST.get("status")
            computer.save() 
            return HttpResponseRedirect("/")
        else:
            return render(request, "form_edit_computer.html", {"computer": computer, "employees": employees, 
                                                               "premises": premises, "suppliers":suppliers})
    except computer.DoesNotExist:
        return HttpResponseNotFound("<h2>Computer not found</h2>")


def delete_premises(request, id):
    try:
        row = Premises.objects.get(id=id)
        row.delete()
        return HttpResponseRedirect("/edit")
    except Premises.DoesNotExist:
        return HttpResponseNotFound("<h2>Section not found</h2>")


def date_export_xls(request):
    if request.method == 'POST':
        date_start = request.POST.get('date_start')
        date_end = request.POST.get('date_end')
        response = HttpResponse(content_type='application/inventory_accounting')
        response['Content-Disposition'] = 'attachment; filename="computer.xlsx"'
 
        wb = xlwt.Workbook(encoding='utf-8')

        main_ws = wb.add_sheet('Computer')

        row_num = 0

        head_style = xlwt.easyxf('font: bold 1;alignment: wrap True; align: vert centre, horiz centre; border: top thick, right thick, bottom thick, left thick; align: wrap 1;')
 
        main_columns = ['ID','Дата постановки на учет', 'ФИО сотрудника', 'Поставщик ','Производитель', 'Процессор', 'Видеокарта', 'ОЗУ, гб.', 'ПЗУ, тб.', 'Статус']

        for col_num in range(len(main_columns)):
            main_ws.write(row_num, col_num, main_columns[col_num], head_style)
 

        main_ws.col(0).width = 3000
        main_ws.col(1).width = 10000
        main_ws.col(2).width = 7000
        main_ws.col(3).width = 10000
        main_ws.col(4).width = 10000
        main_ws.col(5).width = 10000
        main_ws.col(6).width = 10000


        date_style = xlwt.XFStyle()
        date_style.num_format_str='dd/mm/yyyy'
        
        font = xlwt.Font()
        font.bold = False
        font.height = 200
        date_style.font = font
        
        borders = xlwt.Borders()
        borders.left = 2
        borders.right = 2
        borders.top = 2
        borders.bottom = 2

        date_style.borders = borders                

        main_style = xlwt.easyxf(
            'font: bold 0, height 200; alignment: wrap True; border: top thick, right thick, bottom thick, left thick')

        rows_table = (Computer.objects.all().values_list('computer_id', 'accounting_date', 'c_employee_name', 'c_supplier_company_name', 
                                              'manufacturer', 'cpu', 'gpu', 'ram', 'rom', 'status').filter(accounting_date__range=[date_start,date_end]))

        for row in rows_table:
            row_num += 1
            for col_num in range(len(row)):
                if (col_num == 1):
                    main_ws.write(row_num, col_num, row[col_num], date_style)
                else:
                    main_ws.write(row_num, col_num, row[col_num], main_style)

    
    
        wb.save(response)
        return response


def employee_export_xls(request):
    if request.method == 'POST':
        employee_name = request.POST.get('name')
        response = HttpResponse(content_type='application/inventory_accounting')
        response['Content-Disposition'] = 'attachment; filename="computer.xlsx"'
 
        wb = xlwt.Workbook(encoding='utf-8')

        main_ws = wb.add_sheet('Computer')

        row_num = 0

        head_style = xlwt.easyxf('font: bold 1;alignment: wrap True; align: vert centre, horiz centre; border: top thick, right thick, bottom thick, left thick; align: wrap 1;')
 
        main_columns = ['ID', 'ФИО сотрудника', 'Дата начала эксплуатации', 'Дата постановки на учет', 'Поставщик', 'Производитель', 'Процессор', 'Видеокарта', 'ОЗУ, гб.', 'ПЗУ, тб.', 'Статус']

        for col_num in range(len(main_columns)):
            main_ws.write(row_num, col_num, main_columns[col_num], head_style)
 

        main_ws.col(0).width = 3000
        main_ws.col(1).width = 10000
        main_ws.col(2).width = 10000
        main_ws.col(3).width = 10000
        main_ws.col(4).width = 10000
        main_ws.col(5).width = 10000
        main_ws.col(6).width = 10000
        main_ws.col(7).width = 10000


        date_style = xlwt.XFStyle()
        date_style.num_format_str='dd/mm/yyyy'
        
        font = xlwt.Font()
        font.bold = False
        font.height = 200
        date_style.font = font
        
        borders = xlwt.Borders()
        borders.left = 2
        borders.right = 2
        borders.top = 2
        borders.bottom = 2

        date_style.borders = borders                

        main_style = xlwt.easyxf(
            'font: bold 0, height 200; alignment: wrap True; border: top thick, right thick, bottom thick, left thick')

        rows_table = (Computer.objects.all().values_list('computer_id', 'c_employee_name', 'start_date', 'accounting_date', 'c_supplier_company_name', 
                                              'manufacturer', 'cpu', 'gpu', 'ram', 'rom', 'status').filter(c_employee_name=employee_name))

        for row in rows_table:
            row_num += 1
            for col_num in range(len(row)):
                if (col_num == 2 or col_num == 3):
                    main_ws.write(row_num, col_num, row[col_num], date_style)
                else:
                    main_ws.write(row_num, col_num, row[col_num], main_style)

    
    
        wb.save(response)
        return response
