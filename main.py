# jogo #
from time import sleep
import time


# criando funcao para validar respostas




print('=+' * 30)
print('BEM VINDO AO JOGO RUBIKS ADVENTURE!!')
print('O objetivo do jogo é se tornar o maior guerreiro da região e conquistar o máximo de poder !')
print('=+' * 30)
print()
print()
print()
print('''
Haverá perguntas em que você deve responder com números.
exemplo: Dar oi para Kafra [1]
(para executar a ação, você deverá escrever 1 como resposta)
      ''')
print('LEMBRE-SE DE RESPONDER SEMPRE DA FORMA QUE É EXPOSTA NA PERGUNTA!')
print('''EXEMPLO:
 você é legal? (sim ou nao) 
 Caso a resposta não for formatada da forma certa, você terá que enviar novamente a resposta.
 A resposta deverá ser "sim" ou "nao", escrito da mesma forma que exposto''')

print()
print()
sleep(1)
nomeUsuario = input('Bem vindo ao jogo, digite seu nome por favor: \n')

print()
print()
print()

print('Para escolher uma classe, digite "espadachim, para selecionar espadachim. Para escolher mago, digite "mago".')
print()

classe = input('Digite a sua classe (espadachim/ mago): \n').lower()
while classe != "espadachim" and classe != "mago":
    classe = input('Digite a sua classe (espadachim/ mago): \n').lower()


print()

print('De acordo com a escolha da sua classe, habilidades e itens serão diferentes. ')
print()
print()

# iniciando variaveis que utilizarei
habilidades = []
inventario = []
nivel = 0


# criando funcoes
def addInventario(item):
    inventario.append(item)


def popInventario(item):
    inventario.pop()


def addHabilidade(skill):
    habilidades.append(skill)

def repetirPergunta2(pergunta, condicao1, condicao2):

    while pergunta != condicao1 and pergunta != condicao2:
        print('Resposta inválida, tente novamente!')
        pergunta = input()


    return str(pergunta)


if classe == "espadachim":
    addHabilidade('espetada insana')
    addHabilidade('bisca louca')
    addHabilidade('bicuda na canela')
    addHabilidade('tapa tapa')

    addInventario('laminas gemeas')
    addInventario('adaga')
    addInventario('escudo de prontera')
    addInventario('botas protetoras')

elif classe== "mago":
    addHabilidade('raio')
    addHabilidade('explosao magica')
    addHabilidade('cotovelada no queixo')
    addHabilidade('ira do deus do trovão')

    addInventario('cajado do aprendiz')
    addInventario('varinha magica')
    addInventario('chapéu do olho mágico')
    addInventario('botas magicas')

print('Olá, meu nome é Kafra, estou aqui para guiar você!')

sleep(1)

print('Você nasceu na cidade de prontera, seus itens atuais são :')
print()

for i in inventario:
    print(i, end='   |   ')

print()
print()
print()

print(' E suas habilidades são :')

for w in habilidades:
    print(w, end='  |   ')

print()
print()

print(
    'Para aprimorar seus equipamentos e habilidades, você precisa derrotar inimigos, tente atravessar a cidade e ir para Sidney, lá encontrará monstros do seu nível.\nSe você for mais corajoso, poderá ir para cidade de Catapimbas, no entanto, o vigia poderá impedir sua entrada, se não for forte o suficiente para entrar.')
print()
print()

sleep(3)
print()
print('=+' * 30)
print('')

perguntaCidade1 = 0


perguntaCidade1 = input('Para qual cidade você quer ir ? ( Sidney/ Catapimbas) \n').lower()
while perguntaCidade1 != 'sidney' and perguntaCidade1 != 'catapimbas':
    perguntaCidade1 = input('Para qual cidade você quer ir ? ( Sidney/ Catapimbas) \n').lower()

if perguntaCidade1 == 'catapimbas':
    print(
        'Você ainda não tem nivel suficiente para entrar na cidade de Catapimbas. Tente novamente mais tarde.Seu nivel atual é {}.'.format(
            nivel))
    print('Então, vamos para Sidney, amigao!!!!!')
    sleep(2)

else:
    print('Ótima escolha, em Sidney você poderá encontrar oponentes dignos, vamos lá!!!!')

print()
print()
print()
print('=+' * 30)
print('Você está sendo teletransportado para Sidney, aperte os cintos!')
print('=+' * 30)
print()
print()

print(
    'A cidade de Sidney é conhecida por grandes florestas, e pelos monstros que ali vivem, os mais conhecidos, são pequenas bolas rosas, chamados de Poring. Além dos porings, existe uma espécie de Coelho Mutante, chamada Lunatic.')
sleep(1)
print('Tome cuidado, essas criaturas parecem ser fofas, mas são letais!')

print()
print()
print()
print()
print('A cidade de Sidney possui um céu lindo, -muitos artistas já homenagearam esse céu, disse Kafra.')
print()
print()
print('Você olha pra cima e constata, realmente, é um céu incrível.')
print()
sleep(3)

print(
    'Chegando na floresta de Sidney, você nota que logo a frente, existe um poring, e lembra das dicas de Kafra, de forma que, pega seu(sua) {} e ataca ele e um duelo é iniciado !!!!!'.format(
        inventario[0]))

print()
print()
print()

sleep(3)

print()

print()

print()
print('~^' * 30)
print('FOI INICIADO UM DUELO ENTRE {} E Poring'.format(nomeUsuario))
print('~^' * 30)
print()

sleep(3)
sleep(4)
vidaUsuario = 100
poderUsuario = 10
print('Você está no nivel {}, possui {} de poder de ataque.\nPoring tem 20 de vida e caso derrotado, derruba uma poção de experiência no chão!'.format(
        nivel, poderUsuario))

sleep(3)

print('Essas são suas habilidades:')
for i in habilidades:
    print(i, end= '  |  ')

ataque1 = input('Qual habilidade você deseja escolher? \n').lower().strip()

while ataque1 != habilidades[0].lower() and ataque1 != habilidades[1].lower() and ataque1  != habilidades[2].lower() and ataque1 != habilidades[3].lower():
    ataque1 = input('Qual habilidade você deseja escolher? \n').lower().strip()



print('A habilidade escolhida foi {}, que sorte, a habilidade usada foi super efetiva!'.format(ataque1))

sleep(3)

print()
print('O Poring foi derrotado em apenas um golpe!!!!')

sleep(3)
print('parabens, você recebeu Poção de Experiência, o item foi adionado em seu inventario!')
addInventario('poção de experiencia')

print()

sleep(3)
print('Você deseja ver seu inventario?')
perguntaInventario1 = input('sim ou nao?\n').lower().strip()
while perguntaInventario1 != 'sim' and perguntaInventario1 != 'nao':
    perguntaInventario1 = input('sim ou nao? \n').lower().strip()

print()
print()

sleep(1)

if perguntaInventario1 == 'sim':
    for i in inventario:
        print(i, end='  |  ')
print()

print('Você deseja usar a poção de experiencia? não será possível usar futuramente!')
perguntaInventario2 = input('sim ou nao?\n').lower().strip()

while perguntaInventario2 != 'sim' and perguntaInventario2 != 'nao':
    perguntaInventario2 = input('sim ou nao? \n').lower().strip()


if perguntaInventario2 == 'sim':
    nivel += 1
    for i in range(2):
        print('+-' * 5)
        print()
    print('Parabéns, você subiu de nível, seu nível agora é {}! '.format(nivel))
    print()
    for i in range(2):
        print('=-' * 5)
        print()
    popInventario(-1)



elif perguntaInventario2 == 'nao':
    print('Que pena, perdeu a chance de subir de nível')
    inventario.pop(-1)

print('Agora esses sao os itens em seu inventario:')
for i in inventario:
    print(i, end='  |  ')
sleep(2)
print()
print()
sleep(1)
print('Você tem a opção de seguir em frente, para Prontera')
print()
sleep(1)
print('Kafra te guia para uma cidade capaz de te fornecer melhores resultados para sua evoluçao pessoal!')
print('Você agradeçe kafra como?')
a = input('''
Abrindo um grande sorriso e abraçando ela [1]
Pulando de alegria [2]\n''').lower().strip()

if a == '1':
    print('{} começa a sorrir muito e da um pulo em cima de Kafra, abracando ela !!! ' .format(nomeUsuario))

elif a == '2':
    print('Você deu um pulo muito alto de alegria e fez uma dancinha para comemorar a sua evolução !')



print()
print()



while True:
        print('Você retorna para Prontera e lá encontra Kafra, ela te diz que você já é capaz de viajar de Catapimbas !')
        sleep(2)
        print('')
        print('Kafra diz que você pode ir para Catapimbas e evoluir!!!!')
        perguntaCidade3 = input('''Qual será sua escolha?
        Agradecer Kafra[1]
        Sair sem falar nada [2] \n''').lower().strip()

        if perguntaCidade3 == '1':
            print('OBRIGADO KAFRA!')


        print('VOCE ESTÁ SENDO TELETRANSPORTADO PARA CATAPIMBAS!')
        sleep(1)


        print('^=' * 30)
        print(
            'Bem vindo a catapimbas, cidade conhecida por possuir monstros capazes de fornecer diversos itens e muita experiencia!')
        print()
        print()
        print()
        sleep(1)
        print('*mensagem de Kafra*')
        print()
        sleep(2)
        print(
            'Graças a bicicleta concedida por Pv, você será capaz de executar uma nova habilidade, chamada "Dar Grau" com sua bike!')
            print('A habilidade nao pode ser usada em combate')

        darGrauHabilidade = input('Digite sim se voce deseja aprender essa nova habilidade: (sim ou SIM) \n').lower().strip()



        habilidades.append("dar grau")
        print('Parabens, essas são suas habilidades agora!')
        print()
        print()
        print()
        for i in habilidades:
            print(i, end=' |  ')

        print()
        print()
        print()
        sleep(2)
        print(
            'A cidade de Catapimbas possui uma vasta quantidade de florestas e você pode ir desfrutar um pouco das belezas naturais catapimbianas!')
        print()

        print()
        sleep(2)
        print(
            'Kafra aparece repentinamente para guiar você até a floresta da Inteligência!\nVocê, rapidamente, pega sua bicicleta e usa sua habilidade "Dar Grau" e logo chega na floresta!.')
        sleep(2)
        print()
        print()
        print(
            'Logo a frente, está Paulo Victor, um rapaz conhecido por dar grandes conselhos para jovens guerreiros como você!')
        sleep(2)
        print(
            'Paulo Victor diz para você que não há nada melhor que adquirir um cubo mágico e aprender algoritmos para resolução dele!')
        print('Dessa forma, adquirir um cubo mágico tornou seu objetivo de vida!')
        sleep(2)
        print('Você, esperto como sempre, visualiza um poster e pega sua bicicleta usando sua habilidade "Dar grau". ')
        sleep(1)
        print('_________________________________________')
        print('|                                        |')
        print('|                                        |')
        print('|         VENHA AQUI                     |')
        print('|         PARA APRENDER SOBRE            |')
        print('|         SEGREDOS DO CUBO MÁGICO        |')
        print('|                                        |')
        print('|          Rua dos só quadrados,23       |')
        print('|________________________________________|')

        sleep(2)
        sleep(4)
        print('Nisso, você decide ir para o local exposto!')
        sleep(2)

        print(
            'De longe, você observa que existem varias pessoas no local, mas em especial, nota a presenca de Renan Cerpe, grande cubista!')
        print('Você fica um pouco nervoso, mas olha para Kafra e lembra que está tudo bem!')
        print('')
        print('Você sabe que é capaz de tudo, então respira e fica tranquilo. "Tudo vai dar certo", diz {}.'.format(
            nomeUsuario))
        print(
            'Você chega na rua do Só quadrados, e nota que para conquistar o cubo mágico, deve derrotar o grande Renan Cerpe, nível 2!')
        print('Você inicia um duelo contra Renan Cerpe:')
        sleep(1)
        print('~^' * 30)
        print('FOI INICIADO UM DUELO ENTRE {} E Renan Cerpe'.format(nomeUsuario))
        print('~^' * 30)
        print()
        sleep(2)
        print('')

        vidaRenan = 50
        print('Essas são suas habilidades:')
        for i in habilidades:
            print(i, end='  |  ')

        ataque1 = input('Qual habilidade você deseja escolher? \n').lower().strip()

        while ataque1 != habilidades[0].lower() and ataque1 != habilidades[1].lower() and ataque1 != habilidades[
            2].lower() and ataque1 != habilidades[3].lower():
            ataque1 = input('Qual habilidade você deseja escolher? \n').lower().strip()


        print()
        print()
        sleep(1)
        print('Renan Cerpe tem 50 de vida!')
        print()

        if ataque1 == habilidades[0].lower().strip():
            print('Você usou {} e deu 10 de dano!'.format(habilidades[0]))
            print('A habilidade usada não foi muito efetiva!')
            vidaRenan = 40
            print('A vida de Renan Cerpe foi para : {} '.format(vidaRenan))

        elif ataque1 == habilidades[1].lower().strip():
            print('Você usou {} e deu 15 de dano!'.format(habilidades[1]))
            print('A habilidade usada não foi muito efetiva!')
            vidaRenan = 35
            print('A vida de Renan Cerpe foi para : {} '.format(vidaRenan))
        elif ataque1 == habilidades[2].lower().strip():
            print('Você usou {} e deu 25 de dano!'.format(habilidades[2]))
            print('A habilidade usada  foi  efetiva!')
            vidaRenan = 25
            print('A vida de Renan Cerpe foi para : {} '.format(vidaRenan))

        elif ataque1 == habilidades[3].lower().strip():
            print('Você usou {} e deu 30 de dano!'.format(habilidades[3]))
            print('A habilidade usada  foi  efetiva!')
            vidaRenan = 20
            print('A vida de Renan Cerpe foi para : {} '.format(vidaRenan))

        elif ataque1 == habilidades[4].lower().strip():
            print('Você usou {} e deu 40 de dano!'.format(habilidades[4]))
            print('A habilidade usada  foi  muito efetiva!')
            vidaRenan = 10
            print('A vida de Renan Cerpe foi para : {} '.format(vidaRenan))

        print('Renan contra-ataca com o golpe Cuber Brasil !!!')
        sleep(1)
        print('O golpe foi super efetivo !!\n Deu 30 de dano!')
        vidaUsuario -= 30
        print('Sua vida atual é de {}!'.format(vidaUsuario))

        print()
        print()
        sleep(1)

        print('Esse é um momento dificil, você está prestes a derrotar um grande nome do cubismo brasileiro!')
        print('Você olha para seu inventario e vê:')
        for i in inventario:
            print(i)

        print('')
        print('E para finalizar o combate, pega o item {} !'.format(inventario[0]))
        print()
        print('-Que item incrivel\n disse Renan.')
        print()
        sleep(1)
        print("{} potencializa em 20% o dano da proxima habilidade que será lançada!".format(inventario[0]))

        print('Suas habilidades disponiveis são: ')
        print()
        for i in habilidades:
            print(i, end='  |  ')

        print()
        sleep(4)
        perguntaCombate1 = input('Digite qual habilidade você quer usar : \n').lower().strip()




        print()
        print('A habilidade usada foi super efetiva! ')
        print('{} deu {} de dano graças ao item {}!!! '.format(perguntaCombate1, 40 * 1.2, inventario[0]))
        print()
        sleep(2)
        print('Renan Cerpe foi derrotado!!! Caramba!!')
        print()
        sleep(1)

        print(
            'Renan Cerpe respira, enquanto está deitado se contorcendo de dor e diz: \nVocê venceu, é dificil dizer isso, mas você venceu! Vou te dar um item incrivel, que poucos cubistas possuem. ')
        print('Você olha nos olhos de Renan, emocionado, pega o item!')
        addInventario('Fellow Cube')

        print(
            '{}, além disso, gostaria de te entregar um pergaminho contendo sabedorias de grandes cubistas, como Feliks Zemdegs '.format(
                nomeUsuario))

        print()

        print('Você deseja utilizar o pergaminho ?')
        perguntaPergaminho = input('sim ou nao? \n').lower().strip()

        while perguntaPergaminho != 'sim':
            perguntaPergaminho = input('É uma oportunidade única, digite "sim"\n').lower().strip()

        print()
        print('Caramba!!!!')

        print()

        print('*-' * 30)
        print('VOCÊ APRENDEU METODO FRIDRICH DE RESOLUÇÃO DE CUBOS!!!')
        print('*-' * 30)
        print()
        print('A habilidade nao pode ser usada em combate')
        addHabilidade("Fridrich")
        print('Suas habilidades são:')

        for k in habilidades:
            print(k)

        print()

        print()
        sleep(2)

        print('Kafra surge para trazer um comunicado!')
        print('-Agora você pode competir com cubistas em campeonatos!\n Disse Kafra!')
        print()

        perguntaCenario = input('Você deseja olhar para o cubo que recebeu? (sim ou nao) :\n').lower().strip()

        while perguntaCenario != 'sim' and perguntaCenario != 'nao':
            print('Resposta invalida, digite novamente:')
            perguntaCenario = input('Você deseja olhar para o cubo que recebeu? (sim ou nao) :').lower().strip()

        if perguntaCenario == 'sim':

            print('Você olha o fellow cube, fica impressionado com a malemolencia do cubo. ')

            print('____________________________________________________________')
            print('|               |                        |                 |')
            print('|               |                        |                 |')
            print('|               |                        |                 |')
            print('|               |                        |                 |')
            print('|__________________________________________________________|')
            print('|               |                        |                 |')
            print('|               |                        |                 |')
            print('|               |     Fellow Cube        |                 |')
            print('|               |                        |                 |')
            print('|__________________________________________________________|')
            print('|               |                        |                 |')
            print('|               |                        |                 |')
            print('|               |                        |                 |')
            print('|               |                        |                 |')
            print('|__________________________________________________________|')

            print()
            sleep(4)
            print('Que cubo bom.')
            print('em seguida, você sai para rua e olha para o céu, enquanto se senta no chão!')
            print('Você exclama: "NÃO DESCANSAREI ENQUANTO NÃO ME TORNAR O MAIOR CUBISTA DO MUNDO!"')
            sleep(2)
            print()
            print()

            print(
                'Kafra, como uma ótima pessoa, informa para você que terá um campeonato próxima semana, nessa mesma cidade, que comtemplará os maiores cubistas da região e será qualificatório para o mundial de cubo mágico!!')
            sleep(5)

            print('-Caramba, Kafra, que coisinha boa!\n disse você!')
            print(
                'Kafra informa que você ganha experiencia, e com isso, melhora sua habilidade como cubista ao abater monstros!')
            print()
            print(
                'Com isso, você decide ir para as florestas combater bichos até aumentar seu nível para chegar com alta habilidade no campeonato mundial!!')

            print()
            sleep(2)

            print()
            print('Kafra informa da Floresta Catapimbana que tem monstros do seu nível e que dropam muita experiencia!')
            print('Você, que não é besta nem nada, vai com sua bicicleta para lá!')

            print()
            sleep(2)
            print(
                'Chegando na floresta, você se depara com um monstro chamado Creep, com 10 de vida e que dropa 50 de experiencia!')

            print()
            print('Você inicia um combate com o Creep')
            print()
            sleep(1)
            print('~^' * 30)
            print('FOI INICIADO UM DUELO ENTRE {} E Creep'.format(nomeUsuario))
            print('~^' * 30)
            print()

            sleep(1)
            print('Digite qual habilidade você deseja usar : ')

            for i in habilidades:
                print(i, end='  |  ')

            perguntaCombate2 = input('Qual habilidade você deseja usar?\n').lower().strip()


            print(perguntaCombate2, 'Foi super efetivo!!')
            print('Parabens, foi adicionado ao seu inventario o item poção de experiencia! ')
            addInventario('poção de experiencia')
            print('Você deseja tomar agora a poção?')
            perguntaPocao = input('Não será possivel tomar futuramente! ( sim ou nao ): \n').lower().strip()

            while perguntaPocao != 'sim' and perguntaPocao != 'nao':
                perguntaPocao = input('Não será possivel tomar futuramente! ( sim ou nao ): \n').lower().strip()

            if perguntaPocao == 'sim':
                nivel += 0.5
                popInventario(-1)

            print('Parabens, seu nivel subiu para {}!'.format(nivel))
            print()
            sleep(2)

            print()
            print('Você está cansado, mas continua caminhando, olha para os lados e pensa, caramba, que dia bonito!')
            print('Você se senta e observa as arvores!')
            print()
            print('Enquanto você descansa, pratica resolucoes de cubo mágico, e chega a resolver ele em 7.04 segundos!')
            print()
            print('Após respirar um pouco, continua caminhando, e encontra outro Creep!')
            print()
            sleep(2)

            print()
            print('você ta cansado, mas sente que da pra batalhar!')

            print()

            print()
            print('~^' * 30)
            print('FOI INICIADO UM DUELO ENTRE {} E Creep'.format(nomeUsuario))
            print('~^' * 30)
            print()

            sleep(1)
            print('Digite qual habilidade você deseja usar : ')

            for i in habilidades:
                print(i, end='  |  ')

            perguntaCombate2 = input('Qual habilidade você deseja usar?\n')

            print(perguntaCombate2, 'Foi super efetivo!!')
            print('Parabens, foi adicionado ao seu inventario o item poção de experiencia! ')
            addInventario('poção de experiencia')

            print('Você deseja tomar agora a poção?')
            perguntaPocao = input('Não será possivel tomar futuramente! ( sim ou nao ):\n ').lower().strip()
            while perguntaPocao != 'sim' and perguntaPocao != 'nao':
                perguntaPocao = input('Não será possivel tomar futuramente! ( sim ou nao ): ').lower().strip()

            if perguntaPocao == 'sim':
                nivel += 0.5
                popInventario(-1)
            print('Parabens, seu nivel subiu para {}!'.format(nivel))
            print()
            sleep(2)

            print()

            sleep(5)


            print('Kafra aparece do nada e te assusta')
            sleep(1)
            print('Você diz para ela: ')
            print('digite o número para ação que deseja efetuar')
            print('''
            Poxa Kafra, que susto! [1]
            KAFRA, o que tu faz aqui? [2]
            E ai, kafrinha! [3]\n''')

            sleep(1)
            a = input()
            if a == '1':
                print('Poxa Kafra, que susto!')

            elif a == '2':
                print('KAFRA, o que tu faz aqui?')

            elif a == '3':
                print('E ai, kafrinha!')
            print()
            print('Kafra então te diz que vai trazer para o campeonato regional de cubo mágico!')
            print('Você diz para ela:')
            print('digite o número para ação que deseja efetuar')
            print()
            perguntaCidade4 = input('''
            Vamos lá, Kafra [1]
            To cansadao, mas bora lá! [2]
            BORA KAFRA TO PRONTO DEMAIS TU É LOUCO!!!!! [3]\n''').lower().strip()

            if perguntaCidade4 == '1':
                print()
                print('Vamos lá, Kafra')

            elif perguntaCidade4 == '2':
                print()
                print('To cansadao, mas bora lá!')

            elif perguntaCidade4 == '3':
                print()
                print('BORA KAFRA TO PRONTO DEMAIS TU É LOUCO!!!!!')

            print()
            sleep(2)

            print()

            print()
            print()
            print()
            print('=+' * 30)
            print('Você está sendo teletransportado para Ginásio de Combate Cuber, aperte os cintos!')
            print('=+' * 30)
            print()
            print()

            sleep(5)

            print('Chegando no Ginásio, você:')
            a = input('''
            Olha pra cima e procura observar o céu como sempre faz. [1]
            procura um cadeira para sentar [2] \n''').lower().strip()

            if a == '1':
                print('Caramba, incrivel como o ceu ta sempre lindo!!!')

            elif a =="2":
                print('to em pé o dia todo, vou pegar uma cadeira pra sentar sio!')
                print('*{} se senta e fica resolvendo o cubo, como estava muito feliz por sentar na cadeira após um tempão em pé, resolucao agora ta em 6.01 segundos!!!*'.format(nomeUsuario))
            sleep(1)
            print()
            print()

            print('Após a sua inscrição, você inicia sua primeira batalha no torneio, contra o senhor Cabañas!')
            print('-Incrivel que o campeonato é de cubo mágico, mas eles batalham fisicamente!\ndisse Kafra.')
            vidaUsuario = 100
            vidaCabanas = 100
            print()
            print('A sua vida foi restaurada para o combate!')
            print()
            sleep(2)
            print()
            print('~^' * 30)
            print('FOI INICIADO UM DUELO ENTRE {} E senhor Cabañas'.format(nomeUsuario))
            print('~^' * 30)
            print()
            print('Você tem {} de vida!' .format(vidaUsuario))
            print('Senhor Cabañas tem 100 de vida!')
            print('senhor Cabañas começa atacando com o golpe SALGADO NA CABEÇA')
            print('O golpe não foi muito efetivo')
            print('Você tomou 20 de dano ! ')
            vidaUsuario -= 20
            print('Sua vida atual é de {}' .format(vidaUsuario))
            sleep(1)
            print('Qual habilidade você deseja escolher? ')
            for i in habilidades:
                print(i, end= '  |   ')

            perguntaHabilidade = input('Qual habilidade vc quer usar? \n').lower().strip()
            while perguntaHabilidade not in habilidades:
                perguntaHabilidade = input('Qual habilidade vc quer usar? \n').lower().strip()

            if perguntaHabilidade == habilidades[0].lower().strip():
                print('Você usou {} e deu 40 de dano!'.format(habilidades[0]))
                print('A habilidade usada não foi muito efetiva!')
                vidaCabanas -= 40
                print('A vida de senhor Cabañas foi para : {} '.format(vidaCabanas))

            elif perguntaHabilidade == habilidades[1].lower().strip():
                print('Você usou {} e deu 50 de dano!'.format(habilidades[1]))
                print('A habilidade usada não foi muito efetiva!')
                vidaCabanas -= 50
                print('A vida de senhor Cabañas foi para : {} '.format(vidaCabanas))
            elif perguntaHabilidade == habilidades[2].lower().strip():
                print('Você usou {} e deu 60 de dano!'.format(habilidades[2]))
                print('A habilidade usada  foi  efetiva!')
                vidaCabanas -= 60
                print('A vida de senhor Cabañas foi para : {} '.format(vidaCabanas))

            elif perguntaHabilidade == habilidades[3].lower().strip():
                print('Você usou {} e deu 70 de dano!'.format(habilidades[3]))
                print('A habilidade usada  foi  efetiva!')
                vidaCabanas -= 70
                print('A vida de senhor Cabañas foi para : {} '.format(vidaCabanas))

            elif perguntaHabilidade == habilidades[4].lower().strip():
                 print('Você usou {} e deu 80 de dano!'.format(habilidades[4]))
                 print('A habilidade usada  foi  muito efetiva!')
                 vidaCabanas -= 80
                 print('A vida de senhor Cabañas foi para : {} '.format(vidaCabanas))

            print('senhor Cabañas contra-ataca com o golpe PLL ATACK H !!!')
            sleep(1)
            print('O golpe foi super efetivo !!\n Deu 30 de dano!')
            vidaUsuario -= 30
            print('Sua vida atual é de {}!'.format(vidaUsuario))

            print()
            print()
            print('O duelo fica cada vez mais acirrado, {} olha para plateia e enxerga Paulo Victor, a pessoa que inspirou ela a seguir no rumo do cubo mágico.'.format(nomeUsuario, nomeUsuario))
            print()
            print(f'{nomeUsuario} fica cada vez mais motivado, quer realizar seu desejo de se tornar o maior cubista de todos os tempos!')
            print(f'{nomeUsuario} tem a opção de utilizar algum item do seu inventario para potencializar seu poder e derrotar o senhor Cabañas!')


            for i in inventario:
                print(i, end='  |  ')

            perguntaCombate3 = input('Digite o item que deseja usar: ').lower().strip()



            print('{} pegou o item {}!' .format(nomeUsuario,perguntaCombate3))
            print('Caramba, esse item escolhido foi perfeito!')
            print('Esse item vai potencializar em 800% o seu proximo ataque!!! Eguas!!!')
            print()
            sleep(1)

            for i in habilidades:
                print(i, end='  |  ')
                print()
            perguntaHabilidade = input('Qual habilidade vc quer usar? \n').lower().strip()

            while perguntaHabilidade not in habilidades:
                perguntaHabilidade = input('Qual habilidade vc quer usar? \n').lower().strip()

            if perguntaHabilidade == habilidades[0].lower().strip():
                print('Você usou {} e deu 800 de dano!'.format(habilidades[0]))
                print('A habilidade usada  foi muito efetiva!')
                vidaCabanas = 0
                print('A vida de senhor Cabañas foi para : {} '.format(vidaCabanas))

            elif perguntaHabilidade == habilidades[1].lower().strip():
                print('Você usou {} e deu 1200 de dano!'.format(habilidades[1]))
                print('A habilidade usada  foi muito efetiva!')
                vidaCabanas = 0
                print('A vida de senhor Cabañas foi para : {} '.format(vidaCabanas))
            elif perguntaHabilidade == habilidades[2].lower().strip():
                print('Você usou {} e deu 3755 de dano!'.format(habilidades[2]))
                print('A habilidade usada  foi  muito efetiva!')
                vidaCabanas = 0
                print('A vida de senhor Cabañas foi para : {} '.format(vidaCabanas))

            elif perguntaHabilidade == habilidades[3].lower().strip():
                print('Você usou {} e deu 2400 de dano!'.format(habilidades[3]))
                print('A habilidade usada  foi  efetiva!')
                vidaCabanas = 0
                print('A vida de senhor Cabañas foi para : {} '.format(vidaCabanas))

            elif perguntaHabilidade == habilidades[4].lower().strip():
                 print('Você usou {} e deu 3200 de dano!'.format(habilidades[4]))
                 print('A habilidade usada  foi  muito efetiva!')
                 vidaCabanas = 0
                 print('A vida de senhor Cabañas foi para : {} '.format(vidaCabanas))
            sleep(1)
            print()

            print('Parece que...')
            sleep(1)
            print('um sonho está se tornando realidade....')

            print('{} ACABA DE DERROTAR SENHOR CABAÑAS !!!!!!!!!' .format(nomeUsuario))
            print()
            sleep(3)

            print('Kafra vem correndo e abraça {}' .format(nomeUsuario))
            print()
            sleep(1)
            print()
            print('Você está muito feliz por ter vencido o combate de um cubista tao forte, como você deseja comemorar sua vitoria?')
            perguntaAcao = input('''
            Você dança pra caramba e da um grito "Eu venci". [1]
            Você fica tao eufórico que começa a abraçar todos pela frente .[2]
            Você fica quietinho e pega seu cubo mágico. [3]\n''').lower().strip()

            print()
            sleep(1)
            if perguntaAcao =='1':
                print('{} da um grito tao alto enquanto faz o quadradinho que acorda a vizinhança inteira, que deselegante!' .format(nomeUsuario))

            elif perguntaAcao  == '2':
                print(f'{nomeUsuario} recebe uma advertencia da organização do evento, pois é necessario manter distanciamento social devido a pandemia do Corona Virus  ')

            elif perguntaAcao == '3':
                print(f'{nomeUsuario} consegue resolver o cubo magico em apenas 5.4 segundos! uau! ')


            print()
            print('A organização do evento informa que a próxima batalha será contra o maior cubista de todos os tempos')
            print('Kafra vem correndo informar para {} que a batalha final sera contra Carlos Salles!' .format(nomeUsuario))

            print('-Caramba !')
            print(f'Exclama {nomeUsuario}')
            print()

            print('Carlos Salles, o grande mestre do cubo mágico e de magic, muito calmamente, explicando sobre a ideologia do Linux, se aproxima e conversa com {}' .format(nomeUsuario))
            print('"Boa sorte, porque sou brabo!" disse Salles.')
            print()


            print('Você toma uma aguinha e corre pro inicio do duelo final')

            print()
            sleep(3)

            print('-Caramba, são os patrões!!!\nDisse Kafra!')
            print()
            print()
            print()
            print("_o_o_" *30)
            print()
            print('           DUELO ENTRE {} E CARLOS SALLES É INICIADO' .format(nomeUsuario))

            print()

            print("_o_o_" *30)

            vidaUsuario = 100
            vidaSalles = 200


            print('"Caramba, to nervosão" disse {}'.format(nomeUsuario))
            print()
            print('A vida de {} foi restaurada para o inicio do duelo' .format(nomeUsuario))
            print('Carlos Salles possui 200 de vida, o cara é forte!')

            print('Carlos Salles inicia o duelo utilizando o golpe PENDRIVE BOOTAVEL COM UBUNTU !!')
            print('O golpe de Salles não foi muito efetivo!')
            print('PENDRIVE BOOTAVEL COM UBUNTU deu 10 de dano!')
            vidaUsuario -= 10
            print('Sua vida atual é de {}' .format(vidaUsuario))

            print('Você começa a rir porque o golpe de Salles foi muito fraco e diz:')
            print('''
            Caramba, Salles, instala um windows KKKK muito ruim Linux! [1]
            Eita, Ubuntu ta fraco, coloca pelo menos um Kali. [2]''')

            perguntaAcao2 = input('Digite o numero correspondente a ação que deseja executar: ').lower().strip()


            while perguntaAcao2 != '1' and perguntaAcao2 != '2':
                perguntaAcao2 = input('Digite o numero correspondente a ação que deseja executar: ').lower().strip()


            if perguntaAcao2 == '1':
                print('Caramba, Salles, instala um windows KKKK muito ruim Linux!')
            elif perguntaAcao2 =='2':
                print('Eita, Ubuntu ta fraco, coloca pelo menos um Kali.')


            print()
            print('Carlos Salles responde: Rapaz, eu vou te mostrar o poder desse Sistema Operacional, só espera !! ')
            print()



            print('Você tem que atacar, qual habilidade deseja usar?')

            for i in habilidades:
                print(i,end='  |  ')
            ataque2 = input('Digite o nome da habilidade:\n').lower().strip()
            while perguntaHabilidade not in habilidades:
                perguntaHabilidade = input('Qual habilidade vc quer usar? \n').lower().strip()
            print('{} utilizou a habilidade {}' .format (nomeUsuario,ataque2))
            print('A habilidade usada foi efetiva.')
            print('A habilidade usada deu 30 de dano!')
            vidaSalles -= 30
            print('agora a vida de Carllos Salles é de {} .' .format(vidaSalles))

            print()
            sleep(2)
            print('"Agora você vai ver o poder do Linux"disse Salles')
            print()
            print('Salles contra ataca com o golpe BlackArch Linux!!')
            print('HAHHAHAHAHAHA AGORA VOCÊ VAI SENTIR O PODER!')
            print('O golpe usado por Carlos Salles foi super efetivo, deu 65 de dano!')
            vidaUsuario -= 85

            print()
            print('Kafra grita: NAAOOOO PODE SER!!!')
            print()
            sleep(3)
            print('''
            A plateia acreditava que aquele era o fim de {}
            mas, quando parecia que não havia mais chance, {} surpreende com o item Fellow Cube
            e utilizando a habilidade Dar Grau, com apenas 5 de vida!'''.format(nomeUsuario,nomeUsuario))


            print('Você da um golpe mega efetivo em Carllos Salles, causando 500 de dano!')
            a = '''
                Caramba, eu nao sabia que tinha esse poder! O cubo mágico me tornou cada vez mais forte, batalhar com creeps,
                lutar contra cubistas, aprender metodos de resolução do cubo, tudo isso me tornou quem eu sou, obrigado por todos que me acompanharam nessa jornada!
                FINALMENTE EU POSSO DIZER
                EU SOU O MAIOR CUBISTA DE TODOS OS TEMPOS, NÃO HÁ NINGUEM COM UM METODO DE RESOLUÇÃO E PODER MAIOR QUE O MEU!!!!!!!!!!!!!!!!!!!!!!!!!!'''

            print(a)


            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            sleep(5)


            print('''
            Muito obrigado por jogar o jogo Rubiks Adventure.
            espero que você tenha se divertido!''')





        break
































