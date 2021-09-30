"""
    Anotação de envio de email com a Api Mailgum

    email_from = "desenvolvedoreneas2000@gmail.com"
    email_to = "eneassilva94@gmail.com"
    passowrd = "*1**23*1"
    message_sub = "send mail."
    message_body = "Hello world!"

    Exemplo 001
    curl -s --user 'api:YOUR_API_KEY' \
    https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages \
    -F from='Excited User <exemple@gmail.com>' \
    -F to= e"desenvolvedoreneas2000@gmail.com" \
    -F to= "eneassilva94@gmail.com" \
    -F subject= "send mail." \
    -F text= "Hello world!"



"""