from tools import*
from tkinter import*

main = Tk()

main.title('Ciphra de Julio Ceasar')

def traduzirMsg(args):
    inputValueMsg=txtMsg.get("1.0","end-1c")
    inputValueChave=txtchave.get("1.0","end-1c")
    if args == 1:
        txtMsgTranslation.delete(1.0, END)
        txtMsgTranslation.insert(END, geraMsgTraduzida('c', inputValueMsg, int(inputValueChave)))
    if args == 2:   
        msgDecrypt = txtMsgTranslation.get("1.0", "end-1c")
        txtMsgTranslation.delete(1.0, END)
        txtMsgTranslation.insert(END, geraMsgTraduzida('d', msgDecrypt, int(inputValueChave)))

lblMsg = Label(main, text="Mensagem", width=15, height=1)
lblMsg.grid(row=0, column=0)
txtMsg = Text(main, height=5, width=30)
txtMsg.grid(row=0, column=1)

lblChave = Label(main, text="Digite sua chave", width=15, height=1)
lblChave.grid(row=1, column=0)
txtchave = Text(main, height=1, width=30)
txtchave.grid(row=1, column=1)

lblMsgTranslation = Label(main, text="Msg Traduzida", width=15, height=1)
lblMsgTranslation.grid(row=2, column=0)
txtMsgTranslation = Text(main, height=5, width=30)
txtMsgTranslation.grid(row=2, column=1)

btnCipher = Button(main, text="Crypto", command=lambda:traduzirMsg(1))
btnDecipher = Button(main, text="Decrypto", command=lambda:traduzirMsg(2))

btnCipher.grid(row=3, column=1)
btnDecipher.grid(row=4, column=1)

# L x A + ME + MT
main.geometry("400x250+200+100")
main.mainloop()