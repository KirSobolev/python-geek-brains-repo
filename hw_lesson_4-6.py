"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники."""

"""5. Продолжить работу над первым заданием. 
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. 
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, 
можно использовать любую подходящую структуру, например словарь."""

"""6. Продолжить работу над вторым заданием. 
Реализуйте механизм валидации вводимых пользователем данных. 
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных."""

from abc import abstractmethod, ABC


class Techs(ABC):
    def __init__(self, model, serial_no):
        self.model = model
        self.serial_no = serial_no
        self.department = None

    def set_department(self, department):
        self.department = department

    @abstractmethod
    def __call__(self, data):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Printer(Techs):
    def print_smth(self, data: str):
        return f'Print {self.model}, serial number: {self.serial_no} printed {data}'

    def __call__(self, data):
        self.print_smth(data)

    def __str__(self):
        return f'Printer model {self.model}, serial number: {self.serial_no}'


class Xerox(Techs):
    def copy_smth(self, data: str):
        return f' {self.model} serial number: {self.serial_no} copied {data}'

    def __call__(self, data):
        self.copy_smth(data)

    def __str__(self):
        return f'Printer model {self.model}, serial number: {self.serial_no}'


class Scanner(Techs):
    def scan_smth(self, data: str):
        return f' {self.model} serial number: {self.serial_no} scanned {data}'

    def __call__(self, data):
        self.scan_smth(data)

    def __str__(self):
        return f'Printer model {self.model}, serial number: {self.serial_no}'


class WarehouseFull(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    def __init__(self, max_volume):
        self.max_volume = max_volume
        self.storage = {
            'scanners': set(),
            'printers': set(),
            'xeroxes': set()
        }
        self.total = 0
        self.mapper = {Scanner: 'scanners',
                       Printer: 'printers',
                       Xerox: 'xeroxes'}

    def get_tech_to_warehouse(self, technics: Techs):
        if self.total == self.max_volume:
            raise WarehouseFull('Склад переполнен')
        self.storage[self.mapper[type(technics)]].add(technics)
        technics.set_department('warehouse')
        self.total += 1

    def get_tech_to_department(self, tech_type, department):
        tech_to_dept = self.storage[tech_type].pop()
        tech_to_dept.set_department(department)

    def get_few_techs_to_warehouse(self, num: int, tech_list):
        if type(num) != int:
            raise ValueError('Неавилдное кличество техники! Введите число!')
        for tech in tech_list[:num]:
            self.get_tech_to_warehouse(tech)

    def __call__(self, *args, **kwargs):
        self.get_tech_to_warehouse(*args, **kwargs)

    def __str__(self):
        return f'Warehouse max capacity is {self.max_volume}, current {self.total}'


wh = Warehouse(10)
printer_1 = Printer('LG', 12)
print(printer_1)
printer_2 = Printer('Logitech', 3)
printer_3 = Printer('Mercedes', 15)
scanner_1 = Scanner('Lorem', 15)
xerox_1 = Xerox('Lorem50', 15)

wh.get_few_techs_to_warehouse(5, [printer_1, printer_2, printer_3, xerox_1, scanner_1])
print(wh)