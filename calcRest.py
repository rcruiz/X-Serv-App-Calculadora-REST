#!/usr/bin/python

"""
Calculadora simple version REST
Rosa Cristina Ruiz Rivas
Alumna de SAT
"""

import webapp


class calcREST(webapp.webApp):

    def parse(self, request):
        """Parse the received request, extracting the relevant information."""

        verbo = request.split(' ', 2)[0]
        recurso = request.split(' ', 2)[1]
        cabCuerpo = request.split('\r\n\r\n', 1)
        if len(cabCuerpo) == 2:
            cuerpo = cabCuerpo[1]
        else:
            cuerpo = ""
        return(verbo, recurso, cuerpo)

    def process(self, parsedRequest):
        """Process the relevant elements of the request.

        Returns the HTTP code for the reply, and an HTML page.
        """

        try:
            operador = parsedRequest[1].split('/')[1]
            op1 = int(parsedRequest[1].split('/')[2])
            op2 = int(parsedRequest[1].split('/')[3])
            if operador == "suma":
                res = op1 + op2
                operando = "+"
            elif operador == "resta":
                res = op1 - op2
                operando = "-"
            elif operador == "multiplicacion":
                res = op1 * op2
                operando = "*"
            elif operador == "division":
                operando = "/"
                res = op1 / op2
            else:
                operando = False
        except:
            httpCode = "400 Bad Request"
            htmlBody = "Usage Error: /operador/num1/num2"
        else:
            if (parsedRequest[0] == 'PUT') and operando is not False:
                httpCode = "200 OK"
                htmlBody = '(' + str(op1) + operando + str(op2) + ')'
                htmlBody += parsedRequest[2]
            elif (parsedRequest[0] == 'GET') and operando is not False:
                httpCode = "200 OK"
                htmlBody = str(op1) + operando + str(op2) + " = " + str(res)
            elif operando is False:
                httpCode = "400 Bad Request"
                htmlBody = "Operador = suma, resta, multiplicacion, division"
            else:
                httpCode = "405 Error"
                htmlBody = "HTTP verb " + parsedRequest[0] + " not supported"
        return (httpCode, "<html><body><p>" + htmlBody + "</p></body></html>")


if __name__ == "__main__":
    testWebApp = calcREST("localhost", 1234)
