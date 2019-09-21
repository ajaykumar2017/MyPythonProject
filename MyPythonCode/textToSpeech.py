from subprocess import call

speech = "Hello World!"
call(["espeak", speech])