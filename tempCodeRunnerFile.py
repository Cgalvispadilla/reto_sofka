_juego()
        gan=""
        for i in ganadores:
            gan+=str(i[1].get_conductor()+"#") 
        print(gan)   
        podio =p.Podio(gan.split("#")[0],gan.split("#")[1],gan.split("#")[2])
        info = sear.mostrarInfo()
        if len(info)>0:
            for x in info: