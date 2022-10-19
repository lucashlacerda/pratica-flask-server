from flask import Flask, request

app = Flask(__name__)

@app.route('/numeros', methods=['GET', 'POST'])
def GET_media():

        if request.method == 'POST':
                primeira = float(request.form.get('primeiro'))
                segunda = float(request.form.get('segundo'))
                terceira = float(request.form.get('terceiro'))
                media = (primeira + segunda + terceira) / 3
                

                if (terceira > segunda and primeira):
                        maior = terceira
                
                elif (segunda > primeira and terceira):
                        maior = segunda
                else:
                        maior = primeira
                        
                if (terceira < segunda and primeira):
                        menor = terceira
                
                elif (segunda < primeira and terceira):
                        menor = segunda
                else:
                        menor = primeira
                        
                
                return ''' <h3> O maior número é: {}</h3><h3> O menor número é: {} </h3><h3> A média dos números é: {}</h3>'''.format(maior, menor, media)
        
        return '''
                <form method="POST">
                <div><label>Primeiro número: <input type="number"

                name="primeiro"></label></div>

                <div><label>Segundo número: <input type="number"

                name="segundo"></label></div>
                <div><label>Terceiro número: <input type="number"

                name="terceiro"></label></div>

                <input type="submit" value="Enviar">
                </form>'''

@app.route ('/imc', methods=['GET','POST'])
def GET_pesoealtura():
        
        if request.method == 'POST':
                peso = float(request.form.get('peso'))
                altura = float(request.form.get('altura'))

                imc = peso / (altura * altura)

                if(imc < 18.5):
                        resultado = "Abaixo do peso"
                elif(imc >= 18.6 and imc <= 24.9):
                        resultado = "Peso ideal (parabéns)"
                elif(imc >= 25 and imc <= 29.9):
                        resultado = "Levemente acima do peso"
                elif(imc >= 30 and imc <= 34.9):
                        resultado = "Obesidade grau I"
                elif(imc >= 35 and imc <= 29.9):
                        resultado = "Obesidade grau II (severa)"
                else:
                        resultado = "Obesidade III (Mórbida)"

                return '''<h3> IMC: {} </h3>'''.format(resultado)
        return '''
                <form method="POST">
                <div><label>Altura: <input type="text"

                name="altura"></label></div>

                <div><label>Peso: <input type="text"

                name="peso"></label></div>

                <input type="submit" value="Enviar">
                </form>'''
        
             


if __name__ == "__main__":
        app.run()
        
        

