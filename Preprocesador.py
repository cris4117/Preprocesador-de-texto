class PreProcesadorTexto:
    def __init__(self,texto):
        self.texto_minuscula=texto.lower()
    
    def limpiar_texto(self):
        self.texto_formato=""
        for caracter in self.texto_minuscula:
            if ('a' <= caracter <= 'z') or (caracter == ' ') or ('á' <= caracter <= 'ú'):
                self.texto_formato+=caracter
            else:
                self.texto_formato+=" "
    
    def tokenizar(self):
        self.palabras = [palabra for palabra in self.texto_formato.split(" ") if palabra]

    def remover_stopwords(self,stopwords):
        self.palabras_filtradas=[]
        for palabra in self.palabras:
            if palabra not in stopwords:
                self.palabras_filtradas.append(palabra)

ruta_entrada="raw-text.txt"
ruta_salida="processed-text.txt"

try:
    with open(ruta_entrada,"r",encoding="utf-8") as archivo:
        raw_text=archivo.read()
except FileNotFoundError:
        print("El archivo no existe")

texto=PreProcesadorTexto(raw_text)
texto.limpiar_texto()
texto.tokenizar()

try:
    with open("stop-words.txt","r",encoding="utf-8") as archivo:
        stop_words=archivo.read().splitlines()
except FileNotFoundError:
        print("El archivo no existe")

texto.remover_stopwords(stop_words)
print(texto.palabras_filtradas)

with open(ruta_salida,"w",encoding="utf-8") as archivo:
    archivo.write("\n".join(texto.palabras_filtradas))