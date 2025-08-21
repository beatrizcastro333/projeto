import serial

PORT = "COM3"  # Porta serial XBEE receiver
BAUDRATE = 9600 

ser = serial.Serial(PORT, BAUDRATE) # Iniciar conexão serial

# Mensagem a ser enviada
mensagem = "Parece que não. Tenho pensado muito sobre marketing desde 2011, quando me interessei pelo tema para escrever meu TCC. De lá para cá, foram cursos, palestras, disciplinas, 6 meses de uma pós-graduação, o mestrado, agora o doutorado, muitos livros, artigos e conversas com outros colegas (principalmente os que não são bibliotecários). O que me faz pressupor que ainda não temos marketing nas bibliotecas brasileiras é o resultado de tudo isso acima, mas que se conclui principalmente em virtude de uma disciplina que fiz em 2016. Entrei para o Doutorado em Ciência da Informação com um projeto sobre marketing e para poder falar com mais propriedade sobre o tema, me matriculei regularmente na disciplina de Teorias em Marketing, do Programa de Administração da UFSC. Os professores responsáveis por ela fizeram estudos em Boston, uma das melhores escolas sobre o assunto internacionalmente e disseram para o aflito doutorando aqui que seu projeto de pesquisa estava longe de ser sobre marketing. Esta disciplina tinha como pilar a obra “Marketing theory: evolution and evaluation”, de Sheth, Gardner e Garrett, onde eles traçam uma linha do tempo com todas as teorias e os principais responsáveis por cada uma delas (poderíamos ter um livro desses na Biblioteconomia). Desmembramos o livro, parágrafo por parágrafo, durante 6 meses, e ali foi possível perceber a evolução de uma área, dos seus conceitos, da relação com outros profissionais, da inserção de novas metas e do acompanhamento com a tecnologia.Buscando sempre trazer relações com a nossa profissão, fui começando a entender que o que temos hoje em nossa área é o mesmo contexto do início do marketing, lá nos anos 1900. Tanto teóricos como profissionais não sabiam se estavam tratando de um método, de uma técnica, de uma arte ou de uma nova área do conhecimento; não sabiam onde o marketing começava e onde terminava e um elemento fundamental ainda estava em desenvolvimento: a competitividade entre as empresas.Foi com a competitividade que o marketing se desenvolveu mais rapidamente, principalmente a partir da década de 30 e nas seguintes de maneira quase que exponencial. E é justamente este elemento que não temos no universo das bibliotecas: não há competição estratégica, de posicionamento de mercado entre estes ambientes, logo, o comodismo acaba por ser quase que inevitável (o que vai bater lá na necessidade da inovação).Além disso, somos semelhantes àquela época (dos anos 1900) que entendia o marketing somente como promoção. É este o nosso grande equívoco. Estamos colocando no mesmo pacote a divulgação, a visibilidade, a promoção e a publicidade como se todos fossem marketing e isso é muito errado. Com as mídias sociais, este quadro se agrava mais ainda. Um tweet, um post, um e-mail, um vídeo, um site… pronto, tenho o marketing da minha biblioteca. Não!\n"

# Enviar a mensagem
ser.write(mensagem.encode())

print(f"Mensagem enviada: {mensagem}")

# Encerrar conexão
ser.close()
