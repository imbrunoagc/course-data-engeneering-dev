class BankAccount:

    account_str_code = "Bank"
    account_code = 123456

    def __init__(self, account_email, account_password, name) -> None:
        self.email = account_email
        self.password = account_password
        self.owner =  name
        self.__code = BankAccount.account_str_code + "-" + str(BankAccount.account_code)
        self.balance = 0
        BankAccount.plus_account_code()

    # Método de classe
    @classmethod
    def plus_account_code(cls):
        cls.account_code += 1

    # Mudança de senha
    def change_password(self, email, current_pass, new_pass):
        if current_pass == self.password and self.email == email:
            self.password = new_pass
        else:
            raise Exception("Senha incorreta.")

    # Saque saldo
    def withdraw(self, value, password):
        # Se a senha for igual
        if password == self.password:
            # Se o saldo for maior que o valor requisitado para saque
            if self.balance > value:
                # Realizar a subtração do saldo e atualizar no saldo ( - valor retirado )
                self.balance = self.balance - value
            else:
                raise Exception("Saldo insufuciente.")
        else:
            raise Exception("Senha incorreta.")
    
    # Depósito de saldo na conta
    def deposit(self, value, password):
        if password == self.password:
            if value >= 0:
                self.balance = self.balance + value
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


bruno_account = BankAccount(account_email="br@gmail.com", account_password=12345678,name="Bruno")
print(bruno_account.view_account()) 

renan_account = BankAccount(account_email="renan@gmail.com", account_password=12345678,name="Renan")
print(renan_account.view_account())

renan_account.deposit(100, 12345678)
print(renan_account.view_account())

renan_account.withdraw(50, 12345678)
print(renan_account.view_account())
