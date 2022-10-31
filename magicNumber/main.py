import filegesture as fg
import searchuser as sc
import Menu
import Account
import level
import magic_number

if Account.start() == 1:
    sc.login(Account.Login())
elif Account.start() == 2:
    sc.registration(Account.Register())
else:
    exit(0)

