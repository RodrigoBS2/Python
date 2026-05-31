import sys
from pyqtgraph.Qt import QtWidgets
from interface import OsciloscopioApp
import serial_reader

if __name__ == '__main__':
    # 1. Inicia a thread que consome dados da porta serial
    conexao_serial = serial_reader.iniciar_leitura_serial()

    # 2. Inicia o motor gráfico do PyQt
    app = QtWidgets.QApplication(sys.argv)
    
    # 3. Cria a interface passando a conexão serial (para fechar a porta ao sair)
    janela = OsciloscopioApp(conexao_serial)
    janela.show()
    
    # 4. Executa o loop principal da aplicação
    sys.exit(app.exec())

