import string

# Aqui pega o alfabeto em minusculo
alpha = string.ascii_lowercase      

# Função para criptografar o texto
def cipher(modo, msg, key):
    text_cipher = ''
    text_decipher = msg.lower()
    for ch in text_decipher:
        if ch in alpha:               
            idx = alpha.find(ch) + key    
            if idx >= 26:
                idx -= 26    
            text_cipher += alpha[idx]
        else:
            text_cipher += ch
    return text_cipher

# Função para descriptografar o texto
def decipher(modo, msg, key):
    text_decipher = ''
    text_cipher = msg.lower()
    for ch in text_cipher:
        if ch in alpha:               
            idx = alpha.find(ch) - key        
            text_decipher += alpha[idx]
        else:
            text_decipher += ch
    return text_decipher

#Função para gerar a mensagem criptografada ou descriptografada
def geraMsgTraduzida(modo, mensagem, chave):
    nova_mensagem = ''
    if modo == 'c' or modo == 'criptografar':
        nova_mensagem = cipher(modo, mensagem, chave)
    elif modo == 'd' or modo == 'descriptografar':
        nova_mensagem = decipher(modo, mensagem, chave)
    return nova_mensagem
