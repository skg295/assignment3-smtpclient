from socket import *
from datetime import datetime


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    # Fill in start
    # Fill in end
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver,port))
    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
           #print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    # Fill in end
    MailCommand = 'MAIL FROM:<SKG295@nyu.edu>\r\n'
    clientSocket.send(MailCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')


    # Send RCPT TO command and handle server response.
    # Fill in start
    # Fill in end
    RCPTCommand = "RCPT TO:<skg295@nyu.edu>\r\n"
    clientSocket.send(RCPTCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')

    # Send DATA command and handle server response.
    # Fill in start
    # Fill in end
    DataCommand = "DATA\r\n"
    clientSocket.send(DataCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)

    # Send message data.
    # Fill in start
    # Fill in end
    m1 = "Date: Sat, 26 Feb 2022 16:54\r\n"
    m2 = "From: skg295@nyu.edu\r\n"
    m3 = "To: skg295@nyu.edu\r\n"
    m4 = "subject: This is the subject line\r\n"
    m5 = "I have written my first email\r\n"

    clientSocket.send(m1.encode())
    clientSocket.send(m2.encode())
    clientSocket.send(m3.encode())
    clientSocket.send(m4.encode())
    clientSocket.send(m5.encode())

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    # Fill in end
    endmessage = ".\r\n"
    clientSocket.send(endmessage.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')

    # Send QUIT command and handle server response.
    # Fill in start
    # Fill in end
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #print("We did it")


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')