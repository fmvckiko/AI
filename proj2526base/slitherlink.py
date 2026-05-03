#!/usr/bin/env python3
# slitherlink.py: Template para implementação do projeto de Inteligência Artificial 2025/2026.
# Devem alterar as classes e funções neste ficheiro de acordo com as instruções do enunciado.
# Além das funções e classes sugeridas, podem acrescentar outras que considerem pertinentes.

# Grupo 00:
# 00000 Nome1
# 00000 Nome2

import random, copy
from sys import stdin
from collections import defaultdict

import utils
from utils import *

from search import (
    Problem,
    Node,
    astar_search,
    breadth_first_tree_search,
    depth_first_tree_search,
    greedy_search,
    recursive_best_first_search,
)


class SlitherlinkState:
    state_id = 0


    def __init__(self, board):
        self.board = board
        self.id = SlitherlinkState.state_id
        SlitherlinkState.state_id += 1
    
    def __lt__(self, other):
        return self.id < other.id

    # TODO: outros metodos da classe

class Cell:
    """representação interna de uma célula"""
    def __init__(self,value:int):
        self.edges = [0,0,0,0]
        self.value = value 

    def activate_edge(self, edge:str):
        match edge:
            case "top":
                self.edges[0] = 1
            case "right":
                self.edges[1] = 1
            case "bottom":
                self.edges[2] = 1
            case "left":
                self.edges[3] = 1
            case _:
                print("uknown edge") #maybe levantar erro

    def get_total_active(self) -> int:
        total = 0
        for i in range(4):
            if self.edges[i] == 1:
                total +=1
        return total
    
    def __str__(self):
        return f"{self.edges[0]}{self.edges[1]}{self.edges[2]}{self.edges[3]}"

class Board:
    """Representação interna de um tabuleiro de Slitherlink."""
    def __init__(self):
        self.board = [[]] #matriz de celulas
    
    def adjacent_cell(self, cell:tuple) -> list:
        """Devolve uma lista das células que fazem
        fronteira com a célula enviada no argumento"""
        #TODO
        pass

    def get_cell_edges(self, row:int, column:int) -> list:
        """Devolve os arestas da célula enviada no argumento"""
        #TODO
        pass

    def get_active_edges(self, row:int, column:int) -> list:
        """Devolve o número de arestas ativas"""
        #TODO
        pass


    def parse_line(self,line:list) -> list:
        i = 0
        new_line = []
        while i < len(line):
            match line[i]:
                case "0":
                    cell = Cell(0)
                case "1":
                    cell = Cell(1)
                case "2":
                    cell = Cell(2)
                case "3":
                    cell = Cell(3)
                case ".":
                    cell = Cell(-1)
            new_line.append(cell)
            i+=1

        return new_line

    def parse_instance(self):
        """Lê o test do standard input (stdin) que é passado como argumento
        e retorna uma instância da classe Board.
        Por exemplo:
            $ python3 pipe.py < test-01.txt

            > from sys import stdin
            > line = stdin.readline().split()
        """
        i=0
        while True:
            line = stdin.readline().split()
            if line == []:
                break
            self.board.append(self.parse_line(line))
            i+=1

    def print_board_debug(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if col != len(self.board[row]) -1:
                    print(f"{self.board[row][col].value}", end="\t")
                else:
                    print(f"{self.board[row][col].value}")
                    

class Slitherlink(Problem):
    def __init__(self, board: Board, gui=None):
        """O construtor especifica o estado inicial."""
        # TODO
        pass


    def actions(self, state: SlitherlinkState):
        """Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento."""
        # TODO
        pass


    def result(self, state: SlitherlinkState, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state)."""
        # TODO
        pass

    def goal_test(self, state: SlitherlinkState):
        """Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se todas as posições do tabuleiro
        estão preenchidas de acordo com as regras do problema."""
        # TODO
        pass

    def h(self, node: Node):
        """Função heuristica utilizada para a procura A*."""
        # TODO
        pass

    


if __name__ == "__main__":
    # TODO:
    # Ler o ficheiro do standard input,
    board = Board()
    board.parse_instance()
    board.print_board_debug()
    # Usar uma técnica de procura para resolver a instância,
    # Retirar a solução a partir do nó resultante,
    # Imprimir para o standard output no formato indicado.
    pass







