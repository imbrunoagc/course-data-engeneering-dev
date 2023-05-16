class BankAccount:
    account_str_code = "Bank"
    account_code = 123456

    def __init__(self):
        print("Crie sua conta bancária")
        self.email = input("Digite o email da conta: ")
        self.password = int(input("Digite a senha da conta: "))
        self.owner = input("Digite o nome do proprietário da conta: ")
        self.__code = BankAccount.account_str_code + "-" + str(BankAccount.account_code)
        self.balance = 0
        BankAccount.plus_account_code()

    @classmethod
    def plus_account_code(cls):
        cls.account_code += 1

    def change_password(self):
        email = input("Digite o email da conta: ")
        current_pass = input("Digite a senha atual: ")
        new_pass = input("Digite a nova senha: ")

        if current_pass == self.password and self.email == email:
            self.password = new_pass
        else:
            raise Exception("Senha incorreta.")

    def withdraw(self):
        value = float(input("Digite o valor para saque: "))
        password = input("Digite a senha da conta: ")

        if password == self.password:
            if self.balance > value:
                self.balance -= value
            else:
                raise Exception("Saldo insuficiente.")
        else:
            raise Exception("Senha incorreta.")

    def deposit(self):
        value = float(input("Digite o valor para depósito: "))
        password = input("Digite a senha da conta: ")

        if password == self.password:
            if value >= 0:
                self.balance += value
            else:
                raise Exception("Deposite um valor positivo.")
        else:
            raise Exception("Senha incorreta.")

    def view_account(self):
        return f"""
        Código da conta: {self.__code} 
        Nome do titular: {self.owner} 
        Saldo: {self.balance}
        """

    # Getter Email 
    @property
    def email(self):
        return self._email
    
    # Getter Senha
    @property
    def password(self):
        return self.__password
    
    # Getter Saldo
    @property
    def balance(self):
        return self._balance

    # Setter Email
    @email.setter
    def email(self, value):
        if isinstance(value, str) and "@" in value:
            self._email = value
        else:
            raise Exception("Email Inválido")

    # Setter Senha
    @password.setter
    def password(self, value):
        if isinstance(value, int) and len(str(value)) >= 8:
            self.__password = value
        else:
            raise Exception("Senha Inválida")

    # Setter Saldo
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise Exception("Saldo não pode ser negativo")
        else:
            self._balance = value

    def run_menu(self):
        while True:
            print("---------- MENU ----------")
            print("1. Criar conta")
            print("2. Visualizar conta")
            print("3. Alterar senha")
            print("4. Sacar saldo")
            print("5. Depositar saldo")
            print("0. Sair")
            print("--------------------------")

            option = input("Digite o número da opção desejada: ")

            if option == "1":
                self.__init__()  # Cria uma nova conta
                print("Conta criada com sucesso!")
            elif option == "2":
                print(self.view_account())
            elif option == "3":
                self.change_password()
                print("Senha alterada com sucesso!")
            elif option == "4":
                self.withdraw()
                print("Saque realizado com sucesso!")
            elif option == "5":
                self.deposit()
                print("Depósito realizado com sucesso!")
            elif option == "0":
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

            print()


# Exemplo de uso
account = BankAccount().run_menu()
