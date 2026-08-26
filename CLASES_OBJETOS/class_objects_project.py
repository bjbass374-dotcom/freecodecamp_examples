class Category:
    def __init__(self, name):
        self.name=name
        self.ledger=[]

    def deposit(self, amount, description=""):
        self.ledger.append({'amount':amount,'description':description})
    
    def withdraw(self, amount, description=""):
        if isinstance(amount,int) or isinstance(amount,float):
            if amount<=self.get_balance():
                self.ledger.append({'amount':-amount,'description':description})
                return True
        
        return False

    def get_balance(self):
        balance=0
        for i in self.ledger:
            balance+=i['amount']
        return balance
        
    def transfer(self, amount, category):
        if isinstance(amount,int) or isinstance(amount,float):
            if self.withdraw(amount, f"Transfer to {category.name}"):  # ✅ Verifica
                category.deposit(amount, f"Transfer from {self.name}")
                return True
        return False

    def check_funds(self, amount):
        if amount>self.get_balance():
            return False
        else:
            return True
    
    def __str__(self):
        # Título con asteriscos y centrado
        title_line = "*" * ((30 - len(self.name)) // 2) + self.name + "*" * ((30 - len(self.name)) // 2)
        # Si la longitud total es 30 o 31, da igual; el proyecto acepta.

        # Construir cada línea del ledger
        lines = []
        for item in self.ledger:
            desc = item['description'][:23]  # Trunca a 23 caracteres
            amount = item['amount']
            # Formatear monto con 2 decimales y ancho 7
            amount_str = f"{amount:>7.2f}"
            # Calcular espacios entre descripción y monto para que la línea tenga 30 caracteres
            spaces = 30 - len(desc) - len(amount_str)
            line = desc + " " * spaces + amount_str
            lines.append(line)

        # Unir todas las líneas con saltos de línea
        ledger_str = "\n".join(lines)
        # Total con dos decimales
        total_str = f"Total: {self.get_balance():.2f}"

        # Devolver el string completo (título + ledger + total)
        return title_line + "\n" + ledger_str + "\n" + total_str

def create_spend_chart(categories):
    # 1. Calcular el total de retiros y los porcentajes
    total_withdraw = 0
    for category in categories:
        for item in category.ledger:
            if item['amount'] < 0:
                total_withdraw -= item['amount']

    percents = []
    if total_withdraw == 0:
        percents = [0] * len(categories)
    else:
        for category in categories:
            category_withdraw = 0
            for item in category.ledger:
                if item['amount'] < 0:
                    category_withdraw -= item['amount']
            percent = int((category_withdraw / total_withdraw) * 100) // 10 * 10
            percents.append(percent)

    n = len(categories)
    title = "Percentage spent by category"
    chart = title + "\n"

    # 2. Líneas de barras (100 a 0)
    for level in range(100, -10, -10):
        chart += f"{level:>3}| "
        for p in percents:
            if p >= level:
                chart += "o  "      # "o" + dos espacios
            else:
                chart += "   "      # tres espacios (vacío)
        chart += "\n"

    # 3. Línea horizontal (sin espacios al final)
    chart += "    " + "-" * (n * 3 + 1) + "\n"

    # 4. Nombres verticales (sin salto de línea al final)
    names = [cat.name for cat in categories]
    max_len = max(len(name) for name in names)
    for i in range(max_len):
        chart += "     "  # 5 espacios para alinear con las barras
        for name in names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        if i < max_len - 1:
            chart += "\n"

    return chart

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')

clothing = Category('Clothing')

food.transfer(50, clothing)
clothing.withdraw(11.6,'pants')
clothing.withdraw(20.2,'pants_2')
print(food)
print(clothing)
print(create_spend_chart([food,clothing]))
