import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
from googlesearch import search
from bs4 import BeautifulSoup
import requests
from pytube import Search

def tic_tac_toe():
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    currentplayer = "X"
    currentplayer2 = 'O'
    winner = None
    gamerunning = True

    def printBoard(board):
        print(board[0] + "|" + board[1] + "|" + board[2])
        print("-----")
        print(board[3] + "|" + board[4] + "|" + board[5])
        print("-----")
        print(board[6] + "|" + board[7] + "|" + board[8])

    def playerInput(board):
        nonlocal currentplayer, currentplayer2, gamerunning
        printBoard(board)
        bakchodi = None
        move = audioo()
        if move is not None:
            if '1' in move.lower() or 'one' in move.lower():
                bakchodi = 1
            elif '2' in move.lower() or 'two' in move.lower() or 'tu' in move.lower() or 'to' in move.lower():
                bakchodi = 2
            elif '3' in move.lower() or 'three' in move.lower():
                bakchodi = 3
            elif '4' in move.lower() or 'four' in move.lower():
                bakchodi = 4
            elif '5' in move.lower() or 'five' in move.lower():
                bakchodi = 5
            elif '6' in move.lower() or 'six' in move.lower() or 'sex' in move.lower() or 'music' in move.lower():
                bakchodi = 6
            elif '7' in move.lower() or 'seven' in move.lower():
                bakchodi = 7
            elif '8' in move.lower() or 'eight' in move.lower() or 'it' in move.lower():
                bakchodi = 8
            elif '9' in move.lower() or 'nine' in move.lower():
                bakchodi = 9
            else:
                print("Invalid move")
                speak("Invalid move")
                return

            if 1 <= bakchodi <= 9 and board[bakchodi - 1] == "-":
                board[bakchodi - 1] = currentplayer
            else:
                print("maybe you will lose the game because you played an illegal move")
                speak('maybe you will lose the game because you played an illegal move')

        printBoard(board)
        bakchodi2 = None
        move2 = audioo()
        if move2 is not None:
            if '1' in move2.lower() or 'one' in move2.lower():
                bakchodi2 = 1
            elif '2' in move2.lower() or 'two' in move2.lower() or 'tu' in move2.lower() or 'to' in move2.lower():
                bakchodi2 = 2
            elif '3' in move2.lower() or 'three' in move2.lower():
                bakchodi2 = 3
            elif '4' in move2.lower() or 'four' in move2.lower() or 'for' in move2.lower():
                bakchodi2 = 4
            elif '5' in move2.lower() or 'five' in move2.lower():
                bakchodi2 = 5
            elif '6' in move2.lower() or 'six' in move2.lower() or 'sex' in move2.lower() or 'music' in move2.lower():
                bakchodi2 = 6
            elif '7' in move2.lower() or 'seven' in move2.lower():
                bakchodi2 = 7
            elif '8' in move2.lower() or 'eight' in move2.lower() or 'it' in move2.lower():
                bakchodi2 = 8
            elif '9' in move2.lower() or 'nine' in move2.lower():
                bakchodi2 = 9
            else:
                print("Invalid move")
                speak("Invalid move")
                return

            if 1 <= bakchodi2 <= 9 and board[bakchodi2 - 1] == "-":
                board[bakchodi2 - 1] = currentplayer2
            else:
                print("maybe you will lose the game because you play an illegal move")
                speak('maybe you will lose the game because you play an illegal move')

        printBoard(board)

    def ch(board):
        nonlocal winner
        if board[0] == board[1] == board[2] and board[0] != "-":
            winner = board[0]
            print("----------winner is", board[0], "---------------")
            speak(f'winner is {board[0]}')
            chatbot()
        elif board[3] == board[4] == board[5] and board[3] != "-":
            winner = board[3]
            print("----------winner is", board[3], "---------------")
            speak(f'winner is {board[3]}')
            chatbot()
        elif board[6] == board[7] == board[8] and board[6] != "-":
            winner = board[6]
            print("----------winner is", board[6], "---------------")
            speak(f'winner is {board[6]}')
            chatbot()

    def cv(board):
        nonlocal winner
        if board[0] == board[3] == board[6] and board[0] != "-":
            winner = board[0]
            print("----------winner is", board[0], "---------------")
            speak(f'winner is {board[0]}')
            chatbot()
        elif board[1] == board[4] == board[7] and board[1] != "-":
            winner = board[1]
            print("----------winner is", board[1], "---------------")
            speak(f'winner is {board[1]}')
            chatbot()
        elif board[2] == board[5] == board[8] and board[2] != "-":
            winner = board[2]
            print("----------winner is", board[2], "---------------")
            speak(f'winner is {board[2]}')
            chatbot()

    def cd(board):
        nonlocal winner
        if board[0] == board[4] == board[8] and board[0] != "-":
            winner = board[0]
            print("----------winner is", board[0], "---------------")
            speak(f'winner is {board[0]}')
            chatbot()
        elif board[2] == board[4] == board[6] and board[2] != "-":
            winner = board[2]
            print("----------winner is", board[2], "---------------")
            speak(f'winner is {board[2]}')
            chatbot()

    while gamerunning:
        playerInput(board)
        ch(board)
        cv(board)
        cd(board)
        if winner == 'X' or winner == 'O':
            print('game over')
            speak('game over')
            print('winner is', winner)
            speak('winner is', winner)
            break
        elif '-' not in board:
            print('game over')
            speak('game over')
            print('its a tie')
            speak('its a tie')
            break


def google_search(query):
    try:
        for result in search(query,num=10):
            print(result)
            speak(result)
            try:
                response=requests.get(result)
                soup=BeautifulSoup(response.text,'html.parser')
                paragraphs=soup.find_all('p')
                if paragraphs:
                    print(paragraphs[0].get_text())
                    speak(paragraphs[0].get_text())
                    print(paragraphs[1].get_text())
                    speak(paragraphs[1].get_text())
                else:
                    print('no information found')
                    speak('no information found')
            except Exception as e:
                print("sorry i could not find any information on this topic")
                speak('sorry i could not find any information on this topic')    
                    
        
    except Exception as e:
        print(e)
        speak('sorry i am not able to search this query')
        print('sorry i am not able to search this query')
        
        
        


  
def audioo():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening your command........")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print('analyzing your command........')
        text=r.recognize_google(audio,language='en-in')
        print(f'you said:{text}')
    except Exception as e:
        print('say that again please........')
        return 'None'
    return text

def youtube_music(noni):
    try:
        search=Search(noni)
        result=search.results[0]
        url=result.watch_url
        title=result.title
        print('playing',title)
        speak(f'playing {title}')
        webbrowser.open(url)
    except Exception as e:
        print('sorry i am not able to find any video on this topic')
    
    
    
    




def openwebsite(command):
    if 'google'  in command.lower():
        speak('opening google')
        webbrowser.open('https://www.google.com')
    elif 'music'  in command.lower() and 'youtube'  in command.lower():
        speak('opening youtube music')
        print('opening youtube music')
        speak('which music do you want to listen...')
        print('which music do you want to listen...')
        cr=audioo()
        youtube_music(cr)
        
    elif 'youtube'  in command.lower():
        speak('opening youtube')
        webbrowser.open('https://www.youtube.com')
    elif 'gmail'  in command.lower():
        speak('opening gmail')
        webbrowser.open('https://www.gmail.com')
    elif 'facebook'  in command.lower():
        speak('opening facebook')
        webbrowser.open('https://www.facebook.com')
    elif 'instagram'  in command.lower():
        speak('opening instagram')
        webbrowser.open('https://www.instagram.com')
    elif 'twitter'  in command.lower():
        speak('opening twitter')
        webbrowser.open('https://www.twitter.com')
    elif 'linkedin'  in command.lower():
        speak('opening linkedin')
        webbrowser.open('https://www.linkedin.com')
    elif 'according to wikipedia' in command.lower() or 'what' in command.lower() or 'when' in command.lower() or 'who' in command.lower() or 'where' in command.lower() or 'why' in command.lower() or 'how' in command.lower() or 'which' in command.lower() or 'whose' in command.lower():
        print('searching  wikipedia....')
        speak('searching wikipedia')
        command=command.replace('according to wikipedia', '')
        results = wikipedia.summary(command, sentences=2)
        speak('According to wikipedia, ' + results)
    elif 'wikipedia' in command.lower():
        speak('opening wikipedia')
        webbrowser.open('https://www.wikipedia.org')
    elif 'stack overflow'  in command.lower():
        speak('opening stack overflow')
        webbrowser.open('https://www.stackoverflow.com')
    elif 'reddit'  in command.lower():
        speak('opening reddit')
        webbrowser.open('https://www.reddit.com')
    elif 'quora'  in command.lower():
        speak('opening quora')
        webbrowser.open('https://www.quora.com')
    elif 'amazon'  in command.lower():
        speak('opening amazon')
        webbrowser.open('https://www.amazon.com')
    elif 'flipkart'  in command.lower():
        speak('opening flipkart')
        webbrowser.open('https://www.flipkart.com')
    elif 'pinterest' in command.lower():
        speak('opening pinterest')
        webbrowser.open('https://www.pinterest.com')
    elif   'snapdeal' in command.lower():
        speak('opening snapdeal')
        webbrowser.open('https://www.snapdeal.com')
    elif  'ebay' in command.lower():
        speak('opening ebay')
        webbrowser.open('https://www.ebay.com')
    elif  'whatsapp' in command.lower():
        speak('opening whatsapp')
        webbrowser.open('https://www.whatsapp.com')
    elif  'netflix' in command.lower():
        speak('opening netflix')
        webbrowser.open('https://www.netflix.com')
    elif  'hotstar' in command.lower():
        speak('opening hotstar')
        webbrowser.open('https://www.hotstar.com')

    elif 'code with harry' in command.lower():
        speak('opening code with harry')
        webbrowser.open('https://www.codewithharry.com')
    elif 'tic tac toe' in command.lower() or 'tic-tac-toe' in command.lower() or 'tic tac to' in command.lower():
        speak(' ok lets play tic tak toe')
        speak('do you want to play in terminal or in browser?')
        print('do you want to play in terminal or in browser? (t/b):')
        c1=audioo()
        if 'terminal' in c1.lower():
            speak('lets play in terminal')
            print('lets play in terminal')
            tic_tac_toe()
        elif 'browser' in c1.lower():
            speak('lets play in browser')
            print('lets play in browser')
            webbrowser.open('https://playtictactoe.org/')
        else:
            speak('invalid input')
            print('invalid input')
            speak('do you want to play or not')
            ss=audioo()
            if 'yes' in ss.lower():
                tic_tac_toe()
            else:
                command=audioo()
                
                
    else:
        speak("sorry i am not capable of replyimg to this command")
        print("sorry i am not capable of replyimg to this command")
        speak('i can show results of this command from google')
        print('do you want results from google (yes/no)')
        
        speak('do you want results from google')
        c1=audioo()
        if 'yes' in c1.lower() or 'go' in c1.lower() or 'show' in c1.lower() or 'search' in c1.lower():
            speak('ok')
            
            speak('searching google....')
            speak('here are the results')
            google_search(command)
            
        elif 'no' in c1.lower() or "'don't" in c1.lower() or 'dont' in c1.lower():
            print('ok')
            speak('ok')
            speak('what you want me to do')
            
        
        

          

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
def wish():
    hour=int(datetime.datetime.now().hour)
    if 0<=hour<12:
        speak('good morning')
        print('good morning')
    elif 12<=hour<18:
        speak('good afternoon')
        print('good afternoon')
    else:
        speak('good evening')
        print('good evening')
       
    

       
    
    
    

def chatbot():
    wish()
    speak('hello, I am mona, your personal assistant. How can I help you today?')
    print('Hello, I am mona, your personal assistant. How can I help you today?')
    while True:
        command= audioo()
        if 'exit' in command.lower():
            print(' bye! have a nice day')
            speak('bye! have a nice day')
            break
        elif 'hello' in command.lower():
            print('hello how can i help you')
            speak('hello how can i help you')
        elif 'hi' in command.lower():
            print('hello how can i help you')
            speak('hello how can i help you')
        elif 'how are you feeling' in command.lower():
            print('i am only a machine i have no feelings')
            speak('i am only a machine i have no feelings')    
        elif 'quit' in command.lower():  
            print(' bye! have a nice day')
            speak('bye! have a nice day')
            break
        elif 'bye' in command.lower():
            print(' bye! have a nice day')
            speak('bye! have a nice day')
            break
        else: 
            openwebsite(command)
chatbot()

