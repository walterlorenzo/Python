frase = 'Curso em Vídeo Python'
print(frase[0:13:2])

print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. In nec sapien sed lacus fermentum cursus. Vestibulum et consequat nibh. Maecenas porta mauris mauris, sit amet venenatis erat efficitur eget. Sed tincidunt cursus dui vitae lacinia. Nulla dignissim metus ut nisi cursus, quis molestie augue aliquam. In placerat enim at dictum tempus. In iaculis enim ut dolor pretium porttitor. Nulla non vestibulum justo, ut porttitor ligula. Sed fringilla tincidunt nulla ut efficitur.

Proin sit amet erat id dolor luctus sodales at non diam. Quisque vitae egestas orci, at pellentesque nisi. Nulla vel tortor sit amet ex fermentum malesuada non ac diam. Quisque placerat justo vitae sapien venenatis maximus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nullam accumsan purus id libero ultricies, ac interdum leo pretium. Proin a pretium nibh. Donec felis ligula, interdum tristique dui vel, feugiat tempus felis. Nam luctus vestibulum est, at pulvinar mi egestas nec. Pellentesque vitae nisi massa. Nam sit amet aliquet ex. Integer in nisl a nulla hendrerit tempor. Nullam nec orci eget velit pellentesque pharetra vel in urna.

Quisque porta ante pharetra euismod posuere. Ut nec turpis in leo tempus interdum eget quis augue. Cras venenatis metus sed pretium sodales. In sit amet enim pharetra, scelerisque leo eu, ullamcorper est. Aliquam magna dui, egestas et facilisis non, commodo lacinia ante. Mauris imperdiet neque felis. Duis leo dolor, maximus quis malesuada et, ullamcorper a odio.

Pellentesque gravida, mauris sit amet tristique pulvinar, diam metus facilisis diam, auctor ornare nibh ex non justo. Maecenas non libero vitae nunc sagittis placerat ac eu erat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Fusce sit amet pulvinar sapien. Donec sodales lacus quis massa ullamcorper, eget fermentum mauris vehicula. Praesent quis tincidunt quam. Suspendisse ac nulla auctor, vulputate nisl quis, vulputate purus. Integer consectetur hendrerit ultrices. Nulla aliquet mi quis quam tristique, et vestibulum est tincidunt. Nullam tellus turpis, venenatis vel dui porttitor, mollis ultricies quam.

Suspendisse ut ex elit. Ut gravida orci at luctus egestas. Nulla sed ante a quam interdum tristique id eget est. Suspendisse at pharetra magna. Etiam eget purus lacus. Etiam malesuada rhoncus turpis at mollis. Nunc volutpat eleifend nisl, vitae commodo sem vulputate nec.""")

texto = """orem ipsum dolor sit amet, consectetur adipiscing elit. In nec sapien sed lacus fermentum cursus. Vestibulum et consequat nibh. Maecenas porta mauris mauris, sit amet venenatis erat efficitur eget. Sed tincidunt cursus dui vitae lacinia. Nulla dignissim metus ut nisi cursus, quis molestie augue aliquam. In placerat enim at dictum tempus. In iaculis enim ut dolor pretium porttitor. Nulla non vestibulum justo, ut porttitor ligula. Sed fringilla tincidunt nulla ut efficitur.

Proin sit amet erat id dolor luctus sodales at non diam. Quisque vitae egestas orci, at pellentesque nisi. Nulla vel tortor sit amet ex fermentum malesuada non ac diam. Quisque placerat justo vitae sapien venenatis maximus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nullam accumsan purus id libero ultricies, ac interdum leo pretium. Proin a pretium nibh. Donec felis ligula, interdum tristique dui vel, feugiat tempus felis. Nam luctus vestibulum est, at pulvinar mi egestas nec. Pellentesque vitae nisi massa. Nam sit amet aliquet ex. Integer in nisl a nulla hendrerit tempor. Nullam nec orci eget velit pellentesque pharetra vel in urna.

Quisque porta ante pharetra euismod posuere. Ut nec turpis in leo tempus interdum eget quis augue. Cras venenatis metus sed pretium sodales. In sit amet enim pharetra, scelerisque leo eu, ullamcorper est. Aliquam magna dui, egestas et facilisis non, commodo lacinia ante. Mauris imperdiet neque felis. Duis leo dolor, maximus quis malesuada et, ullamcorper a odio.

Pellentesque gravida, mauris sit amet tristique pulvinar, diam metus facilisis diam, auctor ornare nibh ex non justo. Maecenas non libero vitae nunc sagittis placerat ac eu erat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Fusce sit amet pulvinar sapien. Donec sodales lacus quis massa ullamcorper, eget fermentum mauris vehicula. Praesent quis tincidunt quam. Suspendisse ac nulla auctor, vulputate nisl quis, vulputate purus. Integer consectetur hendrerit ultrices. Nulla aliquet mi quis quam tristique, et vestibulum est tincidunt. Nullam tellus turpis, venenatis vel dui porttitor, mollis ultricies quam.

Suspendisse ut ex elit. Ut gravida orci at luctus egestas. Nulla sed ante a quam interdum tristique id eget est. Suspendisse at pharetra magna. Etiam eget purus lacus. Etiam malesuada rhoncus turpis at mollis. Nunc volutpat eleifend nisl, vitae commodo sem vulputate nec."""

print(len(texto)) # Esse comando faz a contagem de quantos caracteres existem #

frase2 = '     Curso em Vídeo Python     '
print(len(frase2))          # Esse comando faz a contagem de quantos caracteres existem #
print(len(frase2.strip()))   # Esse comando tira os espaços desnecessários #
print(frase[0])       # Mostra primeiro caracter #
frase = frase.replace('Python', 'Android') # trocando cacteres por outros usando replace #
print(frase)
print('Curso' in frase) # Mostra que a palavra está em "frase" #
print(frase.find('Curso')) # Mostra que está na posição 0 #
print(frase.find('curso')) # Não tem essa palavra escrita em minúscula então o resultado é -1 #
print(frase.lower().find('curso')) # Agora pedi para que achasse como se fosse em minúsculo e mostrou a posição #
dividido = frase.split() # vai dividir a frase #
print(dividido)