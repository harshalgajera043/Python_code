def outerfunction(text):
    def innerfunction():
        print(text)

    innerfunction()

outerfunction('Hello World !')
