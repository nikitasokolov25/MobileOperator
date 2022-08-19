import pyodbc
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import scrolledtext
import bcrypt
connection_to_db = pyodbc.connect(r'Driver={SQL Server};Server=LAPTOP-VSD2CVQ7\SQLEXPRESS;Database=Coursework;Trusted_Connection=yes;')
cursor = connection_to_db.cursor()

def clickedExitDirectorButton():
    registerNewManagerButton.grid_forget()
    deleteManagerButton.grid_forget()
    addNewTariffButton.grid_forget()
    changeTariffDataButton.grid_forget()
    deleteTariffButton.grid_forget()
    addNewPhoneNumberButton.grid_forget()
    deletePhoneNumberButton.grid_forget()
    changeManagerButton.grid_forget()
    addNewServiceButton.grid_forget()
    changeServiceButton.grid_forget()
    checkBestManagersButton.grid_forget()
    checkBestTariffsButton.grid_forget()
    checkProfitButton.grid_forget()
    exitDirectorButton.grid_forget()
    lblDirector.grid_forget()
    startApp()

def clickedOkCheckProfitButton():
    profitText.delete(1.0, END)
    profitText.grid_forget()
    OkCheckProfitButton.grid_forget()
    clickedEntry2Button()

def clickedCheckProfitButton():
    registerNewManagerButton.grid_forget()
    deleteManagerButton.grid_forget()
    addNewTariffButton.grid_forget()
    changeTariffDataButton.grid_forget()
    deleteTariffButton.grid_forget()
    addNewPhoneNumberButton.grid_forget()
    deletePhoneNumberButton.grid_forget()
    changeManagerButton.grid_forget()
    addNewServiceButton.grid_forget()
    changeServiceButton.grid_forget()
    checkBestManagersButton.grid_forget()
    checkBestTariffsButton.grid_forget()
    checkProfitButton.grid_forget()
    exitDirectorButton.grid_forget()

    cursor.execute(f"""Select (Select Sum(sumTariffs) from SumTariff) + (Select Sum(sumServices) from SumService) as profit""")
    profitText.insert(INSERT, cursor.fetchone().profit)
    profitText.insert(INSERT, ' рублей')
    profitText.grid(row=1, column=0)
    OkCheckProfitButton.grid(row=2, column=0)

def clickedOkCheckBestTariffsButton():
    bestTariffsText.delete(1.0, END)
    bestTariffsText.grid_forget()
    OkCheckBestTariffsButton.grid_forget()
    clickedEntry2Button()

def clickedCheckBestTariffsButton():
    registerNewManagerButton.grid_forget()
    deleteManagerButton.grid_forget()
    addNewTariffButton.grid_forget()
    changeTariffDataButton.grid_forget()
    deleteTariffButton.grid_forget()
    addNewPhoneNumberButton.grid_forget()
    deletePhoneNumberButton.grid_forget()
    changeManagerButton.grid_forget()
    addNewServiceButton.grid_forget()
    changeServiceButton.grid_forget()
    checkBestManagersButton.grid_forget()
    checkBestTariffsButton.grid_forget()
    checkProfitButton.grid_forget()
    exitDirectorButton.grid_forget()

    cursor.execute(f"""Select Name, Count(PhoneNumbers.IdTariffPlan) as countTariff from PhoneNumbers, TariffPlans where PhoneNumbers.IdTariffPlan = TariffPlans.IdTariffPlan group by Name order by countTariff Desc""")
    while 1:
        current = cursor.fetchone()
        if not current:
            break
        bestTariffsText.insert(INSERT, current.Name)
        bestTariffsText.insert(INSERT, ' -> ')
        bestTariffsText.insert(INSERT, current.countTariff)
        bestTariffsText.insert(INSERT, '\n')
    bestTariffsText.grid(row=1, column=0)
    OkCheckBestTariffsButton.grid(row=2, column=0)

def clickedOkCheckBestManagersButton():
    managersText.delete(1.0, END)
    managersText.grid_forget()
    OkCheckBestManagersButton.grid_forget()
    clickedEntry2Button()

def clickedCheckBestManagersButton():
    registerNewManagerButton.grid_forget()
    deleteManagerButton.grid_forget()
    addNewTariffButton.grid_forget()
    changeTariffDataButton.grid_forget()
    deleteTariffButton.grid_forget()
    addNewPhoneNumberButton.grid_forget()
    deletePhoneNumberButton.grid_forget()
    changeManagerButton.grid_forget()
    addNewServiceButton.grid_forget()
    changeServiceButton.grid_forget()
    checkBestManagersButton.grid_forget()
    checkBestTariffsButton.grid_forget()
    checkProfitButton.grid_forget()
    exitDirectorButton.grid_forget()

    cursor.execute(f"""Select Name, Count(PhoneNumbersCallers.IdManager) as countNumbers from PhoneNumbersCallers, Managers where Managers.IdManager = PhoneNumbersCallers.IdManager group by Name order by countNumbers Desc""")
    while 1:
        current = cursor.fetchone()
        if not current:
            break
        managersText.insert(INSERT, current.Name)
        managersText.insert(INSERT, ' -> ')
        managersText.insert(INSERT, current.countNumbers)
        managersText.insert(INSERT, '\n')
    managersText.grid(row=1, column=0)
    OkCheckBestManagersButton.grid(row=2, column=0)

def clickedOkChangeServiceButton():
    lblChooseService.grid_forget()
    comboChooseService.grid_forget()
    lblNameChooseService.grid_forget()
    lblPriceChooseService.grid_forget()
    lblDescriptionChooseService.grid_forget()
    txtNameChooseService.grid_forget()
    txtPriceChooseService.grid_forget()
    txtDescriptionChooseService.grid_forget()
    OkChangeServiceButton.grid_forget()

    name = comboChooseService.get()
    newName = txtNameChooseService.get()
    newPrice = txtPriceChooseService.get()
    newDesc = txtDescriptionChooseService.get()
    if not newName or not newPrice or not newDesc:
        messagebox.showinfo('Предупреждение', 'Все поля должны быть заполнены!')
        clickedChangeServiceButton()
    else:
        cursor.execute(f"""Update AdditionalServices Set Name = '{newName}', Price = '{newPrice}', Description = '{newDesc}' where IdAdditionalService = (Select IdAdditionalService from AdditionalServices where Name = '{name}')""")
        connection_to_db.commit()
        messagebox.showinfo('УРА', 'Услуга успешно изменена!')
        clickedEntry2Button()

def clickedChangeServiceButton():
    registerNewManagerButton.grid_forget()
    deleteManagerButton.grid_forget()
    addNewTariffButton.grid_forget()
    changeTariffDataButton.grid_forget()
    deleteTariffButton.grid_forget()
    addNewPhoneNumberButton.grid_forget()
    deletePhoneNumberButton.grid_forget()
    changeManagerButton.grid_forget()
    addNewServiceButton.grid_forget()
    changeServiceButton.grid_forget()
    checkBestManagersButton.grid_forget()
    checkBestTariffsButton.grid_forget()
    checkProfitButton.grid_forget()
    exitDirectorButton.grid_forget()

    lblChooseService.grid(row=1, column=0)
    services = []
    cursor.execute(f"Select Name from AdditionalServices")
    while 1:
        current = cursor.fetchone()
        if not current:
            break
        services.append(current.Name)
    comboChooseService['values'] = services
    comboChooseService.grid(column=1, row=1)
    lblNameChooseService.grid(column=0, row=2)
    lblPriceChooseService.grid(column=0, row=3)
    lblDescriptionChooseService.grid(column=0, row=4)
    txtNameChooseService.grid(column=1, row=2)
    txtPriceChooseService.grid(column=1, row=3)
    txtDescriptionChooseService.grid(column=1, row=4)
    OkChangeServiceButton.grid(column=1, row=5)

def clickedOkAddNewServiceButton():
    lblNameService.grid_forget()
    lblPriceService.grid_forget()
    lblDescriptionService.grid_forget()
    txtNameService.grid_forget()
    txtPriceService.grid_forget()
    txtDescriptionService.grid_forget()
    OkAddNewServiceButton.grid_forget()

    name = txtNameService.get()
    price = txtPriceService.get()
    desc = txtDescriptionService.get()
    if not name or not price or not desc:
        messagebox.showinfo('Предупреждение', 'Все поля должны быть заполнены!')
        clickedAddNewServiceButton()
    else:
        cursor.execute(f"""Insert into AdditionalServices(Name, Price, Description, isActive) values ('{name}', '{price}', '{desc}', 1)""")
        connection_to_db.commit()
        messagebox.showinfo('УРА', 'Услуга успешно добавлена!')
        clickedEntry2Button()

def clickedAddNewServiceButton():
    registerNewManagerButton.grid_forget()
    deleteManagerButton.grid_forget()
    addNewTariffButton.grid_forget()
    changeTariffDataButton.grid_forget()
    deleteTariffButton.grid_forget()
    addNewPhoneNumberButton.grid_forget()
    deletePhoneNumberButton.grid_forget()
    changeManagerButton.grid_forget()
    addNewServiceButton.grid_forget()
    changeServiceButton.grid_forget()
    checkBestManagersButton.grid_forget()
    checkBestTariffsButton.grid_forget()
    checkProfitButton.grid_forget()
    exitDirectorButton.grid_forget()

    lblNameService.grid(column=0, row=1)
    lblPriceService.grid(column=0, row=2)
    lblDescriptionService.grid(column=0, row=3)
    txtNameService.grid(column=1, row=1)
    txtPriceService.grid(column=1, row=2)
    txtDescriptionService.grid(column=1, row=3)
    OkAddNewServiceButton.grid(column=1, row=4)

def clickedOkChangeManagerButton():
    lblChooseManager.grid_forget()
    comboDeleteManager.grid_forget()
    lblNameManager.grid_forget()
    lblAddressManager.grid_forget()
    lblPhoneManager.grid_forget()
    txtNameManager.grid_forget()
    txtAddressManager.grid_forget()
    txtPhoneManager.grid_forget()
    OkChangeManagerButton.grid_forget()

    name = comboDeleteManager.get()
    newName = txtNameManager.get()
    newAddress = txtAddressManager.get()
    newPhone = txtPhoneManager.get()
    if not newName or not newAddress or not newPhone:
        messagebox.showinfo('Предупреждение', 'Все поля должны быть заполнены!')
        clickedChangeManagerButton()
    else:
        cursor.execute(f"""Update Managers Set Name = '{newName}', WorkAddress = '{newAddress}', PhoneNumber = '{newPhone}' where IdManager = (Select IdManager from Managers where Name = '{name}')""")
        connection_to_db.commit()
        messagebox.showinfo('УРА', 'Данные менеджера успешно изменены!')
        clickedEntry2Button()

def clickedChangeManagerButton():
    registerNewManagerButton.grid_forget()
    deleteManagerButton.grid_forget()
    addNewTariffButton.grid_forget()
    changeTariffDataButton.grid_forget()
    deleteTariffButton.grid_forget()
    addNewPhoneNumberButton.grid_forget()
    deletePhoneNumberButton.grid_forget()
    changeManagerButton.grid_forget()
    addNewServiceButton.grid_forget()
    changeServiceButton.grid_forget()
    checkBestManagersButton.grid_forget()
    checkBestTariffsButton.grid_forget()
    checkProfitButton.grid_forget()
    exitDirectorButton.grid_forget()

    lblChooseManager.grid(row=1, column=0)
    managers = []
    cursor.execute(f"Select Name from Managers")
    while 1:
        current = cursor.fetchone()
        if not current:
            break
        managers.append(current.Name)
    comboDeleteManager['values'] = managers
    comboDeleteManager.grid(column=1, row=1)
    lblNameManager.grid(row=2, column=0)
    lblAddressManager.grid(row=3, column=0)
    lblPhoneManager.grid(row=4, column=0)
    txtNameManager.grid(row=2, column=1)
    txtAddressManager.grid(row=3, column=1)
    txtPhoneManager.grid(row=4, column=1)
    OkChangeManagerButton.grid(row=5, column=1)

def clickedOkDeletePhoneNumberButton():
    lblDeleteNumber.grid_forget()
    comboDeleteNumbers.grid_forget()
    OkDeletePhoneNumberButton.grid_forget()

    number = comboDeleteNumbers.get()
    try:
        cursor.execute(f"""Delete from PhoneNumbers where PhoneNumber = '{number}'""")
        connection_to_db.commit()
        messagebox.showinfo('УРА', 'Номер успешно удален!')
        clickedEntry2Button()
    except pyodbc.IntegrityError:
        messagebox.showinfo('Предупреждение', 'Номер используется, нельзя удалить!')
        clickedDeletePhoneNumberButton()

def clickedDeletePhoneNumberButton():
    registerNewManagerButton.grid_forget()
    deleteManagerButton.grid_forget()
    addNewTariffButton.grid_forget()
    changeTariffDataButton.grid_forget()
    deleteTariffButton.grid_forget()
    addNewPhoneNumberButton.grid_forget()
    deletePhoneNumberButton.grid_forget()
    changeManagerButton.grid_forget()
    addNewServiceButton.grid_forget()
    changeServiceButton.grid_forget()
    checkBestManagersButton.grid_forget()
    checkBestTariffsButton.grid_forget()
    checkProfitButton.grid_forget()
    exitDirectorButton.grid_forget()

    lblDeleteNumber.grid(row=1, column=0)
    numbers = []
    cursor.execute(f"Select PhoneNumber from PhoneNumbers")
    while 1:
        current = cursor.fetchone()
        if not current:
            break
        numbers.append(current.PhoneNumber)
    comboDeleteNumbers['values'] = numbers
    comboDeleteNumbers.grid(column=1, row=1)
    OkDeletePhoneNumberButton.grid(column=1, row=2)

def clickedOkAddNewPhoneNumberButton():
    lblNewPhone.grid_forget()
    txtNewPhone.grid_forget()
    OkAddNewPhoneNumberButton.grid_forget()
    phone = txtNewPhone.get()
    if not phone:
        messagebox.showinfo('Предупреждение', 'Номер не может быть пустым')
        clickedAddNewPhoneNumberButton()
    else:
        cursor.execute(f"""exec addNumber '{phone}'""")
        connection_to_db.commit()
        messagebox.showinfo('УРА', 'Номер успешно добавлен!')
        clickedEntry2Button()

def clickedAddNewPhoneNumberButton():
    registerNewManagerButton.grid_forget()
    deleteManagerButton.grid_forget()
    addNewTariffButton.grid_forget()
    changeTariffDataButton.grid_forget()
    deleteTariffButton.grid_forget()
    addNewPhoneNumberButton.grid_forget()
    deletePhoneNumberButton.grid_forget()
    changeManagerButton.grid_forget()
    addNewServiceButton.grid_forget()
    changeServiceButton.grid_forget()
    checkBestManagersButton.grid_forget()
    checkBestTariffsButton.grid_forget()
    checkProfitButton.grid_forget()
    exitDirectorButton.grid_forget()

    lblNewPhone.grid(row=1, column=0)
    txtNewPhone.grid(row=1, column=1)
    OkAddNewPhoneNumberButton.grid(row=2, column=1)

def clickedOkDeleteTariffButton():
    lblChangeTariff.grid_forget()
    comboChangeTariff.grid_forget()
    OkDeleteTariffButton.grid_forget()
    name = comboChangeTariff.get()
    try:
        cursor.execute(f"""Delete from TariffPlans where Name = '{name}'""")
        connection_to_db.commit()
        messagebox.showinfo('УРА', 'Тариф успешно удален!')
        clickedEntry2Button()
    except pyodbc.IntegrityError:
        messagebox.showinfo('Предупреждение', 'Этот тариф в данный момент используется!')
        clickedDeleteTariffButton()

def clickedDeleteTariffButton():
    registerNewManagerButton.grid_forget()
    deleteManagerButton.grid_forget()
    addNewTariffButton.grid_forget()
    changeTariffDataButton.grid_forget()
    deleteTariffButton.grid_forget()
    addNewPhoneNumberButton.grid_forget()
    deletePhoneNumberButton.grid_forget()
    changeManagerButton.grid_forget()
    addNewServiceButton.grid_forget()
    changeServiceButton.grid_forget()
    checkBestManagersButton.grid_forget()
    checkBestTariffsButton.grid_forget()
    checkProfitButton.grid_forget()
    exitDirectorButton.grid_forget()

    lblChangeTariff.grid(column=0, row=1)
    tariffs = []
    cursor.execute(f"Select Name from TariffPlans")
    while 1:
        current = cursor.fetchone()
        if not current:
            break
        tariffs.append(current.Name)
    comboChangeTariff['values'] = tariffs
    comboChangeTariff.grid(column=1, row=1)
    OkDeleteTariffButton.grid(column=1, row=2)

def clickedOkChangeTariffDataButton():
    name = comboChangeTariff.get()
    newName = txtNameChangeTariff.get()
    newPrice = txtPriceChangeTariff.get()
    newDesc = txtDescriptionChangeTariff.get()

    lblChangeTariff.grid_forget()
    comboChangeTariff.grid_forget()
    lblNameChangeTariff.grid_forget()
    lblPriceChangeTariff.grid_forget()
    lblDescriptionChangeTariff.grid_forget()
    txtNameChangeTariff.grid_forget()
    txtPriceChangeTariff.grid_forget()
    txtDescriptionChangeTariff.grid_forget()
    OkChangeTariffDataButton.grid_forget()

    if not newName or not newPrice or not newDesc:
        messagebox.showinfo('Предупреждение', 'Все поля должны быть заполнены!')
        clickedChangeTariffDataButton()
    else:
        cursor.execute(f"""Update TariffPlans Set Name = '{newName}', Price = '{newPrice}', Description = '{newDesc}' where IdTariffPlan = (Select IdTariffPlan from TariffPlans where Name = '{name}')""")
        connection_to_db.commit()
        messagebox.showinfo('УРА', 'Данные тарифа успешно изменены')
        clickedEntry2Button()


def clickedChangeTariffDataButton():
    registerNewManagerButton.grid_forget()
    deleteManagerButton.grid_forget()
    addNewTariffButton.grid_forget()
    changeTariffDataButton.grid_forget()
    deleteTariffButton.grid_forget()
    addNewPhoneNumberButton.grid_forget()
    deletePhoneNumberButton.grid_forget()
    changeManagerButton.grid_forget()
    addNewServiceButton.grid_forget()
    changeServiceButton.grid_forget()
    checkBestManagersButton.grid_forget()
    checkBestTariffsButton.grid_forget()
    checkProfitButton.grid_forget()
    exitDirectorButton.grid_forget()

    lblChangeTariff.grid(column=0, row=1)
    tariffs = []
    cursor.execute(f"Select Name from TariffPlans")
    while 1:
        current = cursor.fetchone()
        if not current:
            break
        tariffs.append(current.Name)
    comboChangeTariff['values'] = tariffs
    comboChangeTariff.grid(column=1, row=1)
    lblNameChangeTariff.grid(column=0, row=2)
    lblPriceChangeTariff.grid(column=0, row=3)
    lblDescriptionChangeTariff.grid(column=0, row=4)
    txtNameChangeTariff.grid(column=1, row=2)
    txtPriceChangeTariff.grid(column=1, row=3)
    txtDescriptionChangeTariff.grid(column=1, row=4)
    OkChangeTariffDataButton.grid(column=1, row=5)

def clickedOkAddNewTariffButton():
    lblNameTariff.grid_forget()
    lblPriceTariff.grid_forget()
    lblDescriptionTariff.grid_forget()
    txtNameTariff.grid_forget()
    txtPriceTariff.grid_forget()
    txtDescriptionTariff.grid_forget()
    OkAddNewTariffButton.grid_forget()
    name = txtNameTariff.get()
    price = txtPriceTariff.get()
    desc = txtDescriptionTariff.get()
    if not name or not price or not desc:
        messagebox.showinfo('Предупреждение', 'Все поля должны быть заполнены')
        clickedAddNewTariffButton()
    else:
        cursor.execute(f"""Insert into TariffPlans(Name, Price, Description, isActive) values ('{name}', '{price}', '{desc}', 1)""")
        connection_to_db.commit()
        messagebox.showinfo('УРА', 'Тариф успешно добавлен!')
        clickedEntry2Button()

def clickedAddNewTariffButton():
    registerNewManagerButton.grid_forget()
    deleteManagerButton.grid_forget()
    addNewTariffButton.grid_forget()
    changeTariffDataButton.grid_forget()
    deleteTariffButton.grid_forget()
    addNewPhoneNumberButton.grid_forget()
    deletePhoneNumberButton.grid_forget()
    changeManagerButton.grid_forget()
    addNewServiceButton.grid_forget()
    changeServiceButton.grid_forget()
    checkBestManagersButton.grid_forget()
    checkBestTariffsButton.grid_forget()
    checkProfitButton.grid_forget()
    exitDirectorButton.grid_forget()

    lblNameTariff.grid(column=0, row=1)
    lblPriceTariff.grid(column=0, row=2)
    lblDescriptionTariff.grid(column=0, row=3)
    txtNameTariff.grid(column=1, row=1)
    txtPriceTariff.grid(column=1, row=2)
    txtDescriptionTariff.grid(column=1, row=3)
    OkAddNewTariffButton.grid(column=1, row=4)

def clickedOkDeleteManagerButton():
    lblChooseManager.grid_forget()
    comboDeleteManager.grid_forget()
    OkDeleteManagerButton.grid_forget()
    name = comboDeleteManager.get()
    try:
        cursor.execute(f"""Delete from Managers where Name = '{name}'""")
        connection_to_db.commit()
        messagebox.showinfo('УРА', 'Менеджер успешно удален!')
        clickedEntry2Button()
    except pyodbc.IntegrityError:
        messagebox.showinfo('Предупреждение', 'Невозможно удалить менеджера!')
        clickedDeleteManagerButton()


def clickedDeleteManagerButton():
    registerNewManagerButton.grid_forget()
    deleteManagerButton.grid_forget()
    addNewTariffButton.grid_forget()
    changeTariffDataButton.grid_forget()
    deleteTariffButton.grid_forget()
    addNewPhoneNumberButton.grid_forget()
    deletePhoneNumberButton.grid_forget()
    changeManagerButton.grid_forget()
    addNewServiceButton.grid_forget()
    changeServiceButton.grid_forget()
    checkBestManagersButton.grid_forget()
    checkBestTariffsButton.grid_forget()
    checkProfitButton.grid_forget()
    exitDirectorButton.grid_forget()

    lblChooseManager.grid(column=0, row=1)
    managers = []
    cursor.execute(f"Select Name from Managers")
    while 1:
        current = cursor.fetchone()
        if not current:
            break
        managers.append(current.Name)
    comboDeleteManager['values'] = managers
    comboDeleteManager.grid(column=1, row=1)
    OkDeleteManagerButton.grid(column=1, row=2)


def clickedOkRegisterNewManagerButton():
    lblLoginDataManager.grid_forget()
    lblPasswordDataManager.grid_forget()
    lblNameDataManager.grid_forget()
    lblAddressDataManager.grid_forget()
    lblPhoneDataManager.grid_forget()
    txtLoginDataManager.grid_forget()
    txtPasswordDataManager.grid_forget()
    txtNameDataManager.grid_forget()
    txtAddressDataManager.grid_forget()
    txtPhoneDataManager.grid_forget()
    OkRegisterNewManagerButton.grid_forget()

    login = txtLoginDataManager.get()
    password = txtPasswordDataManager.get()
    name = txtNameDataManager.get()
    address = txtAddressDataManager.get()
    phone = txtPhoneDataManager.get()

    try:
        key = b'$2b$12$COnvlB9Kses3CthyxNl9pu'
        password = bcrypt.hashpw(str.encode(password), key)
        cursor.execute(f"""exec Register_Manager '{login}', '{password.decode()}', '{name}', '{address}', '{phone}'""")
        connection_to_db.commit()
        messagebox.showinfo('УРА', 'Регистрация прошла успешно!')
        clickedEntry2Button()
    except:
        messagebox.showinfo('Предупреждение', 'Такой логин или телефон уже существует!')
        clickedRegisterNewManagerButton()

def clickedRegisterNewManagerButton():
    registerNewManagerButton.grid_forget()
    deleteManagerButton.grid_forget()
    addNewTariffButton.grid_forget()
    changeTariffDataButton.grid_forget()
    deleteTariffButton.grid_forget()
    addNewPhoneNumberButton.grid_forget()
    deletePhoneNumberButton.grid_forget()
    changeManagerButton.grid_forget()
    addNewServiceButton.grid_forget()
    changeServiceButton.grid_forget()
    checkBestManagersButton.grid_forget()
    checkBestTariffsButton.grid_forget()
    checkProfitButton.grid_forget()
    exitDirectorButton.grid_forget()

    lblLoginDataManager.grid(column=0, row=1)
    lblPasswordDataManager.grid(column=0, row=2)
    lblNameDataManager.grid(column=0, row=3)
    lblAddressDataManager.grid(column=0, row=4)
    lblPhoneDataManager.grid(column=0, row=5)
    txtLoginDataManager.grid(column=1, row=1)
    txtPasswordDataManager.grid(column=1, row=2)
    txtNameDataManager.grid(column=1, row=3)
    txtAddressDataManager.grid(column=1, row=4)
    txtPhoneDataManager.grid(column=1, row=5)
    OkRegisterNewManagerButton.grid(column=1, row=6)

def clickedExitManagerButton():
    changeCallerStatusButton.grid_forget()
    changeCallerPersonalDataButton.grid_forget()
    seeFreePhoneNumbersButton.grid_forget()
    givePhoneNumberButton.grid_forget()
    exitManagerButton.grid_forget()
    lblManager.grid_forget()
    startApp()

def clickedOkGivePhoneNumberButton():
    lblNewPhoneCallers.grid_forget()
    lblAvailablePhoneNumbers.grid_forget()
    comboAvailablePhoneNumbers.grid_forget()
    comboNewPhoneCallers.grid_forget()
    OkGivePhoneNumberButton.grid_forget()
    newCaller = comboNewPhoneCallers.get()
    newPhoneNumber = comboAvailablePhoneNumbers.get()
    cursor.execute(f"""Insert into PhoneNumbersCallers(IdCaller, IdPhoneNumber, IdManager) values ((Select IdCaller from Callers where Name = '{newCaller}'), (Select IdPhoneNumber from PhoneNumbers where PhoneNumber = '{newPhoneNumber}'), '{mainUserId}')""")
    connection_to_db.commit()
    cursor.execute(f"""Update PhoneNumbers Set isActive = 1 where PhoneNumber = '{newPhoneNumber}'""")
    connection_to_db.commit()
    messagebox.showinfo('УРА', 'Номер успешно подключен!')
    clickedEntry2Button()

def clickedGivePhoneNumberButton():
    window1.geometry('500x220')
    changeCallerStatusButton.grid_forget()
    changeCallerPersonalDataButton.grid_forget()
    seeFreePhoneNumbersButton.grid_forget()
    givePhoneNumberButton.grid_forget()
    exitManagerButton.grid_forget()

    newPhoneCallers = []
    cursor.execute(f"Select Name from Callers")
    while 1:
        current = cursor.fetchone()
        if not current:
            break
        newPhoneCallers.append(current.Name)
    comboNewPhoneCallers['values'] = newPhoneCallers

    availablePhoneNumbers = []
    cursor.execute(f"Select PhoneNumber from PhoneNumbers where isActive=0")
    while 1:
        current = cursor.fetchone()
        if not current:
            break
        availablePhoneNumbers.append(current.PhoneNumber)
    comboAvailablePhoneNumbers['values'] = availablePhoneNumbers

    comboNewPhoneCallers.grid(row=1, column=1)
    comboAvailablePhoneNumbers.grid(row=2, column=1)
    lblNewPhoneCallers.grid(row=1, column=0)
    lblAvailablePhoneNumbers.grid(row=2, column=0)
    OkGivePhoneNumberButton.grid(row=3, column=1)

def clickedOkSeeFreePhoneNumbersButton():
    phoneNumbersText.delete(1.0, END)
    phoneNumbersText.grid_forget()
    OkSeeFreePhoneNumbersButton.grid_forget()
    clickedEntry2Button()

def clickedSeeFreePhoneNumbersButton():
    window1.geometry('500x220')
    changeCallerStatusButton.grid_forget()
    changeCallerPersonalDataButton.grid_forget()
    seeFreePhoneNumbersButton.grid_forget()
    givePhoneNumberButton.grid_forget()
    exitManagerButton.grid_forget()
    cursor.execute(f"""Select PhoneNumber from PhoneNumbers where isActive=0""")
    while 1:
        current = cursor.fetchone()
        if not current:
            break
        phoneNumbersText.insert(INSERT, current.PhoneNumber)
        phoneNumbersText.insert(INSERT, '\n')
    phoneNumbersText.grid(row=1, column=0)
    OkSeeFreePhoneNumbersButton.grid(row=2, column=0)

def clickedOkChangeCallerPersonalData2Button():
    newName = entryNameCaller.get()
    newAddress = entryAddressCaller.get()
    newPassport = entryPassportCaller.get()
    if not newName or not newAddress or not newPassport:
        messagebox.showinfo('ERROR', 'Все поля должны быть заполнены!')
        clickedOkChangeCallerPersonalDataButton()
    else:
        cursor.execute(f"""Update Callers Set Name = ISNULL('{newName}', Name), Address = ISNULL('{newAddress}', Address),
        Passport = ISNULL('{newPassport}', Passport) where Name = '{nameChosenCaller}'""")
        connection_to_db.commit()
        messagebox.showinfo('УРА', 'Персональные данные успешно изменены!')
        lblNameDataCaller.grid_forget()
        lblAddressDataCaller.grid_forget()
        lblPassportDataCaller.grid_forget()
        entryNameCaller.grid_forget()
        entryAddressCaller.grid_forget()
        entryPassportCaller.grid_forget()
        OkChangeCallerPersonalData2Button.grid_forget()
        clickedEntry2Button()

def clickedOkChangeCallerPersonalDataButton():
    global nameChosenCaller
    nameChosenCaller = comboDataCallers.get()
    comboDataCallers.grid_forget()
    lblDataCallers.grid_forget()
    OkChangeCallerPersonalDataButton.grid_forget()
    lblNameDataCaller.grid(row=1, column=0)
    lblAddressDataCaller.grid(row=2, column=0)
    lblPassportDataCaller.grid(row=3, column=0)
    entryNameCaller.grid(row=1, column=1)
    entryAddressCaller.grid(row=2, column=1)
    entryPassportCaller.grid(row=3, column=1)
    OkChangeCallerPersonalData2Button.grid(row=4, column=1)


def clickedChangeCallerPersonalDataButton():
    window1.geometry('500x220')
    changeCallerStatusButton.grid_forget()
    changeCallerPersonalDataButton.grid_forget()
    seeFreePhoneNumbersButton.grid_forget()
    givePhoneNumberButton.grid_forget()
    exitManagerButton.grid_forget()
    dataCallers = []
    cursor.execute(f"Select Name from Callers")
    while 1:
        current = cursor.fetchone()
        if not current:
            break
        dataCallers.append(current.Name)
    comboDataCallers['values'] = dataCallers

    comboDataCallers.grid(row=1, column=1)
    lblDataCallers.grid(row=1, column=0)
    OkChangeCallerPersonalDataButton.grid(row=2, column=1)

def clickedOkChangeStatusCallerButton():
    nameCaller = comboStatusCallers.get()
    print(nameCaller)
    cursor.execute(f"""Update Users Set isActive = 1-isActive where IdUser = (Select IdUser from Callers where Name = '{nameCaller}')""")
    connection_to_db.commit()
    messagebox.showinfo('УРА', 'Статус абонента успешно изменен!')
    comboStatusCallers.grid_forget()
    lblStatusCallers.grid_forget()
    OkChangeStatusCallerButton.grid_forget()
    clickedEntry2Button()

def clickedChangeCallerStatusButton():
    window1.geometry('500x220')
    changeCallerStatusButton.grid_forget()
    changeCallerPersonalDataButton.grid_forget()
    seeFreePhoneNumbersButton.grid_forget()
    givePhoneNumberButton.grid_forget()
    exitManagerButton.grid_forget()
    statusCallers = []
    cursor.execute(f"Select Name from Callers")
    while 1:
        current = cursor.fetchone()
        if not current:
            break
        statusCallers.append(current.Name)
    comboStatusCallers['values'] = statusCallers

    comboStatusCallers.grid(row=1, column=1)
    lblStatusCallers.grid(row=1, column=0)
    OkChangeStatusCallerButton.grid(row=2, column=1)

def clickedExitCallerButton():
    changeTariffButton.grid_forget()
    seeTariffsButton.grid_forget()
    seeServicesButton.grid_forget()
    seePersonalDataButton.grid_forget()
    addServiceButton.grid_forget()
    exitCallerButton.grid_forget()
    lblCaller.grid_forget()
    startApp()

def clickedOkAddServiceButton():
    phoneNumber = comboPhoneNumbers.get()
    nameService = comboServices.get()
    cursor.execute(f"""Declare @date date Set @date = CONVERT (date, GETDATE()) Insert into AdditionalServicesPhoneNumbers(IdAdditionalService, IdPhoneNumberCaller, Date) values ((Select IdAdditionalService from AdditionalServices where Name = '{nameService}'), (Select IdPhoneNumberCaller from PhoneNumbersCallers where IdPhoneNumber = (Select IdPhoneNumber from PhoneNumbers where PhoneNumber = '{phoneNumber}')), @date)""")
    connection_to_db.commit()
    messagebox.showinfo('УРА', 'Услуга успешно подключена!')
    lblServices.grid_forget()
    lblPhoneNumbers.grid_forget()
    comboPhoneNumbers.grid_forget()
    comboServices.grid_forget()
    OkAddServiceButton.grid_forget()
    clickedEntry2Button()

def clickedAddServiceButton():
    changeTariffButton.grid_forget()
    seeTariffsButton.grid_forget()
    seeServicesButton.grid_forget()
    seePersonalDataButton.grid_forget()
    addServiceButton.grid_forget()
    exitCallerButton.grid_forget()

    lblPhoneNumbers.grid(row=10, column=0)
    phoneNumbers = ['']
    cursor.execute(f"Select PhoneNumber from PhoneNumbersCallers, PhoneNumbers where PhoneNumbersCallers.IdPhoneNumber=PhoneNumbers.IdPhoneNumber and IdCaller = '{mainUserId}'")
    while 1:
        current = cursor.fetchone()
        if not current:
            break
        phoneNumbers.append(current.PhoneNumber)
    comboPhoneNumbers['values'] = phoneNumbers

    comboPhoneNumbers.grid(row=10, column=1)

    lblServices.grid(row=50, column=0)
    services = ['']
    cursor.execute(f"Select Name from AdditionalServices")
    while 1:
        current = cursor.fetchone()
        if not current:
            break
        services.append(current.Name)
    comboServices['values'] = services

    comboServices.grid(row=50, column=1)
    OkAddServiceButton.grid(row=70, column=1)


def clickedOkSeePersonalDataButton():
    personalDataText.delete(1.0, END)
    personalDataText.grid_forget()
    OkSeePersonalDataButton.grid_forget()
    clickedEntry2Button()

def clickedSeePersonalDataButton():
    window1.geometry('500x220')
    changeTariffButton.grid_forget()
    seeTariffsButton.grid_forget()
    seeServicesButton.grid_forget()
    seePersonalDataButton.grid_forget()
    addServiceButton.grid_forget()
    exitCallerButton.grid_forget()
    cursor.execute(F"""Select * from Callers where IdCaller = '{mainUserId}'""")
    current = cursor.fetchone()
    personalDataText.insert(INSERT, 'Ваше имя: ')
    personalDataText.insert(INSERT, current.Name)
    personalDataText.insert(INSERT, '\n')
    personalDataText.insert(INSERT, 'Ваш адрес: ')
    personalDataText.insert(INSERT, current.Address)
    personalDataText.insert(INSERT, '\n')
    personalDataText.insert(INSERT, 'Ваш номер паспорта: ')
    personalDataText.insert(INSERT, current.Passport)
    personalDataText.insert(INSERT, '\n')
    personalDataText.grid(row=1, column=0)
    OkSeePersonalDataButton.grid(row=2, column=0)

def clickedOkSeeServicesButton():
    servicesText.delete(1.0, END)
    servicesText.grid_forget()
    OkSeeServicesButton.grid_forget()
    clickedEntry2Button()

def clickedSeeServicesButton():
    window1.geometry('500x220')
    changeTariffButton.grid_forget()
    seeTariffsButton.grid_forget()
    seeServicesButton.grid_forget()
    seePersonalDataButton.grid_forget()
    addServiceButton.grid_forget()
    exitCallerButton.grid_forget()
    cursor.execute(f"""Select * from AdditionalServices where isActive = 1""")
    while 1:
        current = cursor.fetchone()
        if not current:
            break
        servicesText.insert(INSERT, current.Name)
        servicesText.insert(INSERT, ' ')
        servicesText.insert(INSERT, current.Price)
        servicesText.insert(INSERT, ' руб ')
        servicesText.insert(INSERT, current.Description)
        servicesText.insert(INSERT, '\n')
    servicesText.grid(row=1, column=0)
    OkSeeServicesButton.grid(row=2, column=0)


def clickedOkSeeTariffsButton():
    tariffsText.delete(1.0, END)
    tariffsText.grid_forget()
    OkSeeTariffsButton.grid_forget()
    clickedEntry2Button()

def clickedSeeTariffs2Button():
    window1.geometry('500x220')
    minTariffPrice = entryMinPrice.get()
    maxTariffPrice = entryMaxPrice.get()

    if minTariffPrice or maxTariffPrice:
        cursor.execute(f"""Select * from TariffPlans where Price >= '{minTariffPrice}' and Price <= '{maxTariffPrice}'""")
    else:
        cursor.execute(f"""Select * from TariffPlans""")
    while 1:
        current = cursor.fetchone()
        if not current:
            break
        tariffsText.insert(INSERT, current.Name)
        tariffsText.insert(INSERT, ' ')
        tariffsText.insert(INSERT, current.Price)
        tariffsText.insert(INSERT, ' руб ')
        tariffsText.insert(INSERT, current.Description)
        tariffsText.insert(INSERT, '\n')
    lblMinTariffPrice.grid_forget()
    entryMinPrice.grid_forget()
    lblMaxTariffPrice.grid_forget()
    entryMaxPrice.grid_forget()
    seeTariffs2Button.grid_forget()
    tariffsText.grid(row=1, column=0)
    OkSeeTariffsButton.grid(row=2, column=0)

def clickedSeeTariffsButton():
    changeTariffButton.grid_forget()
    seeTariffsButton.grid_forget()
    seeServicesButton.grid_forget()
    seePersonalDataButton.grid_forget()
    addServiceButton.grid_forget()
    exitCallerButton.grid_forget()
    lblMinTariffPrice.grid(row=1, column=0)
    entryMinPrice.grid(row=1, column=1)
    lblMaxTariffPrice.grid(row=2, column=0)
    entryMaxPrice.grid(row=2, column=1)
    seeTariffs2Button.grid(row=3, column=0)

def clickedOkChangeTariffButton():
    phoneNumber = comboPhoneNumbers.get()
    nameTariff = comboTariffs.get()
    cursor.execute(f"""Update PhoneNumbers Set IdTariffPlan = (Select IdTariffPlan from TariffPlans where Name = '{nameTariff}') where IdPhoneNumber = (Select IdPhoneNumber from PhoneNumbers where PhoneNumber = '{phoneNumber}')""")
    connection_to_db.commit()
    messagebox.showinfo('УРА', 'Тариф успешно изменен!')
    lblPhoneNumbers.grid_forget()
    lblTariffs.grid_forget()
    comboTariffs.grid_forget()
    comboPhoneNumbers.grid_forget()
    OkChangeTariffButton.grid_forget()
    clickedEntry2Button()

def clickedChangeTariffButton():
    changeTariffButton.grid_forget()
    seeTariffsButton.grid_forget()
    seeServicesButton.grid_forget()
    seePersonalDataButton.grid_forget()
    addServiceButton.grid_forget()
    exitCallerButton.grid_forget()
    lblPhoneNumbers.grid(row=10, column=0)
    phoneNumbers = ['']
    cursor.execute(f"Select PhoneNumber from PhoneNumbersCallers, PhoneNumbers where PhoneNumbersCallers.IdPhoneNumber=PhoneNumbers.IdPhoneNumber and IdCaller = '{mainUserId}'")
    while 1:
        current = cursor.fetchone()
        if not current:
            break
        phoneNumbers.append(current.PhoneNumber)
    comboPhoneNumbers['values'] = phoneNumbers

    comboPhoneNumbers.grid(row=10, column=1)

    lblTariffs.grid(row=50, column=0)
    tariffs = ['']
    cursor.execute(f"Select Name from TariffPlans")
    while 1:
        current = cursor.fetchone()
        if not current:
            break
        tariffs.append(current.Name)
    comboTariffs['values'] = tariffs

    comboTariffs.grid(row=50, column=1)
    OkChangeTariffButton.grid(row=70, column=1)

def clickedEntry2Button():
    window1.geometry('300x200')
    login2 = txtLogin2.get()
    password2 = txtPassword2.get()
    global mainUserId
    if (login2 == 'admin' and password2 == 'admin'): #ВСЕ ДЛЯ ДИРЕКТОРА
        window1.geometry('500x400')
        lblLogin2.grid_forget()
        txtLogin2.grid_forget()
        lblPassword2.grid_forget()
        txtPassword2.grid_forget()
        entry2Button.grid_forget()
        #lblDirector.grid(column=0, row=0)

        registerNewManagerButton.grid(column=0, row=1)
        deleteManagerButton.grid(column=0, row=2)
        addNewTariffButton.grid(column=0, row=3)
        changeTariffDataButton.grid(column=0, row=4)
        deleteTariffButton.grid(column=0, row=5)
        addNewPhoneNumberButton.grid(column=0, row=6)
        deletePhoneNumberButton.grid(column=0, row=7)
        changeManagerButton.grid(column=0, row=8)
        addNewServiceButton.grid(column=0, row=9)
        changeServiceButton.grid(column=0, row=10)
        checkBestManagersButton.grid(column=0, row=11)
        checkBestTariffsButton.grid(column=0, row=12)
        checkProfitButton.grid(column=0, row=13)
        exitDirectorButton.grid(column=0, row=14)
    else:
        key = b'$2b$12$COnvlB9Kses3CthyxNl9pu'
        ifPass = ''
        password2 = bcrypt.hashpw(str.encode(password2), key)
        cursor.execute(f"Select Name, IdCaller, Password from Users, Callers where Users.IdUser=Callers.IdUser and Users.Login = '{login2}'")
        row2 = cursor.fetchone()
        if row2:
            ifPass = str.encode(row2.Password)
        if password2 != ifPass:
            cursor.execute(f"Select Name, IdManager, Password from Users, Managers where Users.IdUser=Managers.IdUser and Users.Login = '{login2}'")
            row2 = cursor.fetchone()
            if row2:
                ifPass = str.encode(row2.Password)
            if password2 != ifPass:
                messagebox.showinfo('Предупреждение', 'Неверный логин или пароль!')
                clickedEntryButton()
            else: #ВСЕ ДЛЯ МЕНЕДЖЕРА
                lblLogin2.grid_forget()
                txtLogin2.grid_forget()
                lblPassword2.grid_forget()
                txtPassword2.grid_forget()
                entry2Button.grid_forget()
                mainUserId = row2.IdManager
                global lblManager
                lblManager = Label(window1, text=row2.Name+'(Manager)')
                #lblManager.grid(column=0, row=0)
                changeCallerStatusButton.grid(column=0, row=1)
                changeCallerPersonalDataButton.grid(column=0, row=2)
                seeFreePhoneNumbersButton.grid(column=0, row=3)
                givePhoneNumberButton.grid(column=0, row=4)
                exitManagerButton.grid(column=0, row=5)

        else: #ВСЕ ДЛЯ КЛИЕНТА
            lblLogin2.grid_forget()
            txtLogin2.grid_forget()
            lblPassword2.grid_forget()
            txtPassword2.grid_forget()
            entry2Button.grid_forget()
            mainUserId = row2.IdCaller
            global lblCaller
            lblCaller = Label(window1, text=row2.Name + '(Caller)')
            #lblCaller.grid(column=0, row=0)
            changeTariffButton.grid(column=0, row=1)
            seeTariffsButton.grid(column=0, row=2)
            seeServicesButton.grid(column=0, row=3)
            seePersonalDataButton.grid(column=0, row=4)
            addServiceButton.grid(column=0, row=5)
            exitCallerButton.grid(column=0, row=6)

def clickedReg2Button():
    name = txtName.get()
    address = txtAddress.get()
    passport = txtPassport.get()
    login = txtLogin.get()
    password = txtPassword.get()
    if (name=='' or address=='' or passport=='' or login=='' or password==''):
        messagebox.showinfo('Предупреждение', 'Все поля должны быть заполнены!')
        clickedRegButton()
    else:
        key = b'$2b$12$COnvlB9Kses3CthyxNl9pu'
        password = bcrypt.hashpw(str.encode(password), key)

        lblName.grid_forget()
        txtName.grid_forget()
        lblAddress.grid_forget()
        txtAddress.grid_forget()
        lblPassport.grid_forget()
        txtPassport.grid_forget()
        lblLogin.grid_forget()
        txtLogin.grid_forget()
        lblPassword.grid_forget()
        txtPassword.grid_forget()
        reg2Button.grid_forget()
        try:
            #cursor.execute(f"Insert into Users(Login, Password, isActive) Values ('{login}', '{password.decode()}', 1)")
            #connection_to_db.commit()
            #cursor.execute(f"Select IdUser from Users where Login = '{login}'")
            #row = cursor.fetchone()
            #idUserCaller = row.IdUser
            cursor.execute(f"""exec Register_Caller '{login}', '{password.decode()}', '{name}', '{address}', '{passport}'""")
            connection_to_db.commit()
            messagebox.showinfo('УРА', 'Регистрация прошла успешно!')
            startApp()
        except:
            messagebox.showinfo('Предупреждение', 'Такой логин или паспорт уже существует!')
            clickedRegButton()

def clickedRegButton():
    window1.geometry('300x200')
    regButton.grid_forget()
    entryButton.grid_forget()
    lblName.grid(column=0, row=0)
    txtName.grid(column=1, row=0)
    lblAddress.grid(column=0, row=10)
    txtAddress.grid(column=1, row=10)
    lblPassport.grid(column=0, row=20)
    txtPassport.grid(column=1, row=20)
    lblLogin.grid(column=0, row=30)
    txtLogin.grid(column=1, row=30)
    lblPassword.grid(column=0, row=40)
    txtPassword.grid(column=1, row=40)
    reg2Button.grid(column=0, row=50)

def clickedEntryButton():
    window1.geometry('300x200')
    regButton.grid_forget()
    entryButton.grid_forget()
    if txtLogin2.get():
        txtLogin2.delete(0, END)
    if txtPassword2.get():
        txtPassword2.delete(0, END)
    lblLogin2.grid(column=0, row=0)
    txtLogin2.grid(column=1, row=0)
    lblPassword2.grid(column=0, row=10)
    txtPassword2.grid(column=1, row=10)
    entry2Button.grid(column=1, row=20)

def startApp():
    window1.geometry('250x120')
    regButton.grid(column=0, row=1)
    entryButton.grid(column=0, row=2)
    window1.mainloop()

window1 = Tk()
window1.title("FakeMTS")
regButton = Button(window1, text="Регистрация", command=clickedRegButton)
entryButton = Button(window1, text="Войти", command=clickedEntryButton)
entry2Button = Button(window1, text="Войти", command=clickedEntry2Button)
reg2Button = Button(window1, text="Зарегистрироваться", command=clickedReg2Button)
lblName = Label(window1, text="Введите имя")
txtName = Entry(window1, width=30)
lblAddress = Label(window1, text="Введите адрес")
txtAddress = Entry(window1, width=30)
lblPassport = Label(window1, text="Введите паспорт")
txtPassport = Entry(window1, width=30)
lblLogin = Label(window1, text="Придумайте логин")
txtLogin = Entry(window1, width=30)
lblPassword = Label(window1, text="Придумайте пароль")
txtPassword = Entry(window1, width=30)
lblLogin2 = Label(window1, text="Введите логин")
txtLogin2 = Entry(window1, width=30)
lblPassword2 = Label(window1, text="Введите пароль")
txtPassword2 = Entry(window1, width=30, show='*')
lblDirector = Label(window1, text='Vladimir Putin(Director)')
changeTariffButton = Button(window1, text="Изменить тариф", command=clickedChangeTariffButton)
seeTariffsButton = Button(window1, text="Посмотреть тарифы", command=clickedSeeTariffsButton)
seeServicesButton = Button(window1, text="Посмотреть доп услуги", command=clickedSeeServicesButton)
seePersonalDataButton = Button(window1, text="Мои личные данные", command=clickedSeePersonalDataButton)
addServiceButton = Button(window1, text="Добавить доп услугу", command=clickedAddServiceButton)
lblPhoneNumbers = Label(window1, text="Выберите телефон")
lblTariffs = Label(window1, text="Выберите тариф")
comboPhoneNumbers = Combobox(window1)
comboTariffs = Combobox(window1)
OkChangeTariffButton = Button(window1, text="ОК", command=clickedOkChangeTariffButton)
lblMinTariffPrice = Label(window1, text="Минимальная цена")
lblMaxTariffPrice = Label(window1, text="Максимальная цена")
entryMinPrice = Entry(window1, width=10)
entryMaxPrice = Entry(window1, width=10)
seeTariffs2Button = Button(window1, text="Посмотреть тарифы", command=clickedSeeTariffs2Button)
tariffsText = scrolledtext.ScrolledText(window1, width=60, height=10)
OkSeeTariffsButton = Button(window1, text="ОК", command=clickedOkSeeTariffsButton)
servicesText = scrolledtext.ScrolledText(window1, width=60, height=10)
OkSeeServicesButton = Button(window1, text="ОК", command=clickedOkSeeServicesButton)
personalDataText = scrolledtext.ScrolledText(window1, width=60, height=10)
OkSeePersonalDataButton = Button(window1, text="ОК", command=clickedOkSeePersonalDataButton)
lblServices = Label(window1, text="Выберите доп услугу")
OkAddServiceButton = Button(window1, text="ОК", command=clickedOkAddServiceButton)
comboServices = Combobox(window1)
exitCallerButton = Button(window1, text="Выйти", command=clickedExitCallerButton)
changeCallerStatusButton = Button(window1, text="Изменить статус абонента", command=clickedChangeCallerStatusButton)
changeCallerPersonalDataButton = Button(window1, text="Изменить персональные данные абонента", command=clickedChangeCallerPersonalDataButton)
seeFreePhoneNumbersButton = Button(window1, text="Посмотреть доступные для выдачи номера", command=clickedSeeFreePhoneNumbersButton)
givePhoneNumberButton = Button(window1, text="Выдать номер абоненту", command=clickedGivePhoneNumberButton)
comboStatusCallers = Combobox(window1)
lblStatusCallers = Label(window1, text="Выберите абонента")
OkChangeStatusCallerButton = Button(window1, text="Изменить", command=clickedOkChangeStatusCallerButton)
comboDataCallers = Combobox(window1)
lblDataCallers = Label(window1, text="Выберите абонента")
OkChangeCallerPersonalDataButton = Button(window1, text="ОК", command=clickedOkChangeCallerPersonalDataButton)
lblNameDataCaller = Label(window1, text="Имя")
lblAddressDataCaller = Label(window1, text="Адрес")
lblPassportDataCaller = Label(window1, text="Паспорт")
entryNameCaller = Entry(window1, width=20)
entryAddressCaller = Entry(window1, width=20)
entryPassportCaller = Entry(window1, width=20)
OkChangeCallerPersonalData2Button = Button(window1, text="ОК", command=clickedOkChangeCallerPersonalData2Button)
phoneNumbersText = scrolledtext.ScrolledText(window1, width=60, height=10)
OkSeeFreePhoneNumbersButton = Button(window1, text="ОК", command=clickedOkSeeFreePhoneNumbersButton)
comboNewPhoneCallers = Combobox(window1)
lblNewPhoneCallers = Label(window1, text="Выберите абонента")
comboAvailablePhoneNumbers = Combobox(window1)
lblAvailablePhoneNumbers = Label(window1, text="Выберите номер телефона")
OkGivePhoneNumberButton = Button(window1, text="ОК", command=clickedOkGivePhoneNumberButton)
exitManagerButton = Button(window1, text="Выйти", command=clickedExitManagerButton)
#ДИРЕКТОР
registerNewManagerButton = Button(window1, text="Регистрация нового менеджера", command=clickedRegisterNewManagerButton)
deleteManagerButton = Button(window1, text="Удалить менеджера", command=clickedDeleteManagerButton)
addNewTariffButton = Button(window1, text="Добавить новый тариф", command=clickedAddNewTariffButton)
changeTariffDataButton = Button(window1, text="Изменить данные тарифа", command=clickedChangeTariffDataButton)
deleteTariffButton = Button(window1, text="Удалить тариф", command=clickedDeleteTariffButton)
addNewPhoneNumberButton = Button(window1, text="Добавить номер телефона", command=clickedAddNewPhoneNumberButton)
deletePhoneNumberButton = Button(window1, text="Удалить номер телефона", command=clickedDeletePhoneNumberButton)
changeManagerButton = Button(window1, text="Изменить данные менеджера", command=clickedChangeManagerButton)
addNewServiceButton = Button(window1, text="Добавить дополнительную услугу", command=clickedAddNewServiceButton)
changeServiceButton = Button(window1, text="Изменить данные услуги", command=clickedChangeServiceButton)
checkBestManagersButton = Button(window1, text="Просмотреть менеджеров по выданным номерам", command=clickedCheckBestManagersButton)
checkBestTariffsButton = Button(window1, text="Просмотреть популярные тарифы", command=clickedCheckBestTariffsButton)
checkProfitButton = Button(window1, text="Посмотреть выручку", command=clickedCheckProfitButton)
exitDirectorButton = Button(window1, text="Выйти", command=clickedExitDirectorButton)
lblLoginDataManager = Label(window1, text="Введите логин")
lblPasswordDataManager = Label(window1, text="Введите пароль")
lblNameDataManager = Label(window1, text="Введите имя")
lblAddressDataManager = Label(window1, text="Введите адрес работы")
lblPhoneDataManager = Label(window1, text="Введите телефон")
txtLoginDataManager = Entry(window1, width=30)
txtPasswordDataManager = Entry(window1, width=30)
txtNameDataManager = Entry(window1, width=30)
txtAddressDataManager = Entry(window1, width=30)
txtPhoneDataManager = Entry(window1, width=30)
OkRegisterNewManagerButton = Button(window1, text="OK", command=clickedOkRegisterNewManagerButton)
lblChooseManager = Label(window1, text='Выберите менеджера')
comboDeleteManager = Combobox(window1)
OkDeleteManagerButton = Button(window1, text="OK", command=clickedOkDeleteManagerButton)
lblNameTariff = Label(window1, text="Введите название")
lblPriceTariff = Label(window1, text="Введите цену")
lblDescriptionTariff = Label(window1, text="Введите описание")
txtNameTariff = Entry(window1, width=30)
txtPriceTariff = Entry(window1, width=30)
txtDescriptionTariff = Entry(window1, width=30)
OkAddNewTariffButton = Button(window1, text="OK", command=clickedOkAddNewTariffButton)
lblChangeTariff = Label(window1, text="Выберите тариф")
comboChangeTariff = Combobox(window1)
lblNameChangeTariff = Label(window1, text="Введите новое имя")
lblPriceChangeTariff = Label(window1, text="Введите новую цену")
lblDescriptionChangeTariff = Label(window1, text="Введите новое описание")
txtNameChangeTariff = Entry(window1, width=30)
txtPriceChangeTariff = Entry(window1, width=30)
txtDescriptionChangeTariff = Entry(window1, width=30)
OkChangeTariffDataButton = Button(window1, text="OK", command=clickedOkChangeTariffDataButton)
OkDeleteTariffButton = Button(window1, text="OK", command=clickedOkDeleteTariffButton)
lblNewPhone = Label(window1, text="Введите номер телефона")
txtNewPhone = Entry(window1, width=30)
OkAddNewPhoneNumberButton = Button(window1, text="OK", command=clickedOkAddNewPhoneNumberButton)
lblDeleteNumber = Label(window1, text="Выберите телефон")
comboDeleteNumbers = Combobox(window1)
OkDeletePhoneNumberButton = Button(window1, text="OK", command=clickedOkDeletePhoneNumberButton)
lblNameManager = Label(window1, text="Введите новое имя")
lblAddressManager = Label(window1, text="Введите новый адрес")
lblPhoneManager = Label(window1, text="Введите новый телефон")
txtNameManager = Entry(window1, width=30)
txtAddressManager = Entry(window1, width=30)
txtPhoneManager = Entry(window1, width=30)
OkChangeManagerButton = Button(window1, text="OK", command=clickedOkChangeManagerButton)
lblNameService = Label(window1, text="Введите название")
lblPriceService = Label(window1, text="Введите цену")
lblDescriptionService = Label(window1, text="Введите описание")
txtNameService = Entry(window1, width=30)
txtPriceService = Entry(window1, width=30)
txtDescriptionService = Entry(window1, width=30)
OkAddNewServiceButton = Button(window1, text="OK", command=clickedOkAddNewServiceButton)
lblChooseService = Label(window1, text="Выберите доп услугу")
comboChooseService = Combobox(window1)
lblNameChooseService = Label(window1, text="Введите новое название")
lblPriceChooseService = Label(window1, text="Введите новую цену")
lblDescriptionChooseService = Label(window1, text="Введите новое описание")
txtNameChooseService = Entry(window1, width=30)
txtPriceChooseService = Entry(window1, width=30)
txtDescriptionChooseService = Entry(window1, width=30)
OkChangeServiceButton = Button(window1, text="OK", command=clickedOkChangeServiceButton)
managersText = scrolledtext.ScrolledText(window1, width=60, height=10)
OkCheckBestManagersButton = Button(window1, text="OK", command=clickedOkCheckBestManagersButton)
bestTariffsText = scrolledtext.ScrolledText(window1, width=60, height=10)
OkCheckBestTariffsButton = Button(window1, text="OK", command=clickedOkCheckBestTariffsButton)
profitText = scrolledtext.ScrolledText(window1, width=40, height=1)
OkCheckProfitButton = Button(window1, text="OK", command=clickedOkCheckProfitButton)
txtPassword2.show = '*'
startApp()
connection_to_db.close()
