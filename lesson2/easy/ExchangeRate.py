import urllib2
import xml.sax.handler

class CurrencyRateHandler(xml.sax.handler.ContentHandler):
        def __init__(self):
                self.inTag = ""
                self.charCode = ""
                self.mapping = {}

        def startElement(self, name, attributes):
                if name in set(["CharCode","Nominal", "Value"]):
                        self.buffer = ""
                        self.inTag = name
                else:
                        self.inTag = ""

        def characters(self, data):
                if self.inTag:
                        self.buffer += data

        def endElement(self,name):
                if name == "CharCode":
                        self.charCode = self.buffer
                        self.mapping[self.charCode] = {}
                elif name == "Nominal":
                        self.mapping[self.charCode][self.inTag] = int(self.buffer)
                elif name == "Value":
                        self.mapping[self.charCode][self.inTag] = float(self.buffer.replace(',','.'))
                self.inTag = ""
        #вывод курса валюты
        def output_of_exchange_rate(self, currency_code):
            for key, value in self.mapping.items():
                if (key == currency_code):
                    m = []
                    for key, val in value.items():
                        m.append(val)
                    print str(m[0])+' '+currency_code+' = '+str(m[1])+' RUB'
                

currency_code = raw_input("Enter the currency code: ")
#подключение и сбор информации
u = urllib2.urlopen("http://www.cbr.ru/scripts/XML_daily.asp", timeout=10)
parser = xml.sax.make_parser()
handler = CurrencyRateHandler()
parser.setContentHandler(handler)
parser.parse(u)

handler.output_of_exchange_rate(currency_code)