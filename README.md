Programa do MEC
---

Encontra-se em anexo um código de elementos de contorno em Python seguindo um fluxo de trabalho bem parecido com aquele do Fenics, ou seja, desenho no Freecad, gero a malha no Gmsh, rodo o programa em Python e, finalmente, faço o pós-processamento no paraview. A construção das matrizes H e G, que é a parte cara, está em Cython, que é compilado. Estou fazendo processamento paralelo usando o openmp. Com isso, a construção da matriz fica extremamente rápido. O problema é que as matrizes são cheias e não simétricas, ou seja, rapidamente estoura a memória.

Estou usando o meshIO para ler a malha do GMSH e escrever o arquivo .vtk que será lido no paraview. Para instalar o meshIO, digite no terminal:

`pip install meshio`

Como tem esta parte que é compilada, antes de rodar o programa, rodem, no terminal, o seguinte comando:

`python setup.py build_ext -i`

Para facilitar o entendimento, também o código em Python puro, sem compilar, que roda problemas simples.


O programa é para a formulação de Laplace e usa elementos triangulares lineares contínuos. A gente fez questão de usar elementos contínuos porque o número de nós é bem menor que no caso de elementos descontínuos, o que faz muita diferença no caso de problemas 3D. A forma como está sendo aplicada as condições de contorno não está documentada. Esta talvez seja a parte mais difícil de se trabalhar com elementos contínuos, onde um nó é dividido com vários elementos.

O programa está ótimo para ser rodado em pcs, especialmente I5 e I7, uma vez que a paralelização é feito com o openmp (memória compartilhada). Bom para dar aula. E, uma vez que ficou bem parecido com o fluxo de trabalho do Fenics, finalmente vamos poder comparar, com condições de mais ou menos igualdade, o MEC com o MEF.

