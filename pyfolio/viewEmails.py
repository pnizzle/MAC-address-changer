import imaplib
M=imaplib.IMAP4_SSL('imap.gmail.com')
email ='ddiyrestorations@gmail.com'# input('please enter your email: ')
password ='pmgefkntyngewfcg'     #input('please enter iklrbgoxajnjbyej for password:')

M.login(email,password)
